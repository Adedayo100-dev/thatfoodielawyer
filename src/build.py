"""Builds the static HTML pages for That Foodie Lawyer into ../site.
Design: "Signature" (Sample C, chosen by the client).
Edit page content below, then run:  python3 src/build.py
"""
from pathlib import Path
from urllib.parse import quote

OUT = Path(__file__).resolve().parent.parent / "site"
SITE = "https://www.thatfoodielawyer.com"
EMAIL = "foodie@thatfoodielawyer.com"

# Paste her Calendly event link here (event must have Stripe payment turned on).
# Calendly links for each paid offer live in src/offers.py

INSTAGRAM = [
    ("@thatfoodielawyer", "https://www.instagram.com/thatfoodielawyer/"),
    ("@tflglobalconsulting", "https://www.instagram.com/tflglobalconsulting/"),
]

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("consulting.html", "Global Consulting"),
    ("experiences.html", "Experiences"),
    ("ideas.html", "Ideas"),
    ("contact.html", "Contact"),
]

A = "→"
IG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>'

MARQUEE = ("Food is business", "Food is culture", "Food is experience", "Food is trust", "Food is community")


def btn(href, label, cls=""):
    return f'<a class="btn {cls}" href="{href}">{label} {A}</a>'


def marquee():
    items = "".join(f"{t}<span>✦</span>" for t in MARQUEE) * 2
    return f'<div class="marquee" aria-hidden="true"><div>{items}</div></div>'


def header(active):
    items = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a></li>' for h, t in NAV
    )
    return f"""
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap hd">
    <a class="brand" href="index.html" aria-label="That Foodie Lawyer home">
      <img class="dark" src="assets/img/logo-tfl.png" alt="That Foodie Lawyer" width="149" height="48">
      <img class="light" src="assets/img/logo-tfl-cream.png" alt="That Foodie Lawyer" width="149" height="48">
    </a>
    <button class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="site-nav">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 7h18M3 12h18M3 17h18"/></svg>
    </button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul>{items}</ul>
      <a class="btn" href="book.html">Book a Strategy Call</a>
    </nav>
  </div>
</header>"""


def footer():
    links = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    social = "".join(f'<a href="{u}" target="_blank" rel="noopener">{IG}{n}</a>' for n, u in INSTAGRAM)
    return f"""
<footer class="site-footer">
  <div class="wrap">
    <div class="ft">
      <h2>Let's Work <span class="it">Together</span></h2>
      <p>TFL brings together food, culture, industry insight and practical strategy to move meaningful ideas forward. I work with founders, organizations, media platforms and experience partners who care about trust, quality and lasting impact. Whether you need an advisor, speaker, collaborator or thoughtful industry voice, I would love to hear what you are building. All services and collaborations are currently delivered virtually unless otherwise agreed. Reach me at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
    <div class="fb">
      <ul>{links}<li><a href="book.html">Book a Strategy Call</a></li></ul>
      <div class="social">{social}</div>
    </div>
    <div class="fm">
      <span>© <span id="yr">2026</span> That Foodie Lawyer. All rights reserved.</span>
      <span>Site by <a href="https://deewhynetworks.com" target="_blank" rel="noopener">Dee-Why</a></span>
    </div>
  </div>
</footer>
<script>document.getElementById('yr').textContent=new Date().getFullYear();</script>"""


def page(filename, title, desc, body, active=None, hdr="soft", og_image=None):
    full_title = "That Foodie Lawyer" if filename == "index.html" else f"{title} | That Foodie Lawyer"
    url = SITE + ("/" if filename == "index.html" else "/" + filename.replace(".html", ""))
    html = f"""<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
{'<base href="/">' if "/" in filename else ""}
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_image or SITE + '/assets/img/og.jpg'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#fbe9a6">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400;62..125,600;62..125,700;62..125,800;62..125,900&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body class="hdr-{hdr}">
{header(active if active is not None else filename)}
<main id="main">
{body}
</main>
{footer()}
<script src="assets/main.js" defer></script>
</body>
</html>
"""
    (OUT / filename).parent.mkdir(parents=True, exist_ok=True)
    (OUT / filename).write_text(html, encoding="utf-8")


def cta(tag, h, it, text, acts):
    return f"""
<section class="section cta on-dark">
  <div class="wrap narrow fade">
    <span class="tag">{tag}</span>
    <h2>{h} <span class="it">{it}</span></h2>
    <p>{text}</p>
    <div class="acts">{acts}</div>
  </div>
</section>"""


# ================================================================ HOME
home = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="tag">About That Foodie Lawyer</span>
      <h1>Food is never just <span class="it">what is on the plate.</span></h1>
      <p>That Foodie Lawyer is a platform for looking deeper at food: the expectations it creates, the experiences it shapes, the trust it requires and the businesses behind it. Through consumer insight, curated experiences, industry conversations and strategic advisory, I am shaping a future where people experience food more fully, beyond what is on the plate, and the industry is equipped to deliver better.</p>
      <div class="acts">{btn("#world", "Enter the World of TFL")}<a class="btn out" href="book.html">Book a Strategy Call</a></div>
    </div>
    <div class="arch">
      <img src="assets/img/azeezat-hero.webp" alt="Azeezat Adejare, That Foodie Lawyer, in a yellow blazer and tie" width="1200" height="1600" fetchpriority="high">
      <span class="sticker">Hi, I'm thatfoodielawyer</span>
    </div>
  </div>
</section>
{marquee()}

<section class="section">
  <div class="wrap duo fade">
    <h2>There is a whole world <span class="it">behind food.</span></h2>
    <div>
      <span class="tag">The TFL Point of View</span>
      <p>Food is personal, commercial and deeply connected to how people live. Behind every plate, product and hospitality moment are choices about quality, trust, service, systems and experience. TFL brings that whole picture into view so consumers can expect better, founders can build better and the industry can move forward with greater intention.</p>
    </div>
  </div>
</section>

<section class="section" id="world" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head fade">
      <h2>Discover TFL <span class="it">from every angle.</span></h2>
      <p>Explore the ideas, experiences, conversations and strategic work shaping a more thoughtful future for food and hospitality.</p>
    </div>
    <div class="tiles fade">
      <a class="tile t-forest" href="consulting.html"><span class="n">01</span><h3>Advise</h3><span class="sub">TFL Global Consulting</span><p>Build a stronger food or hospitality business with clearer decisions, smarter systems and practical support.</p><span class="go">Explore Consulting {A}</span></a>
      <a class="tile t-sun" href="experiences.html"><span class="n">02</span><h3>Experience</h3><span class="sub">Experiences by TFL</span><p>Step into thoughtfully curated experiences designed to feel intentional, engaging and worth remembering.</p><span class="go">Discover Experiences {A}</span></a>
      <a class="tile t-white" href="ideas.html"><span class="n">03</span><h3>Explore</h3><span class="sub">Ideas &amp; Industry Voice</span><p>Look deeper at the culture, systems, standards and stories shaping how food is experienced.</p><span class="go">Explore Ideas {A}</span></a>
      <a class="tile t-orange" href="contact.html?topic=Collaboration"><span class="n">04</span><h3>Connect</h3><span class="sub">Speaking, Media &amp; Collaborations</span><p>Bring the TFL perspective to your platform, audience, event or creative project.</p><span class="go">Work With Me {A}</span></a>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="wrap split">
    <div class="stack fade">
      <img src="assets/img/azeezat-green.webp" alt="Azeezat in a green shirt and head wrap, sipping a drink" loading="lazy">
      <img src="assets/img/food-table.webp" alt="A TFL event table with pastries and drinks under copper lamps" loading="lazy">
    </div>
    <div class="fade">
      <span class="tag">Ideas &amp; Industry Voice</span>
      <h2>A wider lens on <span class="it">where food is going.</span></h2>
      <p class="lead">The future of food will not be shaped by taste alone. It will be shaped by trust, culture, regulation, technology, customer expectations and the people willing to connect the dots. I bring legal thinking, industry insight and a consumer-minded perspective to the conversations defining what comes next.</p>
      <div class="acts">{btn("ideas.html", "Explore the TFL Point of View")}</div>
      <details class="reveal">
        <summary>Learn more <span class="plus" aria-hidden="true">+</span></summary>
        <div class="reveal-body">
          <p>Food is changing quickly, but the most useful conversations still begin with better questions. What makes an experience memorable? What earns and keeps consumer trust? What helps a founder grow without weakening the business behind the brand? Through articles, commentary, speaking and media, I examine the forces shaping food and hospitality and make the bigger picture easier to see.</p>
          <div class="acts" style="margin-top:8px;gap:22px">
            <a class="text-link" href="ideas.html">Read the Latest</a>
            <a class="text-link" href="contact.html?topic=Speaking">Invite Me to Speak</a>
            <a class="text-link" href="contact.html?topic=Collaboration">Explore Collaborations</a>
          </div>
        </div>
      </details>
    </div>
  </div>
</section>

<section class="section strip-sec">
  <div class="wrap">
    <div class="strip fade">
      <img src="assets/img/food-table.webp" alt="A TFL event table under copper food lamps" loading="lazy">
      <img src="assets/img/azeezat-bite.webp" alt="Azeezat at a restaurant table holding up a falafel" loading="lazy">
      <img src="assets/img/food-pastries.webp" alt="Platters of pastries and fresh fruit at a TFL event" loading="lazy">
    </div>
    <div class="strip-cap"><span class="it">Experiences by TFL</span><a class="text-link" href="experiences.html">Discover Experiences {A}</a></div>
  </div>
</section>

<section class="section testi">
  <div class="wrap fade">
    <span class="tag">Client Words</span>
    <blockquote>Awesome working with TFL!!! She really cares about your business and its growth. She is professional, factual, and process-driven. You can't miss it with TFL.</blockquote>
    <p class="who"><a href="https://www.instagram.com/realaladun/" target="_blank" rel="noopener">Aladun Inc.</a></p>
  </div>
</section>

{cta("Start a Conversation", "Let us make food", "matter more.",
     "Whether you are building a stronger business, creating a meaningful experience or looking for a fresh industry perspective, I would love to hear what you are working on.",
     btn("contact.html", "Start the Conversation", "sun") + '<a class="btn out" href="book.html">Book a Strategy Call</a>')}
"""
page("index.html", "Home",
     "That Foodie Lawyer is a platform for looking deeper at food: consumer insight, curated experiences, industry conversations and strategic advisory by Azeezat Adejare.",
     home)

# ================================================================ ABOUT
about = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="tag">About That Foodie Lawyer</span>
      <h1>I see the whole world <span class="it">behind food.</span></h1>
      <p>I created That Foodie Lawyer to explore everything that shapes how food is experienced. TFL brings together consumer expectations, thoughtful experiences, practical industry insight and the systems behind trust. It is a platform for helping people look deeper, expect better and understand the choices that shape what reaches the plate and what keeps them coming back.</p>
      <div class="acts">{btn("#meet", "Meet Azeezat")}</div>
    </div>
    <div class="arch"><img src="assets/img/azeezat-about.webp" alt="Azeezat at a restaurant table, playfully holding a falafel up to her eye" width="1200" height="1600" fetchpriority="high" style="object-position:center 30%"></div>
  </div>
</section>
{marquee()}

<section class="section">
  <div class="wrap duo fade">
    <h2>More than what is <span class="it">on the plate.</span></h2>
    <div>
      <span class="tag">TFL Worldview</span>
      <p>Food is business. Food is culture. Food is memory, trust and experience. Behind every dish, product and hospitality moment are choices about people, standards, systems, service and story. TFL exists to make those choices more visible and to show how much becomes possible when the whole picture is considered.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head fade">
      <h2>A point of view <span class="it">with purpose.</span></h2>
      <p>Three principles shape how I explore ideas, create experiences and support the people building the future of food.</p>
    </div>
    <div class="tiles short fade" style="--cols:3">
      <div class="tile t-forest"><span class="n">01</span><h3>Curiosity</h3><p style="margin-top:14px">I look beneath the surface. I ask what shaped the food, who is represented, what the consumer experiences and what the business needs to thrive.</p></div>
      <div class="tile t-sun"><span class="n">02</span><h3>Clarity</h3><p style="margin-top:14px">I make complex ideas easier to understand and act on, whether the subject is culture, compliance, strategy or customer trust.</p></div>
      <div class="tile t-white"><span class="n">03</span><h3>Connection</h3><p style="margin-top:14px">I bring people, perspectives and possibilities together. The strongest food stories and businesses are built through meaningful relationships.</p></div>
    </div>
  </div>
</section>

<section class="section bg-soft" id="meet">
  <div class="wrap split">
    <div class="fade">
      <span class="tag">Meet Azeezat</span>
      <h2>An industry voice <span class="it">with a practical lens.</span></h2>
      <p>I am Azeezat Adejare, also known as That Foodie Lawyer. I am a dual-qualified lawyer, food and hospitality strategist, and the founder of TFL Global Consulting. My work brings together legal and commercial judgment, consumer insight and a clear view of what makes food businesses and experiences worthy of trust.</p>
      <p>I created TFL to raise expectations around how food is experienced and to equip the people behind food to build with greater clarity, consistency and intention. From advisory work and industry conversations to curated experiences and consumer-facing insight, I look at the whole picture: the promise a brand makes, the systems that support it and the experience that brings people back.</p>
      <div class="acts">{btn("#work-with-me", "Work With Me")}</div>
    </div>
    <div class="media arch-img fade"><img src="assets/img/azeezat-table.webp" alt="Azeezat in a yellow blazer at a set table with drinks and falafel" loading="lazy"></div>
  </div>
</section>

<section class="section" id="work-with-me">
  <div class="wrap">
    <div class="sec-head fade">
      <h2>Ways to <span class="it">work together.</span></h2>
      <p>There are several ways to work with me, depending on what you are building and the perspective you need.</p>
    </div>
    <div class="ways fade">
      <div class="way"><div class="ico">A</div><h3>Advisory</h3><p>Strategic support for food and hospitality founders through TFL Global Consulting.</p></div>
      <div class="way"><div class="ico">S</div><h3>Speaking</h3><p>Thoughtful, practical conversations on food, law, culture, consumer expectations and business growth.</p></div>
      <div class="way"><div class="ico">M</div><h3>Media</h3><p>Interviews, commentary, features and contributions informed by legal, commercial, industry and consumer insight.</p></div>
      <div class="way"><div class="ico">C</div><h3>Collaborations</h3><p>Aligned projects, campaigns and experiences that move food and hospitality forward.</p></div>
    </div>
    <div class="acts">{btn("contact.html", "Tell Me What You Are Working On")}<a class="btn out" href="mailto:{EMAIL}">{EMAIL}</a></div>
  </div>
</section>

<section class="section quote">
  <div class="wrap fade"><blockquote>The future of food will be shaped by the people willing to see the whole picture.</blockquote></div>
</section>

<section class="section">
  <div class="wrap center narrow fade">
    <span class="tag">Enter the World of TFL</span>
    <h2>Let us make food <span class="it">matter more.</span></h2>
    <p class="lead">Explore the ideas, experiences, conversations and strategic work helping people experience food more thoughtfully and helping the industry move forward with greater intention.</p>
    <div class="acts">{btn("index.html#world", "Explore TFL")}</div>
  </div>
</section>
"""
page("about.html", "About",
     "Meet Azeezat Adejare, That Foodie Lawyer: dual-qualified lawyer, food and hospitality strategist and founder of TFL Global Consulting.",
     about)

# ================================================================ CONSULTING
from offers import CORE, STANDALONE


def ul(items, cls="checks"):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def offer_card(i, o):
    best = (f"<p>{o['best_intro']}</p>" if o["best_intro"] else "") + (ul(o["best"], "chips") if o["best"] else "")
    explored = f'<h4>Commonly explored</h4>{ul(o["explored"], "chips")}' if o.get("explored") else ""
    return f"""
      <article class="ocard {o['tile']}" id="{o['id']}">
        <div class="ocard-top">
          <span class="n">Offer {i:02d}</span>
          <h3>{o['name']}</h3>
          {f'<div class="oprice">{o["price"]} <small>{o["unit"]}</small></div>' if o.get("bookable") else '<div class="orec">Recommended after your Strategy Call</div>'}
          <div class="ometa">{o['meta']}</div>
        </div>
        <p class="osnap">{o['snapshot'][0]}</p>
        <details class="odetails">
          <summary>See what is included <span class="plus" aria-hidden="true">+</span></summary>
          <div class="odbody">
            {"".join(f"<p>{p}</p>" for p in o['snapshot'][1:])}
            <h4>Best for</h4>{best}
            <h4>{o['deliverables_label']}</h4>{ul(o['deliverables'])}
            {explored}
            <h4>Outcomes</h4>{ul(o['outcomes'])}
          </div>
        </details>
        <div class="acts" style="margin-top:auto;padding-top:22px">{btn(o['page'], o['cta']) if o.get("bookable") else btn("book.html", "Start with a Strategy Call", "out")}</div>
      </article>"""


core_html = "".join(offer_card(i, o) for i, o in enumerate(CORE, 1))
POLICY = "Payments are non-refundable. You can reschedule up to 48 hours before your call."
partner = CORE[3]

standalone_html = ""
for i, s_ in enumerate(STANDALONE, 1):
    lists = "".join(f"<div><h4>{t}</h4>{ul(items)}</div>" for t, items in s_["lists"])
    plain = s_["name"].replace("&amp;", "&")
    standalone_html += f"""
      <details class="service">
        <summary><span class="num">{i:02d}</span><span><h3>{s_['name']}</h3><span class="sprice">{s_['price']}</span></span><span class="plus" aria-hidden="true">+</span></summary>
        <div class="body">
          <p>{s_['snapshot']}</p>
          <div class="sgrid">{lists}</div>
          <a class="btn" href="contact.html?service={quote(plain)}">Ask about this service {A}</a>
        </div>
      </details>"""

consulting = f"""
<section class="page-hero forest on-dark">
  <div class="ring" aria-hidden="true"></div>
  <div class="wrap" style="position:relative">
    <img src="assets/img/logo-consulting-cream.png" alt="TFL Global Consulting" style="width:min(260px,60vw);height:auto;margin-bottom:34px">
    <h1>Build a food or hospitality business <span class="it">ready for more.</span></h1>
    <p class="lead">Helping food and hospitality businesses build growth-ready operations through smarter systems, strategic compliance, risk intelligence and better customer experiences that protect profit and support sustainable growth.</p>
    <div class="acts">{btn("#offers", "View the Offer Suite", "sun")}<a class="btn out" href="book.html">Book a Strategy Call</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap duo fade">
    <h2>Great food needs <span class="it">a strong business behind it.</span></h2>
    <div>
      <span class="tag">The TFL Point of View</span>
      <p>A memorable product may earn attention, but strong systems, sound decisions, consistent delivery and customer trust are what help a business last. My advisory work looks at the full operating picture, then helps you focus on the changes that matter most.</p>
      <p>Good food deserves a business built to support it. The work can include strategy, operational readiness, compliance, risk, customer experience and implementation support.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head fade">
      <h2>From clarity <span class="it">to capability.</span></h2>
      <p>Support is structured to help you understand the real challenge, identify the right priorities and turn better decisions into stronger business practices.</p>
    </div>
    <div class="tiles short fade">
      <div class="tile t-forest"><span class="n">01</span><h3>Strategy &amp; Direction</h3><p style="margin-top:14px">Clarify the decision in front of you, identify hidden risks and opportunities, and define the most useful path forward.</p></div>
      <div class="tile t-sun"><span class="n">02</span><h3>Readiness &amp; Risk</h3><p style="margin-top:14px">Examine the systems, compliance gaps and operational barriers that may be limiting growth, trust or profitability.</p></div>
      <div class="tile t-white"><span class="n">03</span><h3>Implementation &amp; Accountability</h3><p style="margin-top:14px">Translate priorities into practical actions, clear ownership and measurable progress.</p></div>
      <div class="tile t-orange"><span class="n">04</span><h3>Ongoing Advisory</h3><p style="margin-top:14px">Navigate growth, complexity and high-impact decisions with consistent strategic support.</p></div>
    </div>
  </div>
</section>

<section class="section bg-soft" id="offers">
  <div class="wrap">
    <div class="sec-head fade">
      <div><span class="tag">TFL Global Consulting Offer Suite</span><h2>Food &amp; Hospitality <span class="it">Growth Advisory.</span></h2></div>
      <p>Every engagement begins with a Strategy Call. Based on what we discover about your business and your goals, I will recommend the offer that best suits your needs.</p>
    </div>
    <div class="offers fade">{core_html}
    </div>
  </div>
</section>


<section class="section testi">
  <div class="wrap fade">
    <span class="tag">Client Words</span>
    <blockquote>Awesome working with TFL!!! She really cares about your business and its growth. She is professional, factual, and process-driven. You can't miss it with TFL.</blockquote>
    <p class="who"><a href="https://www.instagram.com/realaladun/" target="_blank" rel="noopener">Aladun Inc.</a></p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="sec-head fade">
      <div><span class="tag">The Partnership Difference</span><h2>Business <span class="it">transformation.</span></h2></div>
      <p>What changes when a business has an experienced strategic partner through the Strategic Growth Advisory Partnership.</p>
    </div>
    <div class="journey fade">
      <div class="jcol before"><h3>Before</h3>{ul(partner['before'])}</div>
      <div class="jarrow" aria-hidden="true">{A}</div>
      <div class="jcol after"><h3>After</h3>{ul(partner['after'])}</div>
    </div>
    <div class="acts center" style="justify-content:center">{btn("book.html", "Start with a Strategy Call")}</div>
  </div>
</section>

<section class="section bg-soft" id="focused-services">
  <div class="wrap">
    <div class="sec-head fade">
      <div><span class="tag">Stand-Alone Services</span><h2>Specialist support for <span class="it">a clearly defined need.</span></h2></div>
      <p>For founders who already know the specific issue they need to solve. Ask about any service and I will confirm scope and investment.</p>
    </div>
    <div class="services fade">{standalone_html}
    </div>
  </div>
</section>
{cta("Start Here", "Not sure", "where to begin?",
     "Book a Strategy Call. In 45 minutes we will clarify your priorities and identify the most useful next step for your business.",
     btn("book.html", "Book a Food &amp; Hospitality Strategy Call", "sun"))}
"""
page("consulting.html", "Global Consulting",
     "TFL Global Consulting helps food and hospitality businesses build growth-ready operations: strategy calls, growth audits, implementation sprints, advisory partnerships and Canadian food compliance services.",
     consulting, hdr="forest")

# ================================================================ EXPERIENCES (interim copy, approved for now)
experiences = f"""
<!-- INTERIM COPY: written in the TFL voice; Azeezat may replace it later. -->
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="tag">Experiences by TFL</span>
      <h1>Food experiences <span class="it">worth remembering.</span></h1>
      <p>The best food experiences stay with people because every detail feels considered. Experiences by TFL brings that standard to intentional gatherings, hospitality moments and story-led experiences that create connection, spark curiosity and leave a lasting impression.</p>
      <div class="acts">{btn("contact.html?topic=Experiences", "Plan an Experience")}</div>
    </div>
    <div class="arch"><img src="assets/img/food-table.webp" alt="A TFL event table with pastries, small chops and drinks under copper food lamps" fetchpriority="high" style="object-position:center 55%"></div>
  </div>
</section>
{marquee()}

<section class="section">
  <div class="wrap duo fade">
    <h2>Every detail tells <span class="it">part of the story.</span></h2>
    <div>
      <span class="tag">The Experience Standard</span>
      <p>A great experience is more than a good meal. It is the welcome, the setting, the conversation, the culture on the table and the feeling people carry home. I design experiences where those details work together, so guests do not just taste the food. They understand it.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head fade"><h2>Intentional <span class="it">by design.</span></h2></div>
    <div class="tiles short fade" style="--cols:3">
      <div class="tile t-forest"><span class="n">01</span><h3>Intentional Gatherings</h3><p style="margin-top:14px">Curated tables, tastings and dinners that bring the right people together around food with meaning.</p></div>
      <div class="tile t-sun"><span class="n">02</span><h3>Hospitality Moments</h3><p style="margin-top:14px">Brand activations, launches and partner events shaped to feel warm, polished and true to the people hosting them.</p></div>
      <div class="tile t-orange"><span class="n">03</span><h3>Story-Led Experiences</h3><p style="margin-top:14px">Experiences built around culture, heritage and the stories behind the dish, designed to spark curiosity and conversation.</p></div>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="wrap split">
    <div class="fade">
      <span class="tag">Partner With TFL</span>
      <h2>Have an experience <span class="it">in mind?</span></h2>
      <p class="lead">Whether you are a brand, venue, organization or community partner, I would love to hear what you are imagining. Tell me about your audience, your occasion and the feeling you want people to leave with, and we will shape it from there.</p>
      <div class="acts">{btn("contact.html?topic=Experiences", "Start the Conversation")}</div>
    </div>
    <div class="media arch-img fade"><img src="assets/img/food-pastries.webp" alt="Platters of golden pastries and fresh fruit at a TFL event" loading="lazy"></div>
  </div>
</section>
"""
page("experiences.html", "Experiences",
     "Experiences by TFL: intentional gatherings, hospitality moments and story-led food experiences that create connection and leave a lasting impression.",
     experiences)

# ================================================================ IDEAS (interim copy)
import json, html as _html
POSTS = json.loads((Path(__file__).parent / "posts.json").read_text(encoding="utf-8"))
arts = "".join(
    f'<a class="article has-img" href="post/{p["slug"]}"><img src="{p["img"]}/v1/fill/w_900,h_560,al_c,q_80/cover.jpg" alt="" loading="lazy"><span class="cat">{p["cat"]}</span><h3>{_html.escape(p["title"])}</h3><span class="go">Read article {A}</span></a>'
    for p in POSTS
)
ideas = f"""
<!-- INTERIM COPY. Articles migrated from Wix (src/posts.json). -->
<section class="page-hero soft">
  <div class="ring" aria-hidden="true" style="border-color:rgba(225,90,63,.35)"></div>
  <div class="wrap" style="position:relative">
    <span class="tag">Ideas &amp; Industry Voice</span>
    <h1>Better questions <span class="it">about food.</span></h1>
    <p class="lead">Food is changing quickly, but the most useful conversations still begin with better questions. What makes an experience memorable? What earns and keeps consumer trust? What helps a founder grow without weakening the business behind the brand? Through articles, commentary, speaking and media, I examine the forces shaping food and hospitality and make the bigger picture easier to see.</p>
    <div class="acts">{btn("#latest", "Read the Latest")}<a class="btn out" href="contact.html?topic=Speaking">Invite Me to Speak</a></div>
  </div>
</section>
{marquee()}

<section class="section" id="latest">
  <div class="wrap">
    <div class="sec-head fade"><h2>The <span class="it">latest.</span></h2><p>Commentary and stories on food, law, culture and business.</p></div>
    <div class="articles fade">{arts}</div>
  </div>
</section>

<section class="section bg-soft">
  <div class="wrap split">
    <div class="media arch-img fade"><img src="assets/img/azeezat-green.webp" alt="Azeezat in a green shirt and head wrap, sipping a drink" loading="lazy"></div>
    <div class="fade">
      <span class="tag">Speaking &amp; Media</span>
      <h2>Bring the TFL perspective <span class="it">to your audience.</span></h2>
      <p class="lead">I contribute a distinctive perspective on food, law, culture, business and consumer experience. Invite me to speak, contribute to a story, join a conversation or collaborate on work that makes food matter more.</p>
      <ul class="steps" style="margin-top:22px">
        <li><span><strong>Speaking:</strong> keynotes, panels and workshops on food, law, culture and business growth.</span></li>
        <li><span><strong>Media:</strong> interviews, commentary and expert contributions.</span></li>
        <li><span><strong>Collaborations:</strong> aligned projects, campaigns and content partnerships.</span></li>
      </ul>
      <div class="acts">{btn("contact.html?topic=Speaking", "Invite Me to Speak")}<a class="btn out" href="contact.html?topic=Collaboration">Explore Collaborations</a></div>
    </div>
  </div>
</section>
"""
page("ideas.html", "Ideas",
     "Commentary, stories and practical perspectives from That Foodie Lawyer on consumer expectations, food law, hospitality, business and culture.",
     ideas)

# ================================================================ BLOG POSTS (same URLs as on Wix: /post/<slug>)
for i, p in enumerate(POSTS):
    out, in_list = [], False
    for kind, text in p["blocks"]:
        t = _html.escape(text)
        if kind == "li":
            if not in_list:
                out.append('<ol class="post-list">'); in_list = True
            head, _, rest = t.partition("?: ") if "?: " in t else t.partition(": ")
            head = head + "?" if "?: " in t else head
            out.append(f"<li><strong>{head}:</strong> {rest}</li>" if rest else f"<li>{t}</li>")
            continue
        if in_list:
            out.append("</ol>"); in_list = False
        out.append(f"<h2>{t}</h2>" if kind == "h" else f"<p>{t}</p>")
    if in_list:
        out.append("</ol>")
    nxt = POSTS[(i + 1) % len(POSTS)]
    body = f"""
<article>
  <section class="page-hero soft post-hero">
    <div class="wrap narrow">
      <a class="text-link" href="ideas.html#latest">{A.replace("→","←")} All ideas</a>
      <p class="post-meta"><span class="tag" style="margin:0">{p["cat"]}</span> <span>{p["date"]} · That Foodie Lawyer</span></p>
      <h1 class="post-title">{_html.escape(p["title"])}</h1>
    </div>
  </section>
  <div class="wrap narrow">
    <img class="post-cover" src="{p["img"]}/v1/fill/w_1400,h_800,al_c,q_80/cover.jpg" alt="">
    <div class="post-body">{"".join(out)}</div>
    <div class="post-next">
      <span class="mini">Read next</span>
      <a href="post/{nxt["slug"]}"><h3>{_html.escape(nxt["title"])}</h3></a>
    </div>
  </div>
</article>
{cta("Start a Conversation", "Let us make food", "matter more.",
     "Whether you are building a stronger business, creating a meaningful experience or looking for a fresh industry perspective, I would love to hear what you are working on.",
     btn("contact.html", "Start the Conversation", "sun") + '<a class="btn out" href="book.html">Book a Strategy Call</a>')}
"""
    desc = p["blocks"][0][1][:155].rsplit(" ", 1)[0] + "..."
    page(f"post/{p['slug']}.html", p["title"], _html.escape(desc), body, active="ideas.html",
         og_image=f'{p["img"]}/v1/fill/w_1200,h_630,al_c,q_80/cover.jpg')

# ================================================================ CONTACT (Netlify Forms)
contact = f"""
<section class="page-hero soft">
  <div class="wrap">
    <span class="tag">Start a Conversation</span>
    <h1>Tell me what you are <span class="it">working on.</span></h1>
    <p class="lead">Whether you are building a stronger business, creating a meaningful experience or looking for a fresh industry perspective, I would love to hear from you.</p>
  </div>
</section>

<section class="section">
  <div class="wrap two">
    <aside class="fade">
      <div class="card-dark">
        <h3>Reach me directly</h3>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p style="opacity:.8;font-size:.95rem;margin:0">All services and collaborations are currently delivered virtually unless otherwise agreed.</p>
      </div>
      <div style="margin-top:30px">
        <h3>Ready for advisory support?</h3>
        <p style="color:var(--soft)">Skip the back and forth. Book and pay for a 45-minute Food &amp; Hospitality Strategy Call ($249 CAD) online.</p>
        {btn("book.html", "Book a Strategy Call")}
      </div>
    </aside>
    <form class="form fade" id="contact-form" name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">
      <input type="hidden" name="form-name" value="contact">
      <p class="hp"><label>Leave this empty <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
      <div class="row">
        <div><label for="name">Name</label><input id="name" name="name" required autocomplete="name"></div>
        <div><label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email"></div>
      </div>
      <div class="row">
        <div><label for="org">Business or organization <span style="font-weight:400;color:var(--soft)">(optional)</span></label><input id="org" name="organization" autocomplete="organization"></div>
        <div><label for="topic">I am interested in</label>
          <select id="topic" name="topic"><option>Advisory</option><option>Speaking</option><option>Media</option><option>Collaboration</option><option>Experiences</option><option>Something else</option></select></div>
      </div>
      <div><label for="message">Message</label><textarea id="message" name="message" required></textarea></div>
      <div><button class="btn" type="submit">Send Message {A}</button></div>
      <p class="form-status" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>
"""
page("contact.html", "Contact",
     "Contact That Foodie Lawyer for advisory, speaking, media, collaborations and experiences. Services delivered virtually.",
     contact)

# ================================================================ BOOKING PAGES (one per core offer)
for o in [x for x in CORE if x.get("bookable")]:
    others = "".join(f'<li><a href="consulting.html#{x["id"]}">{x["name"]}</a></li>' for x in CORE if x is not o)
    book = f"""
<section class="page-hero forest on-dark">
  <div class="ring" aria-hidden="true"></div>
  <div class="wrap" style="position:relative">
    <span class="tag">Book with TFL Global Consulting</span>
    <h1>{o['name']}</h1>
    <p class="lead">{o['price']} {o['unit']} · {o['meta']}</p>
  </div>
</section>

<section class="section">
  <div class="wrap two">
    <div>
      <p class="lead">{o['snapshot'][0]}</p>
      <h2 style="font-size:clamp(1.8rem,3vw,2.4rem);margin-top:34px">How booking <span class="it">works</span></h2>
      <ol class="bsteps">
        <li><span class="n">1</span><span><strong>Choose a time</strong> that works for you in the calendar.</span></li>
        <li><span class="n">2</span><span><strong>Share a little context</strong> about your business and what you want to focus on.</span></li>
        <li><span class="n">3</span><span><strong>{o['pay_note']}</strong></span></li>
        <li><span class="n">4</span><span><strong>Get your confirmation</strong> and Google Meet link by email straight away.</span></li>
      </ol>
      <div class="kv" style="grid-template-columns:1fr">
        <div><h4>{o['deliverables_label']}</h4>{ul(o['deliverables'])}</div>
        <div><h4>Outcomes</h4>{ul(o['outcomes'])}</div>
      </div>
      <div class="policy"><strong>Booking policy.</strong> {POLICY}</div>
      <p class="mini" style="margin-top:28px">Where the call can lead</p>
      <p style="color:var(--soft);font-size:.95rem">After the call, I may recommend one of these, based on your goals and what we uncover together:</p>
      <ul class="checks">{others}</ul>
      <p style="color:var(--soft);font-size:.92rem;margin-top:20px">Questions before booking? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
    <div>
      <div class="shell"><div class="calendly-inline-widget" data-url="{o['calendly']}?hide_gdpr_banner=1&amp;background_color=ffffff&amp;text_color=16130f&amp;primary_color=e15a3f"></div></div>
      <div class="confirm" role="status"><strong>You are booked.</strong> Check your email for your confirmation and meeting link. I look forward to speaking with you.</div>
    </div>
  </div>
</section>
"""
    page(o["page"], o["name"].replace("&amp;", "&"),
         f"Book the {o['name'].replace('&amp;', '&')} with Azeezat Adejare, That Foodie Lawyer. {o['price']} {o['unit']}, virtual.",
         book, active="book.html" if o["page"] == "book.html" else "consulting.html", hdr="forest")

# ================================================================ 404
page("404.html", "Page not found", "Page not found.", f"""
<section class="page-hero soft"><div class="wrap center">
<span class="tag">404</span><h1 style="margin:0 auto .4em">Not on <span class="it">the menu.</span></h1>
<p class="lead" style="margin:0 auto">The page you are looking for may have moved.</p><div class="acts">{btn("index.html", "Back to Home")}</div>
</div></section>""", active="")

print("Built:", sorted(p.name for p in OUT.glob("*.html")))
