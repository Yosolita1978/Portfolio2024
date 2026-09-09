# -*- coding: utf-8 -*-
"""
Generates the static HTML pages for yosola.co.

    python3 tools/build.py

WHY THIS EXISTS
    The site is plain HTML with no framework, so the nav bar and footer
    are physically repeated in all eight pages. Editing them by hand
    means making the same change eight times and hoping none is missed.
    This script holds the shared shell ONCE and stamps out every page
    from it, so the nav and footer are always identical.

WHAT IT IS NOT
    Not a build step. The files it writes are plain static HTML that
    Amplify serves directly. Nobody needs Python to view, deploy or host
    the site. This script is only for editing convenience.

WHAT IT OVERWRITES
    index.html, 404.html, sitemap.xml, robots.txt, and index.html inside
    about/ ventures/ projects/ teaching/ certifications/ chat/.
    It does NOT touch css/, js/, images/, docs/, ascii/ or podfic/.
    Edit page CONTENT here, then re-run. Edit STYLES in css/ directly.
"""

import os
import datetime

SITE = "https://www.yosola.co"
CV = "/docs/cristina-rodriguez-cv-engineering-2026.pdf"


def file_date(path):
    """Last-modified date of a file, as YYYY-MM-DD."""
    return datetime.date.fromtimestamp(os.path.getmtime(path)).isoformat()


# The generated pages take their content from this script, so this script's
# own mtime is the honest "last modified" date for them.
MODIFIED = file_date(os.path.abspath(__file__))

# The repository root: one level up from tools/.
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Every page: (slug, nav label). Slug "" is the home page.
NAV_ITEMS = [
    ("",               "home"),
    ("about",          "about"),
    ("ventures",       "ventures"),
    ("projects",       "projects"),
    ("teaching",       "teaching"),
    ("certifications", "certifications"),
    ("chat",           "chat"),
]

SOCIALS = [
    ("linkedin", "https://www.linkedin.com/in/crissrodriguez/"),
    ("github",   "https://github.com/Yosolita1978"),
    ("youtube",  "https://www.youtube.com/@crissrodriguez9940/videos"),
    ("play",     "https://play.google.com/store/apps/developer?id=yosola"),
]


def url_for(slug):
    return "/" if slug == "" else "/%s/" % slug


def nav_html(active):
    links = []
    for slug, label in NAV_ITEMS:
        current = ' aria-current="page"' if slug == active else ""
        links.append(
            '                        <li><a href="%s"%s>%s</a></li>'
            % (url_for(slug), current, label)
        )
    return """    <nav class="nav">
        <div class="nav-inner">
            <a class="nav-logo" href="/">~/cristina-rodriguez</a>

            <button class="nav-toggle" type="button" id="nav-toggle"
                    aria-expanded="false" aria-controls="nav-menu" aria-label="Toggle navigation">
                <span></span><span></span><span></span>
            </button>

            <div class="nav-menu" id="nav-menu">
                <ul class="nav-list">
%s
                </ul>
                <a class="nav-cv" href="%s" target="_blank" rel="noopener">download-cv</a>
            </div>
        </div>
    </nav>""" % ("\n".join(links), CV)


FOOTER = """    <footer class="footer">
        <div class="shell">
            <div class="footer-grid">
                <div class="footer-col footer-brand-col">
                    <a class="footer-brand" href="/">~/cristina-rodriguez</a>
                    <p class="footer-tagline">
                        <a href="https://www.comadrelab.dev/" target="_blank" rel="noopener">comadrelab &middot; comadrelab.dev</a>
                    </p>
                </div>

                <div class="footer-col">
                    <p class="footer-heading">site/</p>
                    <ul>
                        <li><a href="/">home</a></li>
                        <li><a href="/about/">about</a></li>
                        <li><a href="/ventures/">ventures</a></li>
                    </ul>
                </div>

                <div class="footer-col">
                    <p class="footer-heading">work/</p>
                    <ul>
                        <li><a href="/projects/">projects</a></li>
                        <li><a href="/teaching/">teaching</a></li>
                        <li><a href="/certifications/">certifications</a></li>
                        <li><a href="/chat/">chat</a></li>
                    </ul>
                </div>
            </div>

            <div class="footer-col" style="margin-bottom:40px;">
                <p class="footer-heading">elsewhere/</p>
                <ul>
                    <li><a href="https://www.linkedin.com/in/crissrodriguez/" target="_blank" rel="noopener">linkedin</a></li>
                    <li><a href="https://github.com/Yosolita1978" target="_blank" rel="noopener">github</a></li>
                    <li><a href="https://www.youtube.com/@crissrodriguez9940/videos" target="_blank" rel="noopener">youtube</a></li>
                    <li><a href="https://play.google.com/store/apps/developer?id=yosola" target="_blank" rel="noopener">google play</a></li>
                </ul>
            </div>

            <div class="footer-bottom">
                <p>Copyright &copy; Cristina Rodriguez 2026 &mdash; All rights reserved</p>
                <p><a href="mailto:yosola@gmail.com">yosola@gmail.com</a></p>
            </div>
        </div>
    </footer>"""


PAGE = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical}">
{robots}
    <!-- ----- OPEN GRAPH ----- -->
    <meta property="og:type" content="{og_type}">
    <meta property="og:site_name" content="Cristina Rodriguez">
    <meta property="og:title" content="{og_title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="{site}/images/profile.png">
    <meta property="og:locale" content="en_US">

    <!-- ----- TWITTER ----- -->
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{og_title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{site}/images/profile.png">

    <!-- ----- FAVICON ----- -->
    <link rel="shortcut icon" href="/images/favicon.png" type="image/x-icon">

    <!-- ----- FONT PRECONNECT ----- -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

    <!-- ----- CSS ----- -->
    <link rel="stylesheet" href="/css/tokens.css">
    <link rel="stylesheet" href="/css/base.css">
    <link rel="stylesheet" href="/css/pages.css">
{extra_head}
    <!-- ----- ANALYTICS ----- -->
    <script defer data-domain="yosola.co" src="https://plausible.io/js/script.js"></script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-RTDXX5NWH2"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', 'G-RTDXX5NWH2');
    </script>

    <!-- ----- STRUCTURED DATA ----- -->
    <script type="application/ld+json">
{jsonld}
    </script>
</head>

<body>
    <a class="skip-link" href="#main">Skip to content</a>

{nav}

    <main id="main">
{body}
    </main>

{footer}

    <!-- ----- LIBRARIES (the hero animation) ----- -->
    <script src="https://unpkg.com/typed.js@2.0.16/dist/typed.umd.js"></script>
    <script src="https://unpkg.com/scrollreveal"></script>

    <!-- ----- SITE SCRIPTS ----- -->
    <script src="/js/nav.js"></script>
    <script src="/js/hero.js"></script>
{extra_scripts}</body>

</html>
"""


def breadcrumb(slug, label):
    return """    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "%s/" },
        { "@type": "ListItem", "position": 2, "name": "%s", "item": "%s%s" }
      ]
    }""" % (SITE, label, SITE, url_for(slug))


def render(slug, title, description, jsonld, body, og_title=None,
           og_type="website", extra_head="", extra_scripts="", noindex=False):
    path = OUT if slug == "" else os.path.join(OUT, slug)
    if not os.path.isdir(path):
        os.makedirs(path)

    jsonld = jsonld.replace("__MOD__", MODIFIED)
    html = PAGE.format(
        title=title,
        description=description,
        canonical=SITE + url_for(slug),
        og_title=og_title or title,
        og_type=og_type,
        site=SITE,
        robots='    <meta name="robots" content="noindex, follow">\n' if noindex else "",
        extra_head=extra_head,
        extra_scripts=extra_scripts,
        jsonld=jsonld,
        nav=nav_html(slug),
        body=body,
        footer=FOOTER,
    )
    target = os.path.join(path, "index.html")
    with open(target, "w") as fh:
        fh.write(html)
    return target


# ============================================================
# CONTENT
# Every item below is carried over from the original index.html
# and main.js. Nothing has been dropped.
# ============================================================

PROJECTS = [
    dict(
        slug="anzuelo",
        name="Anzuelo &mdash; Social Lead Finder &amp; Content Hub",
        url="https://anzuelo.vercel.app",
        img="/images/anzuelo.jpg",
        status="live",
        desc="Social media lead finder and content hub. A Python agent searches seven platforms, scores each lead with Claude Haiku using prompt caching, and flags content gaps into Supabase. A Next.js 16 dashboard adds a content studio that generates posts and finished visuals through chained Visual Director and FLUX image agents. No automatic sending, by design.",
        tags=["Next.js 16", "TypeScript", "Python", "Claude Haiku", "Supabase", "FLUX", "Multi-agent"],
    ),
    dict(
        slug="nouvie",
        name="Nouvie &mdash; Order &amp; Inventory System",
        url="https://www.nouvie.co/",
        img="/images/nouvie.jpg",
        status="live",
        desc="Order-management admin for a regulated, document-heavy business: PDF invoice generation, Excel export and role-based access, plus a public storefront with structured data. Built mobile-first for a non-technical owner at a Colombian cleaning products company.",
        tags=["Next.js", "Prisma", "PostgreSQL", "Supabase", "PDF pipeline", "Vercel"],
    ),
    dict(
        slug="sustainability-bot",
        name="Sustainability Bot",
        url="https://github.com/Yosolita1978/sustainability-ai-platform",
        img="/images/sustainability.png",
        status="archived",
        desc="AI-powered training platform that generates compliance-focused sustainability messaging playbooks using a multi-agent workflow. Deployment retired &mdash; source on GitHub.",
        tags=["Next.js", "React", "TypeScript", "Python", "FastAPI", "CrewAI", "OpenAI API", "Vercel"],
    ),
    dict(
        slug="sazon-bot",
        name="Sazon Mexican Bot",
        url="https://sazonbot.vercel.app/",
        img="/images/sazon.png",
        status="live",
        desc="Bilingual recipe assistant with a FastAPI and LangChain backend, a Next.js front end and streaming responses. Semantic search over a recipe corpus, with recipe scaling and ingredient substitutions.",
        tags=["Next.js", "React", "TypeScript", "Tailwind CSS", "Python", "FastAPI", "LangChain", "GPT-4o-mini", "FAISS", "Vercel"],
    ),
    dict(
        slug="soneto-bot",
        name="Soneto Bot",
        url="https://sonetobot.vercel.app/",
        img="/images/soneto.png",
        status="live",
        desc="Full-stack app that discovers Spanish poems, stores them in a database, and automatically posts to Mastodon with duplicate prevention, plus a public browsing site and admin dashboard.",
        tags=["Next.js", "TypeScript", "Tailwind CSS", "NextAuth.js", "Supabase", "PostgreSQL", "Mastodon API", "Vercel"],
    ),
    dict(
        slug="picas-y-fijas",
        name="Bulls &amp; Cows / Picas y Fijas",
        url="https://www.picasyfijas.com/",
        img="/images/bulls.png",
        status="live",
        desc="Fully bilingual (EN/ES) web version of the classic number guessing game with auto language detection, cultural emoji adaptations, shareable results, and PWA-ready offline support.",
        tags=["JavaScript", "HTML", "CSS", "i18n", "Service Worker", "PWA", "localStorage"],
    ),
    dict(
        slug="ascii-converter",
        name="ASCII Art Converter",
        url="/ascii/",
        img="/images/ascii.png",
        status="live",
        desc="Client-side converter that transforms images into ASCII art with supersampling, histogram equalization, themes, split-view comparison, and export tools. No uploads &mdash; everything stays local.",
        tags=["JavaScript", "HTML", "CSS", "Canvas API", "Clipboard API", "PNG Export"],
    ),
    dict(
        slug="cristina-multiverse",
        name="Cristina Multiverse",
        url="https://github.com/Yosolita1978/Cristina-Multiverse",
        img="/images/multiverse.png",
        status="archived",
        desc="Interactive AI avatar generator with Stable Diffusion prompts, plus a showcase of a Google Vertex AI / Model Garden talk at DevFest Seattle 2024. Deployment retired &mdash; source on GitHub.",
        tags=["React", "Vite", "Node.js", "Hugging Face", "Google Vertex AI", "Stable Diffusion"],
    ),
]

TEACHING = [
    dict(
        slug="mujertech-bootcamp",
        name="MujerTech: AI &amp; Business Bootcamp",
        sub="E-learning platform &middot; Spanish-first",
        desc="A bilingual learning platform built solo, from data model to deploy: Next.js App Router, next-intl, Supabase magic-link auth, strict TypeScript and a role-gated admin. Three scaffolded modules end in a real marketing piece, built around &ldquo;La IA propone, t&uacute; decides&rdquo;: AI as a helper, not a replacement. Live with 25 learners.",
        tags=["Next.js App Router", "TypeScript", "next-intl", "Supabase", "Instructional Design", "Bilingual"],
        link="https://bootcamp.mujertech.org",
        youtube=None,
    ),
    dict(
        slug="handle-google",
        name="Learning How to Handle Google",
        sub="Interactive course &middot; Beginners",
        desc="An interactive course helping beginners use email and Google tools on mobile devices with confidence. Includes simple steps, practice tasks, and cheat sheets for checking email, sending photos, opening shared files, and joining meetings.",
        tags=["Instructional Design", "Google Workspace", "Mobile", "Articulate"],
        link="https://share.articulate.com/wf7q8eO2vnum75kWXD9S8",
        youtube=None,
    ),
    dict(
        slug="nextjs-course-techconme",
        name="Next.js Course with TechConMe",
        sub="Course design &amp; delivery",
        desc="Designed and taught a hands-on course on building dynamic web applications using Next.js, covering topics such as routing, authentication, and state management.",
        tags=["Next.js", "React", "JavaScript", "Auth0", "FireBase"],
        link="https://github.com/Yosolita1978/Conference-Landing?tab=readme-ov-file#nextjs-course-overview",
        youtube="https://www.youtube.com/playlist?list=PLH72tRyNBul4xwHGPuduuoUuQ1b2qz1Bc",
    ),
    dict(
        slug="avatar-workshop-sd15",
        name="Social Media Avatar Workshop with Stable Diffusion",
        sub="Workshop facilitation",
        desc="Led a workshop on creating personalized social media avatars using Stable Diffusion v1.5, covering image generation techniques, model tuning, and artistic enhancement.",
        tags=["Stable Diffusion", "Machine Learning", "Image Generation", "Python"],
        link="https://github.com/Yosolita1978/AiWorkshop",
        youtube="https://www.youtube.com/watch?v=szc4FA7nyBo",
    ),
    dict(
        slug="express-react-vite",
        name="Your First Express and React App with Vite",
        sub="Template &amp; tutorial",
        desc="Built a full-stack web application template using React for the frontend and Express for the backend, leveraging Vite for rapid development and database integration.",
        tags=["React", "Express", "Vite", "Full-Stack Development", "Database Integration"],
        link="https://github.com/Techtonica/Template2023ReactAndVite",
        youtube="https://youtu.be/Oj1L3BuIJuw",
    ),
]

VENTURES = [
    dict(
        slug="comadrelab",
        name="comadrelab/",
        sub="Web Studio for Small Businesses",
        desc="Full-stack and AI systems for small businesses and Latin American clients &mdash; architecture, data modeling and deployment end to end. Six client projects shipped and supported since 2024.",
        link="https://www.comadrelab.dev/",
        link_label="See services &amp; work &rarr;",
        external=True,
    ),
    dict(
        slug="mujertech",
        name="mujertech/",
        sub="AI Training for Women Entrepreneurs",
        desc="A 16-week bootcamp teaching AI tools and business strategy to women entrepreneurs in Latin America. Launching in Bogot&aacute;.",
        link="https://bootcamp.mujertech.org",
        link_label="Visit the bootcamp &rarr;",
        external=True,
    ),
]


def external_attrs(url):
    return ' target="_blank" rel="noopener"' if url.startswith("http") else ""


def tags_html(tags, indent="                        "):
    items = "\n".join('%s    <span>%s</span>' % (indent, t) for t in tags)
    return '%s<div class="tags">\n%s\n%s</div>' % (indent, items, indent)


def hero(cmd, title_html, strings, body, extra="", wide=True, portrait=False):
    """The shared hero block. Every page uses this, so every page gets
    the same typing animation and the same reveal entrance."""
    typed = ""
    if strings:
        typed = ' data-strings="%s"' % "|".join(strings)

    left = """                    <p class="cmd" data-reveal>%s</p>
                    <h1 class="hero-title" data-reveal>%s<span class="typedText"%s></span><span class="cursor">_</span></h1>
                    <p class="hero-body" data-reveal>%s</p>
%s""" % (cmd, title_html, typed, body, extra)

    if portrait:
        return """        <section class="hero">
            <div class="shell">
                <div class="hero-grid">
                    <div>
%s
                    </div>
                    <div data-reveal>
                        <div class="portrait">
                            <img src="/images/profile.png" alt="Portrait of Cristina Rodriguez" width="600" height="600">
                        </div>
                        <p class="portrait-caption">./profile.png</p>
                    </div>
                </div>
            </div>
        </section>""" % left

    return """        <section class="hero">
            <div class="shell">
                <div class="hero-grid hero-grid--wide">
                    <div>
%s
                    </div>
                </div>
            </div>
        </section>""" % left


# ============================================================
# SHARED BLOCK BUILDERS
# ============================================================

def venture_cards():
    out = []
    for v in VENTURES:
        out.append("""                    <article class="card">
                        <h3 class="card-name">%s</h3>
                        <p class="card-sub">%s</p>
                        <p class="card-desc">%s</p>
                        <a class="card-link" href="%s"%s>%s</a>
                    </article>""" % (
            v["name"], v["sub"], v["desc"], v["link"],
            external_attrs(v["link"]), v["link_label"]))
    return "\n".join(out)


def project_rows(items, key="slug"):
    out = []
    for p in items:
        out.append("""                    <a class="proj-row" href="%s"%s>
                        <span class="proj-row-name">%s/</span>
                        <span class="proj-row-tech">%s</span>
                    </a>""" % (
            p["link"] if "link" in p else p["url"],
            external_attrs(p["link"] if "link" in p else p["url"]),
            p[key],
            " &middot; ".join(t.lower() for t in p["tags"])))
    return "\n".join(out)


def project_cards():
    out = []
    for p in PROJECTS:
        ext = external_attrs(p["url"])
        out.append("""                    <article class="proj-card">
                        <!-- Decorative: the heading below links to the same URL, so the
                             thumbnail is hidden from assistive tech and takes an empty alt.
                             Do not add alt text here; it would duplicate the link. -->
                        <a class="proj-thumb" href="%s"%s tabindex="-1" aria-hidden="true">
                            <img src="%s" alt="" loading="lazy" width="800" height="450">
                        </a>
                        <div class="proj-body">
                            <span class="proj-status status-%s">%s</span>
                            <h3 class="card-name"><a href="%s"%s>%s</a></h3>
                            <p class="card-desc">%s</p>
%s
                            <a class="card-link" href="%s"%s>%s &rarr;</a>
                        </div>
                    </article>""" % (
            p["url"], ext, p["img"], p["status"], p["status"],
            p["url"], ext, p["name"], p["desc"],
            tags_html(p["tags"], "                            "),
            p["url"], ext,
            "View source" if p["status"] == "archived" else "Visit site"))
    return "\n".join(out)


def teaching_cards():
    out = []
    for t in TEACHING:
        links = ['                            <a class="card-link" href="%s"%s>View project &rarr;</a>'
                 % (t["link"], external_attrs(t["link"]))]
        if t["youtube"]:
            links.append('                            <a class="card-link" href="%s" target="_blank" rel="noopener">Watch on YouTube &rarr;</a>'
                         % t["youtube"])
        out.append("""                    <article class="card">
                        <h3 class="card-name">%s</h3>
                        <p class="card-sub">%s</p>
                        <p class="card-desc">%s</p>
%s
                        <div class="card-links">
%s
                        </div>
                    </article>""" % (
            t["name"], t["sub"], t["desc"],
            tags_html(t["tags"], "                        "),
            "\n".join(links)))
    return "\n".join(out)


CERT_CARD = """                <div class="cert-card">
                    <div>
                        <h3 class="cert-title">Certificate in E-Learning Instructional Design</h3>
                        <p class="cert-issuer">University of Washington</p>
                        <p class="cert-desc">A professional certificate in instructional design, learning theory, and building effective online learning experiences &mdash; deepening my work as a technical curriculum developer.</p>
                        <a class="card-link" href="https://badges.parchment.com/public/assertions/9tIVWOtySumknWMyR-n2Dg" target="_blank" rel="noopener">Verify the credential &rarr;</a>
                    </div>
                    <div class="cert-badge">
                        <iframe src="https://badges.parchment.com/public/assertions/9tIVWOtySumknWMyR-n2Dg?embedVersion=1&amp;embedWidth=370&amp;embedHeight=167&amp;utm_source=html_embed"
                                title="Badge: Certificate in E-Learning Instructional Design" loading="lazy"></iframe>
                    </div>
                </div>"""


CERT_CARD_HF = """                <div class="cert-card">
                    <div>
                        <h3 class="cert-title">AI Agents Fundamentals</h3>
                        <p class="cert-issuer">Hugging Face &middot; 2025</p>
                        <p class="cert-desc">Foundations of agentic AI systems &mdash; tool use, planning and multi-step orchestration. The groundwork behind the multi-agent pipeline running in <a href="/projects/" class="text-link">Anzuelo</a>.</p>
                    </div>
                </div>"""


PERSON_JSONLD = """    {
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "Cristina Rodriguez",
      "url": "https://www.yosola.co/",
      "image": "https://www.yosola.co/images/profile.png",
      "jobTitle": ["Software Engineer", "Technical Curriculum Developer", "Founder of ComadreLab"],
      "description": "Software engineer and founder of ComadreLab, a web studio for small businesses. Builds full-stack applications with Next.js, React, TypeScript, Python, and AI. Certified in E-Learning Instructional Design (University of Washington). Also runs MujerTech, an AI training program for women entrepreneurs in Latin America.",
      "email": "mailto:yosola@gmail.com",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Seattle",
        "addressRegion": "WA",
        "addressCountry": "US"
      },
      "homeLocation": { "@type": "Place", "name": "Seattle, Washington" },
      "knowsAbout": [
        "Software Engineering", "Full-Stack Development", "Next.js", "React",
        "TypeScript", "JavaScript", "Python", "FastAPI", "LangChain", "CrewAI",
        "Anthropic API", "Claude", "Model Context Protocol", "MCP", "FastMCP",
        "Claude Code", "pgvector", "Docker", "GitHub Actions", "n8n",
        "OpenAI API", "GPT-4o-mini", "FAISS", "Tailwind CSS", "Node.js", "Prisma",
        "PostgreSQL", "Supabase", "NextAuth.js", "Vercel", "Google Vertex AI",
        "Stable Diffusion", "Hugging Face", "Canvas API", "PWA", "Service Workers",
        "i18n", "Mobile-First Design", "Technical Curriculum Development",
        "Instructional Design", "E-Learning", "AI Training", "Bilingual Content Creation"
      ],
      "hasCredential": [
        {
          "@type": "EducationalOccupationalCredential",
          "name": "Certificate in E-Learning Instructional Design",
          "credentialCategory": "certificate",
          "recognizedBy": {
            "@type": "CollegeOrUniversity",
            "name": "University of Washington",
            "sameAs": "https://www.washington.edu/"
          },
          "url": "https://badges.parchment.com/public/assertions/9tIVWOtySumknWMyR-n2Dg"
        },
        {
          "@type": "EducationalOccupationalCredential",
          "name": "AI Agents Fundamentals",
          "credentialCategory": "certificate",
          "recognizedBy": { "@type": "Organization", "name": "Hugging Face" }
        }
      ],
      "sameAs": [
        "https://www.linkedin.com/in/crissrodriguez/",
        "https://github.com/Yosolita1978",
        "https://play.google.com/store/apps/developer?id=yosola",
        "https://www.youtube.com/@crissrodriguez9940/videos"
      ],
      "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.yosola.co/" }
    }"""


SOCIAL_ROW = """                    <div class="social-row" data-reveal>
                        <a href="https://www.linkedin.com/in/crissrodriguez/" target="_blank" rel="noopener">linkedin</a>
                        <span class="sep">&middot;</span>
                        <a href="https://github.com/Yosolita1978" target="_blank" rel="noopener">github</a>
                        <span class="sep">&middot;</span>
                        <a href="https://www.youtube.com/@crissrodriguez9940/videos" target="_blank" rel="noopener">youtube</a>
                    </div>"""

HOME_BTNS = """                    <div class="btn-row" data-reveal>
                        <a class="btn btn-primary" href="https://www.comadrelab.dev/#contact" target="_blank" rel="noopener">work with me</a>
                        <a class="btn btn-ghost" href="mailto:yosola@gmail.com">hire me</a>
                        <a class="btn btn-ghost" href="%s" target="_blank" rel="noopener">download cv</a>
                    </div>
""" % CV

# ------------------------------------------------------------
# Old hash links such as yosola.co/#projects are already indexed by
# Google and shared elsewhere. This sends them to the new page.
# It runs in <head> so it redirects before anything paints.
# ------------------------------------------------------------
LEGACY_REDIRECT = """
    <!-- ----- LEGACY HASH LINKS (yosola.co/#projects -> /projects/) ----- -->
    <script>
        (function () {
            var map = {
                '#about': '/about/',
                '#ventures': '/ventures/',
                '#mujertech': '/ventures/',
                '#projects': '/projects/',
                '#education': '/teaching/',
                '#certifications': '/certifications/',
                '#chatbot': '/chat/',
                '#chat': '/chat/'
            };
            var target = map[window.location.hash];
            if (target) window.location.replace(target);
        })();
    </script>
"""


# ============================================================
# HOME
# ============================================================
home_body = """%s

        <!-- ----- VENTURES ----- -->
        <section class="section section--alt">
            <div class="shell">
                <div class="cmd-row" data-reveal>
                    <h2 class="cmd">ls ventures/</h2>
                    <a class="link-arrow" href="/ventures/">all ventures &rarr;</a>
                </div>
                <div class="card-grid" data-reveal-group>
%s
                </div>
            </div>
        </section>

        <!-- ----- PROJECTS ----- -->
        <section class="section">
            <div class="shell">
                <div class="cmd-row" data-reveal>
                    <h2 class="cmd">ls projects/</h2>
                    <a class="link-arrow" href="/projects/">all projects &rarr;</a>
                </div>
                <div class="proj-rows" data-reveal-group>
%s
                </div>
            </div>
        </section>

        <!-- ----- TEACHING ----- -->
        <section class="section section--alt">
            <div class="shell">
                <div class="cmd-row" data-reveal>
                    <h2 class="cmd">ls teaching/</h2>
                    <a class="link-arrow" href="/teaching/">all teaching work &rarr;</a>
                </div>
                <div class="proj-rows" data-reveal-group>
%s
                </div>
            </div>
        </section>

        <!-- ----- CERTIFICATIONS + CHAT ----- -->
        <section class="section">
            <div class="shell">
                <div class="split">
                    <div data-reveal>
                        <h2 class="cmd">cat certifications.md</h2>
                        <h3 class="teaser-title">Certificate in E-Learning Instructional Design</h3>
                        <p class="card-sub">University of Washington</p>
                        <p class="teaser-body">A professional certificate in instructional design, learning theory, and building effective online learning experiences &mdash; deepening my work as a technical curriculum developer.</p>
                        <a class="link-arrow" href="/certifications/">see certifications &rarr;</a>
                    </div>
                    <div data-reveal>
                        <h2 class="cmd">ask-me-anything</h2>
                        <p class="teaser-body">An interactive AI assistant that knows all about my professional journey, technical skills, and project experience. Built with Hugging Face Transformers.</p>
                        <p class="prompt-box">Ask anything about Cristina Rodriguez&hellip;</p>
                        <a class="link-arrow" href="/chat/">open the chatbot &rarr;</a>
                    </div>
                </div>
            </div>
        </section>""" % (
    hero(
        "whoami",
        "software engineer<br>&amp; ",
        ["technical curriculum developer", "instructional designer", "ai trainer"],
        'Software engineer and technical curriculum developer, certified in E-Learning Instructional Design by the University of Washington. I run <a href="https://www.comadrelab.dev/" target="_blank" rel="noopener" class="text-link">ComadreLab</a>, a web studio for small businesses, and <a href="/ventures/" class="text-link">MujerTech</a>, an AI training program for women entrepreneurs in Latin America. I build with Next.js, Python, and the Anthropic API.',
        extra=HOME_BTNS + SOCIAL_ROW,
        portrait=True,
    ),
    venture_cards(),
    project_rows(PROJECTS),
    project_rows(TEACHING),
)

render(
    "",
    "Cristina Rodriguez &mdash; Software Engineer &amp; Technical Curriculum Developer",
    "Seattle-based software engineer and technical curriculum developer with 5+ years of experience. Founder of ComadreLab, a web studio for small businesses, and MujerTech, an AI bootcamp for women entrepreneurs in Latin America. Building with Next.js, Python, the Anthropic API and MCP.",
    """    [
%s,
    {
      "@context": "https://schema.org",
      "@type": "ProfilePage",
      "name": "Cristina Rodriguez",
      "url": "https://www.yosola.co/",
      "dateModified": "__MOD__",
      "author": {
        "@type": "Person",
        "name": "Cristina Rodriguez",
        "url": "https://www.yosola.co/"
      },
      "mainEntity": { "@type": "Person", "name": "Cristina Rodriguez", "url": "https://www.yosola.co/" }
    }
    ]""" % PERSON_JSONLD,
    home_body,
    og_type="profile",
    extra_head=LEGACY_REDIRECT,
)


# ============================================================
# ABOUT
# Drafted from llms-full.txt, the resume PDF and the JSON-LD that
# was already on the site. Everything here was already published
# somewhere on yosola.co -- nothing is invented. REVIEW THE COPY.
# ============================================================
about_body = """%s

        <section class="section">
            <div class="shell">
                <div class="prose" data-reveal-group>
                    <h2>What I do</h2>
                    <p>I sit between two jobs that people usually treat as separate: building software, and teaching people how to build software. In practice they feed each other. Writing curriculum forces me to understand a technology well enough to explain it plainly, and shipping real applications keeps the curriculum honest about how the work actually goes.</p>
                    <p>I run two things of my own. <strong>ComadreLab</strong> is a web studio for small businesses, where I am founder and lead engineer &mdash; six client projects shipped since 2024, built mobile-first and wired into the tools a business already uses. <strong>MujerTech</strong> is a 16-week AI and business bootcamp for women entrepreneurs in Latin America, Spanish-first and currently running with its first cohort.</p>
                    <p>Most of my work lands in one of three places: full-stack applications for small businesses, AI tools that solve a specific problem rather than being a chatbot for its own sake, and bilingual technical training for people who have been left out of tech education. Before tech I spent two decades in communications and project management, which is most of the reason I am comfortable in front of a room.</p>

                    <h2>What I have shipped</h2>
                    <ul>
                        <li><strong>MujerTech</strong> &mdash; live and running with its first cohort of 25 learners.</li>
                        <li><strong>Picas y Fijas</strong> &mdash; played by 1,092 people across 177 cities.</li>
                        <li><strong>Nouvie</strong> &mdash; order and inventory system running in production for a Colombian cleaning products company.</li>
                        <li><strong>ComadreLab</strong> &mdash; six client projects shipped and supported since 2024.</li>
                        <li><strong>Techtonica</strong> &mdash; 50+ engineers mentored and onboarded since 2021.</li>
                    </ul>
                </div>
            </div>
        </section>

        <section class="section section--alt">
            <div class="shell">
                <h2 class="cmd" data-reveal>cat experience.txt</h2>
                <dl class="skill-rows" data-reveal-group>
                    <div class="skill-row"><dt>comadrelab/</dt><dd>Founder &amp; Lead Engineer &mdash; 2024 to present</dd></div>
                    <div class="skill-row"><dt>elm-learning/</dt><dd>Technical Curriculum Developer &mdash; March 2024 to February 2026</dd></div>
                    <div class="skill-row"><dt>techtonica/</dt><dd>Technical Program Manager &mdash; May 2021 to December 2023</dd></div>
                    <div class="skill-row"><dt>education/</dt><dd>B.A. in Communication</dd></div>
                </dl>
            </div>
        </section>

        <section class="section">
            <div class="shell">
                <h2 class="cmd" data-reveal>cat status.txt</h2>
                <dl class="skill-rows" data-reveal-group>
                    <div class="skill-row"><dt>location/</dt><dd>Seattle, Washington &mdash; Pacific time</dd></div>
                    <div class="skill-row"><dt>remote/</dt><dd>Open to remote, and to hybrid in the Seattle area</dd></div>
                    <div class="skill-row"><dt>work-auth/</dt><dd>US Permanent Resident (Green Card) &mdash; no sponsorship required</dd></div>
                    <div class="skill-row"><dt>languages/</dt><dd>Bilingual &mdash; Spanish and English</dd></div>
                    <div class="skill-row"><dt>experience/</dt><dd>5+ years in software engineering and technical curriculum</dd></div>
                </dl>
            </div>
        </section>

        <section class="section section--alt">
            <div class="shell">
                <h2 class="cmd" data-reveal>cat skills.txt</h2>
                <dl class="skill-rows" data-reveal-group>
                    <div class="skill-row"><dt>engineering/</dt><dd>TypeScript (strict) &middot; JavaScript &middot; Python &middot; SQL &middot; React &middot; Next.js (App Router) &middot; Node.js &middot; FastAPI &middot; Prisma</dd></div>
                    <div class="skill-row"><dt>ai-agents/</dt><dd>Anthropic API &middot; Claude &middot; MCP / FastMCP &middot; LangChain &middot; OpenAI API &middot; multi-agent orchestration &middot; human-in-the-loop design &middot; retrieval with pgvector &middot; n8n</dd></div>
                    <div class="skill-row"><dt>data/</dt><dd>PostgreSQL &middot; Supabase (RLS) &middot; Firebase &middot; multi-tenant SaaS &middot; PDF and document pipelines</dd></div>
                    <div class="skill-row"><dt>infra/</dt><dd>Docker &middot; AWS &middot; Vercel &middot; GitHub Actions &middot; Git / GitHub</dd></div>
                </dl>
            </div>
        </section>

        <section class="section">
            <div class="shell">
                <div class="split">
                    <div data-reveal>
                        <h2 class="cmd">cd work/</h2>
                        <p class="teaser-body">See what I have shipped and what I have taught.</p>
                        <div class="card-links">
                            <a class="link-arrow" href="/projects/">projects &rarr;</a>
                            <a class="link-arrow" href="/teaching/">teaching &rarr;</a>
                            <a class="link-arrow" href="/ventures/">ventures &rarr;</a>
                        </div>
                    </div>
                    <div data-reveal>
                        <h2 class="cmd">contact</h2>
                        <p class="teaser-body">Working on something I could help with? The fastest way to reach me is email.</p>
                        <div class="btn-row">
                            <a class="btn btn-primary" href="mailto:yosola@gmail.com">yosola@gmail.com</a>
                            <a class="btn btn-ghost" href="%s" target="_blank" rel="noopener">download cv</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>""" % (
    hero(
        "cat about.md",
        "i build software<br>and i teach<br>",
        ["people to build it", "ai to non-engineers", "in english &amp; spanish"],
        "Software engineer and technical curriculum developer based in Seattle. 5+ years building production software and teaching other people to build it.",
    ),
    CV,
)

render(
    "about",
    "About Cristina Rodriguez &mdash; Technical Curriculum Developer &amp; Software Engineer",
    "Cristina Rodriguez is a software engineer and technical curriculum developer in Seattle with 5+ years of experience. Builds full-stack and AI products with Next.js, Python, the Anthropic API and MCP. Founder of ComadreLab and MujerTech. US Permanent Resident, open to remote.",
    """    [
%s,
%s,
    {
      "@context": "https://schema.org",
      "@type": "AboutPage",
      "name": "About Cristina Rodriguez",
      "url": "https://www.yosola.co/about/",
      "dateModified": "__MOD__",
      "author": {
        "@type": "Person",
        "name": "Cristina Rodriguez",
        "url": "https://www.yosola.co/"
      },
            "mainEntity": { "@type": "Person", "name": "Cristina Rodriguez", "url": "https://www.yosola.co/" }
    }
    ]""" % (PERSON_JSONLD, breadcrumb("about", "About")),
    about_body,
    og_type="profile",
)


# ============================================================
# VENTURES
# ============================================================
ventures_body = """%s

        <section class="section">
            <div class="shell">
                <h2 class="cmd" data-reveal>ls ventures/</h2>
                <div class="card-grid" data-reveal-group>
%s
                </div>
            </div>
        </section>

        <section class="section section--alt">
            <div class="shell">
                <div class="split">
                    <div data-reveal>
                        <h2 class="cmd">cat comadrelab/README.md</h2>
                        <p class="teaser-body">ComadreLab is my web studio, where I am founder and lead engineer. I design and ship full-stack and AI systems for small businesses and Latin American clients, owning architecture, data modeling and deployment end to end &mdash; including LLM features running in production: multi-agent pipelines, MCP tooling and retrieval, on Next.js/TypeScript and Python. Six client projects shipped and supported since 2024, among them <a href="/projects/" class="text-link">Nouvie</a> and <a href="/projects/" class="text-link">Anzuelo</a>.</p>
                        <a class="link-arrow" href="https://www.comadrelab.dev/" target="_blank" rel="noopener">comadrelab.dev &rarr;</a>
                    </div>
                    <div data-reveal>
                        <h2 class="cmd">cat mujertech/README.md</h2>
                        <p class="teaser-body">MujerTech is a 16-week bootcamp teaching AI tools and business strategy to women entrepreneurs in Latin America, launching in Bogot&aacute;. The platform is Spanish-first and mobile-first, with three scaffolded bilingual modules that end in a real marketing piece the learner can use. The guiding idea is &ldquo;La IA propone, t&uacute; decides&rdquo; &mdash; AI as a helper, not a replacement.</p>
                        <a class="link-arrow" href="https://bootcamp.mujertech.org" target="_blank" rel="noopener">bootcamp.mujertech.org &rarr;</a>
                    </div>
                </div>
            </div>
        </section>""" % (
    hero(
        "ls ventures/",
        "two things<br>i am building<br>",
        ["a web studio", "an ai bootcamp", "for people, not hype"],
        "ComadreLab is a web studio for small businesses. MujerTech is an AI training program for women entrepreneurs in Latin America. Both exist to put good tools in the hands of people who are usually sold bad ones.",
    ),
    venture_cards(),
)

render(
    "ventures",
    "Ventures &mdash; ComadreLab &amp; MujerTech | Cristina Rodriguez",
    "ComadreLab is a web studio building fast, mobile-first sites and automations for small businesses. MujerTech is a 16-week AI and business bootcamp for women entrepreneurs in Latin America, launching in Bogota.",
    """    [
%s,
    {
      "@context": "https://schema.org",
      "@type": "CollectionPage",
      "name": "Ventures",
      "url": "https://www.yosola.co/ventures/",
      "dateModified": "__MOD__",
      "author": {
        "@type": "Person",
        "name": "Cristina Rodriguez",
        "url": "https://www.yosola.co/"
      },
            "mainEntity": {
        "@type": "ItemList",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "item": {
              "@type": "Organization", "name": "ComadreLab", "url": "https://www.comadrelab.dev/",
              "description": "A web studio building fast, mobile-first websites and automations for small businesses.",
              "founder": { "@type": "Person", "name": "Cristina Rodriguez" } } },
          { "@type": "ListItem", "position": 2, "item": {
              "@type": "Organization", "name": "MujerTech", "url": "https://bootcamp.mujertech.org",
              "description": "A 16-week bootcamp teaching AI tools and business strategy to women entrepreneurs in Latin America.",
              "founder": { "@type": "Person", "name": "Cristina Rodriguez" } } }
        ]
      }
    }
    ]""" % breadcrumb("ventures", "Ventures"),
    ventures_body,
)


# ============================================================
# PROJECTS
# ============================================================
projects_body = """%s

        <section class="section">
            <div class="shell">
                <div class="cmd-row" data-reveal>
                    <h2 class="cmd">ls projects/</h2>
                    <a class="link-arrow" href="/teaching/">teaching work &rarr;</a>
                </div>
                <div class="proj-grid" data-reveal-group>
%s
                </div>
            </div>
        </section>""" % (
    hero(
        "ls projects/",
        "things i have<br>shipped, mostly<br>",
        ["full-stack apps", "ai tools", "bilingual by default"],
        "Client work, AI experiments and small tools. Live projects are running in production; archived ones have had their deployment retired but the source is still on GitHub.",
    ),
    project_cards(),
)

projects_items = ",\n".join(
    """          { "@type": "ListItem", "position": %d, "name": "%s", "url": "%s" }"""
    % (i + 1,
       p["name"].replace("&mdash;", "-").replace("&amp;", "and"),
       p["url"] if p["url"].startswith("http") else SITE + p["url"])
    for i, p in enumerate(PROJECTS)
)

render(
    "projects",
    "Projects &mdash; Full-Stack &amp; AI Work | Cristina Rodriguez",
    "Software projects by Cristina Rodriguez: Nouvie order and inventory system, Sazon Mexican recipe bot, Soneto Bot, Picas y Fijas, an ASCII art converter and more. Built with Next.js, TypeScript, Python, FastAPI, LangChain and Supabase.",
    """    [
%s,
    {
      "@context": "https://schema.org",
      "@type": "CollectionPage",
      "name": "Projects",
      "url": "https://www.yosola.co/projects/",
      "dateModified": "__MOD__",
      "author": {
        "@type": "Person",
        "name": "Cristina Rodriguez",
        "url": "https://www.yosola.co/"
      },
            "mainEntity": {
        "@type": "ItemList",
        "itemListElement": [
%s
        ]
      }
    }
    ]""" % (breadcrumb("projects", "Projects"), projects_items),
    projects_body,
)


# ============================================================
# TEACHING
# ============================================================
teaching_body = """%s

        <section class="section">
            <div class="shell">
                <div class="cmd-row" data-reveal>
                    <h2 class="cmd">ls teaching/</h2>
                    <a class="link-arrow" href="/certifications/">certifications &rarr;</a>
                </div>
                <div class="card-grid" data-reveal-group>
%s
                </div>
            </div>
        </section>

        <section class="section section--alt">
            <div class="shell">
                <div class="split">
                    <div data-reveal>
                        <h2 class="cmd">cat approach.md</h2>
                        <p class="teaser-body">I design curriculum the way I design software: start from what the learner actually needs to do, cut everything that does not serve it, and make sure the thing works before adding polish. Every course above ends in something the learner built, not a quiz they passed.</p>
                    </div>
                    <div data-reveal>
                        <h2 class="cmd">cat credentials.md</h2>
                        <p class="teaser-body">Certified in E-Learning Instructional Design by the University of Washington &mdash; formal grounding in learning theory behind the hands-on teaching work.</p>
                        <a class="link-arrow" href="/certifications/">see certifications &rarr;</a>
                    </div>
                </div>
            </div>
        </section>""" % (
    hero(
        "ls teaching/",
        "courses,<br>workshops &amp;<br>",
        ["curriculum design", "technical training", "learning that sticks"],
        "Curriculum and workshops I have designed and delivered &mdash; from a Spanish-first AI bootcamp to a Next.js course, a Stable Diffusion workshop, and a beginner course on using Google tools on a phone.",
    ),
    teaching_cards(),
)

teaching_items = ",\n".join(
    """          { "@type": "ListItem", "position": %d, "item": {
              "@type": "Course", "name": "%s", "url": "%s",
              "description": "%s",
              "provider": { "@type": "Person", "name": "Cristina Rodriguez", "url": "https://www.yosola.co/" } } }"""
    % (i + 1,
       t["name"].replace("&amp;", "and"),
       t["link"],
       t["desc"].replace("&mdash;", "-").replace("&ldquo;", "").replace("&rdquo;", "")
                .replace("&uacute;", "u").replace("&amp;", "and").replace('"', "'"))
    for i, t in enumerate(TEACHING)
)

render(
    "teaching",
    "Teaching &amp; Curriculum &mdash; Courses and Workshops | Cristina Rodriguez",
    "Technical curriculum and workshops designed and delivered by Cristina Rodriguez: the MujerTech AI and business bootcamp, a Next.js course, a Stable Diffusion avatar workshop, an Express and React template, and beginner Google Workspace training.",
    """    [
%s,
    {
      "@context": "https://schema.org",
      "@type": "CollectionPage",
      "name": "Teaching and Curriculum",
      "url": "https://www.yosola.co/teaching/",
      "dateModified": "__MOD__",
      "author": {
        "@type": "Person",
        "name": "Cristina Rodriguez",
        "url": "https://www.yosola.co/"
      },
            "mainEntity": {
        "@type": "ItemList",
        "itemListElement": [
%s
        ]
      }
    }
    ]""" % (breadcrumb("teaching", "Teaching"), teaching_items),
    teaching_body,
)


# ============================================================
# CERTIFICATIONS
# ============================================================
certifications_body = """%s

        <section class="section">
            <div class="shell">
                <h2 class="cmd" data-reveal>cat certifications.md</h2>
                <div class="cert-stack" data-reveal-group>
%s
%s
                </div>
            </div>
        </section>

        <section class="section section--alt">
            <div class="shell">
                <div class="split">
                    <div data-reveal>
                        <h2 class="cmd">why it matters</h2>
                        <p class="teaser-body">Instructional design is the difference between explaining something and teaching it. The certificate gave formal grounding in learning theory, assessment design and course structure &mdash; the theory behind the curriculum work I was already doing.</p>
                    </div>
                    <div data-reveal>
                        <h2 class="cmd">cd teaching/</h2>
                        <p class="teaser-body">See how this shows up in practice: the courses, bootcamps and workshops I have designed and delivered.</p>
                        <a class="link-arrow" href="/teaching/">teaching work &rarr;</a>
                    </div>
                </div>
            </div>
        </section>""" % (
    hero(
        "cat certifications.md",
        "credentials<br>behind the<br>",
        ["curriculum work", "learning theory", "teaching practice"],
        "Formal credentials that back up the curriculum and training work.",
    ),
    CERT_CARD,
    CERT_CARD_HF,
)

render(
    "certifications",
    "Certifications &mdash; E-Learning Instructional Design, UW | Cristina Rodriguez",
    "Cristina Rodriguez holds a Certificate in E-Learning Instructional Design from the University of Washington and AI Agents Fundamentals from Hugging Face \u2014 the grounding behind her curriculum work and her multi-agent AI projects.",
    """    [
%s,
    {
      "@context": "https://schema.org",
      "@type": "CollectionPage",
      "name": "Certifications",
      "url": "https://www.yosola.co/certifications/",
      "dateModified": "__MOD__",
      "author": {
        "@type": "Person",
        "name": "Cristina Rodriguez",
        "url": "https://www.yosola.co/"
      },
            "mainEntity": {
        "@type": "ItemList",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "item": {
              "@type": "EducationalOccupationalCredential",
              "name": "Certificate in E-Learning Instructional Design",
              "credentialCategory": "certificate",
              "url": "https://badges.parchment.com/public/assertions/9tIVWOtySumknWMyR-n2Dg",
              "recognizedBy": {
                "@type": "CollegeOrUniversity",
                "name": "University of Washington",
                "sameAs": "https://www.washington.edu/"
              },
              "about": { "@type": "Person", "name": "Cristina Rodriguez", "url": "https://www.yosola.co/" } } },
          { "@type": "ListItem", "position": 2, "item": {
              "@type": "EducationalOccupationalCredential",
              "name": "AI Agents Fundamentals",
              "credentialCategory": "certificate",
              "recognizedBy": { "@type": "Organization", "name": "Hugging Face" },
              "about": { "@type": "Person", "name": "Cristina Rodriguez", "url": "https://www.yosola.co/" } } }
        ]
      }
    }
    ]""" % breadcrumb("certifications", "Certifications"),
    certifications_body,
)


# ============================================================
# CHAT
# ============================================================
chat_body = """%s

        <section class="section">
            <div class="shell">
                <div class="cmd-row" data-reveal>
                    <h2 class="cmd">ask-me-anything</h2>
                    <a class="link-arrow" href="https://huggingface.co/spaces/ECRodriguez/career_chatbot" target="_blank" rel="noopener">view on hugging face &rarr;</a>
                </div>

                <div class="tags" data-reveal>
                    <span>AI/ML</span>
                    <span>NLP</span>
                    <span>Hugging Face</span>
                    <span>Python</span>
                    <span>Transformers</span>
                </div>

                <div class="chat-frame" data-reveal data-src="https://hf.co/embed/ECRodriguez/career_chatbot">
                    <div class="chat-placeholder" id="chat-placeholder">
                        <p class="chat-placeholder-text">The assistant runs on Hugging Face and opens in an embedded frame.</p>
                        <button class="btn btn-primary" type="button" id="chat-start">./start-chat.sh</button>
                        <p class="chat-note">Loads on demand &mdash; nothing is sent to Hugging Face until you start it.</p>
                    </div>
                </div>
            </div>
        </section>""" % hero(
    "ask-me-anything",
    "ask a bot<br>about my<br>",
    ["career", "projects", "technical skills"],
    "An interactive AI assistant that knows about my professional journey, technical skills and project experience. Ask it about my background in software development, curriculum design, or any of my projects. Built with Hugging Face Transformers.",
)

render(
    "chat",
    "Chat &mdash; Ask Me Anything AI Assistant | Cristina Rodriguez",
    "An interactive AI assistant trained on Cristina Rodriguez's professional background. Ask about her software engineering work, curriculum design experience and projects. Built with Hugging Face Transformers.",
    """    [
%s,
    {
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "Ask Me Anything Chatbot",
      "url": "https://www.yosola.co/chat/",
      "dateModified": "__MOD__",
      "author": {
        "@type": "Person",
        "name": "Cristina Rodriguez",
        "url": "https://www.yosola.co/"
      },
            "description": "An interactive AI assistant that answers questions about Cristina Rodriguez's professional journey, technical skills and project experience.",
      "about": { "@type": "Person", "name": "Cristina Rodriguez", "url": "https://www.yosola.co/" }
    }
    ]""" % breadcrumb("chat", "Chat"),
    chat_body,
    extra_scripts='    <script src="/js/chat.js"></script>\n',
)


# ============================================================
# 404  -->  written to /404.html at the site root, because that is
# where the Amplify custom-404 rule points.
# ============================================================
notfound_body = """        <section class="hero">
            <div class="shell">
                <div class="notfound">
                    <h2 class="cmd" data-reveal>cat $REQUEST_URI</h2>
                    <p class="notfound-code" data-reveal>404</p>
                    <h1 class="hero-title" data-reveal>no such file<br>or <span class="typedText" data-strings="directory|page|route"></span><span class="cursor">_</span></h1>
                    <p class="hero-body" data-reveal>That page does not exist. It may have moved when the site was reorganised. Try one of these instead.</p>
                    <div class="btn-row" data-reveal>
                        <a class="btn btn-primary" href="/">cd ~</a>
                        <a class="btn btn-ghost" href="/projects/">projects</a>
                        <a class="btn btn-ghost" href="/teaching/">teaching</a>
                        <a class="btn btn-ghost" href="/about/">about</a>
                    </div>
                </div>
            </div>
        </section>"""

html_404 = PAGE.format(
    title="404 &mdash; Page Not Found | Cristina Rodriguez",
    description="The page you are looking for does not exist.",
    canonical=SITE + "/404.html",
    og_title="404 &mdash; Page Not Found",
    og_type="website",
    site=SITE,
    robots='    <meta name="robots" content="noindex, follow">\n',
    extra_head="",
    extra_scripts="",
    jsonld="""    {
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "404 - Page Not Found",
      "url": "https://www.yosola.co/404.html"
    }""",
    nav=nav_html(None),
    body=notfound_body,
    footer=FOOTER,
)
with open(os.path.join(OUT, "404.html"), "w") as fh:
    fh.write(html_404)


# ============================================================
# SITEMAP
# ============================================================
LASTMOD = MODIFIED
# /ascii/ is hand-maintained, so it carries its own file date.
ASCII_LASTMOD = file_date(os.path.join(OUT, "ascii", "index.html"))
urls = []
for slug, _ in NAV_ITEMS:
    priority = "1.0" if slug == "" else ("0.9" if slug in ("projects", "teaching", "about") else "0.8")
    urls.append("""  <url>
    <loc>%s%s</loc>
    <lastmod>%s</lastmod>
    <changefreq>monthly</changefreq>
    <priority>%s</priority>
  </url>""" % (SITE, url_for(slug), LASTMOD, priority))

urls.append("""  <url>
    <loc>%s/ascii/</loc>
    <lastmod>%s</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.6</priority>
  </url>""" % (SITE, ASCII_LASTMOD))

with open(os.path.join(OUT, "sitemap.xml"), "w") as fh:
    fh.write("""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
%s
</urlset>
""" % "\n".join(urls))


# ============================================================
# LLMS.TXT
# Generated from NAV_ITEMS so the page list cannot drift.
# llms-full.txt stays hand-maintained: it is long-form prose.
# ============================================================
PAGE_BLURBS = {
    "":               "Home",
    "about":          "About, background, experience and skills",
    "ventures":       "ComadreLab and MujerTech",
    "projects":       "Software projects",
    "teaching":       "Courses, workshops and curriculum",
    "certifications": "Credentials",
    "chat":           "AI assistant that answers questions about Cristina",
}

llms_pages = "\n".join(
    "- %s: %s%s" % (PAGE_BLURBS[slug], SITE, url_for(slug))
    for slug, _ in NAV_ITEMS
)

llms_projects = "\n".join(
    "- %s: %s" % (
        p["name"].replace("&mdash;", "-").replace("&amp;", "&"),
        p["url"] if p["url"].startswith("http") else SITE + p["url"])
    for p in PROJECTS
)

with open(os.path.join(OUT, "llms.txt"), "w") as fh:
    fh.write("""# Cristina Rodriguez

> Software Engineer and Technical Curriculum Developer in Seattle. 5+ years building production software and teaching other people to build it. US Permanent Resident, open to remote.

## Canonical URL
%s/

## Pages
%s

## Profiles
- LinkedIn: https://www.linkedin.com/in/crissrodriguez/
- GitHub: https://github.com/Yosolita1978
- YouTube: https://www.youtube.com/@crissrodriguez9940/videos
- Google Play: https://play.google.com/store/apps/developer?id=yosola

## Ventures
- ComadreLab (web studio for small businesses): https://www.comadrelab.dev/
- MujerTech (AI training for women entrepreneurs in Latin America): https://bootcamp.mujertech.org

## Projects
%s

## Contact
Email: yosola@gmail.com

## More Context
For detailed information, see: %s/llms-full.txt
""" % (SITE, llms_pages, llms_projects, SITE))


# ============================================================
# ROBOTS
# ============================================================
with open(os.path.join(OUT, "robots.txt"), "w") as fh:
    fh.write("""User-agent: *
Allow: /

# AI crawlers and answer engines are explicitly welcome.
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

Sitemap: %s/sitemap.xml
""" % SITE)

print("Generated:")
for slug, _ in NAV_ITEMS:
    print("  %-18s -> %s" % (url_for(slug), os.path.join(OUT, slug, "index.html")))
print("  /404.html")
print("  /sitemap.xml")
print("  /robots.txt")
print("  /llms.txt")
