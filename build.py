#!/usr/bin/env python3
"""Build static rank-and-rent site: Chimney Sweep Peoria IL."""
from __future__ import annotations

from pathlib import Path
import json
from datetime import date

ROOT = Path(__file__).resolve().parent
TODAY = date.today().isoformat()
SITE_NAME = "Peoria Chimney Sweep"
# Live on GitHub Pages until custom domain is connected.
# Custom domain candidate: https://chimneysweeppeoriail.com
DOMAIN = "https://pitangu.github.io/peoria-chimney-sweep-poc"
BASE = "/peoria-chimney-sweep-poc"  # "" if hosting at domain root
PHONE_DISPLAY = "(309) 555-0148"
PHONE_TEL = "+13095550148"
BRAND = "Peoria Chimney Sweep"
CITY = "Peoria"
STATE = "IL"
GEO_REGION = "US-IL"
LAT, LNG = "40.6936", "-89.5890"

def u(path: str) -> str:
    """Prefix site paths for project-page or root hosting."""
    if not path.startswith("/"):
        path = "/" + path
    if path == "/":
        return BASE + "/" if BASE else "/"
    return BASE + path


NAV = [
    ("Home", u("/")),
    ("Chimney Sweep", u("/services/chimney-sweep/")),
    ("Chimney Inspection", u("/services/chimney-inspection/")),
    ("Installation & Repair", u("/services/chimney-repair/")),
    ("Dryer Vent Cleaning", u("/services/dryer-vent-cleaning/")),
    ("Service Areas", u("/areas/")),
    ("Blog", u("/blog/")),
    ("Contact", u("/contact/")),
]

AREAS = [
    ("peoria", "Peoria", "Peoria, IL is our home base. We serve wood, gas, and pellet fireplaces across the city, from the West Bluff to North Peoria and near Bradley University."),
    ("east-peoria", "East Peoria", "East Peoria homeowners along the Illinois River deal with freeze-thaw stress on masonry. We sweep, inspect, and repair chimneys throughout East Peoria."),
    ("pekin", "Pekin", "Pekin, IL homes with older masonry chimneys need annual creosote removal before heating season. Local chimney sweep and inspection for Pekin residents."),
    ("washington", "Washington", "Washington, IL chimney cleaning, Level 1-2 inspections, caps, and tuckpointing for residential fireplaces and inserts."),
    ("morton", "Morton", "Morton, IL chimney sweep and fireplace safety services - creosote cleaning, camera inspections, and masonry repairs."),
    ("dunlap", "Dunlap", "Dunlap and north-metro homes: professional chimney sweeping, dryer vent cleaning, and safety inspections."),
    ("metamora", "Metamora", "Metamora chimney services including sweep, cap installation, and flue inspections for wood-burning systems."),
    ("peoria-heights", "Peoria Heights", "Peoria Heights chimney cleaning and repair with careful indoor protection for finished homes."),
    ("germantown-hills", "Germantown Hills", "Germantown Hills fireplace and chimney maintenance - sweep, inspection, waterproofing, and liner checks."),
    ("chillicothe", "Chillicothe", "Chillicothe, IL chimney sweep and creosote removal for river-area homes heading into winter."),
]

SERVICES = [
    {
        "slug": "chimney-sweep",
                "name": "Chimney Sweep",
                "title": "Chimney Sweep Peoria IL | Chimney Cleaning",
                "h1": "Chimney Sweep in Peoria, IL",
                "meta": "Chimney sweep and cleaning in Peoria, IL. Creosote removal and careful indoor cleanup. Call " + PHONE_DISPLAY + ".",
                "icon": "SW",
                "summary": "Chimney cleaning that removes creosote and soot so your fireplace drafts properly.",
                "body_extra": """
        <h2>Why get a yearly sweep</h2>
        <p>Central Illinois winters mean heavy fireplace use. Every wood fire leaves behind creosote - a flammable byproduct that builds up inside the flue. Industry guidance (NFPA 211) recommends chimneys be inspected at least once a year and cleaned when needed. A professional chimney sweep in Peoria, IL reduces chimney-fire risk, improves draft, and keeps smoke where it belongs.</p>
        <h2>What a standard sweep includes</h2>
        <ul>
        <li>Indoor floor protection and careful setup before work starts</li>
        <li>HEPA-style vacuum containment to limit soot in living spaces</li>
        <li>Brushing of flue, smoke chamber, and firebox as accessible</li>
        <li>Removal of soot, creosote, and loose debris</li>
        <li>Visual check for obvious damage, blockages, or animal nesting</li>
        <li>Plain-English notes on what we found and any recommended next steps</li>
        </ul>
        <h2>On service day</h2>
        <ol class="process-list">
        <li><strong>Confirm scope</strong> - wood vs gas, last service date, and symptoms (smoke, odor, slow draft).</li>
        <li><strong>Protect the home</strong> - cover work paths and set up vacuum containment.</li>
        <li><strong>Clean the system</strong> - brush and remove buildup from accessible flue paths.</li>
        <li><strong>Review findings</strong> - walk through results and only recommend repairs that matter for safety or function.</li>
        </ol>
        <h2>Signs you may need service now</h2>
        <ul>
        <li>It has been more than 12 months since your last cleaning</li>
        <li>Smoke spills into the room when you burn</li>
        <li>Strong creosote or musty odor, especially after rain</li>
        <li>White staining (efflorescence) on exterior brick</li>
        <li>Animals or birds nesting near the flue opening</li>
        </ul>
        <div class="callout"><strong>Local tip:</strong> Peoria's freeze-thaw cycles crack crowns and loosen mortar. Pair your sweep with a quick exterior look before the first hard freeze.</div>
        <h2>Chimney sweep FAQs - Peoria, IL</h2>
        <div class="faq">
        <details><summary>How long does a chimney cleaning take?</summary><p>Many single-flue residential sweeps take about 45-90 minutes on site. Heavy creosote, multiple flues, or difficult access can take longer.</p></details>
        <details><summary>Will there be soot in my house?</summary><p>Technicians use floor protection and vacuum containment. Living spaces should stay clean; you may notice temporary equipment in the work area.</p></details>
        <details><summary>Do gas fireplaces need sweeping?</summary><p>Gas systems usually produce less creosote than wood, but they still need periodic inspection for venting, corrosion, animals, and safety.</p></details>
        </div>
        """,
            },
    {
        "slug": "chimney-inspection",
                "name": "Chimney Inspection",
                "title": "Chimney Inspection Peoria IL | NFPA 211",
                "h1": "Chimney Inspection in Peoria, IL",
                "meta": "NFPA 211 chimney inspections in Peoria, IL. Clear report and direct quote if repairs are needed. Call " + PHONE_DISPLAY + ".",
                "icon": "IN",
                "summary": "NFPA 211 style inspections, a clear report, and a direct quote if work is needed.",
                "body_extra": """
        <h2>When to get an inspection in Peoria</h2>
        <p>Buyers, sellers, and careful homeowners across the Peoria metro use chimney inspections to catch hidden problems before they become expensive repairs - or safety hazards. The inspection level should match your situation.</p>
        <h2>Level 1 vs Level 2</h2>
        <ul>
        <li><strong>Level 1:</strong> Routine annual check when nothing major has changed - readily accessible portions of the chimney and appliance.</li>
        <li><strong>Level 2:</strong> Common after a home sale, weather event, or system change. Often includes more of the accessible chimney structure and may use camera scanning of flues when needed.</li>
        </ul>
        <h2>What's included</h2>
        <ul>
        <li>Inspection work aligned with NFPA 211 levels (Level 1 / Level 2 as needed)</li>
        <li>A clear written report of findings</li>
        <li>Photos of problem areas when present</li>
<li>A direct quote if repair or follow-up work is recommended</li>
        </ul>
        <h2>How the inspection goes</h2>
        <ol class="process-list">
        <li><strong>Intake</strong> - home sale, annual check, smoke issues, or storm damage?</li>
        <li><strong>On-site evaluation</strong> - accessible interior and exterior components as the level requires.</li>
        <li><strong>Findings review</strong> - clear summary of what is fine, what to watch, and what needs repair.</li>
        </ol>
        <div class="callout"><strong>Note:</strong> The tech on site will explain what they can see and what they recommend.</div>
        <h2>Questions</h2>
        <div class="faq">
        <details><summary>Do I need an inspection before selling my Peoria home?</summary><p>Many buyers and inspectors flag fireplace/chimney condition. A Level 2-style inspection is commonly requested around real-estate transactions.</p></details>
        <details><summary>Is camera scanning always included?</summary><p>Not always. Camera use depends on access, inspection level, and whether interior flue conditions need a closer look.</p></details>
        <details><summary>What if repairs are recommended?</summary><p>You get prioritized options. Safety items come first; cosmetic or longer-term maintenance is labeled clearly.</p></details>
        </div>
        """,
            },
    {
        "slug": "chimney-repair",
                "name": "Chimney Installation and Repair",
                "title": "Chimney Installation and Repair Peoria IL",
                "h1": "Chimney Installation and Repair in Peoria, IL",
                "meta": "Chimney installation and repair in Peoria, IL: new work, caps, crowns, tuckpointing, flashing, and waterproofing. Call " + PHONE_DISPLAY + ".",
                "icon": "RP",
                "summary": "New installs plus caps, crowns, mortar repair, and waterproofing.",
                "body_extra": """
        <h2>Installation and common repairs around Peoria</h2>
        <p>We handle new chimney and fireplace-related installs when needed, plus repairs on existing systems. Water is the enemy of masonry. Rain, snow, and freeze-thaw cycles around Peoria open mortar joints, crack crowns, and rust dampers. Small repairs now often prevent full rebuilds later.</p>
        <ul>
        <li>Chimney and related fireplace system installation</li>
<li>Chimney cap installation (animals, rain, embers)</li>
        <li>Crown repair and rebuild</li>
        <li>Tuckpointing and brick replacement</li>
        <li>Flashing repair at the roof line</li>
        <li>Breathable masonry waterproofing</li>
        <li>Damper repair or top-sealing dampers</li>
        </ul>
        <h2>How repair jobs usually go</h2>
        <ol class="process-list">
        <li><strong>Identify the failure</strong> - leak path, crown cracks, missing cap, bad flashing, or deteriorated mortar.</li>
        <li><strong>Scope the fix</strong> - safety and water intrusion first; optional upgrades labeled clearly.</li>
        <li><strong>Complete the work</strong> - materials matched to the job; cleanup when finished.</li>
        <li><strong>Prevention tips</strong> - what to watch next season so the same issue doesn't return quickly.</li>
        </ol>
        <h2>Why waiting costs more</h2>
        <p>Moisture inside the flue damages liners and can migrate into attics and living spaces. If a sweep or inspection flags masonry issues, fixing them before winter is usually the lower-cost path.</p>
        <div class="faq">
        <details><summary>Can you repair just the cap?</summary><p>Often yes. A quality cap is one of the highest-ROI small repairs for keeping water and animals out.</p></details>
        <details><summary>Do you handle full rebuilds?</summary><p>Scope depends on the technician and job complexity. Severe structural work may require specialized masonry scheduling.</p></details>
        </div>
        """,
            },
    {
        "slug": "chimney-cap-installation",
        "name": "Chimney Cap Installation",
        "title": "Chimney Cap Installation Peoria IL",
        "h1": "Chimney Cap Installation in Peoria, IL",
        "meta": "Chimney cap installation in Peoria, IL. Keep rain, animals, and debris out of your flue. Stainless options available. Call " + PHONE_DISPLAY + ".",
        "icon": "CP",
        "summary": "A proper cap keeps rain, raccoons, and leaves out - and sparks in.",
        "body_extra": """
<h2>Why caps matter</h2>
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
        "icon": "CR",
        "summary": "Targeted creosote cleaning - including harder glazed stages - to lower chimney-fire risk.",
        "body_extra": """
<h2>Creosote stages</h2>
<ul>
<li><strong>Stage 1:</strong> Dusty, flaky soot - standard brushing usually handles it.</li>
<li><strong>Stage 2:</strong> Harder, tar-like flakes that need thorough mechanical cleaning.</li>
<li><strong>Stage 3:</strong> Glazed, shiny coating that can require specialized removal methods.</li>
</ul>
<p>Burning wet wood, smoldering overnight fires, and restricted air supply speed up creosote growth. If your Peoria chimney hasn't been serviced in years, start with an inspection plus sweep.</p>
""",
    },
    {
        "slug": "dryer-vent-cleaning",
        "name": "Dryer Vent Cleaning",
        "title": "Dryer Vent Cleaning Peoria IL | Lint Fire Prevention",
        "h1": "Dryer Vent Cleaning in Peoria, IL",
        "meta": "Dryer vent cleaning in Peoria, IL. Remove lint buildup, cut fire risk, and help clothes dry faster. Call " + PHONE_DISPLAY + ".",
        "icon": "DV",
        "summary": "Lint removal from dryer ducts - safer laundry rooms and shorter dry times.",
        "body_extra": """
<h2>Why dryer vents clog</h2>
<p>Even if you clean the lint screen every load, lint collects in the duct run - especially on long routes through crawlspaces or multi-story homes common around Peoria.</p>
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
<p>If you burn wood through a Central Illinois winter, your chimney works hard. The short answer most Peoria homeowners need: <strong>inspect every year, clean when the inspection says so</strong> - often annually for frequent wood burners.</p>
<h2>NFPA guidance in plain English</h2>
<p>NFPA 211 calls for chimneys and vents to be inspected at least once a year. Cleaning frequency depends on fuel type, how often you burn, and how much creosote has built up. Gas systems still need inspections even when they produce less creosote than wood.</p>
<h2>Peoria-specific factors</h2>
<ul>
<li>Long heating seasons mean more burn hours</li>
<li>Freeze-thaw weather stresses crowns and mortar</li>
<li>Older housing stock may have aging liners or caps</li>
</ul>
<h2>Don't wait for these warning signs</h2>
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
<p>Creosote is the dark, tar-like residue left when wood smoke cools inside a flue. It is flammable. When enough accumulates, a normal fire can ignite the deposit - a chimney fire that can exceed 2,000°F.</p>
<h2>What increases creosote</h2>
<ul>
<li>Burning unseasoned (wet) wood</li>
<li>Smoldering, low-air overnight burns</li>
<li>Restricted air supply or undersized flues</li>
<li>Long gaps between professional cleanings</li>
</ul>
<h2>Prevention that actually works</h2>
<p>Burn dry hardwood, give the fire enough air, and book a professional <a href="/services/chimney-sweep/">chimney sweep in Peoria, IL</a> on a regular schedule. If glazed creosote is present, standard light brushing may not be enough - ask for a full evaluation.</p>
""",
    },
    {
        "slug": "signs-you-need-chimney-cap",
        "title": "5 Signs Your Peoria Chimney Needs a Cap",
        "meta": "Rain entry, animals, leaves, and sparks - signs a chimney cap belongs on your Peoria home.",
        "date": "2026-08-10",
        "html": """
<p>A chimney cap is one of the cheapest upgrades that prevents expensive damage. Here's when Peoria homeowners should act.</p>
<ol>
<li><strong>Water in the firebox after storms</strong> - open flues catch rain and melting snow.</li>
<li><strong>Birds, squirrels, or raccoons</strong> - warm flues are prime nesting spots.</li>
<li><strong>Leaves and debris smells</strong> - organic material in the flue is a fire hazard.</li>
<li><strong>Ember concerns on wooded lots</strong> - mesh spark arrestors help keep embers contained.</li>
<li><strong>No cap on a visual roof check</strong> - many older homes never received one.</li>
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
        "title": "Dryer Vent Cleaning vs Chimney Cleaning: What's the Difference?",
        "meta": "Both prevent home fires, but dryer vents and chimneys need different tools and schedules.",
        "date": "2026-08-15",
        "html": """
<p>Homeowners sometimes confuse the two. Both remove combustible buildup - lint in dryer ducts, creosote in chimneys - but the systems are different.</p>
<table>
<thead><tr><th></th><th>Chimney</th><th>Dryer vent</th></tr></thead>
<tbody>
<tr><td>Hazard</td><td>Creosote / chimney fire / CO</td><td>Lint fire / overheating</td></tr>
<tr><td>Typical schedule</td><td>Annual inspection</td><td>Every 1-2 years (more if heavy use)</td></tr>
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
      <div><label for="message">What's going on?</label><textarea id="message" name="message" placeholder="e.g. annual sweep, smoke in room, home inspection…"></textarea></div>
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
        <option value="Chimney Installation and Repair">Chimney Installation and Repair</option>
        <option value="Chimney Cap">Chimney Cap</option>
        <option value="Creosote Removal">Creosote Removal</option>
        <option value="Dryer Vent Cleaning">Dryer Vent Cleaning</option>
        <option value="Not sure">Not sure / call me</option>
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
    def fix(html: str) -> str:
        """Rewrite root-absolute URLs for GitHub project Pages base path."""
        if not BASE:
            return html
        out = []
        i = 0
        while True:
            # find href=" or src="
            j1 = html.find('href="', i)
            j2 = html.find('src="', i)
            candidates = [j for j in (j1, j2) if j >= 0]
            if not candidates:
                out.append(html[i:])
                break
            j = min(candidates)
            out.append(html[i:j])
            # attribute
            if html.startswith('href="', j):
                attr = 'href="'
            else:
                attr = 'src="'
            k = j + len(attr)
            end = html.find('"', k)
            url = html[k:end]
            if url.startswith('/') and not url.startswith('//') and not url.startswith(BASE + '/') and url != BASE and not url.startswith(BASE + '?'):
                if url == '/':
                    url = BASE + '/'
                else:
                    url = BASE + url
            out.append(attr + url + '"')
            i = end + 1
        return ''.join(out)
        # avoid double-prefixing
        html = html.replace(BASE + BASE, BASE)
        for attr in ("href", "src"):
            html = html.replace(f'{attr}="/', f'{attr}="{BASE}/')
            # fix accidental double base
            html = html.replace(f'{attr}="{BASE}{BASE}/', f'{attr}="{BASE}/')
        return html
    nav_html = "\n".join(
        f'<li><a href="{href}">{label}</a></li>' for label, href in NAV
    )
    services_footer = "\n".join(
        f'<li><a href="/services/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES
    )
    areas_footer = "\n".join(
        f'<li><a href="/areas/{a[0]}/">{a[1]}, IL</a></li>' for a in AREAS[:6]
    )
    return fix(f"""<!DOCTYPE html>
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
                  <img class="logo-mark" src="/images/logo.svg" width="42" height="42" alt="" decoding="async">
                  <div>{BRAND}<span>Chimney Sweep · Peoria, IL</span></div>
                </a>
        <div class="header-actions">
          <a class="btn btn-primary header-call" data-phone-link="text" href="tel:{PHONE_TEL}">Call Now</a>
          <button type="button" class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="primary-nav">
            <span class="nav-toggle-bars" aria-hidden="true"></span>
          </button>
        </div>
        <nav id="primary-nav" class="primary-nav" aria-label="Primary">
          <ul>
            {nav_html}
            <li class="nav-call-item"><a class="btn btn-primary" data-phone-link="text" href="tel:{PHONE_TEL}">Call Now</a></li>
          </ul>
        </nav>
      </div>
    </header>
    <main>
      {body}
    </main>
    <div class="mobile-call-bar" role="region" aria-label="Quick call">
      <a class="btn btn-primary btn-block" data-phone-link href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
      <a class="btn btn-secondary btn-block" href="/contact/">Free Callback</a>
    </div>
  <section class="cta-band">
    <div class="container">
      <h2>Need a chimney sweep near Peoria?</h2>
      <p>Request a callback or call <strong>{PHONE_DISPLAY}</strong>. Cleaning, inspections, and repairs.</p>
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
        <p>Chimney cleaning, inspections, repairs, and dryer vent service for Peoria-area homes.</p>
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
""")


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
            "Most standard cleanings are a few hundred dollars. Price depends on access, buildup, and whether you also need an inspection or repairs. Call for a quote.",
        ),
        (
            "How long does it take?",
            "Often 45 to 90 minutes for one flue. Heavy creosote or more than one flue takes longer.",
        ),
        (
            "Do gas fireplaces need service?",
            "Yes. They make less creosote than wood, but vents still need checks for blockages, corrosion, and safe draft.",
        ),
        (
            "Will there be soot in the house?",
            "The tech should cover floors and run a vacuum. You should not get soot tracked through the house.",
        ),
        (
            "Which towns do you cover?",
            "Peoria, East Peoria, Pekin, Washington, Morton, Dunlap, Metamora, Peoria Heights, Germantown Hills, Chillicothe, and nearby towns.",
        ),
        (
            "What happens after I call?",
            "We confirm your town and the job, set a time, then go over results when the work is done.",
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
          <a class="more" href="/services/{s['slug']}/">Learn more</a>
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
      <span class="eyebrow">Serving Peoria, IL and nearby towns</span>
      <h1>Chimney Sweep in Peoria, IL</h1>
      <p class="lede">Chimney cleaning, inspections, repairs, and dryer vent cleaning for Peoria-area homes. Call for an appointment or request a callback.</p>
      <ul class="hero-points">
        <li>We work clean: floors covered, soot vacuumed</li>
        <li>You get a clear report of what we found</li>
        <li>Wood, gas, and pellet systems</li>
        <li>Often same-week openings in season</li>
      </ul>
      <div class="hero-ctas">
        <a class="btn btn-primary btn-lg" data-phone-link href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
        <a class="btn btn-secondary btn-lg" href="#quote">Request a Callback</a>
      </div>
      <div class="trust-row">
        <span><strong>Yearly</strong> safety checks</span>
        <span><strong>Wood, gas, pellet</strong></span>
        <span><strong>Peoria metro</strong></span>
      </div>
    </div>
    <div class="quote-card" id="quote">
      <h2>Request a callback</h2>
      <p class="sub">Leave your number. We usually call back the same business day.</p>
      {lead_form(compact=True)}
    </div>
  </div>
</section>

<section class="trust-strip">
  <div class="container trust-strip-grid">
    <div class="trust-item">
      <strong>Call or form</strong>
      <p>Reach us by phone or the short form on this page.</p>
    </div>
    <div class="trust-item">
      <strong>Common jobs</strong>
      <p>Sweeps, inspections, caps, repairs, and dryer vents.</p>
    </div>
    <div class="trust-item">
      <strong>Clean work habits</strong>
      <p>Floors covered and soot vacuumed while we work.</p>
    </div>
    <div class="trust-item">
      <strong>Nearby towns</strong>
      <p>Peoria, East Peoria, Pekin, Washington, Morton, Dunlap, and more.</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>Services</h2>
      <p>Pick the job you need, or call if you are not sure.</p>
    </div>
    <div class="grid-3">{cards}</div>
  </div>
</section>

<section class="bg-navy">
  <div class="container grid-2">
    <div>
      <div class="section-head">
        <h2>How it works</h2>
        <p>Three simple steps.</p>
      </div>
      <div class="steps">
        <div class="step"><div class="step-num">1</div><div><h3>Call or send the form</h3><p>Tell us your town, wood, gas, or pellet, and the problem (smoke, smell, yearly cleaning, home sale, and so on).</p></div></div>
        <div class="step"><div class="step-num">2</div><div><h3>We schedule a visit</h3><p>A tech comes out, protects the work area, and does the cleaning or inspection you booked.</p></div></div>
        <div class="step"><div class="step-num">3</div><div><h3>You get the results</h3><p>If things look good, you are set. If something needs repair, we explain it in plain terms.</p></div></div>
      </div>
    </div>
    <div>
      <div class="section-head">
        <h2>Why yearly service matters here</h2>
        <p>Peoria winters are long. Creosote and freeze-thaw damage add up.</p>
      </div>
      <ul class="checklist">
        <li>Creosote can fuel chimney fires</li>
        <li>Blocked flues can push smoke and gases inside</li>
        <li>Open tops attract birds and animals</li>
        <li>Cracked crowns let water into the masonry</li>
        <li>Home sales often need a closer inspection</li>
      </ul>
      <p style="margin-top:1.25rem"><a class="btn btn-primary" href="/services/chimney-sweep/">Chimney sweep details</a></p>
    </div>
  </div>
</section>

<section class="bg-cream">
  <div class="container">
    <div class="section-head">
      <h2>What to expect</h2>
      <p>No hype. Just how a normal job should go.</p>
    </div>
    <div class="grid-3">
      <article class="card">
        <h3>Yearly check</h3>
        <p>Most homes should get the chimney looked at once a year. How often you clean depends on fuel type and how much you burn.</p>
      </article>
      <article class="card">
        <h3>Clean setup</h3>
        <p>Floors covered and soot vacuumed are part of a normal sweep, not an add-on.</p>
      </article>
      <article class="card">
        <h3>Straight answers</h3>
        <p>Safety items first. Optional work is labeled so you can decide.</p>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>Towns we serve</h2>
      <p>Peoria metro and nearby communities.</p>
    </div>
    <div class="area-pills">{area_pills}</div>
  </div>
</section>

<section class="bg-cream">
  <div class="container grid-2">
    <div>
      <div class="section-head">
        <h2>Common questions</h2>
        <p>Quick answers before you book.</p>
      </div>
      <div class="faq">{faq_html}</div>
    </div>
    <div class="card">
      <h3>Ready to schedule?</h3>
      <p>Call or send the form for chimney cleaning or an inspection in the Peoria area.</p>
      {lead_form()}
    </div>
  </div>
</section>
"""
    extra = json_ld_home() + json_ld_faq(faqs)
    write("index.html", base(
        "Chimney Sweep Peoria IL | Cleaning and Inspection",
        f"Chimney sweep and cleaning in Peoria, IL. Inspections, repairs, creosote removal, and dryer vent cleaning. Call {PHONE_DISPLAY}.",
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
    <p>Need <strong>{s['name'].lower()} in Peoria, IL</strong>? Call <a data-phone-link="text" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> or use the form. We will confirm timing and what the job includes.</p>
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
    <p>If you are in {name} and need a yearly cleaning, have smoke or odor issues, or need an inspection, we can help with:</p>
    <ul>{svc_links}</ul>
    <h2>Local weather note</h2>
    <p>Cold weather and freeze-thaw cycles are hard on masonry. Getting the chimney checked in {name} before winter helps catch creosote and water issues early. Selling a home? Ask about a fuller inspection.</p>
    <div class="callout"><strong>Serving {name} from the Peoria metro.</strong> Call <a data-phone-link="text" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> and mention you're in {name} for routing.</div>
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
          <a class="more" href="/blog/{p['slug']}/">Read article</a>
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
      <h2>Need a visit?</h2>
      <p class="sub">Request a callback</p>
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
    <p>Call <a data-phone-link="text" href="tel:{PHONE_TEL}" style="color:#fff;font-weight:700">{PHONE_DISPLAY}</a> or send the form - we cover Peoria and nearby towns.</p>
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
      <p>Monday-Friday 8:00 a.m. - 6:00 p.m.<br>Saturday by appointment during peak season</p>
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
    <p>Chimney cleaning and fireplace safety help for Peoria-area homeowners.</p>
  </div>
</section>
<section>
  <div class="container prose" style="max-width:48rem">
    <p>{BRAND} exists to make it easy for people in Peoria and nearby communities to find chimney sweeping, inspections, repairs, and dryer vent cleaning without wading through national directories.</p>
    <p>We help Peoria-area homeowners book chimney cleaning, inspections, repairs, and dryer vent service.</p>
    <h2>Our standards</h2>
    <ul>
      <li>Safety-first recommendations aligned with common industry guidance (including annual inspection mindset)</li>
      <li>Respect for your home - floor protection and clean work habits</li>
      <li>Plain English findings instead of scare tactics</li>
      <li>Coverage across the Peoria metro, not just downtown</li>
    </ul>
    <p><a class="btn btn-primary" href="/contact/">Contact us</a></p>
  </div>
</section>
"""
    write("about/index.html", base(
        f"About {BRAND}",
        f"About {BRAND} - local chimney sweep and fireplace safety resources for Peoria, Illinois.",
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
    readme = f"""# {BRAND} - Rank & Rent POC

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
- Phone placeholder: `{PHONE_DISPLAY}` - replace with CallRail/Twilio tracking number

## Publish
GitHub Pages (project or user site) or Cloudflare Pages/Netlify.
Custom domain candidate: `chimneysweeppeoriail.com` (confirm availability before purchase).

## Post-launch SEO (required for page-1)
1. Buy domain + set DNS to host
2. Google Search Console verify + submit sitemap
3. Replace phone with tracking number + call recording
4. Wire form to email/CRM
5. Citations: GBP (if eligible), Apple Business Connect, Bing Places, Yelp, BBB, Angi - NAP consistent
6. 5-15 local backlinks / sponsorships / chamber / home-services directories over time
7. Monthly content + seasonal posts (pre-winter)

## Honest ranking note
Publishing alone does **not** guarantee positions 1-3. This POC is built to *compete* in a weak local SERP; rankings typically take weeks-months of indexing, content, and links. We track baselines after go-live.

## Rebuild
```bash
python build.py
```
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")

    # research notes
    notes = f"""# POC selection notes - {TODAY}

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
| Stump grinding Peoria | Facebook page in top results - weak web presence, good secondary niche |
| Power washing Peoria/Eugene | Several dedicated local sites |
| Crawl space Peoria | Franchise/national players strong |

### Monetization path
1. Rank for sweep/cleaning + inspection terms
2. Capture calls/forms via tracking number
3. Free trial week to 2-3 local chimney companies
4. Flat monthly rent once ROI is obvious ($500-1500/mo range depending on call volume)

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
