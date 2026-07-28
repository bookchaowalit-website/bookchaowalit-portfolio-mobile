#!/usr/bin/env python3
"""Generate phone screenshot mockups for Google Play Store listing."""

from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = "screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Play Store phone screenshot: 1080x1920 (9:16)
W, H = 1080, 1920

# Colors - Material 3 inspired
BG = (255, 255, 255)
BG_DARK = (30, 30, 30)
PRIMARY = (20, 20, 20)
PRIMARY_CONTAINER = (230, 230, 230)
SURFACE = (255, 255, 255)
ON_SURFACE = (20, 20, 20)
ON_SURFACE_VARIANT = (100, 100, 100)
OUTLINE = (200, 200, 200)
SECONDARY_CONTAINER = (240, 240, 240)
ACCENT = (102, 102, 255)
GREEN = (76, 175, 80)
STATUS_BAR = (245, 245, 245)
NAV_BAR_BG = (250, 250, 250)

# Dark mode colors
D_BG = (20, 20, 20)
D_SURFACE = (30, 30, 30)
D_ON_SURFACE = (240, 240, 240)
D_ON_SURFACE_VARIANT = (170, 170, 170)
D_OUTLINE = (60, 60, 60)
D_SECONDARY_CONTAINER = (50, 50, 50)
D_PRIMARY_CONTAINER = (45, 45, 45)
D_STATUS_BAR = (25, 25, 25)
D_NAV_BAR_BG = (25, 25, 25)

try:
    font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 52)
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 38)
    font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
    font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    font_tiny = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    font_icon = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
except:
    font_large = ImageFont.load_default()
    font_title = font_large
    font_subtitle = font_large
    font_body = font_large
    font_small = font_large
    font_tiny = font_large
    font_icon = font_large


def draw_status_bar(draw, dark=False):
    """Draw Android status bar."""
    bg = D_STATUS_BAR if dark else STATUS_BAR
    text_color = D_ON_SURFACE if dark else ON_SURFACE
    draw.rectangle([0, 0, W, 80], fill=bg)
    draw.text((40, 25), "9:41", fill=text_color, font=font_small)
    # Battery, wifi icons (simple shapes)
    draw.rectangle([W-120, 32, W-40, 52], outline=text_color, width=2)
    draw.rectangle([W-118, 34, W-60, 50], fill=text_color)
    # Signal bars
    for i in range(4):
        h = 10 + i * 4
        draw.rectangle([W-180+i*12, 52-h, W-170+i*12, 52], fill=text_color)


def draw_nav_bar(draw, selected_index, dark=False):
    """Draw bottom navigation bar with 5 tabs."""
    bg = D_NAV_BAR_BG if dark else NAV_BAR_BG
    border = D_OUTLINE if dark else OUTLINE
    y_start = H - 120
    draw.rectangle([0, y_start, W, H], fill=bg)
    draw.line([0, y_start, W, y_start], fill=border, width=1)

    tabs = [
        ("Home", "⌂"),
        ("Projects", "▦"),
        ("About", "●"),
        ("Contact", "✉"),
        ("Settings", "⚙"),
    ]
    tab_w = W // 5
    for i, (label, icon) in enumerate(tabs):
        cx = tab_w * i + tab_w // 2
        color = PRIMARY if i == selected_index else (ON_SURFACE_VARIANT if not dark else D_ON_SURFACE_VARIANT)
        # Icon circle
        if i == selected_index:
            draw.rounded_rectangle([cx-30, y_start+15, cx+30, y_start+60], radius=20, fill=PRIMARY_CONTAINER if not dark else D_PRIMARY_CONTAINER)
        draw.text((cx-8, y_start+20), icon, fill=color, font=font_icon)
        draw.text((cx-20, y_start+70), label, fill=color, font=font_tiny)


def draw_rounded_rect(draw, bbox, radius, fill=None, outline=None, width=1):
    """Draw a rounded rectangle."""
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)


def screenshot_home():
    """Generate Home screen screenshot."""
    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)

    draw_status_bar(draw)

    # Hero section with gradient-like background
    for y in range(80, 500):
        alpha = max(0, 1.0 - (y - 80) / 420)
        c = int(230 * alpha + 255 * (1 - alpha))
        draw.line([0, y, W, y], fill=(c, c, c))

    # Avatar circle
    draw.ellipse([60, 160, 220, 320], fill=PRIMARY)
    draw.text((120, 200), "C", fill=BG, font=font_large)

    # Name & title
    draw.text((60, 350), "Chaowalit Greepoke", fill=ON_SURFACE, font=font_large)
    draw.text((60, 420), "Generalist & Solopreneur", fill=ACCENT, font=font_subtitle)
    draw.text((60, 470), "Building full-stack products, integrating", fill=ON_SURFACE_VARIANT, font=font_body)
    draw.text((60, 505), "AI systems, and growing digital presence", fill=ON_SURFACE_VARIANT, font=font_body)

    # Buttons
    draw_rounded_rect(draw, [60, 560, 320, 620], radius=30, fill=PRIMARY)
    draw.text((110, 572), "✉  Hire Me", fill=BG, font=font_body)
    draw_rounded_rect(draw, [350, 560, 620, 620], radius=30, outline=PRIMARY, width=2)
    draw.text((395, 572), "🌐  Website", fill=PRIMARY, font=font_body)

    # About section
    draw.text((60, 680), "About", fill=ON_SURFACE, font=font_title)
    draw.line([60, 730, 200, 730], fill=PRIMARY, width=3)
    draw.text((60, 750), "Generalist & Solopreneur building", fill=ON_SURFACE_VARIANT, font=font_body)
    draw.text((60, 785), "full-stack products, integrating AI", fill=ON_SURFACE_VARIANT, font=font_body)
    draw.text((60, 820), "systems, and growing digital presence.", fill=ON_SURFACE_VARIANT, font=font_body)

    # Info chips
    chips = ["📍 Bangkok", "💼 3+ Years", "💻 Full-Stack", "✨ AI"]
    cx = 60
    for chip in chips:
        tw = len(chip) * 14 + 30
        draw_rounded_rect(draw, [cx, 880, cx+tw, 930], radius=15, fill=SECONDARY_CONTAINER)
        draw.text((cx+15, 888), chip, fill=ON_SURFACE_VARIANT, font=font_small)
        cx += tw + 12

    # Tech Stack
    draw.text((60, 980), "Tech Stack", fill=ON_SURFACE, font=font_title)
    draw.line([60, 1030, 260, 1030], fill=PRIMARY, width=3)
    skills = ["Flutter", "Dart", "Next.js", "React", "TypeScript", "Python", "FastAPI", "PostgreSQL", "Docker", "AWS"]
    sx, sy = 60, 1050
    for skill in skills:
        tw = len(skill) * 16 + 30
        if sx + tw > W - 60:
            sx = 60
            sy += 50
        draw_rounded_rect(draw, [sx, sy, sx+tw, sy+40], radius=12, fill=SECONDARY_CONTAINER)
        draw.text((sx+15, sy+6), skill, fill=ON_SURFACE_VARIANT, font=font_small)
        sx += tw + 10

    # Featured Projects
    draw.text((60, 1250), "Featured Projects", fill=ON_SURFACE, font=font_title)
    draw.line([60, 1300, 380, 1300], fill=PRIMARY, width=3)
    draw.text((W-180, 1255), "View All →", fill=ACCENT, font=font_body)

    projects = [
        ("Portfolio Website", "Next.js portfolio with MDX blog", ["Next.js", "React", "MDX"]),
        ("AI Trading Bot", "Automated crypto trading system", ["Python", "AI", "API"]),
        ("E-Commerce Platform", "Full-stack online store", ["Flutter", "Firebase"]),
    ]
    py = 1320
    for name, desc, tags in projects:
        draw_rounded_rect(draw, [60, py, W-60, py+160], radius=16, outline=OUTLINE, width=2)
        draw.text((90, py+15), name, fill=ON_SURFACE, font=font_subtitle)
        draw.text((90, py+60), desc, fill=ON_SURFACE_VARIANT, font=font_small)
        tx = 90
        for tag in tags:
            tw = len(tag) * 14 + 20
            draw_rounded_rect(draw, [tx, py+100, tx+tw, py+135], radius=8, fill=SECONDARY_CONTAINER)
            draw.text((tx+10, py+105), tag, fill=ON_SURFACE_VARIANT, font=font_tiny)
            tx += tw + 8
        draw.text((W-120, py+20), "→", fill=ON_SURFACE_VARIANT, font=font_icon)
        py += 175

    draw_nav_bar(draw, 0)

    img.save(os.path.join(OUTPUT_DIR, "phone_screenshot_1_home.png"))
    print("✓ Home screenshot saved")


def screenshot_projects():
    """Generate Projects screen screenshot."""
    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)

    draw_status_bar(draw)

    # Header gradient
    for y in range(80, 300):
        alpha = max(0, 1.0 - (y - 80) / 220)
        c = int(230 * alpha + 255 * (1 - alpha))
        draw.line([0, y, W, y], fill=(c, c, c))

    draw.text((60, 140), "Projects", fill=ON_SURFACE, font=font_large)
    draw.line([60, 200, 240, 200], fill=PRIMARY, width=3)
    draw.text((60, 220), "A selection of projects I've built —", fill=ON_SURFACE_VARIANT, font=font_body)
    draw.text((60, 255), "from web apps to mobile and automation.", fill=ON_SURFACE_VARIANT, font=font_body)

    projects = [
        ("Portfolio Website", "Next.js portfolio with MDX blog, dark mode, SEO optimization, and cloudflare deployment", ["Next.js", "React", "TypeScript", "MDX"]),
        ("AI Trading Bot", "Automated cryptocurrency trading system with ML predictions and risk management", ["Python", "TensorFlow", "Binance API"]),
        ("E-Commerce Platform", "Full-stack online store with payment processing, inventory management, and analytics", ["Flutter", "Firebase", "Stripe"]),
        ("Task Automation CLI", "Command-line tool for automating development workflows and deployments", ["Python", "Docker", "CI/CD"]),
        ("Real-time Chat App", "WebSocket-based chat application with rooms, file sharing, and message encryption", ["Node.js", "Socket.io", "MongoDB"]),
        ("Weather Dashboard", "Interactive weather visualization with 7-day forecasts and location-based alerts", ["React", "D3.js", "OpenWeather"]),
        ("Fitness Tracker", "Mobile app for tracking workouts, nutrition, and progress with social features", ["Flutter", "SQLite", "Charts"]),
        ("Blog CMS", "Headless CMS with markdown editor, image optimization, and API-first design", ["FastAPI", "PostgreSQL", "S3"]),
    ]

    py = 310
    for i, (name, desc, tags) in enumerate(projects):
        draw_rounded_rect(draw, [60, py, W-60, py+180], radius=16, outline=OUTLINE, width=2)
        draw.text((90, py+15), name, fill=ON_SURFACE, font=font_subtitle)
        # Wrap description
        words = desc.split()
        line = ""
        ly = py + 60
        for word in words:
            test = line + word + " "
            if len(test) > 45:
                draw.text((90, ly), line.strip(), fill=ON_SURFACE_VARIANT, font=font_small)
                ly += 30
                line = word + " "
            else:
                line = test
        if line:
            draw.text((90, ly), line.strip(), fill=ON_SURFACE_VARIANT, font=font_small)

        tx = 90
        tag_y = py + 135
        for tag in tags:
            tw = len(tag) * 14 + 20
            if tx + tw > W - 120:
                break
            draw_rounded_rect(draw, [tx, tag_y, tx+tw, tag_y+32], radius=8, fill=SECONDARY_CONTAINER)
            draw.text((tx+10, tag_y+4), tag, fill=ON_SURFACE_VARIANT, font=font_tiny)
            tx += tw + 8
        draw.text((W-120, py+20), "→", fill=ON_SURFACE_VARIANT, font=font_icon)
        py += 195

    draw_nav_bar(draw, 1)

    img.save(os.path.join(OUTPUT_DIR, "phone_screenshot_2_projects.png"))
    print("✓ Projects screenshot saved")


def screenshot_project_detail():
    """Generate Project Detail screen screenshot."""
    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)

    draw_status_bar(draw)

    # Hero header
    for y in range(80, 450):
        alpha = max(0, 1.0 - (y - 80) / 370)
        c = int(220 * alpha + 255 * (1 - alpha))
        draw.line([0, y, W, y], fill=(c, c, c))

    # Back button & open in browser
    draw.text((40, 110), "← Back", fill=ON_SURFACE, font=font_body)
    draw.text((W-250, 110), "Open ↗", fill=ACCENT, font=font_body)

    # Project icon
    draw.rounded_rectangle([60, 200, 200, 340], radius=30, fill=PRIMARY)
    draw.text((105, 240), "P", fill=BG, font=font_large)

    # Project name
    draw.text((230, 210), "Portfolio Website", fill=ON_SURFACE, font=font_title)

    # Tags
    tags = ["Next.js", "React", "TypeScript", "MDX"]
    tx = 230
    for tag in tags:
        tw = len(tag) * 14 + 20
        draw_rounded_rect(draw, [tx, 270, tx+tw, 305], radius=8, fill=SECONDARY_CONTAINER)
        draw.text((tx+10, 275), tag, fill=ON_SURFACE_VARIANT, font=font_tiny)
        tx += tw + 8

    draw.text((230, 320), "Modern portfolio with blog", fill=ON_SURFACE_VARIANT, font=font_small)

    # Description section
    draw.text((60, 400), "Description", fill=ON_SURFACE, font=font_title)
    draw.line([60, 450, 280, 450], fill=PRIMARY, width=3)
    desc_lines = [
        "A modern, responsive portfolio website",
        "built with Next.js 14 and React. Features",
        "include a dynamic blog with MDX support,",
        "dark mode toggle, SEO optimization,",
        "automated OG image generation, and",
        "deployment on Cloudflare Pages.",
    ]
    for i, line in enumerate(desc_lines):
        draw.text((60, 470 + i*35), line, fill=ON_SURFACE_VARIANT, font=font_body)

    # Key Features
    fy = 710
    draw.text((60, fy), "Key Features", fill=ON_SURFACE, font=font_title)
    draw.line([60, fy+50, 290, fy+50], fill=PRIMARY, width=3)

    features = [
        "Responsive design with Material 3",
        "Dynamic MDX blog with syntax highlighting",
        "Automated OG image generation",
        "Dark/light theme with system detection",
        "Cloudflare Pages deployment with CI/CD",
        "SEO optimized with dynamic metadata",
    ]
    fy += 70
    for feat in features:
        draw.rounded_rectangle([60, fy, 100, fy+35], radius=6, fill=GREEN)
        draw.text((70, fy+3), "✓", fill=BG, font=font_tiny)
        draw.text((120, fy+3), feat, fill=ON_SURFACE, font=font_body)
        fy += 50

    # Screenshots section
    fy += 20
    draw.text((60, fy), "Screenshots", fill=ON_SURFACE, font=font_title)
    draw.line([60, fy+50, 300, fy+50], fill=PRIMARY, width=3)

    fy += 70
    screenshots = ["Home View", "Blog View", "Project View"]
    for i, label in enumerate(screenshots):
        sx = 60 + i * 320
        draw_rounded_rect(draw, [sx, fy, sx+290, fy+380], radius=16, fill=SECONDARY_CONTAINER, outline=OUTLINE, width=2)
        # Simple mockup inside
        draw.rectangle([sx+20, fy+20, sx+270, fy+60], fill=PRIMARY_CONTAINER)
        draw.rectangle([sx+20, fy+70, sx+270, fy+300], fill=BG)
        draw.rectangle([sx+20, fy+310, sx+270, fy+360], fill=PRIMARY_CONTAINER)
        draw.text((sx+80, fy+400), label, fill=ON_SURFACE_VARIANT, font=font_small)

    # CTA button
    draw_rounded_rect(draw, [60, H-250, W-60, H-180], radius=30, fill=PRIMARY)
    draw.text((W//2-120, H-235), "Open in Browser", fill=BG, font=font_title)

    img.save(os.path.join(OUTPUT_DIR, "phone_screenshot_3_detail.png"))
    print("✓ Project Detail screenshot saved")


def screenshot_settings():
    """Generate Settings screen screenshot."""
    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)

    draw_status_bar(draw)

    # Header
    for y in range(80, 260):
        alpha = max(0, 1.0 - (y - 80) / 180)
        c = int(230 * alpha + 255 * (1 - alpha))
        draw.line([0, y, W, y], fill=(c, c, c))

    draw.text((60, 140), "Settings", fill=ON_SURFACE, font=font_large)
    draw.line([60, 200, 270, 200], fill=PRIMARY, width=3)

    # Appearance section
    draw.text((60, 260), "Appearance", fill=ON_SURFACE, font=font_title)
    draw.line([60, 310, 260, 310], fill=PRIMARY, width=3)

    themes = [
        ("System Default", "⚙", True),
        ("Light Mode", "☀", False),
        ("Dark Mode", "☾", False),
    ]
    ty = 330
    for label, icon, selected in themes:
        draw_rounded_rect(draw, [60, ty, W-60, ty+80], radius=16,
                         fill=SECONDARY_CONTAINER if selected else BG,
                         outline=PRIMARY if selected else OUTLINE, width=2 if selected else 1)
        draw.text((100, ty+20), f"{icon}  {label}", fill=ON_SURFACE, font=font_subtitle)
        # Radio button
        rx = W - 130
        draw.ellipse([rx, ty+22, rx+36, ty+58], outline=PRIMARY if selected else OUTLINE, width=2)
        if selected:
            draw.ellipse([rx+8, ty+30, rx+28, ty+50], fill=PRIMARY)
        ty += 95

    # Language section
    ty += 20
    draw.text((60, ty), "Language", fill=ON_SURFACE, font=font_title)
    draw.line([60, ty+50, 230, ty+50], fill=PRIMARY, width=3)
    ty += 70

    langs = [
        ("🇬🇧  English", True),
        ("🇹🇭  ภาษาไทย", False),
    ]
    for label, selected in langs:
        draw_rounded_rect(draw, [60, ty, W-60, ty+80], radius=16,
                         fill=SECONDARY_CONTAINER if selected else BG,
                         outline=PRIMARY if selected else OUTLINE, width=2 if selected else 1)
        draw.text((100, ty+20), label, fill=ON_SURFACE, font=font_subtitle)
        rx = W - 130
        draw.ellipse([rx, ty+22, rx+36, ty+58], outline=PRIMARY if selected else OUTLINE, width=2)
        if selected:
            draw.ellipse([rx+8, ty+30, rx+28, ty+50], fill=PRIMARY)
        ty += 95

    # About section
    ty += 30
    draw.text((60, ty), "About", fill=ON_SURFACE, font=font_title)
    draw.line([60, ty+50, 200, ty+50], fill=PRIMARY, width=3)
    ty += 70

    draw_rounded_rect(draw, [60, ty, W-60, ty+260], radius=16, outline=OUTLINE, width=1)
    about_items = [
        ("App Name", "Chaowalit Portfolio"),
        ("Developer", "Chaowalit Greepoke"),
        ("Version", "1.0.0"),
        ("Platform", "Android & iOS"),
    ]
    ay = ty + 20
    for label, value in about_items:
        draw.text((90, ay), label, fill=ON_SURFACE_VARIANT, font=font_body)
        draw.text((90, ay+32), value, fill=ON_SURFACE, font=font_body)
        ay += 65
        if ay < ty + 260 - 30:
            draw.line([90, ay-10, W-90, ay-10], fill=OUTLINE, width=1)

    draw_nav_bar(draw, 4)

    img.save(os.path.join(OUTPUT_DIR, "phone_screenshot_4_settings.png"))
    print("✓ Settings screenshot saved")


def screenshot_about():
    """Generate About screen screenshot."""
    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)

    draw_status_bar(draw)

    # Header
    for y in range(80, 350):
        alpha = max(0, 1.0 - (y - 80) / 270)
        c = int(230 * alpha + 255 * (1 - alpha))
        draw.line([0, y, W, y], fill=(c, c, c))

    # Avatar
    draw.ellipse([W//2-80, 140, W//2+80, 300], fill=PRIMARY)
    draw.text((W//2-20, 185), "C", fill=BG, font=font_large)

    draw.text((60, 330), "About Me", fill=ON_SURFACE, font=font_large)
    draw.line([60, 390, 280, 390], fill=PRIMARY, width=3)

    bio_lines = [
        "I'm a Generalist & Solopreneur",
        "based in Bangkok, Thailand with 3+ years",
        "of experience building full-stack products.",
        "",
        "I specialize in integrating AI systems,",
        "developing cross-platform mobile apps,",
        "and growing digital presence from idea",
        "to deployment.",
        "",
        "My approach combines technical expertise",
        "with business acumen to deliver complete",
        "solutions that solve real problems.",
    ]
    by = 420
    for line in bio_lines:
        draw.text((60, by), line, fill=ON_SURFACE_VARIANT if line else ON_SURFACE, font=font_body)
        by += 38

    # Experience cards
    by += 20
    draw.text((60, by), "Experience", fill=ON_SURFACE, font=font_title)
    draw.line([60, by+50, 280, by+50], fill=PRIMARY, width=3)
    by += 70

    experiences = [
        ("🚀", "Solopreneur", "Building full-stack products end-to-end"),
        ("💼", "Freelance Developer", "Web & mobile apps for clients"),
        ("🤖", "AI Engineer", "ML models, automation, integrations"),
        ("🌐", "Full-Stack Developer", "React, Flutter, Node.js, Python"),
    ]
    for icon, title, desc in experiences:
        draw_rounded_rect(draw, [60, by, W-60, by+120], radius=16, outline=OUTLINE, width=1)
        draw.text((90, by+15), f"{icon}  {title}", fill=ON_SURFACE, font=font_subtitle)
        draw.text((90, by+65), desc, fill=ON_SURFACE_VARIANT, font=font_small)
        by += 135

    # Skills summary
    by += 10
    draw.text((60, by), "Core Skills", fill=ON_SURFACE, font=font_title)
    draw.line([60, by+50, 270, by+50], fill=PRIMARY, width=3)
    by += 70

    skills = ["Flutter", "Dart", "React", "Next.js", "TypeScript", "Python", "FastAPI", "Node.js", "PostgreSQL", "Docker", "AWS", "Firebase"]
    sx, sy = 60, by
    for skill in skills:
        tw = len(skill) * 16 + 30
        if sx + tw > W - 60:
            sx = 60
            sy += 50
        draw_rounded_rect(draw, [sx, sy, sx+tw, sy+40], radius=12, fill=SECONDARY_CONTAINER)
        draw.text((sx+15, sy+6), skill, fill=ON_SURFACE_VARIANT, font=font_small)
        sx += tw + 10

    draw_nav_bar(draw, 2)

    img.save(os.path.join(OUTPUT_DIR, "phone_screenshot_5_about.png"))
    print("✓ About screenshot saved")


def screenshot_dark_mode():
    """Generate Dark Mode screenshot (Settings in dark)."""
    img = Image.new('RGB', (W, H), D_BG)
    draw = ImageDraw.Draw(img)

    draw_status_bar(draw, dark=True)

    # Header
    for y in range(80, 260):
        alpha = max(0, 1.0 - (y - 80) / 180)
        c = int(50 * alpha + 30 * (1 - alpha))
        draw.line([0, y, W, y], fill=(c, c, c))

    draw.text((60, 140), "Settings", fill=D_ON_SURFACE, font=font_large)
    draw.line([60, 200, 270, 200], fill=D_ON_SURFACE, width=3)

    # Appearance
    draw.text((60, 260), "Appearance", fill=D_ON_SURFACE, font=font_title)
    draw.line([60, 310, 260, 310], fill=D_ON_SURFACE, width=3)

    themes = [
        ("System Default", "⚙", False),
        ("Light Mode", "☀", False),
        ("Dark Mode", "☾", True),
    ]
    ty = 330
    for label, icon, selected in themes:
        draw_rounded_rect(draw, [60, ty, W-60, ty+80], radius=16,
                         fill=D_SECONDARY_CONTAINER if selected else D_SURFACE,
                         outline=D_ON_SURFACE if selected else D_OUTLINE, width=2 if selected else 1)
        draw.text((100, ty+20), f"{icon}  {label}", fill=D_ON_SURFACE, font=font_subtitle)
        rx = W - 130
        draw.ellipse([rx, ty+22, rx+36, ty+58], outline=D_ON_SURFACE if selected else D_OUTLINE, width=2)
        if selected:
            draw.ellipse([rx+8, ty+30, rx+28, ty+50], fill=D_ON_SURFACE)
        ty += 95

    # Language
    ty += 20
    draw.text((60, ty), "Language", fill=D_ON_SURFACE, font=font_title)
    draw.line([60, ty+50, 230, ty+50], fill=D_ON_SURFACE, width=3)
    ty += 70

    langs = [("🇬🇧  English", True), ("🇹🇭  ภาษาไทย", False)]
    for label, selected in langs:
        draw_rounded_rect(draw, [60, ty, W-60, ty+80], radius=16,
                         fill=D_SECONDARY_CONTAINER if selected else D_SURFACE,
                         outline=D_ON_SURFACE if selected else D_OUTLINE, width=2 if selected else 1)
        draw.text((100, ty+20), label, fill=D_ON_SURFACE, font=font_subtitle)
        rx = W - 130
        draw.ellipse([rx, ty+22, rx+36, ty+58], outline=D_ON_SURFACE if selected else D_OUTLINE, width=2)
        if selected:
            draw.ellipse([rx+8, ty+30, rx+28, ty+50], fill=D_ON_SURFACE)
        ty += 95

    # About
    ty += 30
    draw.text((60, ty), "About", fill=D_ON_SURFACE, font=font_title)
    draw.line([60, ty+50, 200, ty+50], fill=D_ON_SURFACE, width=3)
    ty += 70

    draw_rounded_rect(draw, [60, ty, W-60, ty+260], radius=16, outline=D_OUTLINE, width=1)
    about_items = [
        ("App Name", "Chaowalit Portfolio"),
        ("Developer", "Chaowalit Greepoke"),
        ("Version", "1.0.0"),
        ("Platform", "Android & iOS"),
    ]
    ay = ty + 20
    for label, value in about_items:
        draw.text((90, ay), label, fill=D_ON_SURFACE_VARIANT, font=font_body)
        draw.text((90, ay+32), value, fill=D_ON_SURFACE, font=font_body)
        ay += 65
        if ay < ty + 260 - 30:
            draw.line([90, ay-10, W-90, ay-10], fill=D_OUTLINE, width=1)

    # Dark nav bar
    y_start = H - 120
    draw.rectangle([0, y_start, W, H], fill=D_NAV_BAR_BG)
    draw.line([0, y_start, W, y_start], fill=D_OUTLINE, width=1)
    tabs = [("Home","⌂"),("Projects","▦"),("About","●"),("Contact","✉"),("Settings","⚙")]
    tab_w = W // 5
    for i, (label, icon) in enumerate(tabs):
        cx = tab_w * i + tab_w // 2
        color = D_ON_SURFACE if i == 4 else D_ON_SURFACE_VARIANT
        if i == 4:
            draw.rounded_rectangle([cx-30, y_start+15, cx+30, y_start+60], radius=20, fill=D_PRIMARY_CONTAINER)
        draw.text((cx-8, y_start+20), icon, fill=color, font=font_icon)
        draw.text((cx-20, y_start+70), label, fill=color, font=font_tiny)

    img.save(os.path.join(OUTPUT_DIR, "phone_screenshot_6_dark_mode.png"))
    print("✓ Dark Mode screenshot saved")


if __name__ == "__main__":
    screenshot_home()
    screenshot_projects()
    screenshot_project_detail()
    screenshot_settings()
    screenshot_about()
    screenshot_dark_mode()
    print(f"\n✅ All 6 screenshots saved to {OUTPUT_DIR}/")
    print("Files:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        if f.endswith('.png'):
            path = os.path.join(OUTPUT_DIR, f)
            size = os.path.getsize(path)
            print(f"  {f} ({size//1024}KB)")
