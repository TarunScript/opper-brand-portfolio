#!/usr/bin/env python3
"""
Build script: Extracts base64 images from the existing HTML
and injects them into the redesigned template.
"""
import re

# Read the source HTML to extract base64 images
with open('OPPER · Organic Soap & Skincare — Portfolio.html', 'r') as f:
    source = f.read()

# Extract unique images by alt text
imgs = re.findall(r'src="(data:image/[^"]+)"[^>]*alt="([^"]*)"', source)
image_map = {}
for src, alt in imgs:
    if alt and alt not in image_map:
        image_map[alt] = src

# Assign to named variables for clarity
IMG_LOGO = image_map.get('OPPER logo: milk splash, saffron flower and gold ring', '')
IMG_SOAPS_TRAY = image_map.get('Handcrafted OPPER soaps on a marble tray', '')
IMG_SOAP_BOX = image_map.get('OPPER soap box with peach and cream bars', '')
IMG_GIFT_BOX = image_map.get('OPPER gift box with soaps and tags', '')
IMG_PREMIUM_BAR = image_map.get('OPPER Premium Goat Milk and Saffron Bathing Bar box', '')
IMG_INGREDIENTS = image_map.get('Welcome to Opper World: ingredients and benefits of OPPER organic soap', '')
IMG_FOUNDER = image_map.get('Geetha, founder of OPPER', '')
IMG_GEET = image_map.get('GEET personalised jute bag, gift box and wooden mug', '')

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>OPPER — Handcrafted Organic Soap &amp; Skincare</title>
<meta name="description" content="OPPER creates handmade organic soap and skincare with goat milk, saffron, ayurvedic herbs and nourishing oils. Pure by nature, made with care.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
/* ===== DESIGN TOKENS ===== */
:root {{
  --ivory: #FAF7F2;
  --cream: #F3EDE3;
  --sage: #DDE5D4;
  --sage-deep: #C2CEB5;
  --forest: #2C3E2D;
  --forest-light: #3D5240;
  --terracotta: #B5785A;
  --terracotta-light: #C99B7E;
  --ink: #1A1E1A;
  --muted: #6B7068;
  --line: #D6CFBF;
  --white: #FFFFFF;
  --serif: 'Playfair Display', Georgia, serif;
  --sans: 'Inter', system-ui, -apple-system, sans-serif;
}}

/* ===== RESET & BASE ===== */
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; scroll-padding-top: 72px; }}
body {{
  background: var(--ivory);
  color: var(--ink);
  font: 400 16px/1.7 var(--sans);
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}}
img {{ max-width: 100%; display: block; height: auto; }}
a {{ color: inherit; text-decoration: none; }}
h1, h2, h3, h4 {{ font-family: var(--serif); font-weight: 400; line-height: 1.15; }}

/* ===== LAYOUT ===== */
.container {{ max-width: 1200px; margin: 0 auto; padding: 0 32px; }}
.section {{ padding: 100px 0; }}
.section--sage {{ background: var(--sage); }}
.section--forest {{ background: var(--forest); color: var(--cream); }}
.section--cream {{ background: var(--cream); }}

/* ===== HEADER ===== */
.header {{
  position: sticky; top: 0; z-index: 100;
  background: rgba(250, 247, 242, 0.92);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--line);
  transition: box-shadow 0.3s;
}}
.header.scrolled {{ box-shadow: 0 2px 20px rgba(0,0,0,0.06); }}
.header__inner {{
  display: flex; justify-content: space-between; align-items: center;
  height: 68px; max-width: 1200px; margin: 0 auto; padding: 0 32px;
}}
.header__logo {{
  font: 600 20px var(--serif);
  letter-spacing: 0.18em;
  color: var(--forest);
  text-transform: uppercase;
}}
.header__nav {{ display: flex; gap: 32px; }}
.header__link {{
  font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase;
  color: var(--muted); font-weight: 500;
  transition: color 0.3s;
  position: relative;
}}
.header__link::after {{
  content: ''; position: absolute; bottom: -4px; left: 0; width: 0;
  height: 1px; background: var(--forest); transition: width 0.3s;
}}
.header__link:hover {{ color: var(--forest); }}
.header__link:hover::after {{ width: 100%; }}

/* Mobile menu */
.header__toggle {{ display: none; background: none; border: none; cursor: pointer; padding: 8px; }}
.header__toggle span {{
  display: block; width: 22px; height: 1.5px; background: var(--forest);
  margin: 5px 0; transition: all 0.3s;
}}

/* ===== HERO ===== */
.hero {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: calc(100vh - 68px);
  align-items: center;
}}
.hero__content {{
  padding: 80px 60px 80px 0;
  padding-left: max(32px, calc((100vw - 1200px) / 2 + 32px));
}}
.hero__label {{
  font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase;
  color: var(--terracotta); margin-bottom: 24px; font-weight: 600;
}}
.hero__title {{
  font-size: clamp(40px, 5.5vw, 72px);
  line-height: 1.08;
  margin-bottom: 28px;
  color: var(--forest);
}}
.hero__title em {{
  font-style: italic;
  color: var(--terracotta);
}}
.hero__desc {{
  font-size: 17px; color: var(--muted); max-width: 440px;
  margin-bottom: 40px; line-height: 1.75;
}}
.hero__image {{
  height: 100%;
  min-height: 560px;
  position: relative;
  overflow: hidden;
}}
.hero__image img {{
  width: 100%; height: 100%;
  object-fit: cover;
  object-position: center;
}}

/* ===== BUTTONS ===== */
.btn {{
  display: inline-flex; align-items: center; gap: 10px;
  padding: 16px 36px;
  font: 500 12px/1 var(--sans);
  letter-spacing: 0.14em; text-transform: uppercase;
  border-radius: 0;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer; border: none;
}}
.btn--primary {{
  background: var(--forest); color: var(--cream);
}}
.btn--primary:hover {{
  background: var(--forest-light);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(44, 62, 45, 0.2);
}}
.btn--outline {{
  background: transparent; color: var(--forest);
  border: 1px solid var(--forest);
  margin-left: 14px;
}}
.btn--outline:hover {{
  background: var(--forest); color: var(--cream);
}}
.btn--light {{
  background: var(--cream); color: var(--forest);
}}
.btn--light:hover {{
  background: var(--white);
  transform: translateY(-2px);
}}
.btn svg {{ width: 16px; height: 16px; }}

/* ===== SECTION HEADINGS ===== */
.section__label {{
  font-size: 11px; letter-spacing: 0.22em; text-transform: uppercase;
  color: var(--terracotta); margin-bottom: 16px; font-weight: 600;
}}
.section--forest .section__label {{ color: var(--terracotta-light); }}
.section__title {{
  font-size: clamp(32px, 4vw, 52px);
  margin-bottom: 20px;
  max-width: 700px;
}}
.section__desc {{
  font-size: 17px; color: var(--muted); max-width: 560px;
  line-height: 1.75;
}}
.section--forest .section__desc {{ color: var(--sage-deep); }}

/* ===== PRODUCT COLLECTION ===== */
.product {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  align-items: stretch;
  margin-bottom: 2px;
}}
.product--reverse {{ direction: rtl; }}
.product--reverse > * {{ direction: ltr; }}
.product__image {{
  position: relative;
  overflow: hidden;
  min-height: 480px;
}}
.product__image img {{
  width: 100%; height: 100%;
  object-fit: cover;
  transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}}
.product__image:hover img {{ transform: scale(1.03); }}
.product__info {{
  padding: 64px 56px;
  display: flex; flex-direction: column; justify-content: center;
}}
.product__tag {{
  font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--terracotta); margin-bottom: 16px; font-weight: 600;
}}
.product__name {{
  font-size: clamp(28px, 3vw, 40px);
  margin-bottom: 16px;
  color: var(--forest);
}}
.product__desc {{
  font-size: 15px; color: var(--muted); line-height: 1.75;
  margin-bottom: 24px;
}}
.product__features {{
  list-style: none; margin-bottom: 32px;
}}
.product__features li {{
  padding: 10px 0;
  border-bottom: 1px solid var(--line);
  font-size: 14px; color: var(--ink);
  display: flex; align-items: center; gap: 12px;
}}
.product__features li::before {{
  content: '';
  width: 6px; height: 6px;
  background: var(--terracotta);
  border-radius: 50%;
  flex-shrink: 0;
}}
.product__badges {{
  display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 28px;
}}
.badge {{
  padding: 6px 16px;
  font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase;
  border: 1px solid var(--sage-deep);
  color: var(--forest);
  font-weight: 500;
}}

/* ===== INGREDIENTS ===== */
.ingredients-grid {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 32px;
  margin-top: 56px;
}}
.ingredient {{
  text-align: center;
  padding: 40px 20px;
  background: rgba(255,255,255,0.5);
  border: 1px solid var(--line);
  transition: transform 0.3s, box-shadow 0.3s;
}}
.ingredient:hover {{
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.06);
}}
.ingredient__icon {{
  font-size: 36px;
  margin-bottom: 16px;
  display: block;
}}
.ingredient__name {{
  font: 600 18px var(--serif);
  margin-bottom: 8px;
  color: var(--forest);
}}
.ingredient__desc {{
  font-size: 13px; color: var(--muted); line-height: 1.65;
}}

/* ===== ABOUT / STORY ===== */
.story {{
  display: grid;
  grid-template-columns: 0.4fr 0.6fr;
  gap: 80px;
  align-items: center;
}}
.story__image {{
  position: relative;
}}
.story__image img {{
  width: 100%;
  aspect-ratio: 3/4;
  object-fit: cover;
}}
.story__image::after {{
  content: '';
  position: absolute;
  top: 16px; left: 16px; right: -16px; bottom: -16px;
  border: 1px solid var(--terracotta-light);
  z-index: -1;
}}
.story blockquote {{
  font: italic 400 clamp(22px, 2.5vw, 30px)/1.4 var(--serif);
  color: var(--forest);
  margin: 32px 0;
  padding-left: 24px;
  border-left: 2px solid var(--terracotta);
}}

/* ===== FOUNDER ===== */
.founder {{
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 72px;
  align-items: center;
}}
.founder__image {{
  position: relative;
}}
.founder__image img {{
  width: 100%;
  max-width: 400px;
  aspect-ratio: 3/4;
  object-fit: cover;
  object-position: top center;
}}
.founder__name {{
  font-size: clamp(28px, 3vw, 42px);
  margin-bottom: 8px;
  color: var(--forest);
}}
.founder__role {{
  font-size: 12px; letter-spacing: 0.16em; text-transform: uppercase;
  color: var(--terracotta); margin-bottom: 24px; font-weight: 600;
}}
.founder__text {{
  font-size: 16px; color: var(--muted); line-height: 1.8;
  margin-bottom: 16px;
}}
.founder blockquote {{
  font: italic 400 20px/1.5 var(--serif);
  color: var(--forest);
  padding: 20px 24px;
  border-left: 2px solid var(--terracotta);
  margin: 28px 0;
  background: rgba(181, 120, 90, 0.06);
}}

/* ===== SOCIAL PROOF ===== */
.proof {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 56px;
  align-items: center;
}}
.proof__stat {{
  font: 400 clamp(80px, 12vw, 140px)/0.9 var(--serif);
  color: var(--terracotta);
}}
.proof__awards {{
  margin-top: 40px;
}}
.proof__awards li {{
  padding: 14px 0;
  border-bottom: 1px solid rgba(255,255,255,0.12);
  font-size: 14px;
  color: var(--sage-deep);
  display: flex; align-items: center; gap: 12px;
}}
.proof__awards li::before {{
  content: '—';
  color: var(--terracotta-light);
}}

/* ===== GEET ===== */
.geet {{
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 64px;
  align-items: center;
}}
.geet__image img {{
  width: 100%;
  border: 1px solid var(--line);
}}
.geet__tags {{
  display: flex; flex-wrap: wrap; gap: 8px; margin: 24px 0 32px;
}}
.geet__tag {{
  padding: 6px 18px;
  font-size: 12px; letter-spacing: 0.08em;
  border: 1px solid var(--forest-light);
  color: var(--forest);
  font-weight: 500;
}}

/* ===== CONTACT ===== */
.contact {{
  text-align: center;
}}
.contact__links {{
  display: flex; flex-wrap: wrap; gap: 16px;
  justify-content: center;
  margin-top: 40px;
}}
.contact__link {{
  display: inline-flex; align-items: center; gap: 10px;
  padding: 16px 32px;
  border: 1px solid var(--sage-deep);
  font-size: 14px; font-weight: 500;
  color: var(--cream);
  transition: all 0.3s;
}}
.contact__link:hover {{
  background: var(--cream);
  color: var(--forest);
  border-color: var(--cream);
}}

/* ===== FOOTER ===== */
.footer {{
  padding: 28px 0;
  text-align: center;
  font-size: 12px; color: var(--muted);
  letter-spacing: 0.05em;
  border-top: 1px solid var(--line);
}}

/* ===== DIVIDER ===== */
.divider {{
  width: 60px; height: 1px;
  background: var(--terracotta);
  margin: 40px 0;
}}
.divider--center {{ margin: 40px auto; }}

/* ===== INGREDIENTS FULL BLEED ===== */
.ingredients-image {{
  width: 100%;
  margin-top: 48px;
  border: 1px solid var(--line);
}}

/* ===== ANIMATIONS ===== */
.reveal {{
  opacity: 0;
  transform: translateY(28px);
  transition: opacity 0.7s ease, transform 0.7s ease;
}}
.reveal.visible {{
  opacity: 1;
  transform: none;
}}

/* ===== RESPONSIVE ===== */
@media (max-width: 900px) {{
  .hero {{
    grid-template-columns: 1fr;
  }}
  .hero__content {{
    padding: 60px 32px 40px;
    order: 2;
  }}
  .hero__image {{
    min-height: 360px;
    order: 1;
  }}
  .product {{
    grid-template-columns: 1fr;
  }}
  .product--reverse {{ direction: ltr; }}
  .product__info {{ padding: 40px 32px; }}
  .product__image {{ min-height: 320px; }}
  .ingredients-grid {{
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }}
  .story {{
    grid-template-columns: 1fr;
    gap: 40px;
  }}
  .story__image {{ max-width: 320px; }}
  .founder {{
    grid-template-columns: 1fr;
    gap: 40px;
  }}
  .founder__image img {{ max-width: 280px; }}
  .proof {{
    grid-template-columns: 1fr;
    gap: 32px;
  }}
  .geet {{
    grid-template-columns: 1fr;
    gap: 32px;
  }}
  .header__nav {{ display: none; }}
  .header__nav.open {{
    display: flex;
    flex-direction: column;
    position: absolute;
    top: 68px; left: 0; right: 0;
    background: var(--ivory);
    padding: 24px 32px;
    border-bottom: 1px solid var(--line);
    gap: 20px;
  }}
  .header__toggle {{ display: block; }}
  .section {{ padding: 64px 0; }}
}}

@media (max-width: 540px) {{
  .ingredients-grid {{
    grid-template-columns: 1fr;
  }}
  .contact__links {{
    flex-direction: column;
    align-items: center;
  }}
  .hero__title {{ font-size: 36px; }}
}}

@media (prefers-reduced-motion: reduce) {{
  *, *::before, *::after {{
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }}
  .reveal {{ opacity: 1; transform: none; }}
}}

/* ===== FOCUS ===== */
:focus-visible {{
  outline: 2px solid var(--terracotta);
  outline-offset: 3px;
}}
</style>
</head>
<body>

<!-- ===== HEADER ===== -->
<header class="header" id="top">
  <div class="header__inner">
    <a href="#top" class="header__logo">Opper</a>
    <nav class="header__nav" id="nav">
      <a href="#collection" class="header__link">Collection</a>
      <a href="#ingredients" class="header__link">Ingredients</a>
      <a href="#story" class="header__link">Our Story</a>
      <a href="#gifting" class="header__link">Gifting</a>
      <a href="#contact" class="header__link">Contact</a>
    </nav>
    <button class="header__toggle" id="menuToggle" aria-label="Toggle navigation">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<!-- ===== HERO ===== -->
<section class="hero">
  <div class="hero__content">
    <p class="hero__label">Handcrafted Organic Skincare</p>
    <h1 class="hero__title">Pure by nature.<br><em>Made with care.</em></h1>
    <p class="hero__desc">Organic soap handcrafted with goat milk, saffron, ayurvedic herbs and nourishing oils. Natural, chemical-free skincare made in small batches.</p>
    <div>
      <a href="#collection" class="btn btn--primary">Explore the Collection</a>
      <a href="#contact" class="btn btn--outline">Enquire</a>
    </div>
  </div>
  <div class="hero__image">
    <img src="{IMG_SOAP_BOX}" alt="OPPER handcrafted soaps with branded packaging on a marble tray" loading="eager" width="640" height="640">
  </div>
</section>

<!-- ===== COLLECTION ===== -->
<section class="section" id="collection">
  <div class="container reveal">
    <p class="section__label">The Collection</p>
    <h2 class="section__title">Skincare rooted in nature, built by hand.</h2>
    <p class="section__desc">Every OPPER bar is a small-batch creation, cold processed to retain the natural goodness of its ingredients.</p>
  </div>
</section>

<!-- Product 1: Flagship -->
<div class="product reveal">
  <div class="product__image">
    <img src="{IMG_PREMIUM_BAR}" alt="OPPER Premium Goat Milk and Saffron Bathing Bar with branded packaging" loading="lazy">
  </div>
  <div class="product__info">
    <p class="product__tag">Flagship</p>
    <h3 class="product__name">Goat Milk &amp; Saffron Bathing Bar</h3>
    <p class="product__desc">The signature OPPER bar — a luxurious blend of goat milk and Kashmiri saffron, cold processed with coconut oil, olive oil, almond oil, aloe vera extract, pure shea butter and essential oils.</p>
    <div class="product__badges">
      <span class="badge">SLS Free</span>
      <span class="badge">Paraben Free</span>
      <span class="badge">Toxin Free</span>
      <span class="badge">Handcrafted</span>
    </div>
    <ul class="product__features">
      <li>Cleanses deeply without stripping natural moisture</li>
      <li>Nourishes and hydrates for soft, healthy skin</li>
      <li>Rich in antioxidants and vitamins</li>
      <li>Free from harsh chemicals and synthetic additives</li>
    </ul>
    <a href="#contact" class="btn btn--primary">Enquire About This Product</a>
  </div>
</div>

<!-- Product 2: Carrot & Shea Butter -->
<div class="product product--reverse reveal">
  <div class="product__image">
    <img src="{IMG_SOAPS_TRAY}" alt="OPPER handcrafted soaps displayed on a marble tray" loading="lazy">
  </div>
  <div class="product__info" style="background: var(--cream);">
    <p class="product__tag">New in the Range</p>
    <h3 class="product__name">Carrot &amp; Shea Butter Bathing Bar</h3>
    <p class="product__desc">Enriched with shea butter for deep nourishment and a smooth, hydrated feel. Gentle on all skin types, including sensitive skin.</p>
    <ul class="product__features">
      <li>Enriched with shea butter for deep hydration</li>
      <li>Gentle on all skin types</li>
      <li>Cold process method retains natural goodness</li>
      <li>No synthetic fragrances, colours or preservatives</li>
    </ul>
    <a href="#contact" class="btn btn--primary">Enquire About This Product</a>
  </div>
</div>

<!-- Product 3: Gift Combos -->
<div class="product reveal">
  <div class="product__image">
    <img src="{IMG_GIFT_BOX}" alt="OPPER gift box containing handcrafted soaps and accessories" loading="lazy">
  </div>
  <div class="product__info">
    <p class="product__tag">Gifting</p>
    <h3 class="product__name">Gift Combinations</h3>
    <p class="product__desc">OPPER soaps are available as curated gift combinations — perfect for birthdays, festivals, return gifts and special occasions. Customised hampers are also available.</p>
    <ul class="product__features">
      <li>Curated gift boxes with handcrafted soaps</li>
      <li>Perfect for festivals and special occasions</li>
      <li>Customised hampers available on request</li>
    </ul>
    <a href="#contact" class="btn btn--primary">Enquire About Gifting</a>
  </div>
</div>

<!-- ===== INGREDIENTS ===== -->
<section class="section section--sage" id="ingredients">
  <div class="container">
    <div class="reveal">
      <p class="section__label">What Goes In</p>
      <h2 class="section__title">Ingredients you can trust.</h2>
      <p class="section__desc">Every OPPER bar is a blend of carefully chosen natural ingredients — no synthetics, no shortcuts.</p>
    </div>

    <div class="ingredients-grid reveal">
      <div class="ingredient">
        <span class="ingredient__icon" aria-hidden="true">🥛</span>
        <h4 class="ingredient__name">Fresh Goat Milk</h4>
        <p class="ingredient__desc">Rich in vitamins and minerals, naturally moisturising and gentle on sensitive skin.</p>
      </div>
      <div class="ingredient">
        <span class="ingredient__icon" aria-hidden="true">🌸</span>
        <h4 class="ingredient__name">Kashmiri Saffron</h4>
        <p class="ingredient__desc">Prized in ayurvedic tradition for its antioxidant properties and warm, natural radiance.</p>
      </div>
      <div class="ingredient">
        <span class="ingredient__icon" aria-hidden="true">🌿</span>
        <h4 class="ingredient__name">Ayurvedic Herbs</h4>
        <p class="ingredient__desc">Aloe vera extract, matcha extract and plant-based ingredients for soothing, balanced care.</p>
      </div>
      <div class="ingredient">
        <span class="ingredient__icon" aria-hidden="true">🥥</span>
        <h4 class="ingredient__name">Nourishing Oils</h4>
        <p class="ingredient__desc">Coconut oil, olive oil, almond oil, shea butter and essential oils, cold pressed to retain their natural goodness.</p>
      </div>
    </div>

    <img src="{IMG_INGREDIENTS}" alt="Detailed ingredient breakdown and benefits of OPPER organic soap" class="ingredients-image reveal" loading="lazy">
  </div>
</section>

<!-- ===== OUR STORY ===== -->
<section class="section" id="story">
  <div class="container">
    <div class="story reveal">
      <div class="story__image">
        <img src="{IMG_FOUNDER}" alt="Geetha, founder of OPPER" loading="lazy">
      </div>
      <div>
        <p class="section__label">Our Story</p>
        <h2 class="section__title">A brand born from purpose.</h2>
        <p class="section__desc">OPPER began with Geetha's simple wish — to build something of her own, rooted in purity and care. As a working professional and mother, she turned a personal passion for natural ingredients into a brand that today serves over 500 customers.</p>
        <blockquote>"Take care of your body. It's the only place you have to live in."</blockquote>
        <div class="divider"></div>
        <p class="founder__text" style="font-size: 14px;">Every relationship earned offline, through word of mouth. No paid ads — just trust, quality, and genuine care.</p>
      </div>
    </div>
  </div>
</section>

<!-- ===== CREDIBILITY ===== -->
<section class="section section--forest">
  <div class="container">
    <div class="proof reveal">
      <div>
        <p class="section__label">Our Journey</p>
        <p class="proof__stat">500+</p>
        <p class="section__desc" style="margin-top: 16px;">customers and growing. Every relationship earned through quality, care and word of mouth.</p>
      </div>
      <div>
        <h3 style="font-size: 24px; margin-bottom: 8px; color: var(--cream);">Recognition</h3>
        <ul class="proof__awards" style="list-style: none;">
          <li>Startup Award — Adya Foundation</li>
          <li>Powerful Women Achiever Award — Anshu Foundation</li>
          <li>Women Power — Sri Adya and VWMCs</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ===== GEET GIFTING ===== -->
<section class="section section--cream" id="gifting">
  <div class="container">
    <div class="geet reveal">
      <div>
        <p class="section__label">Sister Brand</p>
        <h2 class="section__title">GEET — Feel the Love</h2>
        <p class="section__desc">Thoughtfulness meets sustainability. GEET creates eco-friendly, personalised gifting solutions for every occasion — spreading love while caring for our planet.</p>
        <div class="geet__tags">
          <span class="geet__tag">Eco-Friendly</span>
          <span class="geet__tag">Personalised</span>
          <span class="geet__tag">Corporate Gifting</span>
          <span class="geet__tag">Made in India</span>
        </div>
        <a href="#contact" class="btn btn--primary">Enquire About Gifting</a>
      </div>
      <div class="geet__image">
        <img src="{IMG_GEET}" alt="GEET personalised jute bag, gift box and wooden mug" loading="lazy">
      </div>
    </div>
  </div>
</section>

<!-- ===== CONTACT ===== -->
<section class="section section--forest" id="contact">
  <div class="container contact reveal">
    <p class="section__label">Get in Touch</p>
    <h2 class="section__title" style="margin: 0 auto 16px; max-width: none;">Let's create something beautiful together.</h2>
    <p class="section__desc" style="margin: 0 auto;">For product enquiries, gifting, partnerships or bulk orders — reach out directly.</p>
    <div class="contact__links">
      <a href="tel:+919008473680" class="contact__link">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        9008473680
      </a>
      <a href="mailto:Opper_naturals@gmail.com" class="contact__link">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="4" width="20" height="16" rx="2"/><polyline points="22,7 12,13 2,7"/></svg>
        Opper_naturals@gmail.com
      </a>
      <a href="https://www.instagram.com/opper_naturals" target="_blank" rel="noopener" class="contact__link">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="5"/><circle cx="17.5" cy="6.5" r="1.5" fill="currentColor" stroke="none"/></svg>
        @opper_naturals
      </a>
    </div>
  </div>
</section>

<!-- ===== FOOTER ===== -->
<footer class="footer">
  <p>&copy; OPPER Organic Soap &amp; Skincare &middot; Pure by Nature, Made with Care</p>
</footer>

<!-- ===== SCRIPTS ===== -->
<script>
// Sticky header shadow
const header = document.querySelector('.header');
window.addEventListener('scroll', () => {{
  header.classList.toggle('scrolled', window.scrollY > 10);
}}, {{ passive: true }});

// Mobile menu toggle
const toggle = document.getElementById('menuToggle');
const nav = document.getElementById('nav');
toggle.addEventListener('click', () => {{
  nav.classList.toggle('open');
}});

// Close mobile menu on link click
nav.querySelectorAll('a').forEach(a => {{
  a.addEventListener('click', () => {{
    nav.classList.remove('open');
  }});
}});

// Reveal on scroll
const reveals = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver((entries) => {{
  entries.forEach(entry => {{
    if (entry.isIntersecting) {{
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }}
  }});
}}, {{ threshold: 0.1, rootMargin: '0px 0px -40px 0px' }});
reveals.forEach(el => observer.observe(el));
</script>

</body>
</html>'''

with open('opper-redesign.html', 'w') as f:
    f.write(html)

print("Done! Written to opper-redesign.html")
print(f"File size: {len(html)} bytes")
