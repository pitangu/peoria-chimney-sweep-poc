#!/usr/bin/env python3
"""Build static rank-and-rent site: Chimney Sweep Peoria IL."""
from __future__ import annotations

from pathlib import Path
import json
from datetime import date

ROOT = Path(__file__).resolve().parent
TODAY = date.today().isoformat()
SITE_NAME = "Peoria Chimney Sweep"
DOMAIN = "https://chimneysweeppeoriail.com"  # primary target domain
# GitHub Pages URL will also work; canonical can be updated after domain connect
PHONE_DISPLAY = "(309) 555-0148"
PHONE_TEL = "+13095550148"
BRAND = "Peoria Chimney Sweep"
CITY = "Peoria"
STATE = "IL"
GEO_REGION = "US-IL"
LAT, LNG = "40.6936", "-89.5890"

NAV = [
    ("Home", "/"),
    ("Chimney Sweep", "/services/chimney-sweep/"),
    ("Chimney Inspection", "/services/chimney-inspection/"),
    ("Chimney Repair", "/services/chimney-repair/"),
    ("Dryer Vent Cleaning", "/services/dryer-vent-cleaning/"),
    ("Service Areas", "/areas/"),
    ("Blog", "/blog/"),
    ("Contact", "/contact/"),
]

AREAS = [
    ("peoria", "Peoria", "Peoria, IL is our home base. We serve wood and gas fireplaces across the city, from the West Bluff to North Peoria and near Bradley University."),
    ("east-peoria", "East Peoria", "East Peoria homeowners along the Illinois River deal with freeze-thaw stress on masonry. We sweep, inspect, and repair chimneys throughout East Peoria."),
    ("pekin", "Pekin", "Pekin, IL homes with older masonry chimneys need annual creosote removal before heating season. Local chimney sweep and inspection for Pekin residents."),
    ("washington", "Washington", "Washington, IL chimney cleaning, Level 1–2 inspections, caps, and tuckpointing for residential fireplaces and inserts."),
    ("morton", "Morton", "Morton, IL chimney sweep and fireplace safety services — creosote cleaning, camera inspections, and masonry repairs."),
    ("dunlap", "Dunlap", "Dunlap and north-metro homes: professional chimney sweeping, dryer vent cleaning, and safety inspections."),
    ("metamora", "Metamora", "Metamora chimney services including sweep, cap installation, and flue inspections for wood-burning systems."),
    ("peoria-heights", "Peoria Heights", "Peoria Heights chimney cleaning and repair with careful indoor protection for finished homes."),
    ("germantown-hills", "Germantown Hills", "Germantown Hills fireplace and chimney maintenance — sweep, inspection, waterproofing, and liner checks."),
    ("chillicothe", "Chillicothe", "Chillicothe, IL chimney sweep and creosote removal for river-area homes heading into winter."),
]

SERVICES = [
    {
        "slug": "chimney-sweep",
        "name": "Chimney Sweep",
        "title": "Chimney Sweep Peoria IL | Professional Chimney Cleaning",
        "h1": "Chimney Sweep in Peoria, IL",
        "meta": "Professional chimney sweep and chimney cleaning in Peoria, IL. Creosote removal, mess-free service, same-week scheduling. Call " + PHONE_DISPLAY + ".",
        "icon": "🧹",
        "summary": "Mess-free chimney cleaning that removes creosote, soot, and debris so your Peoria fireplace vents safely.",
        "body_extra": """
<h2>Why Peoria homeowners schedule an annual chimney sweep</h2>
<p>Central Illinois winters mean heavy fireplace use. Every wood fire leaves behind creosote — a flammable byproduct that builds up inside the flue. The National Fire Protection Association (NFPA 211) recommends chimneys be inspected at least once a year and cleaned when needed. A professional chimney sweep in Peoria, IL reduces chimney-fire risk, improves draft, and keeps smoke where it belongs.</p>
<h2>What our chimney cleaning includes</h2>
<ul>
<li>Protective floor coverings and HEPA-filtered vacuum setup</li>
<li>Brushing of flue, smoke chamber, and firebox</li>
<li>Removal of soot, creosote, and loose debris</li>
<li>Visual check for obvious damage, blockages, or animal nests</li>
<li>Before/after notes so you know what we found</li>
</ul>
<h2>Signs you need a chimney sweep now</h2>
<ul>
<li>It has been more than 12 months since your last cleaning</li>
<li>Smoke spills into the room when you burn</li>
<li>Strong creosote or musty odor, especially after rain</li>
<li>White staining (efflorescence) on exterior brick</li>
<li>Animals or birds nesting near the flue opening</li>
</ul>
<div class="callout"><strong>Local tip:</strong> Peoria’s freeze-thaw cycles crack crowns and loosen mortar. Pair your sweep with a quick exterior look before the first hard freeze.</div>
""",
    },
    {
        "slug": "chimney-inspection",
        "name": "Chimney Inspection",
        "title": "Chimney Inspection Peoria IL | Level 1 & 2 Inspections",
        "h1": "Chimney Inspection in Peoria, IL",
        "meta": "NFPA-style chimney inspections in Peoria, IL. Level 1 and Level 2 evaluations with clear photo notes. Schedule at " + PHONE_DISPLAY + ".",
        "icon": "🔎",
        "summary": "Clear, photo-backed chimney inspections so you know if your system is safe to burn.",
        "body_extra": """
<h2>When you need a chimney inspection</h2>
<p>Buyers, sellers, and careful homeowners in the Peoria metro use chimney inspections to catch hidden problems before they become expensive repairs — or safety hazards. We follow industry inspection levels so the scope matches your situation.</p>
<h2>Level 1 vs Level 2</h2>
<ul>
<li><strong>Level 1:</strong> Routine annual check when nothing has changed — readily accessible portions of the chimney and appliance.</li>
<li><strong>Level 2:</strong> After a home sale, weather event, or system change. May include camera scanning of flues and more of the accessible chimney structure.</li>
</ul>
<h2>What you receive</h2>
<ul>
<li>Plain-English summary of findings</li>
<li>Photos of problem areas when present</li>
<li>Prioritized recommendations (safety first, then maintenance)</li>
<li>No pressure upsells — rent the lead flow model means results speak for themselves</li>
</ul>
""",
    },
    {
        "slug": "chimney-repair",
        "name": "Chimney Repair",
        "title": "Chimney Repair Peoria IL | Caps, Crowns & Masonry",
        "h1": "Chimney Repair in Peoria, IL",
        "meta": "Chimney repair in Peoria, IL: caps, crowns, tuckpointing, flashing, and waterproofing. Protect your home from water and freeze damage. Call " + PHONE_DISPLAY + ".",
        "icon": "🧱",
        "summary": "Caps, crowns, tuckpointing, and waterproofing that stop water before it wrecks the flue.",
        "body_extra": """
<h2>Common chimney repairs in Central Illinois</h2>
<p>Water is the enemy of masonry. Rain, snow, and freeze-thaw cycles around Peoria open mortar joints, crack crowns, and rust dampers. Small repairs now prevent full rebuilds later.</p>
<ul>
<li>Chimney cap installation (animals, rain, embers)</li>
<li>Crown repair and rebuild</li>
<li>Tuckpointing and brick replacement</li>
<li>Flashing repair at the roof line</li>
<li>Breathable masonry waterproofing</li>
<li>Damper repair or top-sealing dampers</li>
</ul>
<h2>Why repair beats “wait and see”</h2>
<p>Moisture inside the flue damages liners and can migrate into attics and living spaces. If your sweep or inspection flags masonry issues, fixing them before winter is usually the lowest-cost path.</p>
""",
    },
    {
        "slug": "chimney-cap-installation",
        "name": "Chimney Cap Installation",
        "title": "Chimney Cap Installation Peoria IL",
        "h1": "Chimney Cap Installation in Peoria, IL",
        "meta": "Chimney cap installation in Peoria, IL. Keep rain, animals, and debris out of your flue. Stainless options available. Call " + PHONE_DISPLAY + ".",
        "icon": "🛡️",
        "summary": "A proper cap keeps rain, raccoons, and leaves out — and sparks in.",
        "body_extra": """
<h2>Why chimney caps matter in Peoria</h2>
<p>Open flues invite rainwater, nesting animals, and leaves. A quality chimney cap with a spark arrestor mesh protects the flue and reduces downdraft issues on windy bluff days.</p>
<ul>
<li>Stainless steel and custom-fit options</li>
<li>Animal exclusion screening</li>
<li>Paired with sweep or inspection appointments when possible</li>
</ul>
""",
    },
    {
        "slug": "creosote-removal",
        "name": "Creosote Removal",
        "title": "Creosote Removal Peoria IL | Chimney Fire Prevention",
        "h1": "Creosote Removal in Peoria, IL",
        "meta": "Creosote removal and glazed creosote treatment for Peoria, IL chimneys. Reduce chimney fire risk. Call " + PHONE_DISPLAY + ".",
        "icon": "🔥",
        "summary": "Targeted creosote cleaning — including harder glazed stages — to lower chimney-fire risk.",
        "body_extra": """
<h2>Creosote stages explained</h2>
<ul>
<li><strong>Stage 1:</strong> Dusty, flaky soot — standard brushing usually handles it.</li>
<li><strong>Stage 2:</strong> Harder, tar-like flakes that need thorough mechanical cleaning.</li>
<li><strong>Stage 3:</strong> Glazed, shiny coating that can require specialized removal methods.</li>
</ul>
<p>Burning wet wood, smoldering overnight fires, and restricted air supply speed up creosote growth. If your Peoria chimney hasn’t been serviced in years, start with an inspection plus sweep.</p>
""",
    },
    {
        "slug": "dryer-vent-cleaning",
        "name": "Dryer Vent Cleaning",
        "title": "Dryer Vent Cleaning Peoria IL | Lint Fire Prevention",
        "h1": "Dryer Vent Cleaning in Peoria, IL",
        "meta": "Dryer vent cleaning in Peoria, IL. Remove lint buildup, cut fire risk, and help clothes dry faster. Call " + PHONE_DISPLAY + ".",
        "icon": "👕",
        "summary": "Lint removal from dryer ducts — safer laundry rooms and shorter dry times.",
        "body_extra": """
<h2>Why dryer vents clog</h2>
<p>Even if you clean the lint screen every load, lint collects in the duct run — especially on long routes through crawlspaces or multi-story homes common around Peoria.</p>
<ul>
<li>Longer drying times and hot clothes</li>
<li>Burning smell during the cycle</li>
<li>Lint around the outdoor exhaust hood</li>
<li>Higher energy use</li>
</ul>
<p>We clean the full vent path and confirm airflow at the exterior termination whenever accessible.</p>
""",
    },
]

BLOG_POSTS = [
    {
        "slug": "how-often-clean-chimney-peoria",
        "title": "How Often Should You Clean a Chimney in Peoria, IL?",
        "meta": "Learn how often Peoria homeowners should schedule chimney cleaning, what NFPA guidance says, and signs you need service sooner.",
        "date": "2026-08-01",
        "html": """
<p>If you burn wood through a Central Illinois winter, your chimney works hard. The short answer most Peoria homeowners need: <strong>inspect every year, clean when the inspection says so</strong> — often annually for frequent wood burners.</p>
<h2>NFPA guidance in plain English</h2>
<p>NFPA 211 calls for chimneys and vents to be inspected at least once a year. Cleaning frequency depends on fuel type, how often you burn, and how much creosote has built up. Gas systems still need inspections even when they produce less creosote than wood.</p>
<h2>Peoria-specific factors</h2>
<ul>
<li>Long heating seasons mean more burn hours</li>
<li>Freeze-thaw weather stresses crowns and mortar</li>
<li>Older housing stock may have aging liners or caps</li>
</ul>
<h2>Don’t wait for these warning signs</h2>
<ul>
<li>Smoke in the living room</li>
<li>Strong odor after rain</li>
<li>Roof-level animal activity</li>
<li>Visible exterior cracks or leaning</li>
</ul>
<p><a href="/contact/">Schedule a chimney sweep in Peoria</a> before peak season fills the calendar.</p>
""",
    },
    {
        "slug": "creosote-chimney-fire-risk",
        "title": "Creosote Buildup: The Chimney Fire Risk Peoria Homeowners Miss",
        "meta": "What creosote is, why it causes chimney fires, and how Peoria homeowners can reduce risk with proper sweeping.",
        "date": "2026-08-05",
        "html": """
<p>Creosote is the dark, tar-like residue left when wood smoke cools inside a flue. It is flammable. When enough accumulates, a normal fire can ignite the deposit — a chimney fire that can exceed 2,000°F.</p>
<h2>What increases creosote</h2>
<ul>
<li>Burning unseasoned (wet) wood</li>
<li>Smoldering, low-air overnight burns</li>
<li>Restricted air supply or undersized flues</li>
<li>Long gaps between professional cleanings</li>
</ul>
<h2>Prevention that actually works</h2>
<p>Burn dry hardwood, give the fire enough air, and book a professional <a href="/services/chimney-sweep/">chimney sweep in Peoria, IL</a> on a regular schedule. If glazed creosote is present, standard light brushing may not be enough — ask for a full evaluation.</p>
""",
    },
    {
        "slug": "signs-you-need-chimney-cap",
        "title": "5 Signs Your Peoria Chimney Needs a Cap",
        "meta": "Rain entry, animals, leaves, and sparks — signs a chimney cap belongs on your Peoria home.",
        "date": "2026-08-10",
        "html": """
<p>A chimney cap is one of the cheapest upgrades that prevents expensive damage. Here’s when Peoria homeowners should act.</p>
<ol>
<li><strong>Water in the firebox after storms</strong> — open flues catch rain and melting snow.</li>
<li><strong>Birds, squirrels, or raccoons</strong> — warm flues are prime nesting spots.</li>
<li><strong>Leaves and debris smells</strong> — organic material in the flue is a fire hazard.</li>
<li><strong>Ember concerns on wooded lots</strong> — mesh spark arrestors help keep embers contained.</li>
<li><strong>No cap on a visual roof check</strong> — many older homes never received one.</li>
</ol>
<p>See <a href="/services/chimney-cap-installation/">chimney cap installation</a> or call us to bundle a cap with your next sweep.</p>
""",
    },
    {
        "slug": "prepare-fireplace-for-winter-illinois",
        "title": "Prepare Your Fireplace for an Illinois Winter (Peoria Checklist)",
        "meta": "A practical pre-winter fireplace checklist for Peoria and Central Illinois homes.",
        "date": "2026-08-12",
        "html": """
<p>Before the first cold snap, run this checklist:</p>
<ul>
<li>Book a sweep/inspection if you have not had one in the last year</li>
<li>Confirm the damper opens and closes cleanly</li>
<li>Check the exterior cap and crown from the ground (binoculars help)</li>
<li>Stack only seasoned firewood off the ground</li>
<li>Test smoke and CO alarms on every level</li>
<li>Clear furniture and storage from around the hearth</li>
</ul>
<p>Ready for hands-on help? <a href="/contact/">Request chimney service in the Peoria area</a>.</p>
""",
    },
    {
        "slug": "dryer-vent-vs-chimney-cleaning",
        "title": "Dryer Vent Cleaning vs Chimney Cleaning: What’s the Difference?",
        "meta": "Both prevent home fires, but dryer vents and chimneys need different tools and schedules.",
        "date": "2026-08-15",
        "html": """
<p>Homeowners sometimes confuse the two. Both remove combustible buildup — lint in dryer ducts, creosote in chimneys — but the systems are different.</p>
<table>
<thead><tr><th></th><th>Chimney</th><th>Dryer vent</th></tr></thead>
<tbody>
<tr><td>Hazard</td><td>Creosote / chimney fire / CO</td><td>Lint fire / overheating</td></tr>
<tr><td>Typical schedule</td><td>Annual inspection</td><td>Every 1–2 years (more if heavy use)</td></tr>
<tr><td>Tools</td><td>Brushes, rods, cameras, HEPA vac</td><td>Rotary brush, vacuum, airflow check</td></tr>
</tbody>
</table>
<p>We offer both <a href="/services/chimney-sweep/">chimney sweeping</a> and <a href="/services/dryer-vent-cleaning/">dryer vent cleaning in Peoria</a> so you can bundle safety services in one visit when routes allow.</p>
""",
    },
]


def lead_form(compact: bool = False) -> str:
    msg_rows = "" if compact else """
    <div class="form-row">
      <div><label for="message">What’s going on?</label><textarea id="message" name="message" placeholder="e.g. annual sweep, smoke in room, home inspection…"></textarea></div>
    </div>"""
    return f"""
<form class="lead-form" data-lead-form novalidate>
  <div style="position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden" aria-hidden="true">
    <label>Company website<input type="text" name="company_website" tabindex="-1" autocomplete="off"></label>
  </div>
  <div class="form-row two">
    <div><label for="name">Name *</label><input id="name" name="name" required autocomplete="name"></div>
    <div><label for="phone">Phone *</label><input id="phone" name="phone" type="tel" required autocomplete="tel"></div>
  </div>
  <div class="form-row two">
    <div><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email"></div>
    <div><label for="city">City / ZIP</label><input id="city" name="city" placeholder="Peoria, East Peoria…"></div>
  </div>
  <div class="form-row">
    <div>
      <label for="service">Service needed</label>
      <select id="service" name="service">
        <option value="Chimney Sweep">Chimney Sweep / Cleaning</option>
        <option value="Chimney Inspection">Chimney Inspection</option>
        <option value="Chimney Repair">Chimney Repair</option>
        <option value="Chimney Cap">Chimney Cap</option>
        <option value="Creosote Removal">Creosote Removal</option>
        <option value="Dryer Vent Cleaning">Dryer Vent Cleaning</option>
        <option value="Not sure">Not sure — call me</option>
      </select>
    </div>
  </div>
  {msg_rows}
  <button class="btn btn-primary btn-block" type="submit">Request a Callback</button>
  <p class="form-note">Prefer to talk now? <a data-phone-link="text" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> · No obligation</p>
  <p class="form-note" data-form-status role="status" aria-live="polite"></p>
</form>
"""


def base(title: str, meta: str, path: str, body: str, extra_head: str = "") -> str:
    canonical = DOMAIN.rstrip("/") + (path if path != "/" else "/")
    nav_html = "\n".join(
        f'<li><a href="{href}">{label}</a></li>' for label, href in NAV
    )
    services_footer = "\n".join(
        f'<li><a href="/services/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES
    )
    areas_footer = "\n".join(
        f'<li><a href="/areas/{a[0]}/">{a[1]}, IL</a></li>' for a in AREAS[:6]
    )
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{meta}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index,follow">
  <meta name="geo.region" content="{GEO_REGION}">
  <meta name="geo.placename" content="Peoria">
  <meta name="ICBM" content="{LAT}, {LNG}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{meta}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary">
  <link rel="stylesheet" href="/css/styles.css">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  {extra_head}
</head>
<body>
  <div class="topbar">
    <div class="container">
      <span>Serving Peoria, East Peoria, Pekin, Washington, Morton & nearby</span>
      <span>Call <a data-phone-link="text" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> · Same-week openings often available</span>
    </div>
  </div>
  <header class="site-header">
    <div class="container header-inner">
      <a class="logo" href="/" aria-label="{BRAND} home">
        <span class="logo-mark" aria-hidden="true">⌂</span>
        <div>{BRAND}<span>Chimney Cleaning · Peoria, IL</span></div>
      </a>
      <nav aria-label="Primary">
        <ul>
          {nav_html}
          <li><a class="btn btn-primary" data-phone-link="text" href="tel:{PHONE_TEL}">Call Now</a></li>
        </ul>
      </nav>
    </div>
  </header>
  <main>
    {body}
  </main>
  <section class="cta-band">
    <div class="container">
      <h2>Need a chimney sweep in the Peoria area?</h2>
      <p>Request a callback or call <strong>{PHONE_DISPLAY}</strong>. Fast scheduling for cleaning, inspections, and repairs.</p>
      <p>
        <a class="btn btn-secondary" href="/contact/">Get a Free Quote</a>
        &nbsp;
        <a class="btn btn-primary" data-phone-link href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
      </p>
    </div>
  </section>
  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <h3>{BRAND}</h3>
        <p>Local lead-generation site connecting Peoria-area homeowners with professional chimney and dryer-vent service. Mess-conscious cleaning, clear recommendations, and safety-first work.</p>
        <p><strong style="color:#fff">Phone:</strong> <a data-phone-link="text" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>
        <strong style="color:#fff">Area:</strong> Peoria metro, Central Illinois</p>
      </div>
      <div>
        <h3>Services</h3>
        <ul>{services_footer}</ul>
      </div>
      <div>
        <h3>Cities</h3>
        <ul>{areas_footer}</ul>
      </div>
      <div>
        <h3>Company</h3>
        <ul>
          <li><a href="/about/">About</a></li>
          <li><a href="/blog/">Blog</a></li>
          <li><a href="/contact/">Contact</a></li>
          <li><a href="/privacy/">Privacy</a></li>
          <li><a href="/sitemap.xml">Sitemap</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <span>© <span data-year></span> {BRAND}. All rights reserved.</span>
      <span>Peoria, Illinois · Chimney sweep, inspection & repair information site</span>
    </div>
  </footer>
  <script src="/js/main.js" defer></script>
</body>
</html>
"""


def write(path: str, html: str) -> None:
    p = ROOT / path.lstrip("/")
    if path.endswith("/"):
        p = p / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")
    print("wrote", p.relative_to(ROOT))


def json_ld_home() -> str:
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "LocalBusiness",
                "@id": DOMAIN + "/#business",
                "name": BRAND,
                "image": DOMAIN + "/favicon.svg",
                "url": DOMAIN + "/",
                "telephone": PHONE_TEL,
                "priceRange": "$$",
                "description": "Chimney sweep, chimney cleaning, inspection, repair, and dryer vent cleaning serving Peoria, IL and nearby communities.",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Peoria",
                    "addressRegion": "IL",
                    "addressCountry": "US",
                },
                "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LNG},
                "areaServed": [
                    {"@type": "City", "name": n} for _, n, _ in AREAS
                ],
                "openingHoursSpecification": [
                    {
                        "@type": "OpeningHoursSpecification",
                        "dayOfWeek": [
                            "Monday",
                            "Tuesday",
                            "Wednesday",
                            "Thursday",
                            "Friday",
                        ],
                        "opens": "08:00",
                        "closes": "18:00",
                    }
                ],
                "hasOfferCatalog": {
                    "@type": "OfferCatalog",
                    "name": "Chimney services",
                    "itemListElement": [
                        {
                            "@type": "Offer",
                            "itemOffered": {
                                "@type": "Service",
                                "name": s["name"],
                                "url": f"{DOMAIN}/services/{s['slug']}/",
                            },
                        }
                        for s in SERVICES
                    ],
                },
            },
            {
                "@type": "WebSite",
                "@id": DOMAIN + "/#website",
                "url": DOMAIN + "/",
                "name": BRAND,
                "publisher": {"@id": DOMAIN + "/#business"},
            },
        ],
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def json_ld_service(s: dict) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": s["name"] + " Peoria IL",
        "serviceType": s["name"],
        "provider": {"@type": "LocalBusiness", "name": BRAND, "telephone": PHONE_TEL},
        "areaServed": {"@type": "City", "name": "Peoria", "containedInPlace": {"@type": "State", "name": "Illinois"}},
        "url": f"{DOMAIN}/services/{s['slug']}/",
        "description": s["meta"],
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def json_ld_faq(faqs: list[tuple[str, str]]) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in faqs
        ],
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def build_home() -> None:
    faqs = [
        (
            "How much does a chimney sweep cost in Peoria, IL?",
            "Most standard residential chimney cleanings in the Peoria area fall in a few-hundred-dollar range depending on flue condition, accessibility, and whether an inspection or repairs are needed. Call for a straightforward quote.",
        ),
        (
            "How long does chimney cleaning take?",
            "A typical single-flue sweep often takes about 45–90 minutes on site, longer if heavy creosote, multiple flues, or access challenges are involved.",
        ),
        (
            "Do gas fireplaces need chimney service?",
            "Yes. Gas systems produce less creosote than wood but still need inspections for proper venting, animal blockages, corrosion, and safety.",
        ),
        (
            "Which cities do you serve?",
            "Peoria, East Peoria, Pekin, Washington, Morton, Dunlap, Metamora, Peoria Heights, Germantown Hills, Chillicothe, and nearby Central Illinois communities.",
        ),
    ]
    faq_html = "\n".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs
    )
    cards = "\n".join(
        f"""<article class="card">
          <div class="icon-badge">{s['icon']}</div>
          <h3>{s['name']}</h3>
          <p>{s['summary']}</p>
          <a class="more" href="/services/{s['slug']}/">Learn more →</a>
        </article>"""
        for s in SERVICES
    )
    area_pills = "\n".join(
        f'<a href="/areas/{slug}/">{name}, IL</a>' for slug, name, _ in AREAS
    )
    body = f"""
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow">Peoria, IL · Chimney & Dryer Vent Pros</span>
      <h1>Chimney Sweep in Peoria, IL — Cleaning, Inspection & Repair</h1>
      <p class="lede">Keep your fireplace safe for Central Illinois winters. Professional chimney cleaning, creosote removal, inspections, caps, and dryer vent cleaning for Peoria and nearby towns.</p>
      <ul class="hero-points">
        <li>Mess-conscious indoor protection & HEPA vacuum setup</li>
        <li>Clear findings — safety first, no jargon runaround</li>
        <li>Serving Peoria, East Peoria, Pekin, Washington, Morton & more</li>
        <li>Same-week appointments often available in season</li>
      </ul>
      <div class="hero-ctas">
        <a class="btn btn-primary btn-lg" data-phone-link href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
        <a class="btn btn-secondary btn-lg" href="#quote">Request a Callback</a>
      </div>
      <div class="trust-row">
        <span><strong>NFPA-minded</strong> annual safety focus</span>
        <span><strong>Wood & gas</strong> systems</span>
        <span><strong>Local</strong> Central Illinois routing</span>
      </div>
    </div>
    <div class="quote-card" id="quote">
      <h2>Get a free callback</h2>
      <p class="sub">Tell us what you need. A scheduler will follow up — usually the same business day.</p>
      {lead_form(compact=True)}
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>Chimney services built for Peoria homes</h2>
      <p>From a quick annual sweep to caps, crowns, and dryer vents — one place for the jobs homeowners actually search for.</p>
    </div>
    <div class="grid-3">{cards}</div>
  </div>
</section>

<section class="bg-navy">
  <div class="container grid-2">
    <div>
      <div class="section-head">
        <h2>How service works</h2>
        <p>Simple on purpose — so you get help without a hard sell.</p>
      </div>
      <div class="steps">
        <div class="step"><div class="step-num">1</div><div><h3>Call or request a callback</h3><p>Share your city, fireplace type, and what you’re seeing (smoke, odor, due for annual service, buyer inspection, etc.).</p></div></div>
        <div class="step"><div class="step-num">2</div><div><h3>We schedule a visit</h3><p>A technician arrives with floor protection and pro tools, then cleans and/or inspects as agreed.</p></div></div>
        <div class="step"><div class="step-num">3</div><div><h3>You get clear next steps</h3><p>If everything looks good, you’re set for the season. If repairs are needed, you get plain-English options.</p></div></div>
      </div>
    </div>
    <div>
      <div class="section-head">
        <h2>Why annual chimney care matters here</h2>
        <p>Peoria winters are long. Creosote, moisture, and freeze-thaw damage don’t take the season off.</p>
      </div>
      <ul class="checklist">
        <li>Chimney fires often start with neglected creosote</li>
        <li>Blocked flues can push carbon monoxide risk indoors</li>
        <li>Open chimneys attract birds and raccoons</li>
        <li>Cracked crowns let water destroy masonry from inside</li>
        <li>Home sales frequently require Level 2 inspections</li>
      </ul>
      <p style="margin-top:1.25rem"><a class="btn btn-primary" href="/services/chimney-sweep/">See chimney sweep details</a></p>
    </div>
  </div>
</section>

<section class="bg-cream">
  <div class="container">
    <div class="section-head">
      <h2>Proudly serving the Peoria metro</h2>
      <p>Neighborhood-level pages help you confirm we cover your town — and help locals find the right service faster.</p>
    </div>
    <div class="area-pills">{area_pills}</div>
  </div>
</section>

<section>
  <div class="container grid-2">
    <div>
      <div class="section-head">
        <h2>What homeowners ask us</h2>
        <p>Straight answers before you book.</p>
      </div>
      <div class="faq">{faq_html}</div>
    </div>
    <div class="card">
      <h3>Ready when you are</h3>
      <p>Whether you need a standard chimney cleaning in Peoria or a full inspection before listing your home, start with a quick call or form.</p>
      {lead_form()}
    </div>
  </div>
</section>
"""
    extra = json_ld_home() + json_ld_faq(faqs)
    write("index.html", base(
        "Chimney Sweep Peoria IL | Chimney Cleaning & Inspection",
        f"Professional chimney sweep and chimney cleaning in Peoria, IL. Creosote removal, inspections, repairs, and dryer vent cleaning. Call {PHONE_DISPLAY}.",
        "/",
        body,
        extra,
    ))


def build_services() -> None:
    for s in SERVICES:
        body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a> · <a href="/services/{s['slug']}/">Services</a> · {s['name']}</div>
    <h1>{s['h1']}</h1>
    <p>{s['summary']}</p>
  </div>
</section>
<div class="container content-wrap">
  <article class="prose">
    <p>Looking for <strong>{s['name'].lower()} in Peoria, IL</strong>? {BRAND} helps homeowners across the Peoria metro keep fireplaces and vents safe, clean, and ready for winter. Call <a data-phone-link="text" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> or request a callback — we’ll confirm fit and timing.</p>
    {s['body_extra']}
    <h2>Cities we serve for {s['name'].lower()}</h2>
    <p>Peoria, East Peoria, Pekin, Washington, Morton, Dunlap, Metamora, Peoria Heights, Germantown Hills, Chillicothe, and surrounding Central Illinois communities.</p>
    <h2>Related services</h2>
    <ul>
      {''.join(f'<li><a href="/services/{o["slug"]}/">{o["name"]}</a></li>' for o in SERVICES if o['slug'] != s['slug'])}
    </ul>
  </article>
  <aside class="sidebar-sticky">
    <div class="quote-card">
      <h2>Request {s['name']}</h2>
      <p class="sub">Peoria-area scheduling · No obligation</p>
      {lead_form(compact=True)}
    </div>
  </aside>
</div>
"""
        write(
            f"services/{s['slug']}/index.html",
            base(s["title"], s["meta"], f"/services/{s['slug']}/", body, json_ld_service(s)),
        )


def build_areas() -> None:
    # index
    pills = "\n".join(
        f"""<article class="card">
          <h3>{name}, IL</h3>
          <p>{blurb[:140]}…</p>
          <a class="more" href="/areas/{slug}/">Chimney services in {name} →</a>
        </article>"""
        for slug, name, blurb in AREAS
    )
    body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a> · Service Areas</div>
    <h1>Chimney Sweep Service Areas near Peoria, IL</h1>
    <p>Local chimney cleaning, inspections, repairs, and dryer vent service across the Peoria metro.</p>
  </div>
</section>
<section>
  <div class="container">
    <div class="grid-3">{pills}</div>
  </div>
</section>
"""
    write("areas/index.html", base(
        "Chimney Sweep Service Areas | Peoria IL Metro",
        "Chimney sweep service areas near Peoria, IL including East Peoria, Pekin, Washington, Morton, Dunlap, and more.",
        "/areas/",
        body,
    ))

    for slug, name, blurb in AREAS:
        svc_links = "".join(
            f'<li><a href="/services/{s["slug"]}/">{s["name"]} in {name}</a></li>' for s in SERVICES
        )
        body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a> · <a href="/areas/">Areas</a> · {name}</div>
    <h1>Chimney Sweep in {name}, IL</h1>
    <p>Chimney cleaning, inspection, repair, and dryer vent cleaning for {name} and nearby neighborhoods.</p>
  </div>
</section>
<div class="container content-wrap">
  <article class="prose">
    <p>{blurb}</p>
    <h2>Chimney services in {name}</h2>
    <p>Homeowners in {name}, Illinois search for reliable local help when smoke spills, odors appear after rain, or it’s simply time for the annual cleaning. We provide:</p>
    <ul>{svc_links}</ul>
    <h2>Why local matters</h2>
    <p>Central Illinois weather punishes masonry. Scheduling chimney maintenance in {name} before peak cold keeps creosote in check and catches crown or cap issues early. If you’re preparing a home for sale in {name}, ask about a Level 2-style inspection scope.</p>
    <div class="callout"><strong>Serving {name} from the Peoria metro.</strong> Call <a data-phone-link="text" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> and mention you’re in {name} for routing.</div>
    <h2>Nearby cities</h2>
    <p class="area-pills" style="margin-top:0.75rem">
      {''.join(f'<a href="/areas/{s}/">{n}, IL</a>' for s, n, _ in AREAS if s != slug)}
    </p>
  </article>
  <aside class="sidebar-sticky">
    <div class="quote-card">
      <h2>Book in {name}</h2>
      <p class="sub">Chimney & dryer vent callbacks</p>
      {lead_form(compact=True)}
    </div>
  </aside>
</div>
"""
        ld = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": f"Chimney Sweep {name} IL",
            "areaServed": {"@type": "City", "name": name},
            "provider": {"@type": "LocalBusiness", "name": BRAND, "telephone": PHONE_TEL},
            "url": f"{DOMAIN}/areas/{slug}/",
        }
        write(
            f"areas/{slug}/index.html",
            base(
                f"Chimney Sweep {name} IL | Chimney Cleaning Near Peoria",
                f"Chimney sweep and chimney cleaning in {name}, IL near Peoria. Inspections, creosote removal, caps, and dryer vent cleaning. Call {PHONE_DISPLAY}.",
                f"/areas/{slug}/",
                body,
                f'<script type="application/ld+json">{json.dumps(ld)}</script>',
            ),
        )


def build_blog() -> None:
    items = "\n".join(
        f"""<article class="post-item">
          <div class="post-meta">{p['date']}</div>
          <h2><a href="/blog/{p['slug']}/">{p['title']}</a></h2>
          <p>{p['meta']}</p>
          <a class="more" href="/blog/{p['slug']}/">Read article →</a>
        </article>"""
        for p in BLOG_POSTS
    )
    body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a> · Blog</div>
    <h1>Chimney Safety Tips for Peoria Homeowners</h1>
    <p>Practical guides on chimney cleaning, creosote, caps, and winter prep in Central Illinois.</p>
  </div>
</section>
<section>
  <div class="container post-list">{items}</div>
</section>
"""
    write("blog/index.html", base(
        "Chimney Tips Blog | Peoria IL",
        "Articles on chimney sweeping, creosote, caps, and fireplace safety for Peoria, Illinois homeowners.",
        "/blog/",
        body,
    ))

    for p in BLOG_POSTS:
        body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a> · <a href="/blog/">Blog</a> · Article</div>
    <h1>{p['title']}</h1>
    <p>Published {p['date']} · Peoria, IL chimney care</p>
  </div>
</section>
<div class="container content-wrap">
  <article class="prose">{p['html']}</article>
  <aside class="sidebar-sticky">
    <div class="quote-card">
      <h2>Need service?</h2>
      <p class="sub">Talk to the Peoria team</p>
      {lead_form(compact=True)}
    </div>
  </aside>
</div>
"""
        ld = {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": p["title"],
            "datePublished": p["date"],
            "dateModified": p["date"],
            "author": {"@type": "Organization", "name": BRAND},
            "publisher": {"@type": "Organization", "name": BRAND},
            "mainEntityOfPage": f"{DOMAIN}/blog/{p['slug']}/",
            "description": p["meta"],
        }
        write(
            f"blog/{p['slug']}/index.html",
            base(
                p["title"] + " | " + BRAND,
                p["meta"],
                f"/blog/{p['slug']}/",
                body,
                f'<script type="application/ld+json">{json.dumps(ld)}</script>',
            ),
        )


def build_static_pages() -> None:
    contact_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a> · Contact</div>
    <h1>Contact {BRAND}</h1>
    <p>Call <a data-phone-link="text" href="tel:{PHONE_TEL}" style="color:#fff;font-weight:700">{PHONE_DISPLAY}</a> or send the form — we cover Peoria and nearby towns.</p>
  </div>
</section>
<section>
  <div class="container grid-2">
    <div class="card">
      <h3>Request a callback</h3>
      {lead_form()}
    </div>
    <div class="prose">
      <h2 class="mt-0">Phone</h2>
      <p><a class="btn btn-primary" data-phone-link href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></p>
      <h2>Hours</h2>
      <p>Monday–Friday 8:00 a.m. – 6:00 p.m.<br>Saturday by appointment during peak season</p>
      <h2>Service area</h2>
      <p>Peoria, East Peoria, Pekin, Washington, Morton, Dunlap, Metamora, Peoria Heights, Germantown Hills, Chillicothe, and surrounding Central Illinois communities.</p>
      <h2>What to have ready</h2>
      <ul>
        <li>City / ZIP</li>
        <li>Wood or gas appliance?</li>
        <li>Last cleaning date (if known)</li>
        <li>Any symptoms (smoke, odor, animals, buyer inspection)</li>
      </ul>
    </div>
  </div>
</section>
"""
    write("contact/index.html", base(
        f"Contact {BRAND} | {PHONE_DISPLAY}",
        f"Contact {BRAND} for chimney sweep, inspection, repair, and dryer vent cleaning in Peoria, IL. Call {PHONE_DISPLAY}.",
        "/contact/",
        contact_body,
    ))

    about_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a> · About</div>
    <h1>About {BRAND}</h1>
    <p>A Peoria-focused chimney information and lead-routing site built for homeowners who want fast, local help.</p>
  </div>
</section>
<section>
  <div class="container prose" style="max-width:48rem">
    <p>{BRAND} exists to make it easy for people in Peoria and nearby communities to find chimney sweeping, inspections, repairs, and dryer vent cleaning without wading through national directories.</p>
    <p>We publish clear local pages for the services and towns people actually search — then connect serious inquiries to qualified local technicians who can do the work.</p>
    <h2>Our standards</h2>
    <ul>
      <li>Safety-first recommendations aligned with common industry guidance (including annual inspection mindset)</li>
      <li>Respect for your home — floor protection and clean work habits</li>
      <li>Plain English findings instead of scare tactics</li>
      <li>Coverage across the Peoria metro, not just downtown</li>
    </ul>
    <p><a class="btn btn-primary" href="/contact/">Contact us</a></p>
  </div>
</section>
"""
    write("about/index.html", base(
        f"About {BRAND}",
        f"About {BRAND} — local chimney sweep and fireplace safety resources for Peoria, Illinois.",
        "/about/",
        about_body,
    ))

    privacy_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a> · Privacy</div>
    <h1>Privacy Policy</h1>
    <p>How we handle contact information submitted on this site.</p>
  </div>
</section>
<section>
  <div class="container prose" style="max-width:48rem">
    <p>Last updated: {TODAY}</p>
    <p>When you submit a form or call the number on this website, you provide contact details so we can respond about chimney or dryer-vent services. We use that information to schedule, follow up, and improve response quality.</p>
    <h2>What we collect</h2>
    <ul>
      <li>Name, phone, email, city/ZIP, and service notes you submit</li>
      <li>Basic technical logs common to websites (e.g., IP, browser) via hosting</li>
    </ul>
    <h2>Sharing</h2>
    <p>Inquiry details may be shared with the local service partner assigned to fulfill your request. We do not sell personal information as a standalone data product.</p>
    <h2>Contact</h2>
    <p>Questions: call <a data-phone-link="text" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
  </div>
</section>
"""
    write("privacy/index.html", base(
        "Privacy Policy | " + BRAND,
        "Privacy policy for Peoria Chimney Sweep contact forms and calls.",
        "/privacy/",
        privacy_body,
    ))


def build_meta_files() -> None:
    urls = ["/", "/contact/", "/about/", "/privacy/", "/blog/", "/areas/"]
    urls += [f"/services/{s['slug']}/" for s in SERVICES]
    urls += [f"/areas/{a[0]}/" for a in AREAS]
    urls += [f"/blog/{p['slug']}/" for p in BLOG_POSTS]

    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        loc = DOMAIN.rstrip("/") + (u if u != "/" else "/")
        priority = "1.0" if u == "/" else ("0.9" if u.startswith("/services/") else "0.7")
        sitemap.append(
            f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>{priority}</priority></url>"
        )
    sitemap.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap), encoding="utf-8")
    print("wrote sitemap.xml")

    robots = f"""User-agent: *
Allow: /

Sitemap: {DOMAIN.rstrip('/')}/sitemap.xml
"""
    (ROOT / "robots.txt").write_text(robots, encoding="utf-8")
    print("wrote robots.txt")

    # favicon svg
    fav = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="12" fill="#1a2744"/>
  <path d="M18 46V22l14-10 14 10v24H18z" fill="#b33a2b"/>
  <rect x="28" y="34" width="8" height="12" fill="#f7f3eb"/>
  <path d="M32 8c0 0 6 6 6 11a6 6 0 1 1-12 0c0-5 6-11 6-11z" fill="#e8a17a"/>
</svg>
"""
    (ROOT / "favicon.svg").write_text(fav, encoding="utf-8")

    # CNAME placeholder note + README
    readme = f"""# {BRAND} — Rank & Rent POC

**Niche:** Chimney sweep / chimney cleaning  
**Market:** Peoria, IL metro (East Peoria, Pekin, Washington, Morton, …)  
**Model:** Rank-and-rent local lead gen (Kyle / website landlord style)

## Why this niche+city
- Live SERP showed directories (Yelp) and aging local sites ranking for core terms
- High intent + solid job value (sweep/inspection/repair)
- Multiple local contractors to rent leads to once traffic arrives
- Exact-match style domains appeared available at research time (verify at registrar)

## Target keywords
- Primary: `chimney sweep peoria il`, `chimney cleaning peoria`
- Secondary: `chimney inspection peoria`, `creosote removal peoria`, `chimney cap peoria`
- Geo expansions: East Peoria, Pekin, Washington, Morton, Dunlap, etc.
- Adjacent: `dryer vent cleaning peoria il`

## Stack
- Static HTML/CSS/JS (fast, crawlable, cheap hosting)
- Schema.org LocalBusiness + Service + FAQ + BlogPosting
- Lead form (mailto/localStorage fallback; wire Formspree/CallRail next)
- Phone placeholder: `{PHONE_DISPLAY}` — replace with CallRail/Twilio tracking number

## Publish
GitHub Pages (project or user site) or Cloudflare Pages/Netlify.
Custom domain candidate: `chimneysweeppeoriail.com` (confirm availability before purchase).

## Post-launch SEO (required for page-1)
1. Buy domain + set DNS to host
2. Google Search Console verify + submit sitemap
3. Replace phone with tracking number + call recording
4. Wire form to email/CRM
5. Citations: GBP (if eligible), Apple Business Connect, Bing Places, Yelp, BBB, Angi — NAP consistent
6. 5–15 local backlinks / sponsorships / chamber / home-services directories over time
7. Monthly content + seasonal posts (pre-winter)

## Honest ranking note
Publishing alone does **not** guarantee positions 1–3. This POC is built to *compete* in a weak local SERP; rankings typically take weeks–months of indexing, content, and links. We track baselines after go-live.

## Rebuild
```bash
python build.py
```
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")

    # research notes
    notes = f"""# POC selection notes — {TODAY}

## Chosen: Chimney Sweep · Peoria, IL

### SERP evidence (browser scan, Aug 2026)
Query `chimney sweep peoria il` showed:
- Yelp directory in top organic
- Local operators with thin/dated sites (e.g. Chimney Doctor, Excel Fireplace GoDaddy-era site)
- National/template city pages (Shamrock) and some stronger local SEO sites also present

Opportunity is **not** zero-competition, but competitors are beatable with a focused, fast, content-complete site + basic off-page.

### Alternatives considered
| Pair | Signal |
|------|--------|
| Dryer vent Fort Wayne | Dedicated local sites already ranking (Vickie's, Old Smokey's) |
| Stump grinding Peoria | Facebook page in top results — weak web presence, good secondary niche |
| Power washing Peoria/Eugene | Several dedicated local sites |
| Crawl space Peoria | Franchise/national players strong |

### Monetization path
1. Rank for sweep/cleaning + inspection terms
2. Capture calls/forms via tracking number
3. Free trial week to 2–3 local chimney companies
4. Flat monthly rent once ROI is obvious ($500–1500/mo range depending on call volume)

### Phone
Placeholder `{PHONE_DISPLAY}` must be replaced before real lead routing.
"""
    (ROOT / "POC-NOTES.md").write_text(notes, encoding="utf-8")


def main() -> None:
    build_home()
    build_services()
    build_areas()
    build_blog()
    build_static_pages()
    build_meta_files()
    print("DONE", ROOT)


if __name__ == "__main__":
    main()
