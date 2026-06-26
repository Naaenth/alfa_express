#!/usr/bin/env python3
"""Generate all 8 complete HTML pages for the Apex Logistics site.
Shared head/header/footer/scripts are defined once and assembled with each
page's unique main content so every output file is complete and consistent.
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("fleet.html", "Fleet"),
    ("careers.html", "Careers"),
    ("contact.html", "Contact"),
]

SERVICE_LINKS = [
    "Road Transport", "Warehousing", "Customs Clearance",
    "Intermodal", "Express Delivery", "Supply Chain Management",
]


def head(title, description, og_image="assets/images/hero-placeholder.svg", extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#1E3A8A">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Apex Logistics">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{og_image}">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">

  <!-- Preconnect for Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <!-- Google Fonts: Montserrat (headings) + Inter (body) -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">

  <!-- Font Awesome (free) -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" referrerpolicy="no-referrer">
  <!-- AOS (Animate On Scroll) -->
  <link rel="stylesheet" href="https://unpkg.com/aos@2.3.4/dist/aos.css">
  <!-- Swiper -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">

  <!-- Site styles -->
  <link rel="stylesheet" href="css/variables.css">
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/responsive.css">
{extra_head}</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
"""


def header(active):
    def link(href, label):
        cur = ' aria-current="page"' if href == active else ""
        if label == "Contact":
            return f'<li><a href="{href}" class="btn btn-accent btn-sm"{cur}>{label}</a></li>'
        return f'<li><a href="{href}"{cur}>{label}</a></li>'

    def mlink(href, label):
        cur = ' aria-current="page"' if href == active else ""
        return f'<li><a href="{href}"{cur}>{label}</a></li>'

    desktop = "\n          ".join(link(h, l) for h, l in NAV)
    mobile = "\n        ".join(mlink(h, l) for h, l in NAV)

    return f"""  <!-- ============ HEADER ============ -->
  <header class="site-header" id="site-header">
    <div class="container header-inner">
      <a href="index.html" class="brand" aria-label="Apex Logistics — home">
        <img src="assets/images/logo-placeholder.svg" alt="" class="brand-logo" width="40" height="40">
        <span class="brand-name">Apex Logistics</span> <!-- REPLACE: company name -->
      </a>

      <nav class="main-nav" aria-label="Main navigation">
        <ul class="nav-list">
          {desktop}
        </ul>
      </nav>

      <button class="nav-toggle" id="nav-toggle" aria-label="Toggle navigation" aria-expanded="false" aria-controls="mobile-nav">
        <span class="nav-toggle-bar"></span>
        <span class="nav-toggle-bar"></span>
        <span class="nav-toggle-bar"></span>
      </button>
    </div>
  </header>

  <!-- Mobile slide-in drawer + overlay -->
  <div class="nav-overlay" id="nav-overlay" hidden></div>
  <aside class="mobile-nav" id="mobile-nav" aria-label="Mobile navigation" aria-hidden="true">
    <div class="mobile-nav-head">
      <span class="brand-name">Apex Logistics</span>
      <button class="mobile-nav-close" id="mobile-nav-close" aria-label="Close navigation">&times;</button>
    </div>
    <ul class="mobile-nav-list">
      {mobile}
    </ul>
    <div class="mobile-nav-foot">
      <a href="tel:+48123456789"><i class="fa-solid fa-phone" aria-hidden="true"></i> +48 123 456 789</a>
    </div>
  </aside>
"""


def footer():
    quick = "\n          ".join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV)
    services = "\n          ".join(f'<li><a href="services.html">{s}</a></li>' for s in SERVICE_LINKS)
    return f"""  <!-- ============ FOOTER ============ -->
  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-col footer-about">
        <div class="footer-brand">
          <img src="assets/images/logo-placeholder.svg" alt="" class="footer-logo" width="36" height="36">
          <span class="brand-name">Apex Logistics</span>
        </div>
        <p class="footer-blurb">Reliable road, warehousing, and supply&nbsp;chain solutions that keep your goods moving across borders — on time, every time.</p>
        <ul class="social-links" aria-label="Social media">
          <li><a href="#" aria-label="Apex Logistics on LinkedIn"><i class="fa-brands fa-linkedin-in" aria-hidden="true"></i></a></li>
          <li><a href="#" aria-label="Apex Logistics on Facebook"><i class="fa-brands fa-facebook-f" aria-hidden="true"></i></a></li>
          <li><a href="#" aria-label="Apex Logistics on X"><i class="fa-brands fa-x-twitter" aria-hidden="true"></i></a></li>
          <li><a href="#" aria-label="Apex Logistics on Instagram"><i class="fa-brands fa-instagram" aria-hidden="true"></i></a></li>
        </ul>
      </div>

      <nav class="footer-col" aria-label="Quick links">
        <h2 class="footer-heading">Quick Links</h2>
        <ul>
          {quick}
        </ul>
      </nav>

      <nav class="footer-col" aria-label="Services">
        <h2 class="footer-heading">Services</h2>
        <ul>
          {services}
        </ul>
      </nav>

      <div class="footer-col">
        <h2 class="footer-heading">Contact</h2>
        <ul class="footer-contact">
          <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> <span>ul. Przykładowa 12, 30-001 Kraków, Poland</span></li> <!-- REPLACE: address -->
          <li><i class="fa-solid fa-phone" aria-hidden="true"></i> <a href="tel:+48123456789">+48 123 456 789</a></li> <!-- REPLACE: phone -->
          <li><i class="fa-solid fa-envelope" aria-hidden="true"></i> <a href="mailto:office@apexlogistics.example">office@apexlogistics.example</a></li> <!-- REPLACE: email -->
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="container footer-bottom-inner">
        <p>&copy; <span id="current-year">2026</span> Apex Logistics. All rights reserved.</p>
        <p class="footer-legal"><a href="privacy.html">Privacy Policy</a> <span aria-hidden="true">·</span> <a href="terms.html">Terms of Use</a></p>
      </div>
    </div>
  </footer>
"""


def scripts(extra=""):
    return f"""  <!-- ============ SCRIPTS ============ -->
  <!-- Libraries (CDN) -->
  <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
  <!-- Site scripts -->
  <script src="js/navigation.js" defer></script>
  <script src="js/main.js" defer></script>
{extra}</body>
</html>
"""


def page(filename, title, description, main_html, extra_head="", extra_scripts="", og_image="assets/images/hero-placeholder.svg"):
    active = filename
    html = (
        head(title, description, og_image, extra_head)
        + header(active)
        + '  <main id="main">\n'
        + main_html
        + "  </main>\n\n"
        + footer()
        + "\n"
        + scripts(extra_scripts)
    )
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename, f"({len(html)} bytes)")


# Reusable section snippets -------------------------------------------------

def page_hero(eyebrow, h1, lead, crumb_label):
    return f"""    <!-- Page hero -->
    <section class="page-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a> <span aria-hidden="true">/</span> <span aria-current="page">{crumb_label}</span>
        </nav>
        <p class="eyebrow eyebrow-light" data-aos="fade-up">{eyebrow}</p>
        <h1 data-aos="fade-up" data-aos-delay="50">{h1}</h1>
        <p class="page-hero-lead" data-aos="fade-up" data-aos-delay="100">{lead}</p>
      </div>
    </section>
"""


def trust_bar():
    logos = "\n          ".join(
        f'<li><img src="assets/images/partner-logo-placeholder.svg" alt="Partner company {i}" loading="lazy" width="140" height="48"></li>'
        for i in range(1, 7)
    )
    return f"""    <!-- Trust bar -->
    <section class="trust-bar" aria-label="Our partners">
      <div class="container">
        <p class="trust-label">Trusted by supply chain teams across Europe</p>
        <ul class="trust-logos">
          {logos}
        </ul>
      </div>
    </section>
"""


SERVICES = [
    ("truck-fast", "Road Transport", "Full-load and groupage road freight across Poland and the EU, with live tracking from pickup to delivery."),
    ("warehouse", "Warehousing", "Secure short- and long-term storage, pick-and-pack, and inventory management in modern facilities."),
    ("file-circle-check", "Customs Clearance", "Import and export customs handling, documentation, and duty advice that keep shipments moving."),
    ("train-subway", "Intermodal", "Combined road, rail, and sea routing that lowers cost and carbon on long-haul lanes."),
    ("bolt", "Express Delivery", "Time-critical and same-day dispatch for urgent freight when the deadline cannot move."),
    ("diagram-project", "Supply Chain Management", "End-to-end planning, consolidation, and reporting that give you one clear view of every shipment."),
]


def services_grid(count=4, with_icons=True):
    items = SERVICES[:count]
    cards = []
    for i, (icon, title, desc) in enumerate(items):
        cards.append(f"""          <article class="card service-card" data-aos="fade-up" data-aos-delay="{i*60}">
            <div class="service-icon"><i class="fa-solid fa-{icon}" aria-hidden="true"></i></div>
            <h3>{title}</h3>
            <p>{desc}</p>
            <a class="card-link" href="services.html">Learn more <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
          </article>""")
    return "\n".join(cards)


INDUSTRIES = [
    ("industry", "Manufacturing"),
    ("cart-shopping", "Retail &amp; E-commerce"),
    ("flask", "Chemicals"),
    ("apple-whole", "Food &amp; Beverage"),
    ("microchip", "Technology"),
    ("car", "Automotive"),
    ("pills", "Pharmaceuticals"),
    ("seedling", "Agriculture"),
]


def industries_grid(count=8):
    cells = []
    for i, (icon, label) in enumerate(INDUSTRIES[:count]):
        cells.append(f"""          <li class="industry" data-aos="zoom-in" data-aos-delay="{i*40}">
            <i class="fa-solid fa-{icon}" aria-hidden="true"></i>
            <span>{label}</span>
          </li>""")
    return "\n".join(cells)


def stats_block(aos=True):
    stats = [
        ("10000", "+", "Deliveries completed"),
        ("98", "%", "On-time performance"),
        ("25", "", "Countries served"),
        ("15", "", "Years of experience"),
    ]
    items = []
    for i, (count, suffix, label) in enumerate(stats):
        items.append(f"""          <div class="stat" data-aos="fade-up" data-aos-delay="{i*80}">
            <span class="stat-number" data-count="{count}" data-suffix="{suffix}">0{suffix}</span>
            <span class="stat-label">{label}</span>
          </div>""")
    inner = "\n".join(items)
    return f"""    <!-- Stats counters -->
    <section class="stats" aria-label="Company statistics">
      <div class="container stats-grid">
{inner}
      </div>
    </section>
"""


def cta_band(title="Ready to move your freight with confidence?",
             text="Tell us about your shipment and our team will design a route, mode, and price that fit your deadline.",
             primary=("contact.html", "Request a Quote"),
             secondary=("services.html", "View Services")):
    return f"""    <!-- CTA band -->
    <section class="cta-band">
      <div class="container cta-inner" data-aos="fade-up">
        <div class="cta-text">
          <h2>{title}</h2>
          <p>{text}</p>
        </div>
        <div class="cta-actions">
          <a href="{primary[0]}" class="btn btn-accent">{primary[1]}</a>
          <a href="{secondary[0]}" class="btn btn-secondary btn-on-dark">{secondary[1]}</a>
        </div>
      </div>
    </section>
"""


def section_head(eyebrow, title, subtitle, center=True):
    cls = "section-head" + (" section-head-center" if center else "")
    sub = f'\n          <p class="section-subtitle">{subtitle}</p>' if subtitle else ""
    return f"""        <div class="{cls}" data-aos="fade-up">
          <p class="eyebrow">{eyebrow}</p>
          <h2>{title}</h2>{sub}
        </div>"""


# ===========================================================================
# INDEX
# ===========================================================================
def build_index():
    hero = f"""    <!-- HERO -->
    <!-- REPLACE all placeholder images in assets/images/ with real photos -->
    <section class="hero">
      <div class="container hero-inner">
        <div class="hero-content" data-aos="fade-up">
          <p class="hero-eyebrow"><i class="fa-solid fa-globe" aria-hidden="true"></i> Global Logistics &amp; Freight Forwarding</p>
          <h1>Moving Your Business Forward.</h1>
          <p class="hero-lead">Apex Logistics plans, ships, and tracks your freight by road, rail, and sea — combining a modern fleet with real-time visibility so your goods arrive on time, every time.</p>
          <div class="hero-actions">
            <a href="contact.html" class="btn btn-accent">Get a Free Quote</a>
            <a href="services.html" class="btn btn-secondary btn-on-dark">Explore Services</a>
          </div>
          <ul class="hero-highlights">
            <li><i class="fa-solid fa-circle-check" aria-hidden="true"></i> Live shipment tracking</li>
            <li><i class="fa-solid fa-circle-check" aria-hidden="true"></i> 25-country coverage</li>
            <li><i class="fa-solid fa-circle-check" aria-hidden="true"></i> Dedicated account manager</li>
          </ul>
        </div>
        <div class="hero-media" data-aos="fade-left" data-aos-delay="150">
          <img src="assets/images/hero-placeholder.svg" alt="Apex Logistics fleet of trucks on the motorway at sunrise" width="560" height="460">
          <div class="hero-badge">
            <span class="hero-badge-num">98%</span>
            <span class="hero-badge-label">On-time delivery</span>
          </div>
        </div>
      </div>
    </section>
"""

    services = f"""    <!-- Services overview -->
    <section class="section services-overview">
      <div class="container">
{section_head("What we do", "Logistics services built around your deadline", "From a single pallet to a full supply chain, we match the right mode and route to every shipment.")}
        <div class="grid grid-4">
{services_grid(4)}
        </div>
        <div class="section-cta" data-aos="fade-up">
          <a href="services.html" class="btn btn-primary">See all services</a>
        </div>
      </div>
    </section>
"""

    fleet = f"""    <!-- Fleet preview -->
    <section class="section section-alt fleet-preview">
      <div class="container fleet-preview-inner">
        <div class="fleet-preview-media" data-aos="fade-right">
          <img src="assets/images/truck1-placeholder.svg" alt="Apex Logistics articulated curtain-side truck" loading="lazy" width="600" height="420">
        </div>
        <div class="fleet-preview-text" data-aos="fade-left">
          <p class="eyebrow">Our fleet</p>
          <h2>A modern, well-maintained fleet for every load</h2>
          <p>From vans for express parcels to 40-tonne articulated trailers, our vehicles are GPS-tracked, regularly serviced, and driven by trained, vetted professionals. Temperature-controlled and oversized options are available on request.</p>
          <ul class="check-list">
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Euro&nbsp;6 tractors and refrigerated trailers</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Real-time GPS and temperature monitoring</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> ADR-certified drivers for hazardous goods</li>
          </ul>
          <a href="fleet.html" class="btn btn-primary">View the fleet</a>
        </div>
      </div>
    </section>
"""

    industries = f"""    <!-- Industries -->
    <section class="section industries">
      <div class="container">
{section_head("Who we serve", "Industries we keep moving", "Specialised handling and compliance for the sectors that depend on dependable delivery.")}
        <ul class="industries-grid">
{industries_grid(8)}
        </ul>
      </div>
    </section>
"""

    steps = [
        ("comments", "1", "Consultation", "We learn your goods, lanes, volumes, and deadlines to understand exactly what success looks like."),
        ("route", "2", "Planning", "Our team designs the optimal mode, route, and schedule and shares a clear, fixed quote."),
        ("truck-fast", "3", "Delivery", "Your freight moves with live tracking and proactive updates at every milestone."),
        ("headset", "4", "Support", "A dedicated manager handles documentation, exceptions, and reporting after delivery."),
    ]
    steps_html = []
    for i, (icon, num, title, desc) in enumerate(steps):
        steps_html.append(f"""          <li class="step" data-aos="fade-up" data-aos-delay="{i*70}">
            <span class="step-num">{num}</span>
            <div class="step-icon"><i class="fa-solid fa-{icon}" aria-hidden="true"></i></div>
            <h3>{title}</h3>
            <p>{desc}</p>
          </li>""")
    how = f"""    <!-- How we work -->
    <section class="section section-alt how-we-work">
      <div class="container">
{section_head("How we work", "Four steps from enquiry to delivery", "A simple, transparent process that keeps you informed at every stage.")}
        <ol class="steps">
{chr(10).join(steps_html)}
        </ol>
      </div>
    </section>
"""

    stats = stats_block()

    testimonials = [
        ("This is placeholder testimonial copy. Apex moved our seasonal stock across three countries without a single missed slot — the live tracking alone saved us hours of phone calls.", "Anna Kowalska", "Operations Lead, Retail Group"),
        ("Placeholder testimonial. Their customs team untangled a complex import that had stalled for a week. Clear communication and a fair, fixed price from start to finish.", "Marek Nowak", "Supply Chain Manager, Manufacturing"),
        ("Sample quote for layout. We switched our long-haul lanes to Apex's intermodal service and cut both cost and emissions while keeping delivery dates intact.", "Sofia Lindgren", "Logistics Director, Food &amp; Beverage"),
        ("Placeholder review text. Responsive, reliable, and genuinely proactive — when a road closure threatened a deadline, they rerouted before we even noticed.", "Tomáš Horák", "Procurement Lead, Technology"),
    ]
    slides = []
    for q, name, role in testimonials:
        slides.append(f"""            <div class="swiper-slide">
              <blockquote class="testimonial card">
                <div class="testimonial-stars" aria-label="Rated 5 out of 5">
                  <i class="fa-solid fa-star" aria-hidden="true"></i><i class="fa-solid fa-star" aria-hidden="true"></i><i class="fa-solid fa-star" aria-hidden="true"></i><i class="fa-solid fa-star" aria-hidden="true"></i><i class="fa-solid fa-star" aria-hidden="true"></i>
                </div>
                <p class="testimonial-quote">&ldquo;{q}&rdquo;</p>
                <footer class="testimonial-author">
                  <img src="assets/images/team-placeholder.svg" alt="" class="testimonial-avatar" loading="lazy" width="48" height="48">
                  <span><strong>{name}</strong><span class="testimonial-role">{role}</span></span>
                </footer>
              </blockquote>
            </div>""")
    testi = f"""    <!-- Testimonials -->
    <section class="section testimonials">
      <div class="container">
{section_head("Client feedback", "What our clients say", "Placeholder testimonials shown for layout — replace with real client quotes.")}
        <div class="swiper testimonials-swiper" data-aos="fade-up">
          <div class="swiper-wrapper">
{chr(10).join(slides)}
          </div>
          <div class="swiper-pagination"></div>
          <button class="swiper-button-prev" aria-label="Previous testimonial"></button>
          <button class="swiper-button-next" aria-label="Next testimonial"></button>
        </div>
      </div>
    </section>
"""

    cta = cta_band()

    map_section = f"""    <!-- Map + contact info -->
    <section class="section section-alt home-contact">
      <div class="container home-contact-inner">
        <div class="home-contact-text" data-aos="fade-right">
          <p class="eyebrow">Get in touch</p>
          <h2>Let's plan your next shipment</h2>
          <p>Our Kraków team responds to most enquiries within one business day. Reach out for a quote, a tracking update, or to discuss a long-term partnership.</p>
          <ul class="contact-list">
            <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> <span>ul. Przykładowa 12, 30-001 Kraków, Poland</span></li> <!-- REPLACE: address -->
            <li><i class="fa-solid fa-phone" aria-hidden="true"></i> <a href="tel:+48123456789">+48 123 456 789</a></li> <!-- REPLACE: phone -->
            <li><i class="fa-solid fa-envelope" aria-hidden="true"></i> <a href="mailto:office@apexlogistics.example">office@apexlogistics.example</a></li> <!-- REPLACE: email -->
            <li><i class="fa-solid fa-clock" aria-hidden="true"></i> <span>Mon–Fri, 08:00–18:00 CET</span></li>
          </ul>
          <a href="contact.html" class="btn btn-primary">Contact us</a>
        </div>
        <div class="home-contact-media" data-aos="fade-left">
          <img src="assets/images/coverage-map-placeholder.svg" alt="Map showing Apex Logistics coverage across Europe" loading="lazy" width="600" height="420">
        </div>
      </div>
    </section>
"""

    main = hero + trust_bar() + services + fleet + industries + how + stats + testi + cta + map_section
    build_index_extra = ""
    page("index.html",
         "Apex Logistics — Road, Rail &amp; Sea Freight Across Europe",
         "Apex Logistics provides road transport, warehousing, customs clearance, intermodal, and express delivery across 25 countries, with live tracking and a modern fleet.",
         main, extra_scripts=build_index_extra)


# ===========================================================================
# ABOUT
# ===========================================================================
def build_about():
    hero = page_hero("About Apex Logistics",
                     "Fifteen years of moving freight, building trust",
                     "We are a Kraków-based logistics provider helping businesses ship smarter across Europe — combining people who care with technology that keeps every load visible.",
                     "About")

    intro = f"""    <!-- Company intro -->
    <section class="section">
      <div class="container two-col">
        <div class="two-col-media" data-aos="fade-right">
          <img src="assets/images/warehouse-placeholder.svg" alt="Apex Logistics distribution warehouse interior" loading="lazy" width="600" height="440">
        </div>
        <div class="two-col-text" data-aos="fade-left">
          <p class="eyebrow">Who we are</p>
          <h2>A logistics partner, not just a carrier</h2>
          <p>Founded in 2011, Apex Logistics grew from a single regional route into a full-service freight forwarder serving manufacturers, retailers, and distributors across the European Union. <!-- REPLACE: company history --></p>
          <p>We believe logistics should be transparent and stress-free. That means honest pricing, proactive communication, and a dedicated point of contact who knows your business — backed by tracking technology that lets you see exactly where your freight is at any moment.</p>
          <ul class="check-list">
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> ISO-aligned quality and safety processes</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Multilingual team across Central Europe</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Carbon reporting on every shipment</li>
          </ul>
        </div>
      </div>
    </section>
"""

    mv = f"""    <!-- Mission &amp; Vision -->
    <section class="section section-alt">
      <div class="container">
{section_head("What drives us", "Mission &amp; vision", "")}
        <div class="grid grid-2 mv-grid">
          <article class="card mv-card" data-aos="fade-up">
            <div class="mv-icon"><i class="fa-solid fa-bullseye" aria-hidden="true"></i></div>
            <h3>Our mission</h3>
            <p>To move our clients' goods reliably and responsibly — giving every business, whatever its size, access to logistics that are transparent, on time, and easy to manage.</p>
          </article>
          <article class="card mv-card" data-aos="fade-up" data-aos-delay="80">
            <div class="mv-icon"><i class="fa-solid fa-eye" aria-hidden="true"></i></div>
            <h3>Our vision</h3>
            <p>To be Central Europe's most trusted logistics partner, recognised for service that goes further and for cutting the carbon cost of freight without cutting reliability.</p>
          </article>
        </div>
      </div>
    </section>
"""

    milestones = [
        ("2011", "Founded in Kraków", "Apex Logistics opens with a small road-freight fleet serving southern Poland."),
        ("2014", "First EU corridors", "We expand into Germany, Czechia, and Slovakia, adding groupage services."),
        ("2017", "Warehousing launched", "A 12,000&nbsp;m² facility opens, adding storage and pick-and-pack to our offer."),
        ("2021", "Going digital", "Live GPS tracking and a client portal give customers full shipment visibility."),
        ("2024", "25-country network", "Intermodal partnerships extend reliable coverage across the European Union."),
    ]
    tl_items = []
    for i, (year, title, desc) in enumerate(milestones):
        side = "left" if i % 2 == 0 else "right"
        tl_items.append(f"""          <li class="timeline-item timeline-{side}" data-aos="fade-up">
            <div class="timeline-marker" aria-hidden="true"></div>
            <div class="timeline-content card">
              <span class="timeline-year">{year}</span>
              <h3>{title}</h3>
              <p>{desc}</p>
            </div>
          </li>""")
    timeline = f"""    <!-- Timeline -->
    <section class="section timeline-section">
      <div class="container">
{section_head("Our journey", "Milestones along the way", "")}
        <ol class="timeline">
{chr(10).join(tl_items)}
        </ol>
      </div>
    </section>
"""

    stats = stats_block()

    team = [
        ("Jan Wiśniewski", "Managing Director"),
        ("Katarzyna Lewandowska", "Head of Operations"),
        ("Piotr Zieliński", "Fleet Manager"),
        ("Magdalena Wójcik", "Customer Success Lead"),
    ]
    team_cards = []
    for i, (name, role) in enumerate(team):
        team_cards.append(f"""          <article class="card team-card" data-aos="fade-up" data-aos-delay="{i*60}">
            <img src="assets/images/team-placeholder.svg" alt="Portrait of {name}" loading="lazy" width="260" height="260">
            <div class="team-body">
              <h3>{name}</h3>
              <p class="team-role">{role}</p>
              <ul class="team-social" aria-label="{name} on social media">
                <li><a href="#" aria-label="{name} on LinkedIn"><i class="fa-brands fa-linkedin-in" aria-hidden="true"></i></a></li>
                <li><a href="mailto:office@apexlogistics.example" aria-label="Email {name}"><i class="fa-solid fa-envelope" aria-hidden="true"></i></a></li>
              </ul>
            </div>
          </article>""")
    team_section = f"""    <!-- Team -->
    <section class="section section-alt team-section">
      <div class="container">
{section_head("Our people", "Meet the leadership team", "The people who make sure your freight is in good hands.")}
        <div class="grid grid-4">
{chr(10).join(team_cards)}
        </div>
      </div>
    </section>
"""

    partners = f"""    <!-- Partners -->
    <section class="section partners-section">
      <div class="container">
{section_head("Our network", "Partners &amp; accreditations", "Placeholder partner logos shown for layout.")}
        <ul class="partners-strip">
{chr(10).join(f'          <li data-aos="zoom-in" data-aos-delay="{i*40}"><img src="assets/images/partner-logo-placeholder.svg" alt="Partner organisation {i+1}" loading="lazy" width="160" height="56"></li>' for i in range(6))}
        </ul>
      </div>
    </section>
"""

    cta = cta_band("Want to work with a team that treats your freight like its own?")

    main = hero + intro + mv + timeline + stats + team_section + partners + cta
    page("about.html",
         "About Us — Apex Logistics",
         "Learn about Apex Logistics: a Kraków-based freight forwarder with 15 years' experience, a modern fleet, and a 25-country European network built on trust and transparency.",
         main)


# ===========================================================================
# SERVICES
# ===========================================================================
def build_services():
    hero = page_hero("Our Services",
                     "End-to-end logistics, one accountable partner",
                     "Road, rail, sea, warehousing, and customs — combined into a single, transparent service designed around your goods and your deadlines.",
                     "Services")

    intro = f"""    <!-- Intro -->
    <section class="section">
      <div class="container narrow text-center" data-aos="fade-up">
        <p class="eyebrow">How we help</p>
        <h2>Solutions for every link in your supply chain</h2>
        <p class="lead">Whether you need a single express delivery or a fully managed European distribution network, our services are modular — use one, or combine them for a seamless door-to-door solution with one point of contact.</p>
      </div>
    </section>
"""

    grid = f"""    <!-- Services grid (6) -->
    <section class="section section-alt">
      <div class="container">
        <div class="grid grid-3">
{services_grid(6)}
        </div>
      </div>
    </section>
"""

    # Three alternating detail sections
    details = [
        ("truck1-placeholder.svg", "Road Transport &amp; Express", "Reliable road freight across Poland and the EU",
         "Our road network handles everything from single pallets to full truckloads. Choose dedicated FTL for direct, time-critical moves, or cost-efficient groupage when you are shipping less than a full load. Every vehicle is GPS-tracked and every shipment comes with proactive status updates.",
         ["Full-load (FTL) and groupage (LTL) services", "Same-day and next-day express options", "Temperature-controlled and ADR transport"], False),
        ("warehouse-placeholder.svg", "Warehousing &amp; Fulfilment", "Storage and fulfilment that scale with demand",
         "Store goods close to your customers in secure, monitored facilities. We handle inbound receiving, putaway, pick-and-pack, and outbound dispatch, with real-time inventory counts available through your client portal. Flexible terms mean you only pay for the space you use.",
         ["Short- and long-term pallet storage", "Pick, pack, and e-commerce fulfilment", "Live inventory and stock reporting"], True),
        ("coverage-map-placeholder.svg", "Customs, Intermodal &amp; Supply Chain", "Cross-border expertise that keeps freight moving",
         "Crossing borders should not slow you down. Our customs specialists prepare documentation, manage duties, and clear shipments quickly, while our intermodal routing blends road, rail, and sea to cut cost and carbon on long-haul lanes — all coordinated under one supply chain plan.",
         ["Import/export customs clearance and advice", "Intermodal road, rail, and sea routing", "Consolidated reporting across all modes"], False),
    ]
    detail_html = []
    for i, (img, title, sub, body, bullets, reverse) in enumerate(details):
        media = f"""        <div class="detail-media" data-aos="fade-{'left' if reverse else 'right'}">
          <img src="assets/images/{img}" alt="{title.replace('&amp;', 'and')} illustration" loading="lazy" width="600" height="440">
        </div>"""
        text = f"""        <div class="detail-text" data-aos="fade-{'right' if reverse else 'left'}">
          <p class="eyebrow">{title}</p>
          <h2>{sub}</h2>
          <p>{body}</p>
          <ul class="check-list">
{chr(10).join(f'            <li><i class="fa-solid fa-check" aria-hidden="true"></i> {b}</li>' for b in bullets)}
          </ul>
          <a href="contact.html" class="btn btn-primary">Discuss this service</a>
        </div>"""
        order = (media + "\n" + text) if not reverse else (text + "\n" + media)
        cls = "detail-row" + (" detail-row-reverse" if reverse else "")
        detail_html.append(f"""    <section class="section {('section-alt ' if i % 2 else '')}detail-section">
      <div class="container {cls}">
{order}
      </div>
    </section>""")

    industries = f"""    <!-- Industries served -->
    <section class="section industries">
      <div class="container">
{section_head("Sector expertise", "Industries we serve", "Compliant, specialised handling for demanding sectors.")}
        <ul class="industries-grid">
{industries_grid(8)}
        </ul>
      </div>
    </section>
"""

    cta = cta_band("Not sure which service you need?",
                   "Send us your goods, lanes, and timelines and we'll recommend the right mix — no obligation.")

    main = hero + intro + grid + "\n".join(detail_html) + "\n" + industries + cta
    page("services.html",
         "Services — Apex Logistics",
         "Explore Apex Logistics services: road transport, warehousing, customs clearance, intermodal, express delivery, and supply chain management — combined into one accountable solution.",
         main)


# ===========================================================================
# FLEET
# ===========================================================================
def build_fleet():
    hero = page_hero("Our Fleet",
                     "The right vehicle for every load",
                     "A modern, GPS-tracked fleet — from city vans to 40-tonne articulated trailers and refrigerated units — maintained to the highest safety standards.",
                     "Fleet")

    overview = f"""    <!-- Overview -->
    <section class="section">
      <div class="container narrow text-center" data-aos="fade-up">
        <p class="eyebrow">Fleet overview</p>
        <h2>Capacity, flexibility, and reliability</h2>
        <p class="lead">We run and partner with a diverse range of vehicles so we can match capacity precisely to your shipment. Every truck is regularly serviced, telematics-equipped, and driven by trained, vetted professionals — keeping your goods safe and your deliveries predictable.</p>
      </div>
    </section>
"""

    vehicles = [
        ("truck1-placeholder.svg", "Articulated Curtain-Sider", "Our workhorse for palletised European freight, with easy side loading.",
         [("Payload", "24 t"), ("Pallets", "33 EUR"), ("Volume", "90 m³")]),
        ("truck2-placeholder.svg", "Refrigerated Trailer", "Temperature-controlled transport for food, pharma, and sensitive goods.",
         [("Payload", "22 t"), ("Range", "-25 to +25 °C"), ("Volume", "86 m³")]),
        ("truck3-placeholder.svg", "Box Rigid Truck", "Ideal for regional distribution and multi-drop urban delivery routes.",
         [("Payload", "10 t"), ("Pallets", "18 EUR"), ("Volume", "45 m³")]),
        ("truck4-placeholder.svg", "Mega Trailer", "Extra internal height for high-volume, lightweight, or bulky cargo.",
         [("Payload", "24 t"), ("Pallets", "33 EUR"), ("Volume", "100 m³")]),
        ("truck5-placeholder.svg", "Express Delivery Van", "Fast, agile transport for parcels and urgent same-day consignments.",
         [("Payload", "1.2 t"), ("Pallets", "3 EUR"), ("Volume", "11 m³")]),
        ("truck6-placeholder.svg", "Flatbed / Oversized", "For machinery, building materials, and abnormal or out-of-gauge loads.",
         [("Payload", "24 t"), ("Length", "13.6 m"), ("Type", "Open deck")]),
    ]
    slides = []
    for img, name, desc, specs in vehicles:
        spec_rows = "".join(f'<li><span>{k}</span><strong>{v}</strong></li>' for k, v in specs)
        slides.append(f"""            <div class="swiper-slide">
              <article class="card vehicle-card">
                <div class="vehicle-media">
                  <img src="assets/images/{img}" alt="{name}" loading="lazy" width="420" height="280">
                </div>
                <div class="vehicle-body">
                  <h3>{name}</h3>
                  <p>{desc}</p>
                  <ul class="vehicle-specs">{spec_rows}</ul>
                </div>
              </article>
            </div>""")
    gallery = f"""    <!-- Vehicle gallery -->
    <section class="section section-alt">
      <div class="container">
{section_head("The vehicles", "Explore our fleet", "Swipe or use the arrows to browse vehicle types and specifications.")}
        <div class="swiper fleet-swiper" data-aos="fade-up">
          <div class="swiper-wrapper">
{chr(10).join(slides)}
          </div>
          <div class="swiper-pagination"></div>
          <button class="swiper-button-prev" aria-label="Previous vehicle"></button>
          <button class="swiper-button-next" aria-label="Next vehicle"></button>
        </div>
      </div>
    </section>
"""

    specs_table = f"""    <!-- Capabilities / specs table -->
    <section class="section">
      <div class="container">
{section_head("At a glance", "Capabilities &amp; specifications", "Typical capacities — exact figures vary by vehicle and configuration.")}
        <div class="table-wrap" data-aos="fade-up">
          <table class="specs-table">
            <caption class="visually-hidden">Fleet vehicle types and their typical capabilities</caption>
            <thead>
              <tr>
                <th scope="col">Vehicle type</th>
                <th scope="col">Max payload</th>
                <th scope="col">Capacity</th>
                <th scope="col">Best for</th>
              </tr>
            </thead>
            <tbody>
              <tr><th scope="row">Articulated curtain-sider</th><td>24 t</td><td>33 EUR pallets</td><td>General palletised freight</td></tr>
              <tr><th scope="row">Refrigerated trailer</th><td>22 t</td><td>-25 to +25 °C</td><td>Chilled &amp; frozen goods</td></tr>
              <tr><th scope="row">Box rigid truck</th><td>10 t</td><td>18 EUR pallets</td><td>Regional multi-drop</td></tr>
              <tr><th scope="row">Mega trailer</th><td>24 t</td><td>100 m³</td><td>High-volume cargo</td></tr>
              <tr><th scope="row">Express van</th><td>1.2 t</td><td>11 m³</td><td>Urgent &amp; same-day</td></tr>
              <tr><th scope="row">Flatbed / oversized</th><td>24 t</td><td>13.6 m deck</td><td>Machinery &amp; abnormal loads</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
"""

    coverage = f"""    <!-- Coverage note + map -->
    <section class="section section-alt">
      <div class="container two-col">
        <div class="two-col-text" data-aos="fade-right">
          <p class="eyebrow">Where we go</p>
          <h2>Coverage across 25 countries</h2>
          <p>From our Kraków base, our fleet and partner network reach every corner of the European Union and beyond. Whether it is a domestic delivery or a multi-country distribution run, we plan the most efficient route and keep you updated the whole way.</p>
          <ul class="check-list">
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Daily departures on major EU corridors</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Intermodal links for long-haul efficiency</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Last-mile delivery in key cities</li>
          </ul>
          <a href="contact.html" class="btn btn-primary">Check your route</a>
        </div>
        <div class="two-col-media" data-aos="fade-left">
          <img src="assets/images/coverage-map-placeholder.svg" alt="Map of Apex Logistics coverage across Europe" loading="lazy" width="600" height="440">
        </div>
      </div>
    </section>
"""

    cta = cta_band("Need capacity for an upcoming shipment?",
                   "Tell us the load, route, and date — we'll confirm the right vehicle and a fixed price.")

    main = hero + overview + gallery + specs_table + coverage + cta
    page("fleet.html",
         "Fleet — Apex Logistics",
         "See the Apex Logistics fleet: curtain-siders, refrigerated trailers, rigid trucks, mega trailers, express vans, and flatbeds — GPS-tracked and maintained for reliable European delivery.",
         main)


# ===========================================================================
# CAREERS
# ===========================================================================
def build_careers():
    hero = page_hero("Careers",
                     "Build your career in logistics",
                     "Join a growing team that values safety, fairness, and doing the job right. From the cab to the office, there's a place for people who take pride in keeping things moving.",
                     "Careers")

    benefits = [
        ("sack-dollar", "Competitive pay", "Fair, transparent salaries with performance bonuses and regular reviews."),
        ("heart-pulse", "Health &amp; wellbeing", "Private medical cover and support programmes for you and your family."),
        ("graduation-cap", "Training &amp; growth", "Funded certifications, ADR training, and clear paths to promotion."),
        ("calendar-check", "Work–life balance", "Predictable scheduling, paid leave, and respect for your time off."),
        ("truck", "Modern equipment", "Newer, well-maintained vehicles and up-to-date tools and systems."),
        ("people-group", "Supportive team", "A friendly, multilingual workplace where your voice is heard."),
    ]
    bcards = []
    for i, (icon, title, desc) in enumerate(benefits):
        bcards.append(f"""          <article class="card benefit-card" data-aos="fade-up" data-aos-delay="{i*50}">
            <div class="benefit-icon"><i class="fa-solid fa-{icon}" aria-hidden="true"></i></div>
            <h3>{title}</h3>
            <p>{desc}</p>
          </article>""")
    why = f"""    <!-- Why work here -->
    <section class="section">
      <div class="container">
{section_head("Why Apex", "Why work with us", "We invest in our people because dependable service starts with a team that's looked after.")}
        <div class="grid grid-3">
{chr(10).join(bcards)}
        </div>
      </div>
    </section>
"""

    drivers = f"""    <!-- For drivers -->
    <section class="section section-alt">
      <div class="container two-col">
        <div class="two-col-media" data-aos="fade-right">
          <img src="assets/images/truck5-placeholder.svg" alt="Apex Logistics professional driver beside a delivery vehicle" loading="lazy" width="600" height="440">
        </div>
        <div class="two-col-text" data-aos="fade-left">
          <p class="eyebrow">For drivers</p>
          <h2>Drive with a company that backs you</h2>
          <p>Our drivers are the face of Apex Logistics, and we treat them that way. You'll get modern, reliable vehicles, planned routes that respect driving-time rules, and a dispatch team that's on your side. New and experienced drivers are both welcome.</p>
          <ul class="check-list">
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Valid C+E licence and driver CPC</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> Tachograph card and clean record</li>
            <li><i class="fa-solid fa-check" aria-hidden="true"></i> ADR certificate a plus (training available)</li>
          </ul>
          <a href="#vacancies" class="btn btn-primary">See driving roles</a>
        </div>
      </div>
    </section>
"""

    vacancies = [
        ("Long-Haul HGV Driver (C+E)", "Kraków / EU routes", "Full-time", "fa-truck-moving"),
        ("Warehouse Operative", "Kraków", "Full-time", "fa-boxes-stacked"),
        ("Logistics Coordinator", "Kraków (Hybrid)", "Full-time", "fa-clipboard-list"),
        ("Customs Clearance Specialist", "Kraków", "Full-time", "fa-file-circle-check"),
        ("Fleet Maintenance Technician", "Kraków", "Full-time", "fa-screwdriver-wrench"),
        ("Customer Service Representative", "Kraków (Hybrid)", "Part-time", "fa-headset"),
    ]
    vrows = []
    for title, loc, ttype, icon in vacancies:
        vrows.append(f"""          <li class="vacancy" data-aos="fade-up">
            <div class="vacancy-icon"><i class="fa-solid {icon}" aria-hidden="true"></i></div>
            <div class="vacancy-info">
              <h3>{title}</h3>
              <p class="vacancy-meta"><span><i class="fa-solid fa-location-dot" aria-hidden="true"></i> {loc}</span> <span><i class="fa-solid fa-clock" aria-hidden="true"></i> {ttype}</span></p>
            </div>
            <a class="btn btn-accent btn-sm" href="mailto:office@apexlogistics.example?subject=Application:%20{title.replace(' ', '%20').replace('+', '%2B')}">Apply</a>
          </li>""")
    vac = f"""    <!-- Vacancies -->
    <section class="section" id="vacancies">
      <div class="container">
{section_head("Open roles", "Current vacancies", "Placeholder openings shown for layout — replace with your live roles.")}
        <ul class="vacancy-list">
{chr(10).join(vrows)}
        </ul>
      </div>
    </section>
"""

    note = f"""    <!-- Application note -->
    <section class="section section-alt">
      <div class="container">
        <div class="apply-note card" data-aos="fade-up">
          <div class="apply-note-icon"><i class="fa-solid fa-paper-plane" aria-hidden="true"></i></div>
          <div class="apply-note-text">
            <h2>Don't see the right role?</h2>
            <p>We're always glad to hear from talented people. Send your CV and a short note about what you're looking for to <a href="mailto:office@apexlogistics.example">office@apexlogistics.example</a> and we'll be in touch when a suitable position opens. <!-- REPLACE: careers email --></p>
          </div>
          <a href="mailto:office@apexlogistics.example?subject=Speculative%20Application" class="btn btn-primary">Send your CV</a>
        </div>
      </div>
    </section>
"""

    main = hero + why + drivers + vac + note
    page("careers.html",
         "Careers — Apex Logistics",
         "Join Apex Logistics. Explore driver, warehouse, and office vacancies, plus benefits including competitive pay, training, and modern equipment. Apply today.",
         main)


# ===========================================================================
# CONTACT
# ===========================================================================
def build_contact():
    hero = page_hero("Contact Us",
                     "Let's plan your next shipment",
                     "Questions, quotes, or tracking updates — our Kraków team is ready to help and replies to most enquiries within one business day.",
                     "Contact")

    form_and_details = f"""    <!-- Form + company details -->
    <section class="section">
      <div class="container contact-grid">
        <div class="contact-form-wrap" data-aos="fade-up">
          <h2>Send us a message</h2>
          <p>Fill in the form and we'll get back to you shortly. Fields marked with <span class="req-star" aria-hidden="true">*</span> are required.</p>
          <form id="contact-form" action="https://api.web3forms.com/submit" method="POST" novalidate>
            <input type="hidden" name="access_key" value="YOUR_WEB3FORMS_KEY"> <!-- REPLACE: Web3Forms access key -->
            <input type="hidden" name="subject" value="New enquiry from Apex Logistics website">
            <input type="hidden" name="from_name" value="Apex Logistics Website">
            <!-- Honeypot anti-spam field -->
            <input type="checkbox" name="botcheck" class="visually-hidden" style="display:none;" tabindex="-1" autocomplete="off">

            <div class="form-row">
              <div class="form-field">
                <label for="name">Full name <span class="req-star" aria-hidden="true">*</span></label>
                <input type="text" id="name" name="name" autocomplete="name" required aria-required="true" placeholder="Jane Smith">
                <span class="field-error" data-error-for="name" aria-live="polite"></span>
              </div>
              <div class="form-field">
                <label for="email">Email address <span class="req-star" aria-hidden="true">*</span></label>
                <input type="email" id="email" name="email" autocomplete="email" required aria-required="true" placeholder="jane@company.com">
                <span class="field-error" data-error-for="email" aria-live="polite"></span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-field">
                <label for="phone">Phone <span class="optional">(optional)</span></label>
                <input type="tel" id="phone" name="phone" autocomplete="tel" placeholder="+48 123 456 789">
                <span class="field-error" data-error-for="phone" aria-live="polite"></span>
              </div>
              <div class="form-field">
                <label for="subject-line">Subject <span class="req-star" aria-hidden="true">*</span></label>
                <input type="text" id="subject-line" name="subject_line" required aria-required="true" placeholder="Quote request">
                <span class="field-error" data-error-for="subject-line" aria-live="polite"></span>
              </div>
            </div>

            <div class="form-field">
              <label for="message">Message <span class="req-star" aria-hidden="true">*</span></label>
              <textarea id="message" name="message" rows="6" required aria-required="true" placeholder="Tell us about your goods, route, and timeline…"></textarea>
              <span class="field-error" data-error-for="message" aria-live="polite"></span>
            </div>

            <div class="form-field form-consent">
              <label class="checkbox-label">
                <input type="checkbox" id="consent" name="consent" required aria-required="true">
                <span>I agree that my details will be used to respond to my enquiry, as described in the <a href="privacy.html">Privacy Policy</a>. <span class="req-star" aria-hidden="true">*</span></span>
              </label>
              <span class="field-error" data-error-for="consent" aria-live="polite"></span>
            </div>

            <button type="submit" class="btn btn-primary btn-block" id="form-submit">Send Message</button>
            <p id="form-status" class="form-status" role="status" aria-live="polite"></p>
          </form>
        </div>

        <aside class="contact-details" data-aos="fade-up" data-aos-delay="100">
          <h2>Company details</h2>
          <ul class="contact-cards">
            <li class="contact-card">
              <span class="contact-card-icon"><i class="fa-solid fa-location-dot" aria-hidden="true"></i></span>
              <div><h3>Address</h3><p>ul. Przykładowa 12, 30-001 Kraków, Poland</p></div> <!-- REPLACE: address -->
            </li>
            <li class="contact-card">
              <span class="contact-card-icon"><i class="fa-solid fa-phone" aria-hidden="true"></i></span>
              <div><h3>Phone</h3><p><a href="tel:+48123456789">+48 123 456 789</a></p></div> <!-- REPLACE: phone -->
            </li>
            <li class="contact-card">
              <span class="contact-card-icon"><i class="fa-solid fa-envelope" aria-hidden="true"></i></span>
              <div><h3>Email</h3><p><a href="mailto:office@apexlogistics.example">office@apexlogistics.example</a></p></div> <!-- REPLACE: email -->
            </li>
            <li class="contact-card">
              <span class="contact-card-icon"><i class="fa-solid fa-clock" aria-hidden="true"></i></span>
              <div><h3>Opening hours</h3><p>Mon–Fri: 08:00–18:00 CET<br>Sat–Sun: Closed</p></div>
            </li>
          </ul>
          <div class="contact-social">
            <h3>Follow us</h3>
            <ul class="social-links social-links-dark" aria-label="Social media">
              <li><a href="#" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in" aria-hidden="true"></i></a></li>
              <li><a href="#" aria-label="Facebook"><i class="fa-brands fa-facebook-f" aria-hidden="true"></i></a></li>
              <li><a href="#" aria-label="X"><i class="fa-brands fa-x-twitter" aria-hidden="true"></i></a></li>
              <li><a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram" aria-hidden="true"></i></a></li>
            </ul>
          </div>
        </aside>
      </div>
    </section>
"""

    map_section = """    <!-- Google Map -->
    <section class="section section-alt map-section">
      <div class="container">
        <div class="section-head section-head-center" data-aos="fade-up">
          <p class="eyebrow">Find us</p>
          <h2>Our location</h2>
        </div>
      </div>
      <div class="map-outer" data-aos="fade-up">
        <div id="map" aria-label="Map showing the Apex Logistics office location"></div>
        <p id="map-fallback" class="map-fallback" hidden>
          <i class="fa-solid fa-triangle-exclamation" aria-hidden="true"></i>
          Map cannot be loaded. Please use the address above for directions:
          ul. Przykładowa 12, 30-001 Kraków, Poland.
        </p>
      </div>
    </section>
"""

    faqs = [
        ("How do I get a shipping quote?",
         "Use the contact form above or email us with your goods, collection and delivery addresses, weight or pallet count, and target dates. We'll reply with a clear, fixed quote — usually within one business day."),
        ("Which countries do you deliver to?",
         "We operate across 25 countries throughout the European Union and beyond, with daily departures on major corridors. If you're unsure whether we cover a route, just ask."),
        ("Can I track my shipment in real time?",
         "Yes. Every shipment is GPS-tracked, and you'll receive proactive status updates at each milestone. Larger or ongoing clients also get access to a live client portal."),
        ("Do you handle customs and documentation?",
         "We do. Our in-house customs specialists prepare import and export documentation, manage duties, and clear shipments so your freight keeps moving across borders."),
    ]
    faq_items = []
    for i, (q, a) in enumerate(faqs):
        faq_items.append(f"""          <li class="accordion-item" data-aos="fade-up">
            <h3 class="accordion-header">
              <button type="button" class="accordion-trigger" aria-expanded="false" aria-controls="faq-panel-{i}" id="faq-trigger-{i}">
                <span>{q}</span>
                <i class="fa-solid fa-chevron-down accordion-icon" aria-hidden="true"></i>
              </button>
            </h3>
            <div class="accordion-panel" id="faq-panel-{i}" role="region" aria-labelledby="faq-trigger-{i}" hidden>
              <div class="accordion-panel-inner"><p>{a}</p></div>
            </div>
          </li>""")
    faq = f"""    <!-- FAQ accordion -->
    <section class="section faq-section">
      <div class="container narrow">
{section_head("Good to know", "Frequently asked questions", "")}
        <ul class="accordion">
{chr(10).join(faq_items)}
        </ul>
      </div>
    </section>
"""

    main = hero + form_and_details + map_section + faq

    extra_scripts = """  <!-- Contact-page scripts -->
  <script src="js/contact.js" defer></script>
  <script src="js/googlemaps.js" defer></script>
  <!-- Google Maps JavaScript API (loads after googlemaps.js so initMap is defined) -->
  <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap"
    onerror="if(window.handleMapError){window.handleMapError();}"></script>
  <!-- REPLACE: Google Maps API key -->
"""
    page("contact.html",
         "Contact Us — Apex Logistics",
         "Contact Apex Logistics in Kraków for quotes, tracking, and support. Use our contact form, call +48 123 456 789, or email office@apexlogistics.example.",
         main, extra_scripts=extra_scripts)


# ===========================================================================
# LEGAL PAGES (privacy + terms)
# ===========================================================================
def legal_section(num, title, paragraphs):
    paras = "\n".join(f"          <p>{p}</p>" for p in paragraphs)
    return f"""        <section class="legal-block" data-aos="fade-up">
          <h2>{num}. {title}</h2>
{paras}
        </section>"""


def build_privacy():
    hero = page_hero("Privacy Policy",
                     "Privacy Policy",
                     "How Apex Logistics collects, uses, and protects your personal data. This is placeholder text and not legal advice.",
                     "Privacy")

    intro = """    <section class="section legal-section">
      <div class="container narrow legal-content">
        <p class="legal-updated"><strong>Last updated:</strong> 1 January 2026 <!-- REPLACE: effective date --></p>
        <p class="legal-disclaimer"><i class="fa-solid fa-circle-info" aria-hidden="true"></i> This page contains generic placeholder text for layout purposes only. Replace it with a policy reviewed by a qualified legal professional before publishing.</p>
"""
    blocks = [
        ("Introduction", ["Apex Logistics (\"we\", \"us\", \"our\") is committed to protecting your privacy. This policy explains what personal data we collect, why we collect it, and how we handle it when you use our website or services.", "By using our website, you agree to the practices described in this policy."]),
        ("Information we collect", ["We may collect information you provide directly, such as your name, email address, phone number, and the contents of any message you send through our contact form.", "We may also collect limited technical information automatically, such as your browser type, device, and how you interact with our site, to help us improve it."]),
        ("How we use your information", ["We use your information to respond to enquiries, provide quotes and services, improve our website, and — where you have agreed — to send relevant updates.", "We process your data only where we have a lawful basis to do so."]),
        ("Cookies and analytics", ["Our website may use cookies and similar technologies to keep the site working and to understand how it is used. You can control cookies through your browser settings.", "Third-party services such as mapping and form handling may set their own cookies, governed by their respective privacy policies."]),
        ("Data sharing", ["We do not sell your personal data. We may share it with trusted service providers who help us operate our business, and only to the extent necessary.", "We may disclose information where required by law or to protect our legal rights."]),
        ("Data retention and security", ["We keep personal data only for as long as necessary for the purposes described here, then delete or anonymise it.", "We apply appropriate technical and organisational measures to protect your data against unauthorised access, loss, or misuse."]),
        ("Your rights", ["Depending on your location, you may have the right to access, correct, delete, or restrict the use of your personal data, and to object to certain processing.", "To exercise any of these rights, contact us using the details below."]),
        ("Contact us", ["If you have questions about this policy or how we handle your data, contact us at office@apexlogistics.example or by post at ul. Przykładowa 12, 30-001 Kraków, Poland."]),
    ]
    body = "\n".join(legal_section(i + 1, t, p) for i, (t, p) in enumerate(blocks))
    closing = """      </div>
    </section>
"""
    main = hero + intro + body + "\n" + closing
    page("privacy.html",
         "Privacy Policy — Apex Logistics",
         "Read the Apex Logistics Privacy Policy: how we collect, use, share, and protect your personal data. Placeholder content for layout.",
         main)


def build_terms():
    hero = page_hero("Terms of Use",
                     "Terms of Use",
                     "The terms that govern your use of the Apex Logistics website. This is placeholder text and not legal advice.",
                     "Terms")

    intro = """    <section class="section legal-section">
      <div class="container narrow legal-content">
        <p class="legal-updated"><strong>Last updated:</strong> 1 January 2026 <!-- REPLACE: effective date --></p>
        <p class="legal-disclaimer"><i class="fa-solid fa-circle-info" aria-hidden="true"></i> This page contains generic placeholder text for layout purposes only. Replace it with terms reviewed by a qualified legal professional before publishing.</p>
"""
    blocks = [
        ("Acceptance of terms", ["By accessing and using the Apex Logistics website, you agree to be bound by these Terms of Use. If you do not agree, please do not use the site."]),
        ("Use of the website", ["You may use this website for lawful purposes only. You agree not to misuse it, interfere with its operation, or attempt to access it in any unauthorised way.", "We may change, suspend, or withdraw any part of the website at any time without notice."]),
        ("Intellectual property", ["All content on this website, including text, graphics, logos, and design, is owned by or licensed to Apex Logistics and is protected by applicable laws.", "You may not reproduce, distribute, or reuse any content without our prior written permission."]),
        ("Quotes and services", ["Information on this website is provided for general guidance. Quotes, capacities, and timelines are indicative and subject to confirmation in a formal agreement.", "Our services are provided under separate terms agreed with each client."]),
        ("Third-party links", ["Our website may contain links to third-party sites. We are not responsible for the content, accuracy, or practices of those sites and provide such links for convenience only."]),
        ("Limitation of liability", ["To the fullest extent permitted by law, Apex Logistics is not liable for any loss or damage arising from your use of, or inability to use, this website.", "The website is provided on an \"as is\" basis without warranties of any kind."]),
        ("Governing law", ["These terms are governed by the laws of Poland. Any disputes will be subject to the exclusive jurisdiction of the Polish courts. <!-- REPLACE: governing jurisdiction -->"]),
        ("Contact us", ["If you have questions about these terms, contact us at office@apexlogistics.example or by post at ul. Przykładowa 12, 30-001 Kraków, Poland."]),
    ]
    body = "\n".join(legal_section(i + 1, t, p) for i, (t, p) in enumerate(blocks))
    closing = """      </div>
    </section>
"""
    main = hero + intro + body + "\n" + closing
    page("terms.html",
         "Terms of Use — Apex Logistics",
         "Read the Apex Logistics Terms of Use governing access to and use of our website. Placeholder content for layout.",
         main)


if __name__ == "__main__":
    build_index()
    build_about()
    build_services()
    build_fleet()
    build_careers()
    build_contact()
    build_privacy()
    build_terms()
    print("All HTML pages generated.")
