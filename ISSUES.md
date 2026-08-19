# ISSUES — Peoria Chimney Sweep POC

Agreed with Amir on 2026-08-19 after full site inspection. Work these in order.

## Open issues (work now / next sessions)

### 5. Expand thin pages
Pages that are too short to rank or convince:
- `services/chimney-cap-installation/` (~193 words)
- `services/creosote-removal/` (~205 words)
- `services/dryer-vent-cleaning/` (~213 words)
- All 5 blog posts (148–220 words; need 600–900 each)
- `about/` (~101 words; trust page)

Rules: plain local-business voice, no em dashes, no SEO jargon, no invented
credentials. Run banned-term scan before push.

### 6. Deepen top 4 town pages
`areas/east-peoria/`, `areas/pekin/`, `areas/washington/`, `areas/morton/`
are 95% identical to each other (doorway-page risk). Rewrite each with
genuinely local content (housing stock age, masonry/weather specifics,
400–500 words). Leave small towns (Dunlap, Metamora, etc.) as-is.

### 7. Photos + og:image share card
- Site has zero photos except logo.svg. Add 2–3 real-subject stock photos
  (fireplace, chimney exterior, cap) on home + main service pages.
  Unsplash/Pexels, commercial-use. No fake "our work" captions.
- Create 1200x630 og:image card; add og:image meta on all pages via build.py.
- Point LocalBusiness schema `image` at the card instead of favicon.svg.
- Amir approves photo choices before push.

### 8. Services hub page + breadcrumb fix
- `/services/` returns 404; create hub page (heading + intro + 6 service
  cards reusing existing copy + sidebar form).
- Service-page breadcrumb "Services" link currently points to itself; point
  it at the new hub.
- Add hub to sitemap.xml; add BreadcrumbList JSON-LD to service pages.

## Publish-day checklist (when site moves to real domain)

Amir's framing: github.io = staging. These fire when the real domain goes live.

- [ ] Analytics: install GA4 (or chosen tool) in build.py, rebuild, push,
      then VERIFY hits appear in the dashboard. Data only counts forward.
- [ ] Form wiring: set FORM_ENDPOINT in js/main.js (Formspree/Getform) and
      replace the guessed backup address `leads@chimneysweeppeoriail.com`
      in js/main.js with a real address on the purchased domain (or Gmail).
      Grep the whole repo for the old guessed domain.
- [ ] Set BASE="" and DOMAIN in build.py, rebuild, verify canonical/sitemap
      hosts match new domain.
- [ ] Replace placeholder phone (309) 555-0148 with tracking number in
      build.py + js/main.js.
- [ ] Google Search Console: verify property, submit sitemap.

## Struck by Amir (2026-08-19, revisit at his call)
- Form endpoint now (folded into publish-day)
- CallRail/phone now (folded into publish-day)
- GSC now (folded into publish-day)
- Domain purchase timing
