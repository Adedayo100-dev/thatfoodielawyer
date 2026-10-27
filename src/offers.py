"""TFL Global Consulting offer suite (from Azeezat's Refined Offer Suite doc).
The Strategy Call is the entry point: the only offer with a price and a booking page.
All other offers are recommended after the call, so they show no price.
Paste the Strategy Call's Calendly link into "calendly" once the paid event is set up.
"""

CORE = [
    {
        "id": "strategy-call",
        "page": "book.html",
        "name": "Food &amp; Hospitality Strategy Call",
        "price": "$249", "unit": "CAD", "meta": "45 minutes · Google Meet", "bookable": True,
        "calendly": "https://calendly.com/REPLACE_WITH_HER_LINK/strategy-call",
        "pay_note": "Pay securely by card through Stripe to confirm your booking.",
        "snapshot": [
            "A focused session designed to help food and hospitality founders make smarter business decisions by identifying hidden risks and uncovering opportunities for growth before they become costly mistakes.",
            "Whether you are preparing to launch, navigating operational challenges, exploring growth opportunities, or simply feeling stuck, this session provides experienced guidance and practical insight to help you move forward with greater clarity and confidence.",
        ],
        "best_intro": "Food and hospitality founders and operators seeking an experienced sounding board to help navigate operational challenges, growth opportunities, regulatory considerations, or key business decisions with greater clarity and confidence.",
        "best": ["Established founders preparing to launch a new food concept, product or location", "Caterers", "Restaurant owners", "Packaged food brands", "Food vendors", "Operators facing growth decisions"],
        "deliverables_label": "Deliverables",
        "deliverables": [
            "45-minute fact-finding and advisory session designed to understand your business, goals, challenges, and opportunities for growth",
            "Identification of key opportunities, risks, or operational considerations impacting your business",
            "Strategic insight to help you evaluate options and make more informed business decisions",
        ],
        "outcomes": [
            "Greater clarity on the challenges, opportunities, or decisions currently facing your business",
            "A clearer understanding of the priorities requiring immediate attention to support growth, profitability, and long-term success",
        ],
        "cta": "Book a Strategy Call",
        "tile": "t-sun",
    },
    {
        "id": "growth-audit",
        "page": "book-growth-audit.html",
        "name": "Growth Readiness Audit",
        "price": "", "unit": "", "meta": "90-minute structured assessment", "bookable": False,
        "calendly": "https://calendly.com/REPLACE_WITH_HER_LINK/growth-readiness-audit",
        "pay_note": "Pay securely by card through Stripe to confirm your booking.",
        "snapshot": [
            "A comprehensive business assessment designed to identify the operational, compliance, and growth barriers that may be limiting profitability, creating unnecessary risk, or preventing your business from reaching its next stage of growth.",
            "This audit helps uncover what is working, what is not, and where strategic improvements can create stronger systems, better decision-making, and a more scalable business.",
        ],
        "best_intro": "",
        "best": ["Established food businesses", "Scaling operators", "Restaurant owners", "Packaged food brands", "Businesses preparing for retail", "Businesses seeking structure and sustainable growth"],
        "deliverables_label": "Deliverables",
        "deliverables": [
            "90-minute structured business assessment examining the systems, practices, and operational factors influencing growth, profitability, and long-term sustainability",
            "Audit Findings Summary highlighting key operational, compliance, and growth observations",
            "Identification of priority risks, opportunities, and areas requiring attention",
        ],
        "outcomes": [
            "Clear visibility into the risks, inefficiencies, and growth barriers that may be impacting profitability, scalability, or operational performance",
            "Insight into the systems, processes, and business practices requiring attention to support stronger operations and sustainable growth",
            "Greater confidence making strategic decisions based on an objective assessment of the current state of the business",
        ],
        "cta": "Book the Audit",
        "tile": "t-white",
    },
    {
        "id": "implementation-sprint",
        "page": "book-implementation-sprint.html",
        "name": "Strategic Implementation Sprint",
        "price": "", "unit": "", "meta": "30-day engagement", "bookable": False,
        "calendly": "https://calendly.com/REPLACE_WITH_HER_LINK/implementation-sprint",
        "pay_note": "Book your first working session and pay for the sprint securely by card through Stripe.",
        "snapshot": [
            "Designed for businesses that know what needs attention but need strategic support turning insight into execution. This engagement helps food and hospitality operators strengthen systems, address priority challenges, and build the operational foundations required for profitable, sustainable growth.",
        ],
        "best_intro": "Businesses that have identified priority opportunities, risks, or operational challenges and require strategic support implementing meaningful improvements.",
        "best": [],
        "deliverables_label": "Deliverables",
        "deliverables": [
            "Three (3) focused working sessions dedicated to tackling your highest-priority operational, compliance, or growth initiatives",
            "A customized implementation roadmap that translates priorities into practical actions, ownership, and measurable progress",
            "Direct access to strategic guidance and feedback via email throughout the engagement period",
        ],
        "outcomes": [
            "Stronger systems, processes, and operational practices that improve consistency, accountability, and day-to-day efficiency",
            "Tangible progress on the initiatives most critical to growth, profitability, and operational performance",
            "Greater readiness for growth through improved structure, stronger execution, and reduced operational friction",
        ],
        "cta": "Start Your Sprint",
        "tile": "t-forest",
    },
    {
        "id": "advisory-partnership",
        "page": "book-advisory-partnership.html",
        "name": "Strategic Growth Advisory Partnership",
        "price": "", "unit": "", "meta": "Ongoing partnership · Minimum 3-month commitment", "bookable": False,
        "calendly": "https://calendly.com/REPLACE_WITH_HER_LINK/advisory-partnership",
        "pay_note": "Book your first advisory session and pay for your first month securely by card through Stripe.",
        "snapshot": [
            "A strategic advisory partnership for food and hospitality businesses committed to strengthening operations, protecting profitability, reducing costly mistakes, and building the systems required for sustainable growth and expansion.",
            "Designed for operators seeking more than occasional advice and looking for an experienced strategic partner to support decision-making, navigate complexity, and maintain momentum as the business grows.",
        ],
        "best_intro": "",
        "best": ["Founders seeking stronger systems and strategic support", "Multi-location restaurants", "Scaling food brands", "Importers and distributors", "Food manufacturers", "Businesses entering retail", "Operators preparing for expansion"],
        "deliverables_label": "Partnership scope",
        "deliverables": [
            "Two strategic advisory sessions per month focused on current priorities, challenges, and growth initiatives",
            "Priority email access for time-sensitive questions and business decisions between sessions",
            "Strategic guidance and feedback on agreed priority areas throughout the engagement period",
            "Accountability support to maintain momentum and progress on key business objectives",
        ],
        "explored": ["Growth planning", "Operational challenges", "Inspections and regulatory considerations", "Expansion opportunities", "Retail readiness", "Team accountability", "Customer experience", "Profitability and operational efficiency"],
        "outcomes": [
            "Greater confidence making high-impact business decisions with experienced strategic support",
            "Reduced exposure to costly mistakes, operational blind spots, and business disruption",
            "Stronger ability to navigate growth and complexity without compromising consistency, customer trust, or operational performance",
            "Earlier visibility into emerging risks and opportunities before they become expensive problems",
            "Greater readiness for expansion, retail opportunities, partnerships, and long-term growth",
        ],
        "before": ["Founder is carrying too much and becoming the bottleneck.", "Growth feels reactive rather than intentional.", "Systems are inconsistent and difficult to scale.", "Important decisions are made without experienced strategic support."],
        "after": ["The business operates with stronger systems, accountability, and operational discipline.", "Founders spend less time firefighting and more time leading strategically.", "Costly mistakes and operational blind spots are identified earlier and managed proactively.", "The business is positioned to grow with greater confidence, stability, and resilience."],
        "cta": "Begin the Partnership",
        "tile": "t-orange",
    },
]

STANDALONE = [
    {
        "name": "Packaging &amp; Label Compliance Review",
        "price": "Priced per SKU",
        "snapshot": "Avoid costly reprints, retailer rejection, and regulatory headaches by ensuring your packaging meets Canadian food labelling requirements before it goes to market.",
        "lists": [
            ("Best for", ["Imported products", "Retail-ready brands", "Food manufacturers", "Businesses launching new products"]),
            ("Review includes", ["Mandatory labelling requirements", "English/French requirements", "Ingredient declarations", "Allergen declarations", "Nutrition Facts Table presence", "Claims and marketing statements", "Net quantity declarations", "Contact information", "General Canadian compliance considerations"]),
            ("Deliverables", ["Written compliance review", "Identified gaps and risks", "Recommendations before printing", "2 rounds of revision with the designer"]),
            ("Outcomes", ["Reduced launch delays", "Protection of brand reputation", "Increased retailer confidence", "Reduced risk of costly reprints"]),
        ],
    },
    {
        "name": "Traceability System Design &amp; Recall Readiness Package",
        "price": "Scoped to your products and complexity",
        "snapshot": "Build the systems needed to trace products, respond effectively to recalls, and strengthen operational resilience. This package helps food businesses establish traceability and recall readiness systems that protect consumers, support regulatory compliance, reduce business disruption, and build confidence with retailers and partners.",
        "lists": [
            ("Deliverables", ["Ingredient &amp; supplier mapping", "Lot coding system", "1-up, 1-down traceability mapping", "Traceability SOP", "Recall plan", "Recall simulation test", "Templates &amp; logs", "Implementation guidance"]),
            ("Ideal for", ["Packaged food businesses", "Importers", "Co-packers", "Businesses supplying retailers or distributors"]),
            ("Outcomes", ["Improved recall readiness", "Reduced business disruption", "Stronger retailer confidence", "Greater regulatory confidence"]),
        ],
    },
    {
        "name": "Preventive Control Plan (PCP) Development &amp; Optimization",
        "price": "Scoped to your products and processes",
        "snapshot": "A Preventive Control Plan is a CFIA requirement for many food businesses. A PCP review is also available for businesses with an existing plan.",
        "lists": [
            ("Deliverables", ["Hazard identification", "Process flow diagrams", "Critical control points", "Preventive controls for sanitation, allergen management, environmental controls, personnel hygiene, supply chain, and storage &amp; distribution", "Monitoring procedures", "Corrective actions", "Verification procedures", "Record-keeping templates"]),
            ("Outcomes", ["Stronger food systems", "Greater operational resilience", "Regulatory readiness", "Reduced compliance risk"]),
        ],
    },
    {
        "name": "Packaging &amp; Label Development and Management",
        "price": "Scoped to your project",
        "snapshot": "Bring your food product to market with confidence through expert coordination of the packaging and label development process. This service coordinates and manages the packaging process. Graphic design fees and laboratory testing fees are billed separately unless otherwise agreed.",
        "lists": [
            ("Services include", ["Packaging strategy consultation", "Ingredient information review", "Coordination of Nutrition Facts Table development", "Collaboration with designers", "Label compliance review", "Claims assessment", "Regulatory guidance", "Revision management", "Bilingual requirements", "Final compliance check prior to printing"]),
            ("Outcomes", ["Market-ready packaging", "Stronger retailer confidence", "Increased consumer trust", "Reduced regulatory risk"]),
        ],
    },
    {
        "name": "Inspection-Ready Assessment",
        "price": "Scoped to your project",
        "snapshot": "A proactive review designed to help businesses identify and address gaps before an inspection, audit, or expansion opportunity.",
        "lists": [
            ("Deliverables", ["Operational walkthrough", "Documentation review", "Compliance gap assessment", "Inspection readiness report", "Prioritized recommendations"]),
            ("Ideal for", ["Restaurants", "Caterers", "Commissary kitchens", "Food manufacturers"]),
            ("Outcomes", ["Improved inspection readiness", "Reduced operational risk", "Greater confidence during inspections"]),
        ],
    },
    {
        "name": "Recall Response &amp; Crisis Advisory",
        "price": "Emergency response support",
        "snapshot": "When a food business faces a recall, undeclared allergen event, consumer complaint, regulatory issue, or other reputational challenge, every decision matters. This engagement provides strategic guidance to help navigate the immediate response, protect consumer trust, reduce business disruption, and emerge stronger on the other side. Each incident is unique: scope, timelines, and investment are determined by the nature of the event, operational complexity, stakeholder involvement, and urgency.",
        "lists": [
            ("Best for", ["Product recalls", "Undeclared allergen events", "Market withdrawals", "Consumer injury or illness allegations", "Regulatory investigations", "Retailer escalations", "Media attention or reputational concerns", "Significant food safety incidents"]),
            ("Support may include", ["Situation assessment and risk identification", "Strategic response planning and prioritization", "Guidance on regulatory and stakeholder considerations", "Review of consumer and public-facing communications", "Root cause analysis support", "Corrective and preventive action planning", "Systems and process improvement recommendations", "Post-incident lessons learned and resilience planning"]),
            ("Outcomes", ["Faster, more coordinated responses during high-pressure situations", "Reduced operational disruption and reputational impact", "Greater confidence communicating with regulators, retailers, partners, and consumers", "Stronger systems and controls to reduce the likelihood of repeat events", "A clearer path from crisis response to business recovery and long-term resilience"]),
        ],
    },
]
