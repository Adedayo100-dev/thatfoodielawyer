"""Builds the static HTML pages for That Foodie Lawyer into ../site.
Edit page content below, then run:  python3 src/build.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "site"
SITE = "https://www.thatfoodielawyer.com"
EMAIL = "foodie@thatfoodielawyer.com"

# Paste her Calendly event link here (event must have Stripe payment turned on).
CALENDLY_URL = "https://calendly.com/REPLACE_WITH_HER_LINK/strategy-call"

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("consulting.html", "Global Consulting"),
    ("experiences.html", "Experiences"),
    ("ideas.html", "Ideas"),
    ("contact.html", "Contact"),
]

A = '<span class="arrow" aria-hidden="true">→</span>'


def btn(href, label, cls="btn-primary"):
    return f'<a class="btn {cls}" href="{href}">{label} {A}</a>'


def header(active):
    items = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a></li>' for h, t in NAV
    )
    return f"""
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="index.html" aria-label="That Foodie Lawyer home"><img src="assets/img/logo-mark.png" alt="" width="78" height="34"><span class="logo-text">That Foodie<br>Lawyer</span></a>
    <button class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="site-nav">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 7h18M3 12h18M3 17h18"/></svg>
    </button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul>{items}</ul>
      <a class="btn btn-primary" href="book.html">Book a Strategy Call</a>
    </nav>
  </div>
</header>"""


def footer():
    links = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f"""
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <h2>Let's Work<br>Together</h2>
      <p>TFL brings together food, culture, industry insight and practical strategy to move meaningful ideas forward. I work with founders, organizations, media platforms and experience partners who care about trust, quality and lasting impact. Whether you need an advisor, speaker, collaborator or thoughtful industry voice, I would love to hear what you are building. All services and collaborations are currently delivered virtually unless otherwise agreed. Reach me at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
    <div class="footer-bottom">
      <ul>{links}<li><a href="book.html">Book a Strategy Call</a></li></ul>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
    <!-- FLODESK: paste the Flodesk newsletter embed code here once the form is ready. -->
    <!-- SOCIAL: add social icon links here once handles are confirmed. -->
    <div class="footer-meta">
      <span>© <span id="yr">2026</span> That Foodie Lawyer. All rights reserved.</span>
      <span>Site by <a href="https://deewhynetworks.com" target="_blank" rel="noopener">Dee-Why</a></span>
    </div>
  </div>
</footer>
<script>document.getElementById('yr').textContent=new Date().getFullYear();</script>"""


def page(filename, title, desc, body, active=None):
    full_title = "That Foodie Lawyer" if filename == "index.html" else f"{title} | That Foodie Lawyer"
    url = SITE + ("/" if filename == "index.html" else "/" + filename.replace(".html", ""))
    html = f"""<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1f4a25">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,600;12..96,700&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=Fraunces:opsz,wght@9..144,400;9..144,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
{header(active or filename)}
<main id="main">
{body}
</main>
{footer()}
<script src="assets/main.js" defer></script>
</body>
</html>
"""
    (OUT / filename).write_text(html, encoding="utf-8")


# ---------------------------------------------------------------- HOME
WORLD = [
    ("advise", "01", "ADVISE", "TFL Global Consulting",
     "Build a stronger food or hospitality business with clearer decisions, smarter systems and practical support.",
     "Good food deserves a business built to support it. Through TFL Global Consulting, I help food and hospitality founders see what is getting in the way of growth, strengthen the systems behind the business, and make better decisions with greater clarity. The work can include strategy, operational readiness, compliance, risk, customer experience and implementation support.",
     [("consulting.html", "Explore TFL Global Consulting", "btn-primary"), ("book.html", "Book a Food &amp; Hospitality Strategy Call", "btn-ghost")]),
    ("experience", "02", "EXPERIENCE", "Experiences by TFL",
     "Step into thoughtfully curated experiences designed to feel intentional, engaging and worth remembering.",
     "The best food experiences stay with people because every detail feels considered. Experiences by TFL brings that standard to intentional gatherings, hospitality moments and story-led experiences that create connection, spark curiosity and leave a lasting impression.",
     [("experiences.html", "Discover TFL Experiences", "btn-primary")]),
    ("explore", "03", "EXPLORE", "Ideas &amp; Industry Voice",
     "Look deeper at the culture, systems, standards and stories shaping how food is experienced.",
     "This is where I look beyond the obvious. Explore commentary, stories and practical perspectives on consumer expectations, food law, hospitality, business, culture and the systems behind memorable food experiences.",
     [("ideas.html", "Explore Ideas", "btn-primary")]),
    ("connect", "04", "CONNECT", "Speaking, Media &amp; Collaborations",
     "Bring the TFL perspective to your platform, audience, event or creative project.",
     "I contribute a distinctive perspective on food, law, culture, business and consumer experience. Invite me to speak, contribute to a story, join a conversation or collaborate on work that makes food matter more.",
     [("contact.html?topic=Collaboration", "Start a Collaboration", "btn-primary")]),
]

cards_html = ""
panels_html = ""
for i, (key, num, title, sub, copy, more, ctas) in enumerate(WORLD):
    sel = "true" if i == 0 else "false"
    cards_html += f"""
      <button class="world-card" role="tab" id="tab-{key}" aria-selected="{sel}" aria-controls="panel-{key}">
        <span class="num">{num}</span>
        <h3>{title}</h3>
        <span class="sub">{sub}</span>
        <p class="copy">{copy}</p>
      </button>"""
    btns = "".join(btn(h, l, c) for h, l, c in ctas)
    panels_html += f"""
    <div class="world-panel" role="tabpanel" id="panel-{key}" aria-labelledby="tab-{key}"{"" if i == 0 else " hidden"}>
      <div><div class="label">{num} · {title}</div><h3>{sub}</h3></div>
      <div><p>{more}</p><div class="btn-row">{btns}</div></div>
    </div>"""

home = f"""
<section class="hero">
  <div class="hero-text">
    <span class="eyebrow">About That Foodie Lawyer</span>
    <h1>Food is never just what is on the plate.</h1>
    <p class="lead">That Foodie Lawyer is a platform for looking deeper at food: the expectations it creates, the experiences it shapes, the trust it requires and the businesses behind it. Through consumer insight, curated experiences, industry conversations and strategic advisory, I am shaping a future where people experience food more fully, beyond what is on the plate, and the industry is equipped to deliver better.</p>
    <div class="btn-row">{btn("#world", "Enter the World of TFL")}</div>
  </div>
  <div class="hero-media">
    <img src="assets/img/azeezat-hero.webp" alt="Azeezat Adejare, That Foodie Lawyer, smiling in a yellow blazer and tie" width="1200" height="1600" fetchpriority="high">
  </div>
</section>

<section class="section bg-blush">
  <div class="wrap center narrow fade">
    <span class="eyebrow">The TFL Point of View</span>
    <h2>There is a whole world behind food.</h2>
    <p class="lead">Food is personal, commercial and deeply connected to how people live. Behind every plate, product and hospitality moment are choices about quality, trust, service, systems and experience. TFL brings that whole picture into view so consumers can expect better, founders can build better and the industry can move forward with greater intention.</p>
  </div>
</section>

<section class="section bg-forest" id="world">
  <div class="wrap">
    <div class="fade">
      <span class="eyebrow">Enter the World of TFL</span>
      <h2>Discover TFL from every angle.</h2>
      <p class="lead" style="max-width:640px">Explore the ideas, experiences, conversations and strategic work shaping a more thoughtful future for food and hospitality.</p>
    </div>
    <div class="world-cards" role="tablist" aria-label="The world of TFL">{cards_html}
    </div>{panels_html}
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="media fade"><img src="assets/img/azeezat-lens.webp" alt="Azeezat in a denim vest and yellow tie, arms crossed" loading="lazy" width="1200" height="1600"></div>
    <div class="fade">
      <span class="eyebrow">Ideas &amp; Industry Voice</span>
      <h2>A wider lens on where food is going.</h2>
      <p class="lead">The future of food will not be shaped by taste alone. It will be shaped by trust, culture, regulation, technology, customer expectations and the people willing to connect the dots. I bring legal thinking, industry insight and a consumer-minded perspective to the conversations defining what comes next.</p>
      <div class="btn-row">{btn("ideas.html", "Explore the TFL Point of View")}</div>
      <details class="reveal">
        <summary>Learn more <span class="plus" aria-hidden="true">+</span></summary>
        <div class="reveal-body">
          <p>Food is changing quickly, but the most useful conversations still begin with better questions. What makes an experience memorable? What earns and keeps consumer trust? What helps a founder grow without weakening the business behind the brand? Through articles, commentary, speaking and media, I examine the forces shaping food and hospitality and make the bigger picture easier to see.</p>
          <div class="btn-row" style="margin-top:12px">
            <a class="text-link" href="ideas.html">Read the Latest</a>
            <a class="text-link" href="contact.html?topic=Speaking">Invite Me to Speak</a>
            <a class="text-link" href="contact.html?topic=Collaboration">Explore Collaborations</a>
          </div>
        </div>
      </details>
    </div>
  </div>
</section>

<section class="section bg-tomato">
  <div class="wrap center narrow fade">
    <span class="eyebrow">Start a Conversation</span>
    <h2>Let us make food matter more.</h2>
    <p class="lead">Whether you are building a stronger business, creating a meaningful experience or looking for a fresh industry perspective, I would love to hear what you are working on.</p>
    <div class="btn-row">{btn("contact.html", "Start the Conversation", "btn-light")}{btn("book.html", "Book a Strategy Call", "btn-ghost")}</div>
  </div>
</section>
"""
page("index.html", "Home",
     "That Foodie Lawyer is a platform for looking deeper at food: consumer insight, curated experiences, industry conversations and strategic advisory by Azeezat Adejare.",
     home)

# ---------------------------------------------------------------- ABOUT
about = f"""
<section class="hero">
  <div class="hero-text">
    <span class="eyebrow">About That Foodie Lawyer</span>
    <h1>I see the whole world behind food.</h1>
    <p class="lead">I created That Foodie Lawyer to explore everything that shapes how food is experienced. TFL brings together consumer expectations, thoughtful experiences, practical industry insight and the systems behind trust. It is a platform for helping people look deeper, expect better and understand the choices that shape what reaches the plate and what keeps them coming back.</p>
    <div class="btn-row">{btn("#meet", "Meet Azeezat")}</div>
  </div>
  <div class="hero-media">
    <img src="assets/img/azeezat-about.webp" alt="Azeezat at a restaurant table, playfully holding a falafel up to her eye" width="1200" height="1600" fetchpriority="high" style="object-position:center 35%">
  </div>
</section>

<section class="section">
  <div class="wrap split wide-left">
    <h2 class="statement fade">More than what is on the plate.</h2>
    <div class="fade">
      <span class="eyebrow">TFL Worldview</span>
      <p class="lead">Food is business. Food is culture. Food is memory, trust and experience. Behind every dish, product and hospitality moment are choices about people, standards, systems, service and story. TFL exists to make those choices more visible and to show how much becomes possible when the whole picture is considered.</p>
    </div>
  </div>
</section>

<section class="section bg-lime">
  <div class="wrap">
    <div class="center narrow fade">
      <span class="eyebrow">What Guides Me</span>
      <h2>A point of view with purpose.</h2>
      <p class="lead">Three principles shape how I explore ideas, create experiences and support the people building the future of food.</p>
    </div>
    <div class="pillars fade" style="--cols:3">
      <div class="pillar"><span class="num">01</span><h3>Curiosity</h3><p>I look beneath the surface. I ask what shaped the food, who is represented, what the consumer experiences and what the business needs to thrive.</p></div>
      <div class="pillar"><span class="num">02</span><h3>Clarity</h3><p>I make complex ideas easier to understand and act on, whether the subject is culture, compliance, strategy or customer trust.</p></div>
      <div class="pillar"><span class="num">03</span><h3>Connection</h3><p>I bring people, perspectives and possibilities together. The strongest food stories and businesses are built through meaningful relationships.</p></div>
    </div>
  </div>
</section>

<section class="section" id="meet">
  <div class="wrap split">
    <div class="fade">
      <span class="eyebrow">Meet Azeezat</span>
      <h2>An industry voice with a practical lens.</h2>
      <p>I am Azeezat Adejare, also known as That Foodie Lawyer. I am a dual-qualified lawyer, food and hospitality strategist, and the founder of TFL Global Consulting. My work brings together legal and commercial judgment, consumer insight and a clear view of what makes food businesses and experiences worthy of trust.</p>
      <p>I created TFL to raise expectations around how food is experienced and to equip the people behind food to build with greater clarity, consistency and intention. From advisory work and industry conversations to curated experiences and consumer-facing insight, I look at the whole picture: the promise a brand makes, the systems that support it and the experience that brings people back.</p>
      <div class="btn-row">{btn("#work-with-me", "Work With Me")}</div>
    </div>
    <div class="media fade"><img src="assets/img/azeezat-table.webp" alt="Azeezat in a yellow blazer at a set table with drinks and falafel" loading="lazy" width="1200" height="1600"></div>
  </div>
</section>

<section class="section bg-cream2" id="work-with-me">
  <div class="wrap">
    <div class="fade" style="max-width:720px">
      <span class="eyebrow">Work With Me</span>
      <h2>Ways to work together.</h2>
      <p class="lead">There are several ways to work with me, depending on what you are building and the perspective you need.</p>
    </div>
    <div class="ways fade">
      <div class="way"><div class="ico">A</div><h3>Advisory</h3><p>Strategic support for food and hospitality founders through TFL Global Consulting.</p></div>
      <div class="way"><div class="ico">S</div><h3>Speaking</h3><p>Thoughtful, practical conversations on food, law, culture, consumer expectations and business growth.</p></div>
      <div class="way"><div class="ico">M</div><h3>Media</h3><p>Interviews, commentary, features and contributions informed by legal, commercial, industry and consumer insight.</p></div>
      <div class="way"><div class="ico">C</div><h3>Collaborations</h3><p>Aligned projects, campaigns and experiences that move food and hospitality forward.</p></div>
    </div>
    <div class="btn-row">{btn("contact.html", "Tell Me What You Are Working On")}<a class="btn btn-ghost" href="mailto:{EMAIL}">{EMAIL}</a></div>
  </div>
</section>

<section class="section bg-tomato quote-band">
  <div class="wrap fade"><blockquote>The future of food will be shaped by the people willing to see the whole picture.</blockquote></div>
</section>

<section class="section">
  <div class="wrap center narrow fade">
    <span class="eyebrow">Enter the World of TFL</span>
    <h2>Let us make food matter more.</h2>
    <p class="lead">Explore the ideas, experiences, conversations and strategic work helping people experience food more thoughtfully and helping the industry move forward with greater intention.</p>
    <div class="btn-row">{btn("index.html#world", "Explore TFL")}</div>
  </div>
</section>
"""
page("about.html", "About",
     "Meet Azeezat Adejare, That Foodie Lawyer: dual-qualified lawyer, food and hospitality strategist and founder of TFL Global Consulting.",
     about)

# ---------------------------------------------------------------- CONSULTING
SERVICES = [
    ("Packaging &amp; Label Compliance Review", "Review Canadian food labelling requirements before printing or going to market, with clear findings and practical corrections."),
    ("Nutrition Facts Table Support", "Coordinate the information and specialist inputs required to develop or update a compliant Nutrition Facts table."),
    ("Traceability &amp; Recall Readiness System", "Build the records, procedures and response tools needed to trace products and respond effectively if a recall occurs."),
    ("Preventive Control Plan Development &amp; Optimization", "Develop or strengthen the food-safety system, records and procedures required for consistent operations and regulatory readiness."),
    ("Packaging &amp; Label Development Support", "Coordinate packaging strategy, required information and specialist contributors from concept through print readiness."),
    ("Inspection-Ready Assessment", "Identify gaps and strengthen documentation, practices and preparedness before an inspection, audit or compliance opportunity."),
    ("Recall Response &amp; Crisis Advisory", "Strategic support during a high-pressure food safety, regulatory or reputation event."),
]
from urllib.parse import quote
services_html = ""
for i, (name, desc) in enumerate(SERVICES, 1):
    plain = name.replace("&amp;", "&")
    services_html += f"""
      <details class="service">
        <summary><span class="num">{i:02d}</span><h3>{name}</h3><span class="plus" aria-hidden="true">+</span></summary>
        <div class="body"><p>{desc}</p><a class="text-link" href="contact.html?service={quote(plain)}">Ask about this service</a></div>
      </details>"""

consulting = f"""
<section class="type-hero forest">
  <div class="plate" aria-hidden="true"></div>
  <div class="wrap" style="position:relative">
    <img src="assets/img/logo-consulting-cream.png" alt="TFL Global Consulting" width="270" height="52" style="height:auto;width:min(270px,60vw);margin-bottom:36px">
    <span class="eyebrow">TFL Global Consulting</span>
    <h1>Build a food or hospitality business ready for more.</h1>
    <p class="lead">I help founders strengthen the systems behind growth, navigate compliance and operational risk, and create the consistency and customer trust that sustainable businesses depend on.</p>
    <div class="btn-row">{btn("book.html", "Book a Food &amp; Hospitality Strategy Call")}</div>
  </div>
</section>

<section class="section bg-blush">
  <div class="wrap center narrow fade">
    <span class="eyebrow">The TFL Point of View</span>
    <h2>Great food needs a strong business behind it.</h2>
    <p class="lead">A memorable product may earn attention, but strong systems, sound decisions, consistent delivery and customer trust are what help a business last. My advisory work looks at the full operating picture, then helps you focus on the changes that matter most.</p>
  </div>
</section>

<section class="section bg-lime">
  <div class="wrap">
    <div class="center narrow fade">
      <span class="eyebrow">Core Advisory Pillars</span>
      <h2>From clarity to capability.</h2>
      <p class="lead">Support is structured to help you understand the real challenge, identify the right priorities and turn better decisions into stronger business practices.</p>
    </div>
    <div class="pillars fade" style="--cols:4">
      <div class="pillar"><span class="num">01</span><h3>Strategy &amp; Direction</h3><p>Clarify the decision in front of you, identify hidden risks and opportunities, and define the most useful path forward.</p></div>
      <div class="pillar"><span class="num">02</span><h3>Readiness &amp; Risk</h3><p>Examine the systems, compliance gaps and operational barriers that may be limiting growth, trust or profitability.</p></div>
      <div class="pillar"><span class="num">03</span><h3>Implementation &amp; Accountability</h3><p>Translate priorities into practical actions, clear ownership and measurable progress.</p></div>
      <div class="pillar"><span class="num">04</span><h3>Ongoing Advisory</h3><p>Navigate growth, complexity and high-impact decisions with consistent strategic support.</p></div>
    </div>
  </div>
</section>

<section class="section" id="offers">
  <div class="wrap">
    <div class="fade" style="max-width:720px">
      <span class="eyebrow">TFL Global Consulting Offer Suite</span>
      <h2>Two ways to begin.</h2>
      <p class="lead">Start with a strategic conversation, or choose a focused service when you already know exactly what you need.</p>
    </div>

    <div class="offer-card fade" style="margin-top:48px" id="strategy-call">
      <div>
        <span class="route-tag">Route 1 · Start Here</span>
        <h2 style="font-size:clamp(1.8rem,3vw,2.5rem)">Food &amp; Hospitality Strategy Call</h2>
        <p class="lead">Start with the right conversation.</p>
        <p>A focused 45-minute advisory session to understand your business, the decision or challenge in front of you, and the risks or opportunities that may not yet be visible. I use the conversation to clarify your priorities and determine whether a focused service, a deeper assessment or longer-term advisory support is the right next step.</p>
        <div class="kv">
          <div><h4>Best for</h4><p>Founders preparing to launch, facing a growth decision, navigating an operational challenge or looking for an experienced sounding board.</p></div>
          <div><h4>You leave with</h4><p>Greater clarity, priority actions and a recommendation for the most suitable next step.</p></div>
        </div>
        <h4 style="font-family:var(--f-body);font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--tomato)">Possible next steps after the call</h4>
        <ol class="next-steps">
          <li><span><strong>Growth Readiness Audit:</strong> a structured assessment of operational, compliance and growth barriers.</span></li>
          <li><span><strong>Strategic Implementation Sprint:</strong> focused support to turn agreed priorities into practical action over 30 days.</span></li>
          <li><span><strong>Strategic Growth Advisory Partnership:</strong> ongoing strategic support for businesses navigating growth and complexity.</span></li>
          <li><span><strong>A focused technical service,</strong> where the need is specific and clearly defined.</span></li>
        </ol>
      </div>
      <aside class="price-box">
        <!-- PRICE: keep editable until final commercial approval -->
        <div class="price">$249<small>CAD</small></div>
        <div class="price-meta">45 minutes · Virtual</div>
        {btn("book.html", "Book a Strategy Call")}
        <ul>
          <li>Pick a time and pay securely online</li>
          <li>Instant confirmation by email</li>
          <li>A clear recommendation for your next step</li>
        </ul>
      </aside>
    </div>

    <div style="margin-top:clamp(64px,8vw,104px)" id="focused-services" class="fade">
      <span class="route-tag">Route 2 · Focused Compliance Services</span>
      <h2>Specialist support for a clearly defined need.</h2>
      <p class="lead" style="max-width:720px">For founders who already know the specific issue they need to solve, these focused services provide practical, defined support without requiring a longer advisory engagement.</p>
    </div>
    <div class="services fade">{services_html}
    </div>
  </div>
</section>

<section class="section bg-tomato">
  <div class="wrap center narrow fade">
    <span class="eyebrow">Start Here</span>
    <h2>Not sure where to begin?</h2>
    <p class="lead">Book a Strategy Call. In 45 minutes we will clarify your priorities and identify the most useful next step for your business.</p>
    <div class="btn-row">{btn("book.html", "Book a Food &amp; Hospitality Strategy Call", "btn-light")}</div>
  </div>
</section>
"""
page("consulting.html", "Global Consulting",
     "TFL Global Consulting helps food and hospitality founders strengthen systems, navigate Canadian food compliance and risk, and build customer trust. Book a Strategy Call.",
     consulting)

# ---------------------------------------------------------------- EXPERIENCES (draft copy)
experiences = f"""
<!-- DRAFT COPY: Experiences page copy was not in the copy doc. Written in the TFL voice for Azeezat to review. -->
<section class="hero">
  <div class="hero-text">
    <span class="eyebrow">Experiences by TFL</span>
    <h1>Food experiences worth remembering.</h1>
    <p class="lead">The best food experiences stay with people because every detail feels considered. Experiences by TFL brings that standard to intentional gatherings, hospitality moments and story-led experiences that create connection, spark curiosity and leave a lasting impression.</p>
    <div class="btn-row">{btn("contact.html?topic=Experiences", "Plan an Experience")}</div>
  </div>
  <div class="hero-media">
    <img src="assets/img/food-table.webp" alt="A TFL event table with pastries, small chops and drinks under copper food lamps" width="1067" height="1600" fetchpriority="high">
  </div>
</section>

<section class="section bg-blush">
  <div class="wrap center narrow fade">
    <span class="eyebrow">The Experience Standard</span>
    <h2>Every detail tells part of the story.</h2>
    <p class="lead">A great experience is more than a good meal. It is the welcome, the setting, the conversation, the culture on the table and the feeling people carry home. I design experiences where those details work together, so guests do not just taste the food. They understand it.</p>
  </div>
</section>

<section class="section bg-lime">
  <div class="wrap">
    <div class="center narrow fade">
      <span class="eyebrow">What We Create</span>
      <h2>Intentional by design.</h2>
    </div>
    <div class="pillars fade" style="--cols:3">
      <div class="pillar"><span class="num">01</span><h3>Intentional Gatherings</h3><p>Curated tables, tastings and dinners that bring the right people together around food with meaning.</p></div>
      <div class="pillar"><span class="num">02</span><h3>Hospitality Moments</h3><p>Brand activations, launches and partner events shaped to feel warm, polished and true to the people hosting them.</p></div>
      <div class="pillar"><span class="num">03</span><h3>Story-Led Experiences</h3><p>Experiences built around culture, heritage and the stories behind the dish, designed to spark curiosity and conversation.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="fade">
      <span class="eyebrow">Partner With TFL</span>
      <h2>Have an experience in mind?</h2>
      <p class="lead">Whether you are a brand, venue, organization or community partner, I would love to hear what you are imagining. Tell me about your audience, your occasion and the feeling you want people to leave with, and we will shape it from there.</p>
      <div class="btn-row">{btn("contact.html?topic=Experiences", "Start the Conversation")}</div>
    </div>
    <div class="media fade"><img src="assets/img/food-pastries.webp" alt="Platters of golden pastries and fresh fruit at a TFL event" loading="lazy" width="1067" height="1600"></div>
  </div>
</section>
"""
page("experiences.html", "Experiences",
     "Experiences by TFL: intentional gatherings, hospitality moments and story-led food experiences that create connection and leave a lasting impression.",
     experiences)

# ---------------------------------------------------------------- IDEAS (draft copy)
ARTICLES = [
    ("Culture", "Debunking Common African Food Myths"),
    ("Culture", "Celebrating World Jollof Rice Day with a Twist"),
    ("Food Law", "Beyond Poutine: 25 Canadian Food Laws That Will Surprise You"),
    ("Industry", "Connecting African Cuisine to the World: Lessons from Thai and Beyond"),
]
arts = "".join(
    f'<a class="article" href="#"><span class="cat">{c}</span><h3>{t}</h3><span class="more">Read article {A}</span></a>'
    for c, t in ARTICLES
)
ideas = f"""
<!-- DRAFT COPY: Ideas page intro uses the "Learn More" copy from the doc. Article links are placeholders until posts are migrated from Wix. -->
<section class="type-hero">
  <div class="plate" aria-hidden="true" style="border-color:rgba(224,87,63,.35)"></div>
  <div class="wrap" style="position:relative">
    <span class="eyebrow">Ideas &amp; Industry Voice</span>
    <h1>Better questions about food.</h1>
    <p class="lead">Food is changing quickly, but the most useful conversations still begin with better questions. What makes an experience memorable? What earns and keeps consumer trust? What helps a founder grow without weakening the business behind the brand? Through articles, commentary, speaking and media, I examine the forces shaping food and hospitality and make the bigger picture easier to see.</p>
    <div class="btn-row">{btn("#latest", "Read the Latest")}{btn("contact.html?topic=Speaking", "Invite Me to Speak", "btn-ghost")}</div>
  </div>
</section>

<section class="section bg-cream2" id="latest">
  <div class="wrap">
    <div class="fade">
      <span class="eyebrow">The Latest</span>
      <h2>Food, law, culture and business.</h2>
    </div>
    <div class="articles fade">{arts}</div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="media fade"><img src="assets/img/azeezat-green.webp" alt="Azeezat in a green shirt and head wrap, sipping a drink" loading="lazy" width="1067" height="1600"></div>
    <div class="fade">
      <span class="eyebrow">Speaking &amp; Media</span>
      <h2>Bring the TFL perspective to your audience.</h2>
      <p class="lead">I contribute a distinctive perspective on food, law, culture, business and consumer experience. Invite me to speak, contribute to a story, join a conversation or collaborate on work that makes food matter more.</p>
      <ul class="next-steps" style="margin-top:24px">
        <li><span><strong>Speaking:</strong> keynotes, panels and workshops on food, law, culture and business growth.</span></li>
        <li><span><strong>Media:</strong> interviews, commentary and expert contributions.</span></li>
        <li><span><strong>Collaborations:</strong> aligned projects, campaigns and content partnerships.</span></li>
      </ul>
      <div class="btn-row">{btn("contact.html?topic=Speaking", "Invite Me to Speak")}{btn("contact.html?topic=Collaboration", "Explore Collaborations", "btn-ghost")}</div>
    </div>
  </div>
</section>
"""
page("ideas.html", "Ideas",
     "Commentary, stories and practical perspectives from That Foodie Lawyer on consumer expectations, food law, hospitality, business and culture.",
     ideas)

# ---------------------------------------------------------------- CONTACT
contact = f"""
<section class="type-hero">
  <div class="wrap">
    <span class="eyebrow">Start a Conversation</span>
    <h1>Tell me what you are working on.</h1>
    <p class="lead">Whether you are building a stronger business, creating a meaningful experience or looking for a fresh industry perspective, I would love to hear from you. I read every message personally.</p>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap booking-grid">
    <aside class="fade">
      <div class="contact-card">
        <h3>Reach me directly</h3>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p style="opacity:.8;font-size:.95rem;margin:0">All services and collaborations are currently delivered virtually unless otherwise agreed.</p>
      </div>
      <div style="margin-top:28px">
        <h3>Ready for advisory support?</h3>
        <p style="color:var(--ink-soft)">Skip the back and forth. Book and pay for a 45-minute Food &amp; Hospitality Strategy Call online.</p>
        {btn("book.html", "Book a Strategy Call")}
      </div>
    </aside>
    <form class="form fade" id="contact-form" action="/api/contact" method="post">
      <div class="row">
        <div><label for="name">Name</label><input id="name" name="name" required autocomplete="name"></div>
        <div><label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email"></div>
      </div>
      <div class="row">
        <div><label for="org">Business or organization <span style="font-weight:400;color:var(--ink-soft)">(optional)</span></label><input id="org" name="organization" autocomplete="organization"></div>
        <div><label for="topic">I am interested in</label>
          <select id="topic" name="topic">
            <option>Advisory</option><option>Speaking</option><option>Media</option><option>Collaboration</option><option>Experiences</option><option>Something else</option>
          </select></div>
      </div>
      <div><label for="message">Message</label><textarea id="message" name="message" required></textarea></div>
      <input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div><button class="btn btn-primary" type="submit">Send Message {A}</button></div>
      <p class="form-status" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>
"""
page("contact.html", "Contact",
     "Contact That Foodie Lawyer for advisory, speaking, media, collaborations and experiences. Services delivered virtually.",
     contact)

# ---------------------------------------------------------------- BOOK
book = f"""
<section class="type-hero forest" style="padding-bottom:clamp(56px,7vw,88px)">
  <div class="plate" aria-hidden="true"></div>
  <div class="wrap" style="position:relative">
    <span class="eyebrow">Food &amp; Hospitality Strategy Call</span>
    <h1>Start with the right conversation.</h1>
    <p class="lead">$249 CAD · 45 minutes · Virtual</p>
  </div>
</section>

<section class="section">
  <div class="wrap booking-grid">
    <div>
      <h2 style="font-size:clamp(1.6rem,2.6vw,2.2rem)">How booking works</h2>
      <ol class="booking-steps">
        <li><span class="n">1</span><span><strong>Choose a time</strong> that works for you in the calendar.</span></li>
        <li><span class="n">2</span><span><strong>Share a little context</strong> about your business and what you want to focus on.</span></li>
        <li><span class="n">3</span><span><strong>Pay securely</strong> by card through Stripe to confirm your booking.</span></li>
        <li><span class="n">4</span><span><strong>Get your confirmation</strong> and video call link by email straight away.</span></li>
      </ol>
      <div class="kv" style="grid-template-columns:1fr">
        <div><h4>Best for</h4><p>Founders preparing to launch, facing a growth decision, navigating an operational challenge or looking for an experienced sounding board.</p></div>
        <div><h4>You leave with</h4><p>Greater clarity, priority actions and a recommendation for the most suitable next step.</p></div>
      </div>
      <p style="color:var(--ink-soft);font-size:.92rem">Questions before booking? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
    <div>
      <div class="booking-shell">
        <div class="calendly-inline-widget" data-url="{CALENDLY_URL}?hide_gdpr_banner=1&amp;background_color=ffffff&amp;text_color=2a2420&amp;primary_color=e0573f"></div>
      </div>
      <div class="confirm" role="status"><strong>You are booked.</strong> Check your email for your confirmation and meeting link. I look forward to speaking with you.</div>
    </div>
  </div>
</section>
"""
page("book.html", "Book a Strategy Call",
     "Book and pay for a 45-minute Food & Hospitality Strategy Call with Azeezat Adejare, That Foodie Lawyer. $249 CAD, virtual.",
     book, active="book.html")

# ---------------------------------------------------------------- 404
page("404.html", "Page not found", "Page not found.", f"""
<section class="type-hero"><div class="wrap center narrow">
<span class="eyebrow">404</span><h1 style="margin:0 auto .4em">This page is not on the menu.</h1>
<p class="lead">The page you are looking for may have moved.</p><div class="btn-row">{btn("index.html", "Back to Home")}</div>
</div></section>""", active="")

print("Built:", sorted(p.name for p in OUT.glob("*.html")))
