#!/usr/bin/env python3
"""
OPPER Luxury Brand Portfolio Builder
Generates a world-class, editorial artisan skincare brand portfolio.
Extracts high-resolution base64 images from the existing HTML files and outputs
a unified, standalone index.html and opper-redesign.html.
"""

import re
import os

# Read the source HTML to extract base64 images
with open('OPPER · Organic Soap & Skincare — Portfolio.html', 'r') as f:
    source = f.read()

# Extract unique images by alt text
imgs = re.findall(r'src="(data:image/[^"]+)"[^>]*alt="([^"]*)"', source)
image_map = {}
for src, alt in imgs:
    if alt and alt not in image_map:
        image_map[alt] = src

IMG_LOGO = image_map.get('OPPER logo: milk splash, saffron flower and gold ring', '')
IMG_SOAPS_TRAY = image_map.get('Handcrafted OPPER soaps on a marble tray', '')
IMG_SOAP_BOX = image_map.get('OPPER soap box with peach and cream bars', '')
IMG_GIFT_BOX = image_map.get('OPPER gift box with soaps and tags', '')
IMG_PREMIUM_BAR = image_map.get('OPPER Premium Goat Milk and Saffron Bathing Bar box', '')
IMG_INGREDIENTS = image_map.get('Welcome to Opper World: ingredients and benefits of OPPER organic soap', '')
IMG_FOUNDER = image_map.get('Geetha, founder of OPPER', '')
IMG_GEET = image_map.get('GEET personalised jute bag, gift box and wooden mug', '')

html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>OPPER · Artisanal Organic Soap &amp; Skincare — Brand Portfolio</title>
  <meta name="description" content="OPPER is an artisan skincare house formulating cold-processed organic soaps with fresh goat milk, Kashmiri saffron, cold-pressed botanicals, and Ayurvedic herbs. Founded by Geetha.">
  <meta name="keywords" content="OPPER, organic soap, goat milk soap, saffron soap, cold process soap, artisan skincare, chemical-free skincare, Geetha founder, GEET gifting">
  <meta name="author" content="OPPER Skincare">
  <meta property="og:title" content="OPPER · Artisanal Organic Soap &amp; Skincare">
  <meta property="og:description" content="Pure by nature. Made with care. Small-batch cold-processed organic skincare crafted with fresh goat milk and Kashmiri saffron.">
  <meta property="og:type" content="website">

  <!-- Typography: Playfair Display & Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <style>
    /* ==========================================================================
       DESIGN TOKENS & CSS VARIABLES
       ========================================================================== */
    :root {{
      --bg-cream: #FAF7F2;
      --bg-surface: #FFFFFF;
      --bg-surface-tint: #F4EFE6;
      --bg-sage: #E8EFE3;
      --bg-sage-soft: #F0F5EC;
      
      --c-forest: #1E3024;
      --c-forest-deep: #142219;
      --c-forest-muted: #2E4535;
      
      --c-saffron: #C27344;
      --c-saffron-light: #DF8958;
      --c-saffron-soft: #FBF0E8;
      
      --c-gold: #B88E3E;
      --c-gold-light: #D4AE5E;
      --c-gold-soft: #F8F3E6;
      
      --c-ink: #181D19;
      --c-ink-light: #333C35;
      --c-muted: #677168;
      --c-border: #E4DCD0;
      --c-border-light: #EFE9DE;
      
      --font-serif: 'Playfair Display', Georgia, serif;
      --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      
      --shadow-sm: 0 2px 8px rgba(30, 48, 36, 0.04);
      --shadow-md: 0 8px 24px rgba(30, 48, 36, 0.06);
      --shadow-lg: 0 16px 40px rgba(30, 48, 36, 0.09);
      --shadow-xl: 0 24px 60px rgba(30, 48, 36, 0.12);
      
      --radius-sm: 4px;
      --radius-md: 8px;
      --radius-lg: 16px;
      --radius-full: 9999px;
      
      --transition-smooth: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    /* ==========================================================================
       RESET & BASE STYLES
       ========================================================================== */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    
    html {{
      scroll-behavior: smooth;
      scroll-padding-top: 80px;
      -webkit-text-size-adjust: 100%;
    }}

    body {{
      background-color: var(--bg-cream);
      color: var(--c-ink);
      font-family: var(--font-sans);
      font-size: 16px;
      line-height: 1.7;
      letter-spacing: -0.01em;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    img {{
      max-width: 100%;
      height: auto;
      display: block;
    }}

    a {{
      color: inherit;
      text-decoration: none;
      transition: var(--transition-smooth);
    }}

    button {{
      font-family: inherit;
      cursor: pointer;
      border: none;
      background: none;
    }}

    h1, h2, h3, h4, h5 {{
      font-family: var(--font-serif);
      font-weight: 500;
      line-height: 1.18;
      color: var(--c-forest);
      letter-spacing: -0.02em;
    }}

    /* Container Utility */
    .container {{
      width: 100%;
      max-width: 1240px;
      margin: 0 auto;
      padding: 0 28px;
    }}

    .container--narrow {{
      max-width: 960px;
    }}

    /* Section Spacing */
    .section {{
      padding: 110px 0;
      position: relative;
    }}

    .section--dense {{
      padding: 70px 0;
    }}

    /* ==========================================================================
       TOP ANNOUNCEMENT BAR
       ========================================================================== */
    .top-bar {{
      background: var(--c-forest-deep);
      color: var(--c-gold-soft);
      font-size: 11.5px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      font-weight: 500;
      padding: 10px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(194, 115, 68, 0.25);
    }}

    .top-bar__ticker {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .top-bar__bullet {{
      color: var(--c-saffron-light);
    }}

    .top-bar__links {{
      display: flex;
      align-items: center;
      gap: 20px;
    }}

    .top-bar__links a:hover {{
      color: #FFFFFF;
    }}

    /* ==========================================================================
       HEADER & NAVIGATION
       ========================================================================== */
    .header {{
      position: sticky;
      top: 0;
      z-index: 200;
      background: rgba(250, 247, 242, 0.94);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--c-border);
      transition: background 0.3s ease, box-shadow 0.3s ease;
    }}

    .header.scrolled {{
      background: rgba(255, 255, 255, 0.96);
      box-shadow: 0 4px 20px rgba(24, 29, 25, 0.06);
    }}

    .header__inner {{
      height: 78px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .header__brand {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .header__logo-img {{
      width: 44px;
      height: 44px;
      border-radius: 50%;
      object-fit: cover;
      box-shadow: 0 2px 8px rgba(0,0,0,0.08);
      border: 1px solid var(--c-gold-light);
    }}

    .header__brand-text {{
      display: flex;
      flex-direction: column;
    }}

    .header__brand-title {{
      font-family: var(--font-serif);
      font-size: 24px;
      letter-spacing: 0.16em;
      font-weight: 600;
      color: var(--c-forest);
      text-transform: uppercase;
      line-height: 1;
    }}

    .header__brand-subtitle {{
      font-size: 10px;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--c-saffron);
      font-weight: 600;
      margin-top: 3px;
    }}

    .header__nav {{
      display: flex;
      align-items: center;
      gap: 34px;
    }}

    .nav-link {{
      font-size: 13px;
      font-weight: 500;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--c-muted);
      position: relative;
      padding: 6px 0;
    }}

    .nav-link::after {{
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 0%;
      height: 1.5px;
      background: var(--c-forest);
      transition: width 0.3s ease;
    }}

    .nav-link:hover {{
      color: var(--c-forest);
    }}

    .nav-link:hover::after {{
      width: 100%;
    }}

    .header__actions {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    /* Mobile toggle */
    .menu-toggle {{
      display: none;
      flex-direction: column;
      gap: 5px;
      padding: 8px;
      cursor: pointer;
    }}

    .menu-toggle span {{
      display: block;
      width: 24px;
      height: 2px;
      background: var(--c-forest);
      transition: var(--transition-smooth);
    }}

    /* ==========================================================================
       BUTTONS & BADGES
       ========================================================================== */
    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      padding: 14px 30px;
      font-size: 12.5px;
      font-weight: 600;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      border-radius: var(--radius-sm);
      transition: var(--transition-smooth);
      position: relative;
      cursor: pointer;
    }}

    .btn--primary {{
      background: var(--c-forest);
      color: #FFFFFF;
      box-shadow: 0 4px 14px rgba(30, 48, 36, 0.2);
    }}

    .btn--primary:hover {{
      background: var(--c-forest-deep);
      transform: translateY(-2px);
      box-shadow: 0 8px 22px rgba(30, 48, 36, 0.3);
    }}

    .btn--saffron {{
      background: var(--c-saffron);
      color: #FFFFFF;
      box-shadow: 0 4px 14px rgba(194, 115, 68, 0.25);
    }}

    .btn--saffron:hover {{
      background: #AA6135;
      transform: translateY(-2px);
      box-shadow: 0 8px 22px rgba(194, 115, 68, 0.35);
    }}

    .btn--outline {{
      border: 1px solid var(--c-forest);
      color: var(--c-forest);
      background: transparent;
    }}

    .btn--outline:hover {{
      background: var(--c-forest);
      color: #FFFFFF;
      transform: translateY(-2px);
    }}

    .btn--outline-light {{
      border: 1px solid rgba(255, 255, 255, 0.4);
      color: #FFFFFF;
      background: transparent;
    }}

    .btn--outline-light:hover {{
      background: #FFFFFF;
      color: var(--c-forest);
      border-color: #FFFFFF;
      transform: translateY(-2px);
    }}

    .btn--sm {{
      padding: 9px 18px;
      font-size: 11px;
    }}

    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      border-radius: var(--radius-full);
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }}

    .badge--forest {{
      background: rgba(30, 48, 36, 0.08);
      color: var(--c-forest);
      border: 1px solid rgba(30, 48, 36, 0.15);
    }}

    .badge--saffron {{
      background: var(--c-saffron-soft);
      color: var(--c-saffron);
      border: 1px solid rgba(194, 115, 68, 0.2);
    }}

    .badge--gold {{
      background: var(--c-gold-soft);
      color: var(--c-gold);
      border: 1px solid rgba(184, 142, 62, 0.3);
    }}

    /* ==========================================================================
       HERO SECTION
       ========================================================================== */
    .hero {{
      padding: 60px 0 90px;
      position: relative;
      overflow: hidden;
    }}

    .hero__grid {{
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      gap: 64px;
      align-items: center;
    }}

    .hero__eyebrow {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 22px;
    }}

    .hero__title {{
      font-size: clamp(42px, 5vw, 68px);
      line-height: 1.08;
      color: var(--c-forest);
      margin-bottom: 24px;
      font-weight: 500;
    }}

    .hero__title em {{
      font-style: italic;
      color: var(--c-saffron);
      font-family: var(--font-serif);
      font-weight: 400;
    }}

    .hero__lead {{
      font-size: 18px;
      line-height: 1.7;
      color: var(--c-muted);
      margin-bottom: 38px;
      max-width: 530px;
    }}

    .hero__actions {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 16px;
      margin-bottom: 48px;
    }}

    .hero__trust-strip {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
      padding-top: 32px;
      border-top: 1px solid var(--c-border);
    }}

    .trust-item {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .trust-item__val {{
      font-family: var(--font-serif);
      font-size: 19px;
      font-weight: 600;
      color: var(--c-forest);
      line-height: 1.2;
    }}

    .trust-item__lbl {{
      font-size: 11px;
      color: var(--c-muted);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-weight: 500;
    }}

    /* Hero Visual Showcase */
    .hero__visual {{
      position: relative;
    }}

    .hero__image-frame {{
      position: relative;
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-xl);
      background: var(--bg-surface);
      border: 1px solid var(--c-border);
    }}

    .hero__image-frame img {{
      width: 100%;
      height: 540px;
      object-fit: cover;
      transition: transform 0.8s ease;
    }}

    .hero__image-frame:hover img {{
      transform: scale(1.02);
    }}

    .hero__floating-card {{
      position: absolute;
      bottom: -24px;
      left: -24px;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(12px);
      padding: 18px 24px;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-lg);
      border: 1px solid var(--c-border);
      max-width: 260px;
    }}

    .hero__floating-card-tag {{
      font-size: 10px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--c-saffron);
      font-weight: 700;
      margin-bottom: 4px;
    }}

    .hero__floating-card-title {{
      font-family: var(--font-serif);
      font-size: 16px;
      color: var(--c-forest);
      font-weight: 600;
    }}

    .hero__floating-stamp {{
      position: absolute;
      top: -18px;
      right: -18px;
      width: 90px;
      height: 90px;
      background: var(--c-forest);
      color: var(--c-gold-soft);
      border-radius: 50%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      font-size: 9px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      font-weight: 600;
      box-shadow: var(--shadow-md);
      border: 2px dashed rgba(184, 142, 62, 0.4);
    }}

    /* ==========================================================================
       MARQUEE TICKER (MANIFIESTO)
       ========================================================================== */
    .marquee {{
      background: var(--c-forest);
      color: var(--c-gold-soft);
      padding: 16px 0;
      overflow: hidden;
      white-space: nowrap;
      position: relative;
    }}

    .marquee__track {{
      display: inline-flex;
      align-items: center;
      gap: 32px;
      animation: marqueeAnimation 28s linear infinite;
    }}

    .marquee__item {{
      font-family: var(--font-serif);
      font-size: 15px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      display: inline-flex;
      align-items: center;
      gap: 24px;
    }}

    .marquee__symbol {{
      color: var(--c-saffron-light);
      font-size: 12px;
    }}

    @keyframes marqueeAnimation {{
      0% {{ transform: translateX(0); }}
      100% {{ transform: translateX(-50%); }}
    }}

    /* ==========================================================================
       SECTION HEADINGS
       ========================================================================== */
    .section-header {{
      text-align: center;
      max-width: 680px;
      margin: 0 auto 64px;
    }}

    .section-header--left {{
      text-align: left;
      margin-left: 0;
    }}

    .section-tag {{
      display: inline-block;
      font-size: 11px;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--c-saffron);
      font-weight: 700;
      margin-bottom: 12px;
    }}

    .section-title {{
      font-size: clamp(32px, 3.8vw, 48px);
      color: var(--c-forest);
      margin-bottom: 16px;
    }}

    .section-desc {{
      font-size: 16px;
      color: var(--c-muted);
      line-height: 1.7;
    }}

    /* ==========================================================================
       PRODUCT SHOWCASE & COLLECTION
       ========================================================================== */
    .collection-tabs {{
      display: flex;
      justify-content: center;
      gap: 12px;
      margin-bottom: 48px;
      flex-wrap: wrap;
    }}

    .tab-btn {{
      padding: 10px 22px;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-full);
      color: var(--c-muted);
      background: var(--bg-surface);
      transition: var(--transition-smooth);
    }}

    .tab-btn.active, .tab-btn:hover {{
      background: var(--c-forest);
      color: #FFFFFF;
      border-color: var(--c-forest);
    }}

    /* Editorial Product Card */
    .product-card {{
      background: var(--bg-surface);
      border: 1px solid var(--c-border);
      border-radius: var(--radius-md);
      overflow: hidden;
      margin-bottom: 48px;
      box-shadow: var(--shadow-sm);
      transition: var(--transition-smooth);
    }}

    .product-card:hover {{
      box-shadow: var(--shadow-lg);
      border-color: var(--c-saffron-light);
    }}

    .product-card__inner {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      align-items: stretch;
    }}

    .product-card--reverse .product-card__inner {{
      direction: rtl;
    }}

    .product-card--reverse .product-card__inner > * {{
      direction: ltr;
    }}

    .product-card__gallery {{
      position: relative;
      overflow: hidden;
      min-height: 460px;
      background: #F2EDE4;
      cursor: zoom-in;
    }}

    .product-card__gallery img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .product-card:hover .product-card__gallery img {{
      transform: scale(1.03);
    }}

    .product-card__overlay-badge {{
      position: absolute;
      top: 20px;
      left: 20px;
      z-index: 2;
    }}

    .product-card__details {{
      padding: 56px 48px;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}

    .product-card__category {{
      font-size: 11px;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--c-saffron);
      font-weight: 700;
      margin-bottom: 10px;
    }}

    .product-card__title {{
      font-size: clamp(28px, 2.8vw, 36px);
      color: var(--c-forest);
      margin-bottom: 16px;
    }}

    .product-card__summary {{
      font-size: 15px;
      color: var(--c-muted);
      line-height: 1.7;
      margin-bottom: 24px;
    }}

    /* Formula Pill Badges */
    .formula-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 26px;
    }}

    .formula-pill {{
      font-size: 11px;
      letter-spacing: 0.06em;
      padding: 5px 12px;
      border-radius: var(--radius-sm);
      background: var(--bg-sage-soft);
      color: var(--c-forest);
      font-weight: 600;
      border: 1px solid rgba(46, 69, 53, 0.15);
    }}

    /* Key Spec Accordion / List */
    .product-specs {{
      border-top: 1px solid var(--c-border-light);
      margin-bottom: 32px;
    }}

    .product-spec-row {{
      display: flex;
      padding: 10px 0;
      border-bottom: 1px solid var(--c-border-light);
      font-size: 13.5px;
    }}

    .product-spec-label {{
      width: 140px;
      font-weight: 600;
      color: var(--c-forest);
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 0.1em;
      padding-top: 2px;
    }}

    .product-spec-value {{
      flex: 1;
      color: var(--c-ink-light);
    }}

    .product-card__actions {{
      display: flex;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
    }}

    /* ==========================================================================
       INGREDIENTS & ALCHEMY CODEX
       ========================================================================== */
    .ingredients-section {{
      background: var(--bg-surface-tint);
      border-top: 1px solid var(--c-border);
      border-bottom: 1px solid var(--c-border);
    }}

    .ingredients-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 24px;
      margin-bottom: 56px;
    }}

    .ingredient-card {{
      background: var(--bg-surface);
      border: 1px solid var(--c-border);
      border-radius: var(--radius-md);
      padding: 32px 24px;
      text-align: center;
      transition: var(--transition-smooth);
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    .ingredient-card:hover {{
      transform: translateY(-4px);
      box-shadow: var(--shadow-md);
      border-color: var(--c-saffron-light);
    }}

    .ingredient-card__icon {{
      width: 58px;
      height: 58px;
      border-radius: 50%;
      background: var(--bg-sage-soft);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 26px;
      margin-bottom: 20px;
      border: 1px solid rgba(46, 69, 53, 0.15);
    }}

    .ingredient-card__name {{
      font-size: 19px;
      color: var(--c-forest);
      margin-bottom: 8px;
      font-family: var(--font-serif);
      font-weight: 600;
    }}

    .ingredient-card__role {{
      font-size: 10.5px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--c-saffron);
      font-weight: 700;
      margin-bottom: 12px;
    }}

    .ingredient-card__desc {{
      font-size: 13.5px;
      color: var(--c-muted);
      line-height: 1.65;
    }}

    /* Big Infographic Banner */
    .codex-banner {{
      background: #FFFFFF;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-md);
      cursor: zoom-in;
      position: relative;
    }}

    .codex-banner img {{
      width: 100%;
      display: block;
    }}

    .codex-banner__zoom-hint {{
      position: absolute;
      bottom: 20px;
      right: 20px;
      background: rgba(24, 29, 25, 0.85);
      backdrop-filter: blur(8px);
      color: #FFFFFF;
      padding: 8px 16px;
      border-radius: var(--radius-full);
      font-size: 11px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    /* ==========================================================================
       OUR ARTISAN CRAFT / 4-STEP TIMELINE
       ========================================================================== */
    .craft-timeline {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 24px;
      margin-top: 48px;
      position: relative;
    }}

    .craft-step {{
      background: var(--bg-surface);
      border: 1px solid var(--c-border);
      border-radius: var(--radius-md);
      padding: 32px 24px;
      position: relative;
    }}

    .craft-step__num {{
      font-family: var(--font-serif);
      font-size: 38px;
      color: var(--c-saffron);
      line-height: 1;
      margin-bottom: 16px;
      font-weight: 400;
    }}

    .craft-step__title {{
      font-size: 18px;
      color: var(--c-forest);
      margin-bottom: 10px;
      font-weight: 600;
    }}

    .craft-step__text {{
      font-size: 13.5px;
      color: var(--c-muted);
      line-height: 1.65;
    }}

    /* ==========================================================================
       FOUNDER STORY & AWARDS
       ========================================================================== */
    .story-section {{
      background: var(--c-forest);
      color: var(--bg-cream);
      position: relative;
      overflow: hidden;
    }}

    .story-grid {{
      display: grid;
      grid-template-columns: 0.9fr 1.1fr;
      gap: 72px;
      align-items: center;
    }}

    .story-visual {{
      position: relative;
    }}

    .story-visual__frame {{
      position: relative;
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.15);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3);
    }}

    .story-visual__frame img {{
      width: 100%;
      height: 520px;
      object-fit: cover;
      object-position: top center;
    }}

    .story-visual__badge {{
      position: absolute;
      bottom: -20px;
      right: -20px;
      background: var(--c-saffron);
      color: #FFFFFF;
      padding: 16px 22px;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-lg);
      font-family: var(--font-serif);
      font-size: 16px;
      text-align: center;
      line-height: 1.25;
    }}

    .story-visual__badge span {{
      display: block;
      font-size: 10px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      font-family: var(--font-sans);
      opacity: 0.9;
      margin-top: 4px;
    }}

    .story-content .section-tag {{
      color: var(--c-gold-light);
    }}

    .story-content .section-title {{
      color: #FFFFFF;
      margin-bottom: 24px;
    }}

    .story-quote {{
      font-family: var(--font-serif);
      font-size: clamp(20px, 2.2vw, 26px);
      font-style: italic;
      color: var(--c-gold-soft);
      line-height: 1.45;
      padding-left: 24px;
      border-left: 2px solid var(--c-saffron-light);
      margin: 28px 0;
    }}

    .story-body {{
      font-size: 15.5px;
      line-height: 1.8;
      color: #D3DDD5;
      margin-bottom: 36px;
    }}

    /* Awards Grid inside Story */
    .awards-list {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      padding-top: 28px;
      border-top: 1px solid rgba(255, 255, 255, 0.15);
    }}

    .award-card {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-sm);
      padding: 16px;
    }}

    .award-card__trophy {{
      font-size: 20px;
      margin-bottom: 8px;
      display: block;
    }}

    .award-card__title {{
      font-size: 13px;
      font-weight: 600;
      color: #FFFFFF;
      margin-bottom: 4px;
      line-height: 1.3;
    }}

    .award-card__org {{
      font-size: 11px;
      color: var(--c-gold-light);
      letter-spacing: 0.05em;
    }}

    /* ==========================================================================
       GEET SUSTAINABLE GIFTING (SISTER BRAND)
       ========================================================================== */
    .geet-section {{
      background: #FFFFFF;
    }}

    .geet-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 64px;
      align-items: center;
    }}

    .geet-content .section-tag {{
      color: var(--c-forest);
    }}

    .geet-features {{
      list-style: none;
      margin: 28px 0 36px;
    }}

    .geet-features li {{
      padding: 10px 0;
      border-bottom: 1px solid var(--c-border-light);
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 14.5px;
      color: var(--c-ink-light);
    }}

    .geet-features li::before {{
      content: '✔';
      color: var(--c-forest);
      font-weight: 700;
    }}

    .geet-visual {{
      position: relative;
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--c-border);
      box-shadow: var(--shadow-lg);
    }}

    .geet-visual img {{
      width: 100%;
      height: 480px;
      object-fit: cover;
    }}

    /* ==========================================================================
       CLIENT REVIEWS & COMMUNITY LOVE
       ========================================================================== */
    .reviews-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
      margin-top: 48px;
    }}

    .review-card {{
      background: var(--bg-surface);
      border: 1px solid var(--c-border);
      border-radius: var(--radius-md);
      padding: 32px 28px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .review-stars {{
      color: var(--c-gold);
      font-size: 14px;
      margin-bottom: 16px;
      letter-spacing: 2px;
    }}

    .review-text {{
      font-size: 14.5px;
      line-height: 1.7;
      color: var(--c-ink-light);
      margin-bottom: 20px;
      font-style: italic;
    }}

    .review-author {{
      display: flex;
      align-items: center;
      gap: 12px;
      border-top: 1px solid var(--c-border-light);
      padding-top: 16px;
    }}

    .review-avatar {{
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: var(--bg-sage);
      color: var(--c-forest);
      font-weight: 700;
      font-size: 13px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .review-author-info {{
      line-height: 1.3;
    }}

    .review-name {{
      font-weight: 600;
      font-size: 13.5px;
      color: var(--c-forest);
    }}

    .review-loc {{
      font-size: 11px;
      color: var(--c-muted);
    }}

    /* ==========================================================================
       CONTACT, WHOLESALE & ORDER INQUIRY
       ========================================================================== */
    .contact-section {{
      background: var(--c-forest-deep);
      color: #FFFFFF;
      position: relative;
    }}

    .contact-box {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-lg);
      padding: 64px 48px;
      text-align: center;
      max-width: 860px;
      margin: 0 auto;
      box-shadow: var(--shadow-xl);
    }}

    .contact-title {{
      font-size: clamp(32px, 3.5vw, 46px);
      color: #FFFFFF;
      margin-bottom: 16px;
    }}

    .contact-subtitle {{
      font-size: 16px;
      color: var(--bg-sage);
      max-width: 540px;
      margin: 0 auto 40px;
      line-height: 1.7;
    }}

    .contact-channels {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin-bottom: 40px;
    }}

    .channel-card {{
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: var(--radius-md);
      padding: 24px 20px;
      text-align: center;
      transition: var(--transition-smooth);
    }}

    .channel-card:hover {{
      background: rgba(255, 255, 255, 0.12);
      border-color: var(--c-saffron-light);
      transform: translateY(-3px);
    }}

    .channel-icon {{
      font-size: 26px;
      margin-bottom: 12px;
      display: inline-block;
    }}

    .channel-label {{
      font-size: 11px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--c-gold-light);
      font-weight: 600;
      margin-bottom: 6px;
    }}

    .channel-val {{
      font-size: 15px;
      font-weight: 600;
      color: #FFFFFF;
      word-break: break-all;
    }}

    /* ==========================================================================
       FOOTER
       ========================================================================== */
    .footer {{
      background: #0E1711;
      color: #8E9B90;
      padding: 60px 0 32px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      font-size: 13px;
    }}

    .footer__top {{
      display: grid;
      grid-template-columns: 1.2fr 0.8fr 1fr;
      gap: 48px;
      margin-bottom: 48px;
    }}

    .footer__brand-title {{
      font-family: var(--font-serif);
      font-size: 24px;
      color: #FFFFFF;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      margin-bottom: 10px;
    }}

    .footer__tagline {{
      font-size: 14px;
      color: var(--c-gold-light);
      margin-bottom: 18px;
      font-style: italic;
    }}

    .footer__col-title {{
      font-size: 11.5px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: #FFFFFF;
      font-weight: 600;
      margin-bottom: 18px;
    }}

    .footer__links {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .footer__links a:hover {{
      color: #FFFFFF;
    }}

    .footer__bottom {{
      padding-top: 28px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      font-size: 12px;
    }}

    /* ==========================================================================
       FLOATING WHATSAPP PILL & QUICK INQUIRY MODAL
       ========================================================================== */
    .floating-cta {{
      position: fixed;
      bottom: 28px;
      right: 28px;
      z-index: 150;
      display: flex;
      align-items: center;
      gap: 10px;
      background: #25D366;
      color: #FFFFFF;
      padding: 13px 22px;
      border-radius: var(--radius-full);
      font-size: 13px;
      font-weight: 600;
      letter-spacing: 0.04em;
      box-shadow: 0 8px 24px rgba(37, 211, 102, 0.35);
      transition: var(--transition-smooth);
    }}

    .floating-cta:hover {{
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 12px 30px rgba(37, 211, 102, 0.45);
      color: #FFFFFF;
    }}

    .floating-cta svg {{
      width: 20px;
      height: 20px;
      fill: currentColor;
    }}

    /* Modal Overlay */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(14, 23, 17, 0.8);
      backdrop-filter: blur(8px);
      z-index: 300;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
      opacity: 0;
      transition: opacity 0.3s ease;
    }}

    .modal-overlay.active {{
      display: flex;
      opacity: 1;
    }}

    .modal-card {{
      background: #FFFFFF;
      width: 100%;
      max-width: 580px;
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-xl);
      border: 1px solid var(--c-border);
      position: relative;
      animation: modalSlideUp 0.35s ease;
    }}

    @keyframes modalSlideUp {{
      from {{ transform: translateY(24px); opacity: 0; }}
      to {{ transform: translateY(0); opacity: 1; }}
    }}

    .modal-header {{
      background: var(--c-forest);
      color: #FFFFFF;
      padding: 24px 28px;
      position: relative;
    }}

    .modal-title {{
      font-size: 22px;
      color: #FFFFFF;
      margin-bottom: 4px;
    }}

    .modal-subtitle {{
      font-size: 12px;
      color: var(--c-gold-soft);
      letter-spacing: 0.05em;
    }}

    .modal-close {{
      position: absolute;
      top: 20px;
      right: 20px;
      color: #FFFFFF;
      font-size: 22px;
      line-height: 1;
      padding: 4px 8px;
      cursor: pointer;
    }}

    .modal-body {{
      padding: 28px;
    }}

    .form-group {{
      margin-bottom: 18px;
    }}

    .form-label {{
      display: block;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--c-forest);
      margin-bottom: 6px;
    }}

    .form-input, .form-select, .form-textarea {{
      width: 100%;
      padding: 12px 14px;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-sm);
      font-family: inherit;
      font-size: 14px;
      background: var(--bg-cream);
      color: var(--c-ink);
      transition: border-color 0.2s ease;
    }}

    .form-input:focus, .form-select:focus, .form-textarea:focus {{
      outline: none;
      border-color: var(--c-saffron);
      background: #FFFFFF;
    }}

    .form-textarea {{
      resize: vertical;
      min-height: 80px;
    }}

    /* Lightbox Modal for Full Images */
    .lightbox-modal {{
      position: fixed;
      inset: 0;
      background: rgba(14, 23, 17, 0.95);
      z-index: 400;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 30px;
      cursor: zoom-out;
    }}

    .lightbox-modal.active {{
      display: flex;
    }}

    .lightbox-img {{
      max-width: 90vw;
      max-height: 88vh;
      object-fit: contain;
      border-radius: var(--radius-sm);
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
    }}

    /* ==========================================================================
       RESPONSIVE BREAKPOINTS
       ========================================================================== */
    @media (max-width: 1024px) {{
      .hero__grid {{
        grid-template-columns: 1fr;
        gap: 48px;
      }}
      .hero__visual {{
        max-width: 580px;
        margin: 0 auto;
      }}
      .story-grid {{
        grid-template-columns: 1fr;
        gap: 48px;
      }}
      .story-visual__frame img {{
        height: 420px;
      }}
      .ingredients-grid, .craft-timeline {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .geet-grid {{
        grid-template-columns: 1fr;
      }}
      .reviews-grid {{
        grid-template-columns: 1fr;
      }}
      .contact-channels {{
        grid-template-columns: 1fr;
      }}
      .footer__top {{
        grid-template-columns: 1fr;
        gap: 32px;
      }}
    }}

    @media (max-width: 768px) {{
      .top-bar {{
        display: none;
      }}
      .header__inner {{
        height: 68px;
      }}
      .header__nav {{
        display: none;
      }}
      .header__nav.open {{
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        position: absolute;
        top: 68px;
        left: 0;
        right: 0;
        background: var(--bg-cream);
        padding: 24px 28px;
        border-bottom: 1px solid var(--c-border);
        box-shadow: var(--shadow-lg);
        gap: 16px;
      }}
      .menu-toggle {{
        display: flex;
      }}
      .section {{
        padding: 70px 0;
      }}
      .hero__title {{
        font-size: 38px;
      }}
      .hero__trust-strip {{
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
      }}
      .product-card__inner {{
        grid-template-columns: 1fr;
      }}
      .product-card__details {{
        padding: 36px 24px;
      }}
      .product-card__gallery {{
        min-height: 320px;
      }}
      .awards-list {{
        grid-template-columns: 1fr;
      }}
      .floating-cta span {{
        display: none;
      }}
      .floating-cta {{
        padding: 14px;
        bottom: 20px;
        right: 20px;
      }}
    }}
  </style>
</head>
<body>

  <!-- ========================================================================
       TOP ANNOUNCEMENT BAR
       ======================================================================== -->
  <aside class="top-bar">
    <div class="top-bar__ticker">
      <span>🌿 100% Botanical Artisanal Skincare</span>
      <span class="top-bar__bullet">·</span>
      <span>Cold-Processed in Small Batches</span>
      <span class="top-bar__bullet">·</span>
      <span>Raw Goat Milk &amp; Kashmiri Saffron</span>
    </div>
    <div class="top-bar__links">
      <a href="tel:+919008473680">Direct Concierge: +91 90084 73680</a>
      <a href="mailto:Opper_naturals@gmail.com">Opper_naturals@gmail.com</a>
    </div>
  </aside>

  <!-- ========================================================================
       STICKY LUXURY HEADER
       ======================================================================== -->
  <header class="header" id="navbar">
    <div class="container">
      <div class="header__inner">
        <!-- Brand Signature -->
        <a href="#top" class="header__brand" aria-label="OPPER Homepage">
          <img src="{IMG_LOGO}" alt="OPPER Royal Seal" class="header__logo-img">
          <div class="header__brand-text">
            <span class="header__brand-title">OPPER</span>
            <span class="header__brand-subtitle">Artisan Skincare</span>
          </div>
        </a>

        <!-- Desktop Navigation -->
        <nav class="header__nav" id="mainNav">
          <a href="#collection" class="nav-link">The Collection</a>
          <a href="#ingredients" class="nav-link">Formulation Codex</a>
          <a href="#craft" class="nav-link">The Ritual</a>
          <a href="#story" class="nav-link">Our Founder</a>
          <a href="#gifting" class="nav-link">Bespoke Gifting</a>
          <a href="#contact" class="nav-link">Retail &amp; Orders</a>
        </nav>

        <!-- Right Quick Actions -->
        <div class="header__actions">
          <button class="btn btn--primary btn--sm" onclick="openOrderModal('General Inquiry')">
            Direct Order
          </button>
          <button class="menu-toggle" id="menuBtn" aria-label="Toggle navigation menu">
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- ========================================================================
       HERO EDITORIAL SHOWCASE
       ======================================================================== -->
  <section class="hero" id="top">
    <div class="container">
      <div class="hero__grid">
        <!-- Left Editorial Copy -->
        <div class="hero__copy">
          <div class="hero__eyebrow">
            <span class="badge badge--saffron">Artisan Cold-Process</span>
            <span class="badge badge--forest">Bengaluru, India</span>
          </div>
          <h1 class="hero__title">
            Pure by nature.<br>
            <em>Crafted with care.</em>
          </h1>
          <p class="hero__lead">
            Handmade organic skincare formulated with farm-fresh goat milk, prized Kashmiri saffron, unrefined botanical oils, and Ayurvedic remedies. Made slowly in small batches for barrier-loving skin wellness.
          </p>
          <div class="hero__actions">
            <a href="#collection" class="btn btn--primary">
              Explore Creations
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
            <button class="btn btn--outline" onclick="openOrderModal('Wholesale & Custom Order')">
              Wholesale &amp; Gifting
            </button>
          </div>

          <!-- Trust & Authenticity Strip -->
          <div class="hero__trust-strip">
            <div class="trust-item">
              <span class="trust-item__val">500+</span>
              <span class="trust-item__lbl">Patrons via Word-of-Mouth</span>
            </div>
            <div class="trust-item">
              <span class="trust-item__val">0%</span>
              <span class="trust-item__lbl">SLS, Parabens, Harsh Toxins</span>
            </div>
            <div class="trust-item">
              <span class="trust-item__val">4-6 Wks</span>
              <span class="trust-item__lbl">Cold-Cured Aging</span>
            </div>
            <div class="trust-item">
              <span class="trust-item__val">3x</span>
              <span class="trust-item__lbl">State &amp; NGO Honors</span>
            </div>
          </div>
        </div>

        <!-- Right Hero Visual -->
        <div class="hero__visual">
          <div class="hero__image-frame" onclick="openLightbox('{IMG_SOAP_BOX}')">
            <img src="{IMG_SOAP_BOX}" alt="OPPER handcrafted organic soap bars in luxury presentation box" loading="eager">
          </div>
          <div class="hero__floating-card">
            <div class="hero__floating-card-tag">Small-Batch Reserve</div>
            <div class="hero__floating-card-title">Goat Milk, Saffron &amp; Shea Butter</div>
          </div>
          <div class="hero__floating-stamp">
            100%<br>Natural<br>Origin
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       BRAND MANIFESTO MARQUEE
       ======================================================================== -->
  <div class="marquee" aria-hidden="true">
    <div class="marquee__track">
      <span class="marquee__item">Fresh Farm Goat Milk <span class="marquee__symbol">✦</span></span>
      <span class="marquee__item">Kashmiri Mongra Saffron <span class="marquee__symbol">✦</span></span>
      <span class="marquee__item">Cold-Pressed Virgin Oils <span class="marquee__symbol">✦</span></span>
      <span class="marquee__item">Raw Unrefined Shea Butter <span class="marquee__symbol">✦</span></span>
      <span class="marquee__item">Zero Synthetic Preservatives <span class="marquee__symbol">✦</span></span>
      <span class="marquee__item">Ayurvedic Botanical Alchemy <span class="marquee__symbol">✦</span></span>
      <span class="marquee__item">Hand-Cut &amp; Slow Cured <span class="marquee__symbol">✦</span></span>
      <span class="marquee__item">Fresh Farm Goat Milk <span class="marquee__symbol">✦</span></span>
      <span class="marquee__item">Kashmiri Mongra Saffron <span class="marquee__symbol">✦</span></span>
      <span class="marquee__item">Cold-Pressed Virgin Oils <span class="marquee__symbol">✦</span></span>
      <span class="marquee__item">Raw Unrefined Shea Butter <span class="marquee__symbol">✦</span></span>
      <span class="marquee__item">Zero Synthetic Preservatives <span class="marquee__symbol">✦</span></span>
    </div>
  </div>

  <!-- ========================================================================
       PRODUCT SHOWCASE & COLLECTION
       ======================================================================== -->
  <section class="section" id="collection">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Curated Formulations</span>
        <h2 class="section-title">The Artisanal Collection</h2>
        <p class="section-desc">
          Every bar is prepared without industrial detergents or chemical foaming agents. Saponified at gentle temperatures to protect botanical vitamins and natural moisturizing glycerine.
        </p>
      </div>

      <!-- Creation 1: Flagship Goat Milk & Saffron -->
      <article class="product-card">
        <div class="product-card__inner">
          <div class="product-card__gallery" onclick="openLightbox('{IMG_PREMIUM_BAR}')">
            <span class="badge badge--saffron product-card__overlay-badge">Flagship Creation</span>
            <img src="{IMG_PREMIUM_BAR}" alt="OPPER Premium Goat Milk and Kashmiri Saffron Bathing Bar Box" loading="lazy">
          </div>
          <div class="product-card__details">
            <span class="product-card__category">Bathing Bar · 100g</span>
            <h3 class="product-card__title">Goat Milk &amp; Kashmiri Saffron Bathing Bar</h3>
            <p class="product-card__summary">
              Our signature formula. Farm-fresh goat milk provides lactic acid to gently lift dull skin, while pure Kashmiri saffron imparts a luminous glow. Deeply conditioning with cold-pressed coconut, sweet almond, and virgin olive oils.
            </p>
            <div class="formula-pills">
              <span class="formula-pill">Lactic Acid (AHA)</span>
              <span class="formula-pill">Antioxidant Crocin</span>
              <span class="formula-pill">Vitamin A, B6, E</span>
              <span class="formula-pill">pH-Balanced</span>
            </div>
            <div class="product-specs">
              <div class="product-spec-row">
                <span class="product-spec-label">Ideal For</span>
                <span class="product-spec-value">Dry, sensitive, uneven, or mature skin types</span>
              </div>
              <div class="product-spec-row">
                <span class="product-spec-label">Key Actives</span>
                <span class="product-spec-value">Raw Goat Milk, Kashmiri Saffron, Cold-Pressed Almond Oil, Aloe Extract, Pure Shea Butter</span>
              </div>
              <div class="product-spec-row">
                <span class="product-spec-label">Sensory Profile</span>
                <span class="product-spec-value">Silky, custard-like rich micro-lather with a soft, warm herbal aroma</span>
              </div>
            </div>
            <div class="product-card__actions">
              <button class="btn btn--primary" onclick="openOrderModal('Goat Milk & Saffron Bathing Bar')">
                Inquire &amp; Order
              </button>
              <a href="https://wa.me/919008473680?text=Hello%20OPPER,%20I%20am%20interested%20in%20ordering%20the%20Goat%20Milk%20%26%20Saffron%20Bathing%20Bar." target="_blank" rel="noopener" class="btn btn--outline">
                WhatsApp Order
              </a>
            </div>
          </div>
        </div>
      </article>

      <!-- Creation 2: Carrot & Shea Butter Bathing Bar -->
      <article class="product-card product-card--reverse">
        <div class="product-card__inner">
          <div class="product-card__gallery" onclick="openLightbox('{IMG_SOAPS_TRAY}')">
            <span class="badge badge--forest product-card__overlay-badge">Barrier Repair</span>
            <img src="{IMG_SOAPS_TRAY}" alt="Handcrafted OPPER Carrot and Shea Butter Soaps on Marble Tray" loading="lazy">
          </div>
          <div class="product-card__details">
            <span class="product-card__category">Bathing Bar · 100g</span>
            <h3 class="product-card__title">Carrot &amp; Pure Shea Butter Bathing Bar</h3>
            <p class="product-card__summary">
              Enriched with vitamin-dense carrot extract and unrefined shea butter. Formulated specifically to shield against trans-epidermal moisture loss, soothe sun-stressed skin, and promote velvet softness.
            </p>
            <div class="formula-pills">
              <span class="formula-pill">Beta-Carotene</span>
              <span class="formula-pill">Stearic &amp; Oleic Lipids</span>
              <span class="formula-pill">Soothes Dryness</span>
              <span class="formula-pill">Hypoallergenic</span>
            </div>
            <div class="product-specs">
              <div class="product-spec-row">
                <span class="product-spec-label">Ideal For</span>
                <span class="product-spec-value">Extremely dry, eczema-prone, dehydrated, or sun-exposed skin</span>
              </div>
              <div class="product-spec-row">
                <span class="product-spec-label">Key Actives</span>
                <span class="product-spec-value">Organic Carrot Puree, Grade-A Shea Butter, Cold-Pressed Olive &amp; Coconut Oils</span>
              </div>
              <div class="product-spec-row">
                <span class="product-spec-label">Sensory Profile</span>
                <span class="product-spec-value">Creamy, ultra-gentle cushion lather that leaves a protective moisture veil</span>
              </div>
            </div>
            <div class="product-card__actions">
              <button class="btn btn--primary" onclick="openOrderModal('Carrot & Shea Butter Bathing Bar')">
                Inquire &amp; Order
              </button>
              <a href="https://wa.me/919008473680?text=Hello%20OPPER,%20I%20am%20interested%20in%20ordering%20the%20Carrot%20%26%20Shea%20Butter%20Bar." target="_blank" rel="noopener" class="btn btn--outline">
                WhatsApp Order
              </a>
            </div>
          </div>
        </div>
      </article>

      <!-- Creation 3: Curated Artisanal Gift Hampers -->
      <article class="product-card">
        <div class="product-card__inner">
          <div class="product-card__gallery" onclick="openLightbox('{IMG_GIFT_BOX}')">
            <span class="badge badge--gold product-card__overlay-badge">Bespoke Suite</span>
            <img src="{IMG_GIFT_BOX}" alt="OPPER Handcrafted Artisanal Gift Box with tags and premium bars" loading="lazy">
          </div>
          <div class="product-card__details">
            <span class="product-card__category">Curated Rituals · Gifting</span>
            <h3 class="product-card__title">Artisan Gift Combos &amp; Hampers</h3>
            <p class="product-card__summary">
              Hand-packaged luxury soap duos and trios nested in sustainable rigid gift boxes with botanical botanical seals and personalized calligraphy tags. Tailored for weddings, Diwali, festive favors, and corporate celebrations.
            </p>
            <div class="formula-pills">
              <span class="formula-pill">Custom Monogramming</span>
              <span class="formula-pill">Eco-Friendly Rigid Box</span>
              <span class="formula-pill">Festive Favors</span>
              <span class="formula-pill">Bulk Pricing Available</span>
            </div>
            <div class="product-specs">
              <div class="product-spec-row">
                <span class="product-spec-label">Occasions</span>
                <span class="product-spec-value">Weddings, baby showers, festive celebrations, luxury corporate gifting</span>
              </div>
              <div class="product-spec-row">
                <span class="product-spec-label">Includes</span>
                <span class="product-spec-value">Assorted OPPER bars, keepsake wooden coasters, personalized greeting note</span>
              </div>
              <div class="product-spec-row">
                <span class="product-spec-label">Minimum Order</span>
                <span class="product-spec-value">From single celebration sets to 500+ bespoke corporate suites</span>
              </div>
            </div>
            <div class="product-card__actions">
              <button class="btn btn--saffron" onclick="openOrderModal('Artisan Gift Combos')">
                Request Custom Gifting
              </button>
              <a href="https://wa.me/919008473680?text=Hello%20OPPER,%20I%20would%20like%20to%20inquire%20about%20Custom%20Artisan%20Gift%20Hampers." target="_blank" rel="noopener" class="btn btn--outline">
                WhatsApp Concierge
              </a>
            </div>
          </div>
        </div>
      </article>
    </div>
  </section>

  <!-- ========================================================================
       BOTANICAL ALCHEMY & INGREDIENT CODEX
       ======================================================================== -->
  <section class="section ingredients-section" id="ingredients">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Pure Formulation Codex</span>
        <h2 class="section-title">Rooted in Nature. Backed by Science.</h2>
        <p class="section-desc">
          We never use sulfates, petrochemical fillers, artificial colorants, or synthetic hardening chemicals. Every element is selected for pure skin nutrition.
        </p>
      </div>

      <!-- Ingredient Highlights Grid -->
      <div class="ingredients-grid">
        <div class="ingredient-card">
          <div class="ingredient-card__icon">🥛</div>
          <h4 class="ingredient-card__name">Raw Goat Milk</h4>
          <span class="ingredient-card__role">Natural AHA Exfoliant</span>
          <p class="ingredient-card__desc">
            Matches skin's natural 5.5 pH mantle. Packed with lactic acid and caprylic acid to break down dead skin bonds while feeding beneficial skin flora.
          </p>
        </div>

        <div class="ingredient-card">
          <div class="ingredient-card__icon">🌸</div>
          <h4 class="ingredient-card__name">Kashmiri Saffron</h4>
          <span class="ingredient-card__role">Luminosity &amp; Tone</span>
          <p class="ingredient-card__desc">
            Hand-harvested crimson stigmas rich in crocin and safranal. Known in Ayurveda for improving skin texture and reviving tired skin with antioxidant protection.
          </p>
        </div>

        <div class="ingredient-card">
          <div class="ingredient-card__icon">🧈</div>
          <h4 class="ingredient-card__name">Raw Shea Butter</h4>
          <span class="ingredient-card__role">Lipid Seal &amp; Softness</span>
          <p class="ingredient-card__desc">
            Extracted from karite nuts. Loaded with stearic, oleic, and linolenic fatty acids that melt upon contact to restore compromised lipid layers.
          </p>
        </div>

        <div class="ingredient-card">
          <div class="ingredient-card__icon">🌿</div>
          <h4 class="ingredient-card__name">Botanical Oils</h4>
          <span class="ingredient-card__role">Nutrient Matrix</span>
          <p class="ingredient-card__desc">
            Cold-pressed coconut, sweet almond, extra virgin olive oil, and organic aloe vera infused to form a restorative, vitamin-rich cleansing bar.
          </p>
        </div>
      </div>

      <!-- Full-bleed Codex Graphic -->
      <div class="codex-banner" onclick="openLightbox('{IMG_INGREDIENTS}')">
        <img src="{IMG_INGREDIENTS}" alt="Complete OPPER World Ingredients breakdown: Coconut Oil, Olive Oil, Almond Oil, Goat Milk, Saffron, Aloe Vera, Shea Butter" loading="lazy">
        <div class="codex-banner__zoom-hint">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35M11 8v6M8 11h6"/></svg>
          Click to Zoom Codex
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       THE ARTISAN COLD-PROCESS RITUAL
       ======================================================================== -->
  <section class="section" id="craft">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Old-World Soapcraft</span>
        <h2 class="section-title">The Slow-Cure Cold Process</h2>
        <p class="section-desc">
          Commercial detergents are mass-manufactured with chemical hardeners and stripped of natural glycerine. We preserve age-old artisanal saponification.
        </p>
      </div>

      <div class="craft-timeline">
        <div class="craft-step">
          <div class="craft-step__num">01</div>
          <h4 class="craft-step__title">Gentle Emulsion</h4>
          <p class="craft-step__text">
            Pure cold-pressed vegetable oils are gently blended with raw goat milk at controlled low temperatures, safeguarding heat-sensitive vitamins and enzymes.
          </p>
        </div>

        <div class="craft-step">
          <div class="craft-step__num">02</div>
          <h4 class="craft-step__title">Botanical Trace</h4>
          <p class="craft-step__text">
            Kashmiri saffron threads, carrot extracts, and soothing aloe vera are stirred by hand right as the batch reaches trace, guaranteeing uniform distribution.
          </p>
        </div>

        <div class="craft-step">
          <div class="craft-step__num">03</div>
          <h4 class="craft-step__title">4 to 6 Weeks Cure</h4>
          <p class="craft-step__text">
            Bars rest on wooden curing racks in ventilated drying rooms. Saponification finishes naturally, water evaporates, and natural glycerine forms.
          </p>
        </div>

        <div class="craft-step">
          <div class="craft-step__num">04</div>
          <h4 class="craft-step__title">Hand-Cut &amp; Checked</h4>
          <p class="craft-step__text">
            Every block is hand-beveled, stamped, inspected for density and texture, and wrapped in breathable eco-conscious paper packaging.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       FOUNDER STORY & HONORS
       ======================================================================== -->
  <section class="section story-section" id="story">
    <div class="container">
      <div class="story-grid">
        <!-- Founder Portrait -->
        <div class="story-visual">
          <div class="story-visual__frame" onclick="openLightbox('{IMG_FOUNDER}')">
            <img src="{IMG_FOUNDER}" alt="Geetha, founder and visionary behind OPPER Skincare" loading="lazy">
          </div>
          <div class="story-visual__badge">
            Geetha
            <span>Founder &amp; Formulator</span>
          </div>
        </div>

        <!-- Founder Narrative -->
        <div class="story-content">
          <span class="section-tag">A Brand Born of Purpose</span>
          <h2 class="section-title">Built with Pure Love &amp; Devotion</h2>
          
          <div class="story-quote">
            "Take care of your body. It's the only place you have to live in."
          </div>

          <p class="story-body">
            OPPER began with Geetha's quiet ambition — to build a meaningful legacy rooted in purity, health, and holistic wellness. Balancing motherhood and a professional career, she was troubled by the aggressive chemical detergents dominating bathroom shelves.
          </p>
          <p class="story-body">
            Turning to ancestral recipes, she began small-batch cold-process experiments using fresh goat milk, Kashmiri saffron, and therapeutic oils. What began as a personal remedy for loved ones quickly evolved into a cult community favorite. Through pure word-of-mouth and uncompromising purity, OPPER has delighted over 500 patrons without a single rupee spent on paid advertising.
          </p>

          <!-- Recognition & Awards -->
          <div class="awards-list">
            <div class="award-card">
              <span class="award-card__trophy">🏆</span>
              <div class="award-card__title">Startup Award</div>
              <div class="award-card__org">Adya Foundation</div>
            </div>
            <div class="award-card">
              <span class="award-card__trophy">🎖️</span>
              <div class="award-card__title">Powerful Women Achiever</div>
              <div class="award-card__org">Anshu Foundation</div>
            </div>
            <div class="award-card">
              <span class="award-card__trophy">⭐</span>
              <div class="award-card__title">Women Power Honor</div>
              <div class="award-card__org">Sri Adya &amp; VWMCs</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       SISTER BRAND: GEET SUSTAINABLE GIFTING
       ======================================================================== -->
  <section class="section geet-section" id="gifting">
    <div class="container">
      <div class="geet-grid">
        <div class="geet-content">
          <span class="section-tag">Sister Brand &amp; Keepsakes</span>
          <h2 class="section-title">GEET — Feel the Love</h2>
          <p class="section-desc">
            Where thoughtful design meets environmental stewardship. GEET curates bespoke, eco-conscious gifting hampers featuring customized jute carryalls, engraved natural wooden mugs, and artisanal keepsakes.
          </p>
          <ul class="geet-features">
            <li>Hand-stitched jute gift bags with customized gold monograms</li>
            <li>Handcrafted wooden beverage mugs &amp; sustainable lifestyle keepsakes</li>
            <li>Custom curation combining OPPER organic bars with bespoke favors</li>
            <li>Loved by premium corporates, boutique weddings, and private galas</li>
          </ul>
          <div class="geet-actions">
            <button class="btn btn--primary" onclick="openOrderModal('GEET Sustainable Gifting Suite')">
              Inquire Bespoke Gifting
            </button>
            <a href="https://wa.me/919008473680?text=Hello%20GEET,%20I%20am%20interested%20in%20customized%20sustainable%20gifting%20hampers." target="_blank" rel="noopener" class="btn btn--outline" style="margin-left: 12px;">
              WhatsApp Gifting Desk
            </a>
          </div>
        </div>
        <div class="geet-visual" onclick="openLightbox('{IMG_GEET}')">
          <img src="{IMG_GEET}" alt="GEET personalized eco-friendly jute bag, wooden mug and gift box" loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       COMMUNITY LOVE & TESTIMONIALS
       ======================================================================== -->
  <section class="section" style="background: var(--bg-cream);">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Community Reflections</span>
        <h2 class="section-title">Loved by Those Who Cherish Pure Skin</h2>
        <p class="section-desc">
          Real feedback from patrons who replaced mass-market body wash with our cold-cured artisan bars.
        </p>
      </div>

      <div class="reviews-grid">
        <div class="review-card">
          <div class="review-stars">★★★★★</div>
          <p class="review-text">
            "My skin used to feel tight and dry after every shower with store-bought soap. The Goat Milk &amp; Saffron bar completely changed that. It creates a rich, creamy lather and leaves skin moisturized even without lotion."
          </p>
          <div class="review-author">
            <div class="review-avatar">A</div>
            <div class="review-author-info">
              <div class="review-name">Ananya S.</div>
              <div class="review-loc">Bengaluru · Verified Patron</div>
            </div>
          </div>
        </div>

        <div class="review-card">
          <div class="review-stars">★★★★★</div>
          <p class="review-text">
            "We ordered 80 customized gift hampers for our daughter's naming ceremony from OPPER and GEET. Every single guest messaged us saying how beautiful the packaging was and how heavenly the soap smelled."
          </p>
          <div class="review-author">
            <div class="review-avatar">P</div>
            <div class="review-author-info">
              <div class="review-name">Praveen &amp; Deepa K.</div>
              <div class="review-loc">Mysuru · Festive Gifting</div>
            </div>
          </div>
        </div>

        <div class="review-card">
          <div class="review-stars">★★★★★</div>
          <p class="review-text">
            "The Carrot and Shea Butter bar has been a blessing for my sensitive skin. No artificial perfumes, no redness, just pure soothing care. You can immediately feel the quality of unrefined ingredients."
          </p>
          <div class="review-author">
            <div class="review-avatar">R</div>
            <div class="review-author-info">
              <div class="review-name">Rohini M.</div>
              <div class="review-loc">Hyderabad · Verified Patron</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       CONTACT, DIRECT CONCIERGE & ORDERS
       ======================================================================== -->
  <section class="section contact-section" id="contact">
    <div class="container">
      <div class="contact-box">
        <span class="badge badge--gold" style="margin-bottom: 16px;">Direct Concierge &amp; Wholesale</span>
        <h2 class="contact-title">Let Us Craft Something Special for You</h2>
        <p class="contact-subtitle">
          Whether you desire personal bars, bespoke wedding favor suites, or corporate client hampers, connect directly with Geetha and the OPPER team.
        </p>

        <div class="contact-channels">
          <a href="tel:+919008473680" class="channel-card">
            <span class="channel-icon">📞</span>
            <div class="channel-label">Direct Phone</div>
            <div class="channel-val">+91 90084 73680</div>
          </a>

          <a href="mailto:Opper_naturals@gmail.com" class="channel-card">
            <span class="channel-icon">✉️</span>
            <div class="channel-label">Email Concierge</div>
            <div class="channel-val">Opper_naturals@gmail.com</div>
          </a>

          <a href="https://www.instagram.com/opper_naturals" target="_blank" rel="noopener" class="channel-card">
            <span class="channel-icon">📷</span>
            <div class="channel-label">Instagram Portfolio</div>
            <div class="channel-val">@opper_naturals</div>
          </a>
        </div>

        <div>
          <button class="btn btn--saffron" onclick="openOrderModal('General Inquiry & Order')">
            Open Order Inquiry Form
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       FOOTER
       ======================================================================== -->
  <footer class="footer">
    <div class="container">
      <div class="footer__top">
        <div>
          <div class="footer__brand-title">OPPER</div>
          <div class="footer__tagline">Pure by nature. Made with care.</div>
          <p style="max-width: 380px; line-height: 1.7;">
            Handcrafted artisanal cold-process organic soaps and wellness creations. Enriched with fresh goat milk, Kashmiri saffron, and cold-pressed botanical oils.
          </p>
        </div>

        <div>
          <div class="footer__col-title">Portfolio Index</div>
          <ul class="footer__links">
            <li><a href="#collection">The Collection</a></li>
            <li><a href="#ingredients">Botanical Codex</a></li>
            <li><a href="#craft">Artisan Process</a></li>
            <li><a href="#story">Our Founder</a></li>
            <li><a href="#gifting">GEET Gifting Suite</a></li>
          </ul>
        </div>

        <div>
          <div class="footer__col-title">Direct Inquiries</div>
          <ul class="footer__links">
            <li><strong>Founder:</strong> Geetha</li>
            <li><strong>Phone:</strong> <a href="tel:+919008473680">+91 90084 73680</a></li>
            <li><strong>Email:</strong> <a href="mailto:Opper_naturals@gmail.com">Opper_naturals@gmail.com</a></li>
            <li><strong>Instagram:</strong> <a href="https://www.instagram.com/opper_naturals" target="_blank" rel="noopener">@opper_naturals</a></li>
            <li><strong>Location:</strong> Bengaluru, Karnataka, India</li>
          </ul>
        </div>
      </div>

      <div class="footer__bottom">
        <div>
          &copy; <span id="currentYear">2026</span> OPPER Organic Soap &amp; Skincare. All Rights Reserved.
        </div>
        <div style="color: var(--c-gold-light);">
          Crafted with devotion &amp; cold-cured pure botanicals.
        </div>
      </div>
    </div>
  </footer>

  <!-- ========================================================================
       FLOATING WHATSAPP ACTION BUTTON
       ======================================================================== -->
  <a href="https://wa.me/919008473680?text=Hello%20OPPER,%20I%20am%20interested%20in%20learning%20more%20about%20your%20organic%20soaps." target="_blank" rel="noopener" class="floating-cta" aria-label="Chat directly on WhatsApp">
    <svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2zm5.8 14.16c-.24.69-1.2 1.27-1.68 1.34-.46.07-1.04.1-3.04-.73-2.55-1.06-4.18-3.66-4.31-3.83-.13-.17-1.02-1.36-1.02-2.6 0-1.24.65-1.85.88-2.1.23-.24.5-.3.67-.3.17 0 .34 0 .49.01.16.01.37-.06.58.44.22.52.75 1.83.82 1.97.07.14.11.31.02.49-.09.17-.14.28-.28.43-.14.16-.3.35-.43.47-.14.14-.29.3-.13.58.17.29.74 1.22 1.58 1.97 1.08.97 2 1.27 2.29 1.41.29.14.46.12.63-.07.17-.2.74-.86.94-1.16.2-.29.4-.24.67-.14.27.1 1.73.82 2.03.97.29.14.49.22.56.34.07.12.07.72-.17 1.41z"/></svg>
    <span>Direct WhatsApp</span>
  </a>

  <!-- ========================================================================
       MODAL: DIRECT ORDER / INQUIRY
       ======================================================================== -->
  <div class="modal-overlay" id="orderModal" onclick="closeOrderModal(event)">
    <div class="modal-card">
      <div class="modal-header">
        <h3 class="modal-title">Inquire / Custom Order</h3>
        <p class="modal-subtitle">Connect directly with Geetha for personal or bulk orders</p>
        <button class="modal-close" onclick="closeOrderModal(null)" aria-label="Close modal">&times;</button>
      </div>
      <div class="modal-body">
        <form onsubmit="handleInquirySubmit(event)">
          <div class="form-group">
            <label class="form-label">Product / Service Interest</label>
            <select class="form-select" id="interestSelect">
              <option value="Goat Milk & Saffron Bathing Bar">Goat Milk &amp; Kashmiri Saffron Bathing Bar</option>
              <option value="Carrot & Shea Butter Bathing Bar">Carrot &amp; Shea Butter Bathing Bar</option>
              <option value="Artisan Gift Combos & Hampers">Artisan Gift Combos &amp; Hampers</option>
              <option value="GEET Bespoke Sustainable Gifting">GEET Bespoke Sustainable Gifting</option>
              <option value="Wholesale / Retail Partnership">Wholesale / Retail Partnership</option>
              <option value="General Brand Inquiry">General Brand Inquiry</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">Your Name</label>
            <input type="text" class="form-input" id="clientName" placeholder="e.g. Priyadarshini Rao" required>
          </div>
          <div class="form-group">
            <label class="form-label">Phone / WhatsApp Number</label>
            <input type="tel" class="form-input" id="clientPhone" placeholder="+91 98765 43210" required>
          </div>
          <div class="form-group">
            <label class="form-label">Order Details / Quantity / City</label>
            <textarea class="form-textarea" id="clientMsg" placeholder="Tell us how many bars, custom requests, or city for dispatch..."></textarea>
          </div>
          <button type="submit" class="btn btn--saffron" style="width: 100%;">
            Send Inquiry via WhatsApp
          </button>
        </form>
      </div>
    </div>
  </div>

  <!-- ========================================================================
       MODAL: LIGHTBOX FULLSCREEN PREVIEW
       ======================================================================== -->
  <div class="lightbox-modal" id="lightboxModal" onclick="closeLightbox()">
    <img src="" alt="Enlarged View" class="lightbox-img" id="lightboxImg">
  </div>

  <!-- ========================================================================
       CLIENT SCRIPTS
       ======================================================================== -->
  <script>
    // Set dynamic year
    document.getElementById('currentYear').textContent = new Date().getFullYear();

    // Sticky Header Scroll Effect
    const header = document.getElementById('navbar');
    window.addEventListener('scroll', () => {{
      header.classList.toggle('scrolled', window.scrollY > 20);
    }}, {{ passive: true }});

    // Mobile Navigation Toggle
    const menuBtn = document.getElementById('menuBtn');
    const mainNav = document.getElementById('mainNav');
    menuBtn.addEventListener('click', () => {{
      mainNav.classList.toggle('open');
    }});

    // Close mobile nav on click
    mainNav.querySelectorAll('a').forEach(link => {{
      link.addEventListener('click', () => {{
        mainNav.classList.remove('open');
      }});
    }});

    // Order Modal Controls
    const orderModal = document.getElementById('orderModal');
    const interestSelect = document.getElementById('interestSelect');

    function openOrderModal(presetInterest) {{
      if (presetInterest && interestSelect) {{
        for (let i = 0; i < interestSelect.options.length; i++) {{
          if (interestSelect.options[i].value.includes(presetInterest) || presetInterest.includes(interestSelect.options[i].value)) {{
            interestSelect.selectedIndex = i;
            break;
          }}
        }}
      }}
      orderModal.classList.add('active');
    }}

    function closeOrderModal(e) {{
      if (!e || e.target === orderModal || e.target.classList.contains('modal-close')) {{
        orderModal.classList.remove('active');
      }}
    }}

    // Handle Form submission via direct WhatsApp link pre-fill
    function handleInquirySubmit(e) {{
      e.preventDefault();
      const interest = document.getElementById('interestSelect').value;
      const name = document.getElementById('clientName').value;
      const phone = document.getElementById('clientPhone').value;
      const msg = document.getElementById('clientMsg').value;

      const whatsappText = `Hello Geetha / OPPER team,%0A%0AMy name is *${{encodeURIComponent(name)}}* (${{encodeURIComponent(phone)}}).%0A%0AI would like to enquire about: *${{encodeURIComponent(interest)}}*.%0A%0ADetails: ${{encodeURIComponent(msg)}}`;
      
      const whatsappUrl = `https://wa.me/919008473680?text=${{whatsappText}}`;
      window.open(whatsappUrl, '_blank');
      closeOrderModal(null);
    }}

    // Lightbox Controls
    const lightboxModal = document.getElementById('lightboxModal');
    const lightboxImg = document.getElementById('lightboxImg');

    function openLightbox(imgSrc) {{
      if (imgSrc) {{
        lightboxImg.src = imgSrc;
        lightboxModal.classList.add('active');
      }}
    }}

    function closeLightbox() {{
      lightboxModal.classList.remove('active');
    }}

    // Close modal on Escape key
    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        closeOrderModal(null);
        closeLightbox();
      }}
    }});
  </script>
</body>
</html>
'''

# Write to index.html and opper-redesign.html
with open('index.html', 'w') as f:
    f.write(html_template)

with open('opper-redesign.html', 'w') as f:
    f.write(html_template)

print(f"Successfully generated index.html and opper-redesign.html ({len(html_template)} bytes)")
