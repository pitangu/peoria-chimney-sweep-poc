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

- [x] Domain purchased: `chimneysweeppeoriail.com` (GoDaddy, 2026-08-19)
- [x] Set BASE="" and DOMAIN=https://chimneysweeppeoriail.com in build.py,
      rebuild, CNAME file + GitHub Pages custom domain
- [ ] **You (GoDaddy DNS):** point the domain at GitHub Pages
      1. GoDaddy → Domain → chimneysweeppeoriail.com → DNS
      2. Delete parking / forwarding A records (currently 76.223.105.230
         and 13.248.243.5)
      3. Apex A records (host `@`):
         - 185.199.108.153
         - 185.199.109.153
         - 185.199.110.153
         - 185.199.111.153
      4. Optional IPv6 AAAA (host `@`):
         - 2606:50c0:8000::153
         - 2606:50c0:8001::153
         - 2606:50c0:8002::153
         - 2606:50c0:8003::153
      5. CNAME `www` → `pitangu.github.io`
      6. Save. Wait 5–30 minutes. Then open https://chimneysweeppeoriail.com/
      7. GitHub repo → Settings → Pages → Enforce HTTPS (once the lock is available)
- [x] Analytics: installed GA4 (gtag.js G-FM1TX0K0KD) across all pages in build.py,
      rebuilt, pushed and verified live. Data now tracks forward.
- [ ] Form wiring: set FORM_ENDPOINT in js/main.js (Formspree/Getform) and
      replace the guessed backup address `leads@chimneysweeppeoriail.com`
      in js/main.js with a real address on the purchased domain (or Gmail).
      Grep the whole repo for the old guessed domain.
- [ ] Replace placeholder phone (309) 555-0148 with tracking number in
      build.py + js/main.js.
- [ ] Google Search Console: verify property, submit sitemap.

## Struck by Amir (2026-08-19, revisit at his call)
- Form endpoint now (folded into publish-day)
- CallRail/phone now (folded into publish-day)
- GSC now (folded into publish-day)
- Domain purchase timing (done 2026-08-19)
