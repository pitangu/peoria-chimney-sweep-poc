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
DOMAIN = "https://pitangu.github.io/peoria-chimney-sweep"
BASE = "/peoria-chimney-sweep"  # "" if hosting at domain root
PHONE_DISPLAY = "(309) 555-0148"
PHONE_TEL = "+130****0148"
BRAND = "Peoria Chimney Sweep"
CITY = "Peoria"
STATE = "IL"
GEO_REGION = "US-IL"
LAT, LNG = "40.6936", "-89.5890"
OG_IMAGE = DOMAIN + "/images/og-card.jpg"


def u(path: str) -> str:
    """Prefix site paths for project-page or root hosting."""
    if not path.startswith("/"):
        path = "/" + path
    if path == "/":
        return BASE + "/" if BASE else "/"
    return BASE + path


NAV = [
    ("Home", u("/")),
    ("Services", u("/services/")),
    ("Areas", u("/areas/")),
    ("Blog", u("/blog/")),
    ("About", u("/about/")),
    ("Contact", u("/contact/")),
]

AREA_LINES = {
    "peoria": "Most of our week is in Peoria proper, from the older brick streets near the river out toward the north side. Winters run long here, and wood stoves work hard from November into March.",
    "east-peoria": "We're across the river in East Peoria all the time. Same-week slots are usually easier there than in Peoria proper.",
    "pekin": "Pekin has a lot of pre-1960 houses with older masonry chimneys. Those need a closer look before heating season, especially if nobody has opened the flue in years.",
    "washington": "Washington jobs often pair a yearly cleaning with a quick look at the cap and crown. Freeze-thaw hits those hard after a few rough winters.",
    "morton": "Morton is a regular stop for us. Plenty of wood-burners and inserts, and dryer vents on longer runs through finished basements.",
    "dunlap": "Newer builds around Dunlap more often have builder-grade prefab fireplace units. Those have their own vent and clearance issues compared with old brick stacks.",
    "metamora": "Metamora is a short hop out. If you burn wood most nights in winter, plan on a cleaning before the cold really sets in.",
    "peoria-heights": "Peoria Heights homes are often finished and carpeted inside, so we take floor protection seriously when we bring tools through the house.",
    "germantown-hills": "Germantown Hills has a lot of newer construction with prefab units. We still check draft, caps, and dryer vents the same way we do on older brick.",
    "chillicothe": "Chillicothe sits along the river corridor where damp air and freeze-thaw are hard on crowns and mortar. A fall check is worth it.",
}

AREA_NEIGHBORS = {
    "peoria": [("east-peoria", "East Peoria"), ("peoria-heights", "Peoria Heights")],
    "east-peoria": [("peoria", "Peoria"), ("washington", "Washington"), ("morton", "Morton")],
    "pekin": [("peoria", "Peoria"), ("east-peoria", "East Peoria"), ("morton", "Morton")],
    "washington": [("east-peoria", "East Peoria"), ("metamora", "Metamora")],
    "morton": [("east-peoria", "East Peoria"), ("washington", "Washington"), ("pekin", "Pekin")],
    "dunlap": [("peoria", "Peoria"), ("germantown-hills", "Germantown Hills")],
    "metamora": [("washington", "Washington"), ("germantown-hills", "Germantown Hills")],
    "peoria-heights": [("peoria", "Peoria"), ("east-peoria", "East Peoria")],
    "germantown-hills": [("dunlap", "Dunlap"), ("metamora", "Metamora"), ("washington", "Washington")],
    "chillicothe": [("peoria", "Peoria"), ("dunlap", "Dunlap")],
}

AREAS = [
    ("peoria", "Peoria", AREA_LINES["peoria"]),
    ("east-peoria", "East Peoria", AREA_LINES["east-peoria"]),
    ("pekin", "Pekin", AREA_LINES["pekin"]),
    ("washington", "Washington", AREA_LINES["washington"]),
    ("morton", "Morton", AREA_LINES["morton"]),
    ("dunlap", "Dunlap", AREA_LINES["dunlap"]),
    ("metamora", "Metamora", AREA_LINES["metamora"]),
    ("peoria-heights", "Peoria Heights", AREA_LINES["peoria-heights"]),
    ("germantown-hills", "Germantown Hills", AREA_LINES["germantown-hills"]),
    ("chillicothe", "Chillicothe", AREA_LINES["chillicothe"]),
]

AREA_DEEP = {
    "east-peoria": """
<p>East Peoria sits across the Illinois River from Peoria. That river air and the freeze-thaw cycle are rough on brick and mortar. If your chimney crown is cracked, water gets in, freezes, and the crack grows every winter.</p>
<p>A lot of calls from this side of the river are simple: it has been a few years since anyone cleaned the flue, the fireplace smells after rain, or a home inspection flagged the chimney during a sale. Those are normal. We would rather catch creosote and water problems in the fall than after the first hard freeze.</p>
<p>When we come out, we cover floors, vacuum while we work, and tell you what we found in plain terms. If the job is only a cleaning, that is what we do. If the cap is missing or the crown is shot, you get a straight quote. No scare routine.</p>
<p>Wood burners work hard here from roughly November through March. That is when creosote builds fastest. Gas units make less creosote, but animals still nest in open tops, and vents still need a look. Raccoons and chimney swifts are common in Illinois in spring if the flue is open.</p>
<p>We also cover Washington and Morton just up the road, so getting to East Peoria is easy most weeks.</p>
""",
    "pekin": """
<p>Pekin has a lot of older housing stock, including plenty of pre-1960 homes with masonry chimneys. Older brick can look fine from the yard and still have soft mortar, a tired liner, or a crown that has been patched once too often.</p>
<p>If you burn wood most of the winter, plan on a yearly check. Creosote does not care that the fireplace "still draws." It builds up quietly. Glazed creosote is worse. That shiny stage needs more than a light brush.</p>
<p>Home sales in town often trigger a closer inspection. Level 1 is the routine yearly look. Level 2 is common when a house is changing hands or something on the system changed. We write down what we see and price repair work only if it is actually needed.</p>
<p>Freeze-thaw along the river valley is hard on crowns. Water gets in the cracks, freezes, and the damage spreads. A cap keeps rain and animals out. Without one, raccoons and birds treat a warm flue like a nest box in spring.</p>
<p>We also cover Peoria and East Peoria nearby if your family has houses on both sides of the river.</p>
""",
    "washington": """
<p>Washington sits northeast of Peoria and gets the same long heating season as the rest of the metro. Wood stoves and inserts work hard from late fall into early spring, which is exactly when creosote builds up in the flue.</p>
<p>A lot of what we see here is preventable. No cleaning for a few years. A missing or rusted cap. A crown with hairline cracks that open wider after each freeze. None of that needs a panic call, but it does need a real look before you light up for the season.</p>
<p>If you are buying or selling, ask for a proper inspection, not just a quick glance. You should leave with a clear report. If something needs work, you should leave with a number, not a vague "we should talk later."</p>
<p>Newer neighborhoods mix masonry stacks with prefab fireplace units. Prefab systems have their own clearances and vent rules. Older brick needs mortar and crown attention. Either way, floors get covered and soot gets vacuumed while we work.</p>
<p>We also cover Metamora and East Peoria just up the road.</p>
""",
    "morton": """
<p>Morton is a steady stop for chimney and dryer vent work. Plenty of homes burn wood or run inserts through the winter, and finished basements often mean longer dryer vent runs that pack with lint.</p>
<p>Chimney calls here are usually about smell, smoke in the room, or a calendar that says it has been too long since the last cleaning. Dryer vent calls are usually about clothes that take forever to dry or a laundry room that feels too hot. Both are fire-risk issues if you ignore them.</p>
<p>Illinois winters are long enough that a November cleaning is not early. Creosote from wood smoke cools and sticks in the flue. Caps keep rain and animals out. Open tops invite raccoons and chimney swifts in spring.</p>
<p>We work clean inside the house, then tell you what matters. Safety items first. Optional work labeled so you can decide. If a full rebuild is beyond what makes sense on site, we will say that instead of improvising.</p>
<p>We also cover East Peoria and Washington nearby.</p>
""",
}

SERVICES = [
    {
        "slug": "chimney-sweep",
        "name": "Chimney Sweep",
        "title": "Chimney Sweep Peoria IL | Chimney Cleaning",
        "h1": "Chimney Sweep in Peoria, IL",
        "meta": "Chimney sweep and cleaning in Peoria, IL. Creosote removal and careful indoor cleanup. Call " + PHONE_DISPLAY + ".",
        "summary": "Yearly cleaning that pulls creosote and soot so the fireplace drafts the way it should.",
        "opener": "If you burn wood through a Peoria winter, creosote builds up in the flue whether you think about it or not. A cleaning once a year keeps it from becoming a fire risk. Here is what we actually do when we come out.",
        "body_extra": """
<img class="content-photo" src="/images/sweep-fireplace.jpg" width="1000" height="667" alt="Brick fireplace and hearth inside a home" loading="lazy" decoding="async">
<h2>Why get a yearly sweep</h2>
<p>Winters around here run roughly November through March. That is a long stretch of wood burning for a lot of houses. Every fire leaves creosote in the flue. NFPA 211 says chimneys should be inspected at least once a year and cleaned when needed. That is not marketing. That is how you keep a normal fire from turning into a flue fire.</p>
<p>Older brick near central Peoria often has soft mortar and tired liners. Newer prefab units in places like Dunlap have different problems, but they still need a look. Either way, waiting until you smell smoke in the living room is the expensive order of operations.</p>
<h2>What a standard sweep includes</h2>
<ul>
<li>Floor covers on the path and around the hearth</li>
<li>Vacuum running while we brush so soot stays contained</li>
<li>Brushing of the flue, smoke chamber, and firebox as far as we can reach</li>
<li>Removal of soot, creosote, and loose debris</li>
<li>A quick look for damage, blockages, or animal nesting</li>
<li>Plain notes on what we found and what can wait</li>
</ul>
<h2>On service day</h2>
<ol class="process-list">
<li><strong>Confirm the job</strong> - wood, gas, or pellet; last cleaning if you know it; smoke, smell, or just yearly maintenance.</li>
<li><strong>Protect the house</strong> - covers down, vacuum set up before brushing starts.</li>
<li><strong>Clean the system</strong> - brush and remove buildup from accessible flue paths.</li>
<li><strong>Walk the results</strong> - what is fine, what needs work, and a straight price if repair is next.</li>
</ol>
<h2>Heavy creosote</h2>
<p>Light, flaky creosote usually comes off with a normal cleaning. Tarry or glazed creosote is different. That shiny stage can need more aggressive removal. If that is what we find, we will say so instead of pretending a light brush fixed it. More detail lives on our <a href="/services/creosote-removal/">creosote removal</a> page.</p>
<h2>Signs you may need service now</h2>
<ul>
<li>It has been more than a year since the last cleaning</li>
<li>Smoke spills into the room when you burn</li>
<li>Strong creosote or musty smell, especially after rain</li>
<li>White staining on exterior brick</li>
<li>Birds or animals around the flue opening</li>
</ul>
<div class="callout"><strong>Local tip:</strong> Freeze-thaw cracks crowns and loosens mortar. Pair a sweep with a ground-level look at the top before the first hard freeze.</div>
<h2>Questions</h2>
<div class="faq">
<details><summary>How long does a cleaning take?</summary><p>Often 45 to 90 minutes for one flue. Heavy buildup or more than one flue takes longer.</p></details>
<details><summary>Will there be soot in the house?</summary><p>We cover floors and vacuum while we work. You should not get soot tracked through the rooms.</p></details>
<details><summary>Do gas fireplaces need this?</summary><p>They make less creosote than wood, but vents still need checks for blockages, corrosion, animals, and safe draft.</p></details>
</div>
""",
    },
    {
        "slug": "chimney-inspection",
        "name": "Chimney Inspection",
        "title": "Chimney Inspection Peoria IL | NFPA 211",
        "h1": "Chimney Inspection in Peoria, IL",
        "meta": "NFPA 211 chimney inspections in Peoria, IL. Clear report and direct quote if repairs are needed. Call " + PHONE_DISPLAY + ".",
        "summary": "NFPA 211 style inspections, a clear report, and a direct quote if work is needed.",
        "opener": "Most inspection calls are either a yearly safety check or a house that is being bought or sold. Either way, you should leave knowing what is fine, what needs work, and what it costs if something is wrong.",
        "body_extra": """
<h2>When to get an inspection</h2>
<p>Yearly checks catch creosote and small water problems before winter. Home sales are different. Buyers and inspectors often want a closer look at the fireplace and flue, not a shrug and a sales pitch.</p>
<p>NFPA 211 is the common industry framework for how deep that look should go. We match the level to the situation instead of upselling a camera job nobody asked for.</p>
<h2>Level 1 vs Level 2</h2>
<ul>
<li><strong>Level 1:</strong> Routine yearly check when nothing major has changed. Readily accessible parts of the chimney and appliance.</li>
<li><strong>Level 2:</strong> Common after a home sale, weather event, or system change. Covers more of the accessible structure and may include camera scanning when the flue needs a closer look.</li>
</ul>
<h2>What you get</h2>
<ul>
<li>Inspection work aligned with NFPA 211 levels (Level 1 or Level 2 as needed)</li>
<li>A clear written report of findings</li>
<li>Photos of problem areas when present</li>
<li>A direct quote if repair or follow-up work is recommended</li>
</ul>
<h2>How the visit goes</h2>
<ol class="process-list">
<li><strong>Intake</strong> - yearly check, home sale, smoke issues, or storm damage.</li>
<li><strong>On-site look</strong> - accessible interior and exterior parts for the level you need.</li>
<li><strong>Findings</strong> - what is fine, what to watch, what needs fixing, and a price if work is next.</li>
</ol>
<div class="callout"><strong>Note:</strong> The tech on site will show you what they can see and what they recommend. No mystery invoice later.</div>
<h2>Questions</h2>
<div class="faq">
<details><summary>Do I need this before selling?</summary><p>Often yes. Many buyers and home inspectors flag fireplace and chimney condition. A Level 2 style scope is common around real estate deals.</p></details>
<details><summary>Is camera scanning always included?</summary><p>Not always. It depends on access, the inspection level, and whether the inside of the flue needs a closer look.</p></details>
<details><summary>What if repairs are recommended?</summary><p>You get options in order of importance. Safety first. Cosmetic or longer-term work is labeled so you can decide.</p></details>
</div>
""",
    },
    {
        "slug": "chimney-repair",
        "name": "Chimney Installation and Repair",
        "title": "Chimney Installation and Repair Peoria IL",
        "h1": "Chimney Installation and Repair in Peoria, IL",
        "meta": "Chimney installation and repair in Peoria, IL: new work, caps, crowns, tuckpointing, flashing, and waterproofing. Call " + PHONE_DISPLAY + ".",
        "summary": "New installs plus caps, crowns, mortar repair, and waterproofing.",
        "opener": "Most repair calls start with water, animals, or a crown that has been cracked for years. We fix what is failing, price it up front, and tell you if a full rebuild is the honest answer.",
        "body_extra": """
<img class="content-photo" src="/images/repair-chimney-exterior.jpg" width="900" height="1125" alt="Exterior brick chimney on a house" loading="lazy" decoding="async">
<h2>Installation and common repairs around Peoria</h2>
<p>We handle new chimney and fireplace-related installs when needed, plus repairs on systems already in place. Water is the usual enemy. Rain, snow, and freeze-thaw open mortar joints, crack crowns, and rust dampers. Small fixes now often beat a rebuild later.</p>
<ul>
<li>Chimney and related fireplace system installation</li>
<li>Chimney cap installation</li>
<li>Crown repair and rebuild</li>
<li>Tuckpointing and brick replacement</li>
<li>Flashing repair at the roof line</li>
<li>Breathable masonry waterproofing</li>
<li>Damper repair or top-sealing dampers</li>
</ul>
<h2>How repair jobs usually go</h2>
<ol class="process-list">
<li><strong>Find the failure</strong> - leak path, crown cracks, missing cap, bad flashing, or soft mortar.</li>
<li><strong>Scope the fix</strong> - safety and water first; optional upgrades labeled clearly.</li>
<li><strong>Do the work</strong> - materials matched to the job; cleanup when finished.</li>
<li><strong>Prevention</strong> - what to watch next season so the same issue does not come right back.</li>
</ol>
<h2>Why waiting costs more</h2>
<p>Moisture inside the flue damages liners and can move into attics and living spaces. If a sweep or inspection flags masonry trouble, fixing it before winter is usually the cheaper path.</p>
<p>Central Peoria still has a lot of older brick. Freeze-thaw is hard on those crowns. Newer prefab units fail differently, but missing caps and poor flashing show up everywhere.</p>
<div class="faq">
<details><summary>Can you repair just the cap?</summary><p>Often yes. A good cap is one of the highest-value small jobs for keeping water and animals out.</p></details>
<details><summary>Do you handle full rebuilds?</summary><p>Scope depends on the job. Severe structural work may need specialized masonry scheduling. We will say that instead of forcing a bad fit.</p></details>
</div>
""",
    },
    {
        "slug": "chimney-cap-installation",
        "name": "Chimney Cap Installation",
        "title": "Chimney Cap Installation Peoria IL",
        "h1": "Chimney Cap Installation in Peoria, IL",
        "meta": "Chimney cap installation in Peoria, IL. Keep rain, animals, and debris out of your flue. Call " + PHONE_DISPLAY + ".",
        "summary": "Keeps rain, animals, and debris out of the flue.",
        "opener": "A missing cap is one of those small problems that turns into stained ceilings, animal nests, and wet masonry. Here is what a cap actually does and when the crown is the real issue.",
        "body_extra": """
<h2>What a chimney cap does</h2>
<p>A cap sits on top of the flue. Good ones keep rain and melting snow out, block animals and leaves, and include mesh that helps hold sparks in. They still let smoke leave. That balance is the whole point.</p>
<p>Open flues invite trouble. Water runs down the liner and into the firebox. Raccoons and chimney swifts treat a warm stack like housing in spring across Illinois. Leaves and twigs collect and smell when they get wet.</p>
<h2>What happens without one</h2>
<ul>
<li>Water damage to the firebox, damper, and sometimes the ceiling below</li>
<li>Animals nesting in the flue</li>
<li>Faster crown and mortar failure once water is inside the masonry</li>
<li>More downdraft and debris smell after storms</li>
</ul>
<h2>Cap types and materials</h2>
<p>Most residential jobs use stainless steel. Some homes need a custom size if the flue or chase is odd. Mesh size matters for animals and for spark control. Cheap thin metal rusts out and becomes the next problem.</p>
<ul>
<li>Single-flue caps for one opening</li>
<li>Multi-flue or chase covers for wider tops</li>
<li>Stainless options that hold up better outdoors</li>
<li>Screening sized to keep animals out without choking the draft</li>
</ul>
<h2>What installation involves</h2>
<p>We confirm the flue size, the condition of the crown, and whether the old cap can come off cleanly. Then the new cap is fitted and secured. If the crown is crumbling, bolting a nice cap to bad concrete is a waste of your money. In that case the crown is the real job.</p>
<ol class="process-list">
<li>Measure the flue and check the crown</li>
<li>Remove the failed cap if one is there</li>
<li>Fit and secure the new cap</li>
<li>Note any crown or flashing work that should come next</li>
</ol>
<h2>When the crown is the real problem</h2>
<p>Freeze-thaw cracks crowns. Water gets in, freezes, and the crack widens. A cap helps a sound crown. It will not save a crown that is already falling apart. If we see that, you get a straight explanation and a quote for crown work, not a silent upsell later.</p>
<div class="callout"><strong>Good bundle:</strong> Cap work often pairs cleanly with a yearly sweep so you are not paying two trip charges for related jobs.</div>
<div class="faq">
<details><summary>Can any cap fit my chimney?</summary><p>No. Flue size and top shape matter. Wrong fit leaks or restricts draft.</p></details>
<details><summary>Will a cap fix a wet basement smell from the fireplace?</summary><p>Sometimes, if rain entry was the cause. If the liner or crown is shot, the cap alone will not be enough.</p></details>
</div>
""",
    },
    {
        "slug": "creosote-removal",
        "name": "Creosote Removal",
        "title": "Creosote Removal Peoria IL | Chimney Fire Prevention",
        "h1": "Creosote Removal in Peoria, IL",
        "meta": "Creosote removal for Peoria-area chimneys. Stages of buildup, glazed creosote, and how cleaning reduces fire risk. Call " + PHONE_DISPLAY + ".",
        "summary": "Removes creosote buildup that can start chimney fires.",
        "opener": "Creosote is the dark residue wood smoke leaves in a flue. It is flammable. If enough builds up, a normal fire can light the deposit. That is a chimney fire, and it is avoidable with the right cleaning.",
        "body_extra": """
<h2>What creosote is</h2>
<p>When wood burns, smoke carries unburned particles up the flue. As that smoke cools, tar sticks to the liner. That deposit is creosote. Light stages brush out. Heavy stages do not behave like ordinary dust.</p>
<p>Long Peoria winters mean more burn hours. Wet wood, smoldering overnight fires, and tight air supply all make creosote worse. The fireplace can still "work" while the flue quietly loads up.</p>
<h2>The three stages</h2>
<ul>
<li><strong>Stage 1:</strong> Dusty, flaky soot. Standard brushing usually handles it.</li>
<li><strong>Stage 2:</strong> Harder, tar-like flakes. Needs a thorough mechanical cleaning.</li>
<li><strong>Stage 3:</strong> Glazed, shiny coating. Can need specialized removal methods beyond a light brush.</li>
</ul>
<p>Glazed creosote is the one homeowners underestimate. It looks smooth. It is still fuel. Pretending a quick sweep erased it is how people get surprised mid-winter.</p>
<h2>Why glazed creosote is dangerous</h2>
<p>Chimney fires can run extremely hot inside the flue. That heat cracks liners, damages surrounding structure, and can spread. You do not need a dramatic movie scene. You need less fuel on the flue walls.</p>
<h2>How removal works</h2>
<ol class="process-list">
<li>Protect floors and set up vacuum containment</li>
<li>Inspect how heavy the buildup is</li>
<li>Brush and remove what a normal cleaning can take</li>
<li>Use more aggressive methods only when glazed deposits require it</li>
<li>Review what remains, if anything, and what burning habits will slow the return</li>
</ol>
<p>If the job is really a standard yearly cleaning, that is what we call it. Creosote removal is the same family of work with more attention when the deposit is past the flaky stage. See also <a href="/services/chimney-sweep/">chimney sweeping</a>.</p>
<h2>Prevention that actually helps</h2>
<ul>
<li>Burn seasoned wood, not wet wood</li>
<li>Give the fire enough air instead of smothering it overnight</li>
<li>Do not treat the fireplace like a trash burn barrel</li>
<li>Get a yearly inspection and clean when the flue needs it</li>
</ul>
<div class="callout"><strong>Bottom line:</strong> Creosote is normal. Ignoring it for years is optional.</div>
<div class="faq">
<details><summary>Can I remove creosote myself?</summary><p>Light soot sometimes, if you know what you are doing. Glazed deposits and full flue work are easy to under-do and easy to make a mess with.</p></details>
<details><summary>Does gas make creosote?</summary><p>Much less than wood. Gas systems still need vent checks for other reasons.</p></details>
</div>
""",
    },
    {
        "slug": "dryer-vent-cleaning",
        "name": "Dryer Vent Cleaning",
        "title": "Dryer Vent Cleaning Peoria IL | Lint Fire Prevention",
        "h1": "Dryer Vent Cleaning in Peoria, IL",
        "meta": "Dryer vent cleaning in Peoria, IL. Clear lint, cut fire risk, and help clothes dry faster. Call " + PHONE_DISPLAY + ".",
        "summary": "Clears lint from dryer ducts so clothes dry faster and safer.",
        "opener": "If laundry takes two cycles and the laundry room feels like a sauna, the vent is often packed with lint. That is not just annoying. Lint burns.",
        "body_extra": """
<h2>Why dryer vents clog</h2>
<p>Cleaning the lint screen every load helps. It does not clean the duct. Lint still rides the airflow and sticks in bends, long runs, and crushed sections. Finished basements and multi-story houses around Peoria often have longer routes, which means more places for lint to stack up.</p>
<h2>Lint fire risk</h2>
<p>Dryers make heat. Lint is fuel. A restricted vent makes the dryer run hotter and longer. That combination is why dryer vents show up in home fire statistics year after year. You do not need scare language. You need airflow.</p>
<h2>Signs the vent is clogged</h2>
<ul>
<li>Clothes take much longer to dry</li>
<li>The laundry room or dryer top feels too hot</li>
<li>Burning smell during a cycle</li>
<li>Lint around the outdoor hood</li>
<li>The outdoor flap barely moves when the dryer runs</li>
</ul>
<h2>What cleaning involves</h2>
<ol class="process-list">
<li>Find the route from the dryer to the outside termination</li>
<li>Brush and vacuum the duct path</li>
<li>Clear the outdoor hood</li>
<li>Check that air is actually moving when the dryer runs</li>
</ol>
<p>We are not selling a magic filter pack. The job is mechanical: get the lint out and confirm the vent can breathe again.</p>
<h2>How often</h2>
<p>Many homes do well every one to two years. Heavy use, long ducts, pets, and households that run laundry daily may need it more often. If dry times suddenly double, do not wait for the calendar.</p>
<div class="callout"><strong>Bundle idea:</strong> Some homeowners schedule dryer vent cleaning with a chimney visit so both fire-risk jobs get handled in one stop when the route allows.</div>
<div class="faq">
<details><summary>Is the lint trap enough?</summary><p>No. The trap catches some lint. The duct still collects the rest.</p></details>
<details><summary>Can plastic vent hose stay?</summary><p>Flexible plastic or foil junk is a common weak point. If we see a bad setup, we will tell you. Replacing bad ducting may be a separate job.</p></details>
</div>
""",
    },
]

BLOG_POSTS = [
    {
        "slug": "how-often-clean-chimney-peoria",
        "title": "How Often Should You Clean a Chimney in Peoria, IL?",
        "meta": "How often Peoria-area homeowners should clean a chimney, what NFPA 211 says, and signs you should not wait.",
        "date": "2026-08-01",
        "html": """
<p>If you burn wood through a Central Illinois winter, the short version is this: get the chimney inspected every year, and clean it when the inspection says so. For a lot of wood-burners here, that means a cleaning most years.</p>
<p>People want a single magic number. Fuel type, how often you burn, and how you burn all change the answer. A gas log set is not the same job as a wood stove that runs every night from Thanksgiving to March.</p>
<h2>What NFPA 211 actually says</h2>
<p>NFPA 211 is the common industry reference for chimneys, fireplaces, and vents. It calls for inspection at least once a year. Cleaning frequency depends on what that inspection finds. That is why "we clean every house the same way every October" is too blunt, and "never clean until there is a problem" is too reckless.</p>
<p>Gas systems still need inspections even though they make less creosote than wood. Animals, corrosion, and blocked vents do not care what fuel you use.</p>
<h2>Why Peoria winters change the math</h2>
<p>Heating season here is long. Roughly November through March, a lot of fireplaces and stoves work hard. More burn hours means more smoke through the flue. More smoke means more creosote if the wood is wet or the fire is starved for air.</p>
<p>Freeze-thaw also beats on crowns and mortar. A cleaning visit is a good time to notice water damage before it becomes a ceiling stain.</p>
<ul>
<li>Long winters mean more creosote opportunity</li>
<li>Older brick near central Peoria often has aging liners and soft joints</li>
<li>Newer prefab units still need draft and termination checks</li>
</ul>
<h2>Wood, gas, and pellet are not the same</h2>
<p>Wood leaves the most creosote. Pellet systems make ash and need vent attention of their own. Gas is cleaner on creosote but still needs a safe vent path. If somebody tells you gas never needs service, ask them about birds in the termination and rusted connectors.</p>
<h2>Signs you should not wait for the calendar</h2>
<ul>
<li>Smoke in the living room</li>
<li>Strong odor after rain</li>
<li>Animals at roof level near the flue</li>
<li>Visible exterior cracks or a leaning stack</li>
<li>It has been years, not months, since anyone looked</li>
</ul>
<h2>A simple schedule that works for most homes</h2>
<ol class="process-list">
<li>Book an inspection before heavy burning season</li>
<li>Clean if buildup is there</li>
<li>Fix caps and crowns that are letting water in</li>
<li>Burn dry wood with enough air if you burn wood at all</li>
</ol>
<p>If you want the work done instead of another article, <a href="/contact/">request a callback</a> or call {phone}. We will tell you whether you need a full cleaning or just a look.</p>
""",
    },
    {
        "slug": "creosote-chimney-fire-risk",
        "title": "Creosote Buildup: The Chimney Fire Risk Peoria Homeowners Miss",
        "meta": "What creosote is, why it causes chimney fires, and how cleaning reduces risk for Peoria-area homes.",
        "date": "2026-08-05",
        "html": """
<p>Creosote is the dark residue left when wood smoke cools inside a flue. It is flammable. When enough accumulates, a normal fire can ignite the deposit. That is a chimney fire. It can get extremely hot inside the flue and damage the liner and surrounding structure.</p>
<p>The miss is not that people have never heard the word. The miss is assuming the fireplace is fine because it still lights and still draws. A flue can look dark from the firebox and still hold a thick layer higher up where you cannot see it without tools.</p>
<h2>How creosote forms</h2>
<p>Incomplete combustion sends unburned particles up the chimney. Cool flue walls make those particles stick. Wet wood, smoldering overnight burns, and restricted air supply all push the process along. Long winters around Peoria give that process more nights to work. From roughly November through March, a wood stove that runs most evenings is stacking hours in the flue whether anyone is thinking about maintenance or not.</p>
<p>Older masonry near central Peoria often has cooler exterior walls and aging liners. That can mean more places for smoke to cool and stick. Newer prefab units behave differently, but bad burning habits still leave residue in the vent path.</p>
<h2>Stages of buildup</h2>
<ul>
<li><strong>Stage 1:</strong> Flaky and dusty. Usually comes off with standard brushing.</li>
<li><strong>Stage 2:</strong> Harder tar flakes. Needs a thorough cleaning.</li>
<li><strong>Stage 3:</strong> Glazed and shiny. Can need more than a light brush.</li>
</ul>
<p>Glazed creosote is the one that fools people. It looks smooth and almost clean. It is still fuel stuck to the flue. If a tech brushes once, shrugs, and leaves without saying what stage they saw, ask. You deserve a plain answer.</p>
<h2>What increases risk</h2>
<ul>
<li>Burning unseasoned wood</li>
<li>Low-air overnight burns</li>
<li>Long gaps between professional cleanings</li>
<li>Ignoring smoke smell or slow draft</li>
<li>Using the fireplace like a dump for trash or wet scraps</li>
</ul>
<p>None of those habits make you a bad homeowner. They just change the chemistry in the flue. Dry wood and enough air are boring advice because they work.</p>
<h2>Prevention that works</h2>
<p>Burn dry hardwood when you burn wood. Give the fire air. Get the chimney inspected yearly and cleaned when buildup is present. If glazed deposits show up, ask for a real evaluation instead of a cosmetic brush-and-go. Details on heavier jobs are on our <a href="/services/creosote-removal/">creosote removal</a> page, and standard cleanings are covered under <a href="/services/chimney-sweep/">chimney sweeping</a>.</p>
<p>A cap will not remove creosote. A nice fire screen will not either. Those are separate jobs. Creosote is about what happens on the inside of the flue after smoke leaves the firebox.</p>
<h2>What a cleaning visit should include</h2>
<p>Floor protection. Vacuum containment. Brushing the accessible flue path. Honest notes if the deposit is past the easy stage. If somebody promises a five-minute "cleaning" with no setup, lower your expectations.</p>
<p>After the visit you should know three things: how heavy the buildup was, whether anything else looked wrong, and whether you need a follow-up repair quote. If the answer is "you're fine until next year," that is a good outcome. Not every visit needs to become a project.</p>
<p>If your flue has not been opened in years, do not wait for a dramatic pop in January. <a href="/contact/">Call or send the form</a> and we will tell you what the job looks like.</p>
""",
    },
    {
        "slug": "signs-you-need-chimney-cap",
        "title": "5 Signs Your Peoria Chimney Needs a Cap",
        "meta": "Rain entry, animals, leaves, and sparks: signs a chimney cap belongs on a Peoria-area home.",
        "date": "2026-08-10",
        "html": """
<p>A chimney cap is one of the cheapest upgrades that prevents expensive damage. It keeps rain and animals out and still lets smoke leave. A lot of older homes never got one. A lot of newer caps are rusted junk that rattle loose after a few seasons.</p>
<p>You do not need a roofing license to spot many of the warning signs. Binoculars from the yard and an honest look at the firebox after storms will tell you a lot.</p>
<h2>1. Water in the firebox after storms</h2>
<p>Open flues catch rain and melting snow. That water stains the firebox, rusts dampers, and feeds masonry damage. If the hearth smells wet after every storm, look up. Water that enters at the top does not always stay politely in the flue. It can migrate into surrounding materials over time.</p>
<h2>2. Birds, squirrels, or raccoons</h2>
<p>Warm flues are prime nesting spots. In Illinois, spring is busy for chimney swifts and raccoons when tops are open. An animal in the flue is a draft problem and a health mess. Nest material also burns. If you hear scratching in the stack, stop lighting fires until it is checked.</p>
<h2>3. Leaves and debris smells</h2>
<p>Organic material in the flue gets wet and stinks. It can also burn. Caps with proper screening stop a lot of that trash before it drops in. Tree cover near the roof makes this more common, not less.</p>
<h2>4. Ember concerns on wooded lots</h2>
<p>Mesh spark arrestors help keep embers from leaving the stack. No cap means less control over what comes out the top during a hot fire. That matters more when dry leaves sit near the house in fall.</p>
<h2>5. No cap on a visual roof check</h2>
<p>Binoculars from the ground are enough to spot a missing top on many houses. If you see a raw open flue, you already have your answer. If you see a bent, rusted, or half-detached cap, treat that as "no cap" for practical purposes.</p>
<h2>When the crown is the real issue</h2>
<p>Freeze-thaw cracks crowns across the Peoria metro. A cap on a failing crown is a band-aid. If the concrete top is crumbling, crown work belongs in the conversation. We would rather say that up front than sell a cap that cannot do its job.</p>
<p>Cap materials matter too. Thin metal that rusts out in a couple of seasons is not a bargain. Stainless options cost more up front and usually last longer outdoors. Fit matters more than brand names on a website. Wrong size leaks or chokes draft.</p>
<p>More detail is on the <a href="/services/chimney-cap-installation/">chimney cap installation</a> page. Caps also pair well with a yearly <a href="/services/chimney-sweep/">sweep</a> so you are not paying two trip charges for related work.</p>
<p>If you want it handled, <a href="/contact/">request a callback</a> or call (309) 555-0148.</p>
""",
    },
    {
        "slug": "prepare-fireplace-for-winter-illinois",
        "title": "Prepare Your Fireplace for an Illinois Winter (Peoria Checklist)",
        "meta": "A practical pre-winter fireplace checklist for Peoria and Central Illinois homes.",
        "date": "2026-08-12",
        "html": """
<p>Before the first cold snap, do the boring work. Illinois winters are long enough that a neglected flue will collect creosote, and a cracked crown will take on water every freeze cycle. The goal is not a perfect showroom hearth. The goal is a system you can light without guessing.</p>
<h2>Checklist</h2>
<ul>
<li>Book a sweep or inspection if you have not had one in the last year</li>
<li>Confirm the damper opens and closes cleanly</li>
<li>Check the exterior cap and crown from the ground</li>
<li>Stack only seasoned firewood off the ground</li>
<li>Test smoke and CO alarms on every level</li>
<li>Clear furniture and storage from around the hearth</li>
<li>Look at the outdoor dryer hood while you are in maintenance mode</li>
<li>Note any white staining on exterior brick or rusty streaks near the top</li>
</ul>
<h2>Why timing matters here</h2>
<p>Heavy wood burning often runs from November into March. That is a long smoke season. Creosote builds during those months. Waiting until January because "we only light it on weekends" is how people discover smoke in the room on the coldest night of the year.</p>
<p>Freeze-thaw is the other half. Water enters small crown cracks in fall, freezes, and widens the damage. A fall visit is not early. It is on time. Spring is fine for some repair work, but you do not want to learn about a blocked flue after the first ice storm.</p>
<h2>Wood habits that reduce problems</h2>
<p>Burn dry wood. Give the fire air. Do not smother logs overnight and call it efficiency. Wet wood and starved fires make more creosote. That is chemistry, not personality. If the wood hisses and bubbles at the ends, it is too wet.</p>
<p>Keep the area around the hearth clear. Ash buckets belong on noncombustible surfaces. Screens help with pop and spark control inside the room, but they do not replace a proper cap on the roof.</p>
<h2>Gas and pellet notes</h2>
<p>Gas units make less creosote than wood, but vents still need a clear path. Animals nest in open tops. Corrosion still happens. Pellet systems need ash attention and vent checks of their own. Do not skip them just because the flame looks clean.</p>
<h2>What we do if you call us</h2>
<p>We cover floors, vacuum while we clean, and tell you what we found. If you need a cap or crown work, you get a direct quote. If everything looks fine, you get to enjoy the fireplace without a sales speech.</p>
<p>Home sale coming up? Say that when you book. Inspection level should match the situation, especially when a buyer or home inspector is involved.</p>
<p>Ready for hands-on help? <a href="/contact/">Request service</a> or call (309) 555-0148.</p>
""",
    },
    {
        "slug": "dryer-vent-vs-chimney-cleaning",
        "title": "Dryer Vent Cleaning vs Chimney Cleaning: What's the Difference?",
        "meta": "Both prevent home fires, but dryer vents and chimneys need different tools and schedules.",
        "date": "2026-08-15",
        "html": """
<p>Homeowners sometimes mix these up because both jobs fight buildup that can burn. The systems are different. The tools are different. The schedule is different. The shared idea is simple: heat plus fuel is a bad roommate.</p>
<p>If you only remember one thing, remember this: the lint screen is not the dryer vent, and the fireplace screen is not the chimney flue. Both need attention deeper in the system than what you see from the living room or laundry room.</p>
<h2>Side by side</h2>
<table>
<thead><tr><th></th><th>Chimney</th><th>Dryer vent</th></tr></thead>
<tbody>
<tr><td>Hazard</td><td>Creosote, chimney fire, poor draft</td><td>Lint fire, overheating dryer</td></tr>
<tr><td>Typical schedule</td><td>Yearly inspection; clean as needed</td><td>Every 1-2 years, sooner with heavy use</td></tr>
<tr><td>Tools</td><td>Brushes, rods, vacuum, sometimes a camera</td><td>Rotary brush, vacuum, airflow check</td></tr>
<tr><td>Common clue</td><td>Smoke smell, slow draft</td><td>Long dry times, hot laundry room</td></tr>
</tbody>
</table>
<h2>Chimney cleaning in plain terms</h2>
<p>Wood smoke leaves creosote in the flue. Long winters around Peoria mean more burn hours. A sweep removes that buildup and is a chance to notice caps, crowns, and animal nests. Details live on the <a href="/services/chimney-sweep/">chimney sweep</a> page.</p>
<p>A good visit protects floors, uses vacuum containment, and ends with plain notes. If glazed creosote is present, that should be said out loud, not buried.</p>
<h2>Dryer vent cleaning in plain terms</h2>
<p>Lint bypasses the screen and packs the duct. Long runs through basements clog faster. The dryer works harder, clothes stay damp, and lint sits there as fuel. See <a href="/services/dryer-vent-cleaning/">dryer vent cleaning</a>.</p>
<p>Signs are practical: two cycles for one load, a hot dryer cabinet, lint at the outdoor hood, or a flap that barely moves when the machine runs. Those are airflow problems, not mysteries.</p>
<h2>Can you do both the same day?</h2>
<p>Often yes when the route allows. Some homeowners like one visit for both fire-risk jobs. Others only need one. We will not invent a bundle you do not need. If the dryer is in a finished basement and the chimney is on the other side of the house, both can still be handled in one appointment when the schedule fits.</p>
<h2>Which one should you book?</h2>
<ul>
<li>Fireplace smell, smoke in the room, or yearly wood burning: start with the chimney</li>
<li>Two-cycle laundry and a hot dryer: start with the vent</li>
<li>Moving into a house and trusting nothing: do both before winter if the budget allows</li>
</ul>
<p>New construction is not automatically safe. Builder-grade dryer vents get crushed in joist bays. Prefab fireplaces still need clear terminations. Age of the house matters less than condition of the path heat and exhaust travel through.</p>
<p>If you are unsure, call (309) 555-0148 and describe the house. We will point you at the job that matches the symptom.</p>
""",
    },
]


def lead_form(compact: bool = False) -> str:
    msg_rows = "" if compact else """
    <div class="form-row">
      <div><label for="message">What's going on?</label><textarea id="message" name="message" placeholder="e.g. annual sweep, smoke in room, home inspection"></textarea></div>
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
    <div><label for="city">City / ZIP</label><input id="city" name="city" placeholder="Peoria, East Peoria"></div>
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
            j1 = html.find('href="', i)
            j2 = html.find('src="', i)
            candidates = [j for j in (j1, j2) if j >= 0]
            if not candidates:
                out.append(html[i:])
                break
            j = min(candidates)
            out.append(html[i:j])
            if html.startswith('href="', j):
                attr = 'href="'
            else:
                attr = 'src="'
            k = j + len(attr)
            end = html.find('"', k)
            url = html[k:end]
            if url.startswith("/") and not url.startswith("//") and not url.startswith(BASE + "/") and url != BASE and not url.startswith(BASE + "?"):
                if url == "/":
                    url = BASE + "/"
                else:
                    url = BASE + url
            out.append(attr + url + '"')
            i = end + 1
        return "".join(out)

    nav_html = "\n".join(f'<li><a href="{href}">{label}</a></li>' for label, href in NAV)
    services_footer = "\n".join(
        f'<li><a href="/services/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES
    )
    areas_footer = "\n".join(
        f'<li><a href="/areas/{a[0]}/">{a[1]}, IL</a></li>' for a in AREAS
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
  <meta property="og:image" content="{OG_IMAGE}">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{meta}">
  <meta name="twitter:image" content="{OG_IMAGE}">
  <link rel="stylesheet" href="/css/styles.css?v=20260819b">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  {extra_head}
</head>
<body>
  <div class="topbar">
    <div class="container">
      <span>Serving the Peoria area · Call <a data-phone-link="text" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> · Same-week openings often available</span>
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
        <strong style="color:#fff">Hours:</strong> Mon-Fri 8:00 a.m. - 6:00 p.m.<br>
        <strong style="color:#fff">Saturday:</strong> morning only in season</p>
      </div>
      <div>
        <h3>Services</h3>
        <ul>{services_footer}</ul>
      </div>
      <div>
        <h3>Towns</h3>
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
      <span>Peoria, Illinois</span>
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
                "image": OG_IMAGE,
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
                "areaServed": [{"@type": "City", "name": n} for _, n, _ in AREAS],
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


def json_ld_breadcrumbs(items: list[tuple[str, str]]) -> str:
    """items: list of (name, absolute_or_site_path). Last item may be current page."""
    elements = []
    for i, (name, path) in enumerate(items, start=1):
        if path.startswith("http"):
            item_url = path
        elif path == "/":
            item_url = DOMAIN + "/"
        else:
            item_url = DOMAIN.rstrip("/") + path
        elements.append(
            {
                "@type": "ListItem",
                "position": i,
                "name": name,
                "item": item_url,
            }
        )
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": elements,
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def neighbor_sentence(slug: str) -> str:
    pairs = [(s, n) for s, n in AREA_NEIGHBORS.get(slug, []) if s and n]
    if not pairs:
        return ""
    links = [f'<a href="/areas/{s}/">{n}</a>' for s, n in pairs[:3]]
    if len(links) == 1:
        return f"<p>We also cover {links[0]} nearby.</p>"
    if len(links) == 2:
        return f"<p>We also cover {links[0]} and {links[1]} just up the road.</p>"
    return f"<p>We also cover {links[0]}, {links[1]}, and {links[2]} nearby.</p>"


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
            "Peoria and nearby towns including East Peoria, Pekin, Washington, Morton, Dunlap, Metamora, Peoria Heights, Germantown Hills, and Chillicothe.",
        ),
        (
            "What happens after I call?",
            "We confirm your town and the job, set a time, then go over results when the work is done.",
        ),
    ]
    faq_html = "\n".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs
    )
    # Four lumpy homepage cards (all six URLs remain live elsewhere)
    home_cards = f"""
<article class="card">
  <h3>Chimney cleaning and creosote removal</h3>
  <p>Yearly cleaning for wood, gas, and pellet systems. If the buildup is heavy or glazed, we treat that as part of the same job family, not a mystery upsell.</p>
  <p><a class="more" href="/services/chimney-sweep/">Chimney sweep details</a> · <a class="more" href="/services/creosote-removal/">Creosote removal</a></p>
</article>
<article class="card">
  <h3>Inspections</h3>
  <p>Yearly checks and home-sale looks under NFPA 211 style levels. You get a clear report and a direct quote if something needs fixing.</p>
  <p><a class="more" href="/services/chimney-inspection/">Inspection details</a></p>
</article>
<article class="card">
  <h3>Repairs, caps, and installs</h3>
  <p>Caps, crowns, mortar joints, waterproofing, and new work when an old system is past patching.</p>
  <p><a class="more" href="/services/chimney-repair/">Repairs and installs</a> · <a class="more" href="/services/chimney-cap-installation/">Caps</a></p>
</article>
<article class="card">
  <h3>Dryer vent cleaning</h3>
  <p>Lint packed in the duct makes dryers run hot and laundry take forever. Clearing the run is a fire-safety job, not a cosmetic one.</p>
  <p><a class="more" href="/services/dryer-vent-cleaning/">Dryer vent details</a></p>
</article>
"""
    body = f"""
    <section class="hero">
      <div class="hero-media" aria-hidden="true">
        <img class="hero-bg-img" src="/images/hero-service-van.jpg" width="1672" height="941" alt="" loading="eager" decoding="async" fetchpriority="high">
        <div class="hero-overlay"></div>
      </div>
      <div class="container">
      <div class="hero-grid">
        <div class="hero-copy">
          <span class="eyebrow">Serving the Peoria area</span>
          <h1>Chimney Sweep in Peoria, IL</h1>
          <p class="lede">Most calls we get are one of three things: the fireplace smells, it's been years since the last cleaning, or someone is buying or selling a house and needs the chimney checked. Whatever yours is, call and we'll tell you straight what it needs and what it doesn't.</p>
          <ul class="hero-points">
            <li>We work clean: floors covered, soot vacuumed</li>
            <li>You get a clear report of what we found</li>
            <li>Wood, gas, and pellet systems</li>
            <li>Often same-week openings in season</li>
          </ul>
          <div class="hero-ctas">
            <a class="btn btn-primary btn-lg" data-phone-link href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
            <a class="btn btn-outline btn-lg" href="#quote">Request a Callback</a>
          </div>
          <div class="trust-row">
            <span><strong>Yearly</strong> safety checks</span>
            <span><strong>Wood, gas, pellet</strong></span>
            <span><strong>Peoria metro</strong></span>
          </div>
        </div>
        <div class="quote-card hero-form" id="quote">
          <h2>Request a callback</h2>
          <p class="sub">Leave your number. We usually call back the same business day.</p>
          {lead_form(compact=True)}
        </div>
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
      <strong>Straight answers</strong>
      <p>Safety first. Optional work labeled so you can decide.</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>What we handle</h2>
    </div>
    <div class="grid-2 home-service-grid">{home_cards}</div>
    <p style="margin-top:1.25rem"><a href="/services/">See all services</a></p>
  </div>
</section>

<section class="bg-navy">
  <div class="container grid-2">
    <div>
      <div class="section-head">
        <h2>How it works</h2>
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
    write(
        "index.html",
        base(
            "Chimney Sweep Peoria IL | Cleaning and Inspection",
            f"Chimney sweep and cleaning in Peoria, IL. Inspections, repairs, creosote removal, and dryer vent cleaning. Call {PHONE_DISPLAY}.",
            "/",
            body,
            extra,
        ),
    )


def build_services() -> None:
    # hub page
    hub_cards = "\n".join(
        f"""<article class="card">
          <h3>{s['name']}</h3>
          <p>{s['summary']}</p>
          <a class="more" href="/services/{s['slug']}/">Learn more</a>
        </article>"""
        for s in SERVICES
    )
    hub_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a> · Services</div>
    <h1>Chimney and Dryer Vent Services in Peoria, IL</h1>
    <p>Cleaning, inspections, repairs, caps, creosote work, and dryer vents. Pick the job that matches the house, or call if you are not sure.</p>
  </div>
</section>
<div class="container content-wrap">
  <div>
    <div class="grid-2">{hub_cards}</div>
  </div>
  <aside class="sidebar-sticky">
    <div class="quote-card">
      <h2>Request a callback</h2>
      <p class="sub">Peoria-area scheduling · No obligation</p>
      {lead_form(compact=True)}
    </div>
  </aside>
</div>
"""
    write(
        "services/index.html",
        base(
            "Chimney and Dryer Vent Services | Peoria IL",
            f"Chimney cleaning, inspection, repair, cap installation, creosote removal, and dryer vent cleaning in Peoria, IL. Call {PHONE_DISPLAY}.",
            "/services/",
            hub_body,
            json_ld_breadcrumbs([("Home", "/"), ("Services", "/services/")]),
        ),
    )

    for s in SERVICES:
        crumbs = [
            ("Home", "/"),
            ("Services", "/services/"),
            (s["name"], f"/services/{s['slug']}/"),
        ]
        body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a> · <a href="/services/">Services</a> · {s['name']}</div>
    <h1>{s['h1']}</h1>
    <p>{s['summary']}</p>
  </div>
</section>
<div class="container content-wrap">
  <article class="prose">
    <p>{s['opener']} Call <a data-phone-link="text" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> or use the form.</p>
    {s['body_extra']}
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
        extra = json_ld_service(s) + json_ld_breadcrumbs(crumbs)
        write(
            f"services/{s['slug']}/index.html",
            base(s["title"], s["meta"], f"/services/{s['slug']}/", body, extra),
        )


def build_areas() -> None:
    pills = "\n".join(
        f"""<article class="card">
          <h3>{name}, IL</h3>
          <p>{blurb[:140]}...</p>
          <a class="more" href="/areas/{slug}/">Chimney services in {name}</a>
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
    write(
        "areas/index.html",
        base(
            "Chimney Sweep Service Areas | Peoria IL Metro",
            "Chimney sweep service areas near Peoria, IL including East Peoria, Pekin, Washington, Morton, Dunlap, and more.",
            "/areas/",
            body,
            json_ld_breadcrumbs([("Home", "/"), ("Service Areas", "/areas/")]),
        ),
    )

    deep_slugs = set(AREA_DEEP.keys())
    for slug, name, blurb in AREAS:
        svc_links = "".join(
            f'<li><a href="/services/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES
        )
        deep = AREA_DEEP.get(slug, "")
        if deep:
            main_copy = f"<p>{blurb}</p>{deep}"
        else:
            main_copy = f"""
<p>{blurb}</p>
<p>If you are in {name} and need a yearly cleaning, have smoke or odor issues, or need an inspection, we can help. Cold weather and freeze-thaw cycles are hard on masonry. Getting the chimney checked before winter helps catch creosote and water issues early.</p>
<p>Wood burners work hard from late fall into early spring around here. Gas and pellet systems still need vent checks. Open tops invite animals in spring.</p>
"""
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
    {main_copy}
    <h2>Services in {name}</h2>
    <ul>{svc_links}</ul>
    {neighbor_sentence(slug)}
    <div class="callout"><strong>{name}:</strong> Call <a data-phone-link="text" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> and we will get you on the schedule.</div>
  </article>
  <aside class="sidebar-sticky">
    <div class="quote-card">
      <h2>Book in {name}</h2>
      <p class="sub">Chimney and dryer vent callbacks</p>
      {lead_form(compact=True)}
    </div>
  </aside>
</div>
"""
        ld_service = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": f"Chimney Sweep {name} IL",
            "areaServed": {"@type": "City", "name": name},
            "provider": {"@type": "LocalBusiness", "name": BRAND, "telephone": PHONE_TEL},
            "url": f"{DOMAIN}/areas/{slug}/",
        }
        crumbs = json_ld_breadcrumbs(
            [("Home", "/"), ("Service Areas", "/areas/"), (name, f"/areas/{slug}/")]
        )
        extra = f'<script type="application/ld+json">{json.dumps(ld_service)}</script>' + crumbs
        write(
            f"areas/{slug}/index.html",
            base(
                f"Chimney Sweep {name} IL | Chimney Cleaning Near Peoria",
                f"Chimney sweep and cleaning in {name}, IL near Peoria. Inspections, creosote removal, caps, and dryer vent cleaning. Call {PHONE_DISPLAY}.",
                f"/areas/{slug}/",
                body,
                extra,
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
    write(
        "blog/index.html",
        base(
            "Chimney Tips Blog | Peoria IL",
            "Articles on chimney sweeping, creosote, caps, and fireplace safety for Peoria, Illinois homeowners.",
            "/blog/",
            body,
        ),
    )

    for p in BLOG_POSTS:
        body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a> · <a href="/blog/">Blog</a> · Article</div>
    <h1>{p['title']}</h1>
    <p>Published {p['date']} · Updated {TODAY}</p>
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
            "dateModified": TODAY,
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
    <p>Call <a data-phone-link="text" href="tel:{PHONE_TEL}" style="color:#fff;font-weight:700">{PHONE_DISPLAY}</a> or send the form. We cover Peoria and nearby towns.</p>
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
      <p>Monday-Friday 8:00 a.m. - 6:00 p.m.<br>Saturday morning only in season</p>
      <h2>Service area</h2>
      <p>Peoria, East Peoria, Pekin, Washington, Morton, Dunlap, Metamora, Peoria Heights, Germantown Hills, Chillicothe, and nearby towns.</p>
      <h2>What to have ready</h2>
      <ul>
        <li>City / ZIP</li>
        <li>Wood, gas, or pellet?</li>
        <li>Last cleaning date if known</li>
        <li>Any symptoms (smoke, odor, animals, buyer inspection)</li>
      </ul>
    </div>
  </div>
</section>
"""
    write(
        "contact/index.html",
        base(
            f"Contact {BRAND} | {PHONE_DISPLAY}",
            f"Contact {BRAND} for chimney sweep, inspection, repair, and dryer vent cleaning in Peoria, IL. Call {PHONE_DISPLAY}.",
            "/contact/",
            contact_body,
        ),
    )

    towns = ", ".join(n for _, n, _ in AREAS)
    about_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a> · About</div>
    <h1>About {BRAND}</h1>
    <p>Chimney and dryer vent work for the Peoria metro.</p>
  </div>
</section>
<section>
  <div class="container prose" style="max-width:48rem">
    <p>We're a small local operation focused on chimney and dryer vent work in the Peoria metro. No sales routine: we come out, do the cleaning or inspection, show you what we found, and tell you if something actually needs fixing or can wait. If we're not the right fit for a job, we'll say so and point you to someone who is.</p>
    <h2>Hours</h2>
    <p>Monday-Friday 8:00 a.m. - 6:00 p.m.<br>Saturday morning only in season</p>
    <h2>Towns we cover</h2>
    <p>{towns}.</p>
    <h2>How we work</h2>
    <ul>
      <li>Floors covered and soot vacuumed on cleaning jobs</li>
      <li>Clear reports after inspections</li>
      <li>Direct quotes when repair work is needed</li>
      <li>Wood, gas, and pellet systems</li>
    </ul>
    <p><a class="btn btn-primary" href="/contact/">Contact us</a></p>
  </div>
</section>
"""
    write(
        "about/index.html",
        base(
            f"About {BRAND}",
            f"About {BRAND}: chimney and dryer vent work for Peoria, Illinois homeowners.",
            "/about/",
            about_body,
        ),
    )

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
      <li>Basic technical logs common to websites (for example IP and browser) via hosting</li>
    </ul>
    <h2>Sharing</h2>
    <p>Inquiry details may be shared with the local service partner assigned to fulfill your request. We do not sell personal information as a standalone data product.</p>
    <h2>Contact</h2>
    <p>Questions: call <a data-phone-link="text" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
  </div>
</section>
"""
    write(
        "privacy/index.html",
        base(
            "Privacy Policy | " + BRAND,
            "Privacy policy for Peoria Chimney Sweep contact forms and calls.",
            "/privacy/",
            privacy_body,
        ),
    )


def build_meta_files() -> None:
    urls = ["/", "/contact/", "/about/", "/privacy/", "/blog/", "/areas/", "/services/"]
    urls += [f"/services/{s['slug']}/" for s in SERVICES]
    urls += [f"/areas/{a[0]}/" for a in AREAS]
    urls += [f"/blog/{p['slug']}/" for p in BLOG_POSTS]

    sitemap = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path in urls:
        loc = DOMAIN.rstrip("/") + (path if path != "/" else "/")
        priority = "1.0" if path == "/" else ("0.9" if path.startswith("/services/") else "0.7")
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

    # Keep existing logo/favicon if present; only write favicon if missing
    fav_path = ROOT / "favicon.svg"
    if not fav_path.exists():
        fav = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="12" fill="#1a2744"/>
  <path d="M18 46V22l14-10 14 10v24H18z" fill="#b33a2b"/>
  <rect x="28" y="34" width="8" height="12" fill="#f7f3eb"/>
  <path d="M32 8c0 0 6 6 6 11a6 6 0 1 1-12 0c0-5 6-11 6-11z" fill="#e8a17a"/>
</svg>
"""
        fav_path.write_text(fav, encoding="utf-8")


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
