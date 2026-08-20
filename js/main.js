/**
 * Peoria Chimney Sweep — form handler + mobile nav + UX helpers
 * Phone/email are placeholders until CallRail (or similar) is wired.
 */
(function () {
  const PHONE_DISPLAY = "(309) 555-0148";
  const PHONE_TEL = "+130****0148";
  const FORM_ENDPOINT = ""; // optional: Formspree / Getform URL
  // Snapshot of consent wording shown on the form at submission time.
  // Keep in sync with the visible checkbox label in build.py lead_form().
  const CONSENT_TEXT =
    "I agree to be contacted by a local chimney professional about my request by phone, text, or email, including via automated technology. Consent is not a condition of purchase. Message and data rates may apply. See our Privacy Policy and Terms of Service.";

  function applyPhoneLinks() {
    document.querySelectorAll("[data-phone-link]").forEach((el) => {
      el.setAttribute("href", "tel:" + PHONE_TEL);
      if (el.dataset.phoneLink === "text") {
        el.textContent = PHONE_DISPLAY;
      }
    });
  }

  function setYear() {
    document.querySelectorAll("[data-year]").forEach((el) => {
      el.textContent = String(new Date().getFullYear());
    });
  }

  function setupMobileNav() {
    const toggle = document.querySelector(".nav-toggle");
    const nav = document.getElementById("primary-nav");
    if (!toggle || !nav) return;

    function closeNav() {
      nav.classList.remove("is-open");
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-label", "Open menu");
    }

    function openNav() {
      nav.classList.add("is-open");
      toggle.setAttribute("aria-expanded", "true");
      toggle.setAttribute("aria-label", "Close menu");
    }

    toggle.addEventListener("click", () => {
      if (nav.classList.contains("is-open")) closeNav();
      else openNav();
    });

    nav.querySelectorAll("a").forEach((a) => {
      a.addEventListener("click", closeNav);
    });

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") closeNav();
    });

    document.addEventListener("click", (e) => {
      if (!nav.classList.contains("is-open")) return;
      if (nav.contains(e.target) || toggle.contains(e.target)) return;
      closeNav();
    });

    window.addEventListener("resize", () => {
      if (window.innerWidth > 900) closeNav();
    });
  }

  function isoWithOffset(d) {
    const pad = (n) => String(n).padStart(2, "0");
    const tzo = -d.getTimezoneOffset();
    const sign = tzo >= 0 ? "+" : "-";
    const abs = Math.abs(tzo);
    const hh = pad(Math.floor(abs / 60));
    const mm = pad(abs % 60);
    return (
      d.getFullYear() +
      "-" +
      pad(d.getMonth() + 1) +
      "-" +
      pad(d.getDate()) +
      "T" +
      pad(d.getHours()) +
      ":" +
      pad(d.getMinutes()) +
      ":" +
      pad(d.getSeconds()) +
      sign +
      hh +
      ":" +
      mm
    );
  }

  async function lookupSubmitterIp() {
    try {
      const ctrl = typeof AbortController !== "undefined" ? new AbortController() : null;
      const timer = ctrl ? setTimeout(() => ctrl.abort(), 2500) : null;
      const res = await fetch("https://api.ipify.org?format=json", {
        signal: ctrl ? ctrl.signal : undefined,
      });
      if (timer) clearTimeout(timer);
      if (!res.ok) return "unavailable";
      const j = await res.json();
      return j && j.ip ? String(j.ip) : "unavailable";
    } catch (_) {
      return "unavailable";
    }
  }

  function handleForms() {
    document.querySelectorAll("form[data-lead-form]").forEach((form) => {
      const consentInput = form.querySelector('input[name="consent"]');
      const consentError = form.querySelector("[data-consent-error]");

      if (consentInput) {
        // Never restore or auto-check consent.
        consentInput.checked = false;
        consentInput.addEventListener("change", () => {
          if (consentInput.checked && consentError) {
            consentError.hidden = true;
          }
        });
      }

      form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const status = form.querySelector("[data-form-status]");
        const btn = form.querySelector('button[type="submit"]');
        const data = Object.fromEntries(new FormData(form).entries());

        // Honeypot
        if (data.company_website) {
          if (status) status.textContent = "Thanks — we'll be in touch shortly.";
          form.reset();
          if (consentInput) consentInput.checked = false;
          return;
        }

        if (!data.name || !data.phone) {
          if (status) status.textContent = "Please add your name and phone number.";
          return;
        }

        if (!consentInput || !consentInput.checked) {
          if (consentError) {
            consentError.hidden = false;
            consentError.focus && consentError.focus();
          }
          if (status) status.textContent = "";
          if (consentInput) consentInput.focus();
          return;
        }
        if (consentError) consentError.hidden = true;

        if (btn) btn.disabled = true;
        if (status) status.textContent = "Sending…";

        const consent_timestamp = isoWithOffset(new Date());
        const consent_page_url = window.location.href;
        const consent_text = CONSENT_TEXT;
        const consent_user_agent = navigator.userAgent || "";
        const consent_ip = await lookupSubmitterIp();

        const payload = {
          ...data,
          consent_timestamp,
          consent_ip,
          consent_page_url,
          consent_text,
          consent_user_agent,
        };

        try {
          if (FORM_ENDPOINT) {
            const res = await fetch(FORM_ENDPOINT, {
              method: "POST",
              headers: { "Content-Type": "application/json", Accept: "application/json" },
              body: JSON.stringify(payload),
            });
            if (!res.ok) throw new Error("bad status");
          } else {
            // Fallback: open mail client so leads aren't lost before CRM is ready
            const subject = encodeURIComponent("Chimney service request — Peoria area");
            const body = encodeURIComponent(
              [
                "Name: " + data.name,
                "Phone: " + data.phone,
                "Email: " + (data.email || ""),
                "City/ZIP: " + (data.city || ""),
                "Service: " + (data.service || ""),
                "Message: " + (data.message || ""),
                "",
                "Consent timestamp: " + consent_timestamp,
                "Consent IP: " + consent_ip,
                "Consent page URL: " + consent_page_url,
                "Consent text: " + consent_text,
                "Consent user agent: " + consent_user_agent,
              ].join("\n")
            );
            // Store locally for operator follow-up (includes immutable consent snapshot)
            try {
              const key = "pcs_leads";
              const prev = JSON.parse(localStorage.getItem(key) || "[]");
              prev.push({
                name: data.name,
                phone: data.phone,
                email: data.email || "",
                city: data.city || "",
                service: data.service || "",
                message: data.message || "",
                consent_timestamp,
                consent_ip,
                consent_page_url,
                consent_text,
                consent_user_agent,
                ts: new Date().toISOString(),
              });
              localStorage.setItem(key, JSON.stringify(prev));
            } catch (_) {}
            window.location.href =
              "mailto:leads@chimneysweeppeoriail.com?subject=" + subject + "&body=" + body;
          }
          if (status) {
            status.textContent =
              "Thanks! If your email app opened, hit send. Or call " + PHONE_DISPLAY + " now.";
          }
          form.reset();
          if (consentInput) consentInput.checked = false;
        } catch (err) {
          if (status) {
            status.textContent =
              "Could not send online. Please call " + PHONE_DISPLAY + " — we're happy to help.";
          }
        } finally {
          if (btn) btn.disabled = false;
        }
      });
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    applyPhoneLinks();
    setYear();
    setupMobileNav();
    handleForms();
  });
})();
