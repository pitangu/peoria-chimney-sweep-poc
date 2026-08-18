/**
 * Peoria Chimney Sweep — form handler + UX helpers
 * Phone/email are placeholders until CallRail (or similar) is wired.
 */
(function () {
  const PHONE_DISPLAY = "(309) 555-0148";
  const PHONE_TEL = "+13095550148";
  const FORM_ENDPOINT = ""; // optional: Formspree / Getform URL

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

  function handleForms() {
    document.querySelectorAll("form[data-lead-form]").forEach((form) => {
      form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const status = form.querySelector("[data-form-status]");
        const btn = form.querySelector('button[type="submit"]');
        const data = Object.fromEntries(new FormData(form).entries());

        // Honeypot
        if (data.company_website) {
          if (status) status.textContent = "Thanks — we'll be in touch shortly.";
          form.reset();
          return;
        }

        if (!data.name || !data.phone) {
          if (status) status.textContent = "Please add your name and phone number.";
          return;
        }

        if (btn) btn.disabled = true;
        if (status) status.textContent = "Sending…";

        try {
          if (FORM_ENDPOINT) {
            const res = await fetch(FORM_ENDPOINT, {
              method: "POST",
              headers: { "Content-Type": "application/json", Accept: "application/json" },
              body: JSON.stringify(data),
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
              ].join("\n")
            );
            // Store locally for operator follow-up
            try {
              const key = "pcs_leads";
              const prev = JSON.parse(localStorage.getItem(key) || "[]");
              prev.push({ ...data, ts: new Date().toISOString() });
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
    handleForms();
  });
})();
