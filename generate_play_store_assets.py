#!/usr/bin/env python3
"""Generate missing Google Play Store assets: app icon, feature graphic, tablet screenshots."""

from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = "screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Colors
BG = (255, 255, 255)
PRIMARY = (20, 20, 20)
ACCENT = (102, 102, 255)
ON_SURFACE = (20, 20, 20)
ON_SURFACE_VARIANT = (100, 100, 100)
SECONDARY_CONTAINER = (240, 240, 240)
OUTLINE = (200, 200, 200)
WHITE = (255, 255, 255)
GRADIENT_LIGHT = (235, 235, 235)
GRADIENT_MID = (210, 210, 210)

# Dark mode
D_BG = (20, 20, 20)
D_SURFACE = (30, 30, 30)
D_ON_SURFACE = (240, 240, 240)
D_ON_SURFACE_VARIANT = (170, 170, 170)
D_OUTLINE = (60, 60, 60)
D_SECONDARY_CONTAINER = (50, 50, 50)

try:
    font_xl = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 180)
    font_huge = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 120)
    font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 52)
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 38)
    font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
    font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    font_tiny = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    font_icon = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
    font_feat_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)
    font_feat_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 42)
except:
    font_xl = ImageFont.load_default()
    font_huge = font_xl
    font_large = font_xl
    font_title = font_xl
    font_subtitle = font_xl
    font_body = font_xl
    font_small = font_xl
    font_tiny = font_xl
    font_icon = font_xl
    font_feat_title = font_xl
    font_feat_sub = font_xl


def draw_rounded_rect(draw, bbox, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)


# ============================================================
# 1. APP ICON (512x512)
# ============================================================
def generate_app_icon():
    size = 512
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Background - rounded square with gradient effect
    margin = 20
    for y in range(margin, size - margin):
        ratio = (y - margin) / (size - 2 * margin)
        r = int(20 + 10 * ratio)
        g = int(20 + 10 * ratio)
        b = int(20 + 10 * ratio)
        draw.line([margin, y, size - margin, y], fill=(r, g, b))

    # Round the corners
    mask = Image.new('L', (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, size-1, size-1], radius=100, fill=255)
    img.putalpha(mask)

    # Draw the "C" letter
    c_bbox = draw.textbbox((0, 0), "C", font=font_xl)
    tw = c_bbox[2] - c_bbox[0]
    th = c_bbox[3] - c_bbox[1]
    cx = (size - tw) // 2
    cy = (size - th) // 2 - 10
    draw.text((cx, cy), "C", fill=WHITE, font=font_xl)

    # Subtle accent line at bottom
    draw.rectangle([margin + 40, size - margin - 30, size - margin - 40, size - margin - 20], fill=ACCENT)

    # Save as PNG with transparency
    img.save(os.path.join(OUTPUT_DIR, "app_icon_512.png"))
    print("✓ App icon (512x512) saved")


# ============================================================
# 2. FEATURE GRAPHIC (1024x500)
# ============================================================
def generate_feature_graphic():
    W, H = 1024, 500
    img = Image.new('RGB', (W, H), PRIMARY)
    draw = ImageDraw.Draw(img)

    # Gradient background
    for y in range(H):
        ratio = y / H
        r = int(20 + 30 * ratio)
        g = int(20 + 30 * ratio)
        b = int(30 + 40 * ratio)
        draw.line([0, y, W, y], fill=(r, g, b))

    # Decorative elements - subtle grid dots
    for x in range(0, W, 40):
        for y in range(0, H, 40):
            draw.ellipse([x-1, y-1, x+1, y+1], fill=(50, 50, 60))

    # Accent bar on left
    draw.rectangle([0, 0, 8, H], fill=ACCENT)

    # Large "C" avatar
    avatar_x, avatar_y = 80, 100
    draw.rounded_rectangle([avatar_x, avatar_y, avatar_x+200, avatar_y+200], radius=40, fill=WHITE)
    c_bbox = draw.textbbox((0, 0), "C", font=font_huge)
    tw = c_bbox[2] - c_bbox[0]
    th = c_bbox[3] - c_bbox[1]
    draw.text((avatar_x + (200-tw)//2, avatar_y + (200-th)//2 - 15), "C", fill=PRIMARY, font=font_huge)

    # Title text
    text_x = 330
    draw.text((text_x, 100), "Chaowalit Greepoke", fill=WHITE, font=font_feat_title)
    draw.text((text_x, 185), "Generalist & Solopreneur", fill=ACCENT, font=font_feat_sub)

    # Separator
    draw.rectangle([text_x, 250, text_x + 400, 253], fill=ACCENT)

    # Feature highlights
    features = [
        "📱  Cross-Platform Mobile Apps",
        "🌐  Full-Stack Web Development",
        "🤖  AI & Automation Systems",
    ]
    fy = 280
    for feat in features:
        draw.text((text_x, fy), feat, fill=(200, 200, 200), font=font_body)
        fy += 50

    # Right side - decorative phone mockup
    phone_x, phone_y = W - 250, 60
    draw.rounded_rectangle([phone_x, phone_y, phone_x+180, phone_y+380], radius=20, outline=(60, 60, 70), width=3)
    draw.rounded_rectangle([phone_x+10, phone_y+40, phone_x+170, phone_y+340], radius=4, fill=(40, 40, 50))
    # Mini content inside phone
    draw.rectangle([phone_x+20, phone_y+50, phone_x+160, phone_y+80], fill=(50, 50, 60))
    draw.rectangle([phone_x+20, phone_y+90, phone_x+100, phone_y+110], fill=ACCENT)
    draw.rectangle([phone_x+20, phone_y+120, phone_x+160, phone_y+200], fill=(45, 45, 55))
    draw.rectangle([phone_x+20, phone_y+210, phone_x+160, phone_y+290], fill=(45, 45, 55))

    img.save(os.path.join(OUTPUT_DIR, "feature_graphic_1024x500.png"))
    print("✓ Feature graphic (1024x500) saved")


# ============================================================
# 3. TABLET SCREENSHOTS (7-inch: 1200x1920, 10-inch: 1600x2560)
# ============================================================
def draw_status_bar_tablet(draw, W, dark=False):
    bg = (25, 25, 25) if dark else (245, 245, 245)
    text_color = (240, 240, 240) if dark else (20, 20, 20)
    draw.rectangle([0, 0, W, 60], fill=bg)
    draw.text((30, 15), "9:41", fill=text_color, font=font_small)
    draw.rectangle([W-100, 20, W-30, 40], outline=text_color, width=2)
    draw.rectangle([W-98, 22, W-50, 38], fill=text_color)


def draw_nav_bar_tablet(draw, W, H, selected_index, dark=False):
    bg = (25, 25, 25) if dark else (250, 250, 250)
    border = (60, 60, 60) if dark else (200, 200, 200)
    text_color = (240, 240, 240) if dark else (20, 20, 20)
    variant = (170, 170, 170) if dark else (100, 100, 100)
    y_start = H - 90
    draw.rectangle([0, y_start, W, H], fill=bg)
    draw.line([0, y_start, W, y_start], fill=border, width=1)

    tabs = [("Home","⌂"),("Projects","▦"),("About","●"),("Contact","✉"),("Settings","⚙")]
    tab_w = W // 5
    for i, (label, icon) in enumerate(tabs):
        cx = tab_w * i + tab_w // 2
        color = text_color if i == selected_index else variant
        draw.text((cx-12, y_start+10), icon, fill=color, font=font_icon)
        draw.text((cx-20, y_start+50), label, fill=color, font=font_tiny)


def generate_tablet_screenshot(tablet_type="7inch"):
    if tablet_type == "7inch":
        W, H = 1200, 1920
    else:
        W, H = 1600, 2560

    scale = W / 1080  # scale factor from phone

    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)

    draw_status_bar_tablet(draw, W)

    # Hero section
    for y in range(60, int(500 * scale)):
        alpha = max(0, 1.0 - (y - 60) / (440 * scale))
        c = int(230 * alpha + 255 * (1 - alpha))
        draw.line([0, y, W, y], fill=(c, c, c))

    # Avatar
    av_size = int(160 * scale)
    margin = int(60 * scale)
    draw.ellipse([margin, int(140*scale), margin+av_size, int(140*scale)+av_size], fill=PRIMARY)
    c_bbox = draw.textbbox((0,0), "C", font=font_huge if tablet_type == "10inch" else font_large)
    tw = c_bbox[2] - c_bbox[0]
    th = c_bbox[3] - c_bbox[1]
    draw.text((margin + (av_size-tw)//2, int(140*scale) + (av_size-th)//2 - int(15*scale)), "C", fill=BG, font=font_huge if tablet_type == "10inch" else font_large)

    # Name
    text_x = margin
    name_y = int(140*scale) + av_size + int(30*scale)
    draw.text((text_x, name_y), "Chaowalit Greepoke", fill=ON_SURFACE, font=font_feat_title if tablet_type == "10inch" else font_large)
    draw.text((text_x, name_y + int(70*scale)), "Generalist & Solopreneur", fill=ACCENT, font=font_feat_sub if tablet_type == "10inch" else font_title)
    draw.text((text_x, name_y + int(120*scale)), "Building full-stack products, integrating AI systems,", fill=ON_SURFACE_VARIANT, font=font_body)
    draw.text((text_x, name_y + int(155*scale)), "and growing digital presence — from idea to deployment.", fill=ON_SURFACE_VARIANT, font=font_body)

    # Buttons
    btn_y = name_y + int(200*scale)
    draw_rounded_rect(draw, [margin, btn_y, margin+int(260*scale), btn_y+int(60*scale)], radius=30, fill=PRIMARY)
    draw.text((margin+int(50*scale), btn_y+int(12*scale)), "✉  Hire Me", fill=BG, font=font_body)
    draw_rounded_rect(draw, [margin+int(290*scale), btn_y, margin+int(560*scale), btn_y+int(60*scale)], radius=30, outline=PRIMARY, width=2)
    draw.text((margin+int(335*scale), btn_y+int(12*scale)), "🌐  Website", fill=PRIMARY, font=font_body)

    # About section
    sec_y = btn_y + int(120*scale)
    draw.text((margin, sec_y), "About", fill=ON_SURFACE, font=font_title)
    draw.line([margin, sec_y+int(50*scale), margin+int(140*scale), sec_y+int(50*scale)], fill=PRIMARY, width=3)
    draw.text((margin, sec_y+int(70*scale)), "Generalist & Solopreneur building full-stack products,", fill=ON_SURFACE_VARIANT, font=font_body)
    draw.text((margin, sec_y+int(105*scale)), "integrating AI systems, and growing digital presence.", fill=ON_SURFACE_VARIANT, font=font_body)

    # Info chips
    chip_y = sec_y + int(160*scale)
    chips = ["📍 Bangkok", "💼 3+ Years", "💻 Full-Stack", "✨ AI"]
    cx = margin
    for chip in chips:
        tw = len(chip) * 16 + 30
        draw_rounded_rect(draw, [cx, chip_y, cx+tw, chip_y+45], radius=15, fill=SECONDARY_CONTAINER)
        draw.text((cx+15, chip_y+8), chip, fill=ON_SURFACE_VARIANT, font=font_small)
        cx += tw + 15

    # Tech Stack
    ts_y = chip_y + int(90*scale)
    draw.text((margin, ts_y), "Tech Stack", fill=ON_SURFACE, font=font_title)
    draw.line([margin, ts_y+int(50*scale), margin+int(200*scale), ts_y+int(50*scale)], fill=PRIMARY, width=3)
    skills = ["Flutter", "Dart", "Next.js", "React", "TypeScript", "Python", "FastAPI", "PostgreSQL", "Docker", "AWS"]
    sx, sy = margin, ts_y + int(70*scale)
    for skill in skills:
        tw = len(skill) * 16 + 30
        if sx + tw > W - margin:
            sx = margin
            sy += 50
        draw_rounded_rect(draw, [sx, sy, sx+tw, sy+40], radius=12, fill=SECONDARY_CONTAINER)
        draw.text((sx+15, sy+6), skill, fill=ON_SURFACE_VARIANT, font=font_small)
        sx += tw + 12

    # Featured Projects
    fp_y = sy + int(80*scale)
    draw.text((margin, fp_y), "Featured Projects", fill=ON_SURFACE, font=font_title)
    draw.line([margin, fp_y+int(50*scale), margin+int(320*scale), fp_y+int(50*scale)], fill=PRIMARY, width=3)

    projects = [
        ("Portfolio Website", "Next.js portfolio with MDX blog", ["Next.js", "React"]),
        ("AI Trading Bot", "Automated crypto trading system", ["Python", "AI"]),
        ("E-Commerce Platform", "Full-stack online store", ["Flutter", "Firebase"]),
    ]
    py = fp_y + int(70*scale)
    for name, desc, tags in projects:
        card_h = int(140 * scale)
        draw_rounded_rect(draw, [margin, py, W-margin, py+card_h], radius=16, outline=OUTLINE, width=2)
        draw.text((margin+30, py+15), name, fill=ON_SURFACE, font=font_subtitle)
        draw.text((margin+30, py+60), desc, fill=ON_SURFACE_VARIANT, font=font_small)
        tx = margin + 30
        for tag in tags:
            tw = len(tag) * 14 + 20
            draw_rounded_rect(draw, [tx, py+card_h-45, tx+tw, py+card_h-12], radius=8, fill=SECONDARY_CONTAINER)
            draw.text((tx+10, py+card_h-42), tag, fill=ON_SURFACE_VARIANT, font=font_tiny)
            tx += tw + 8
        draw.text((W-margin-60, py+20), "→", fill=ON_SURFACE_VARIANT, font=font_icon)
        py += card_h + 15

    draw_nav_bar_tablet(draw, W, H, 0)

    filename = f"tablet_7inch_screenshot_1_home.png" if tablet_type == "7inch" else f"tablet_10inch_screenshot_1_home.png"
    img.save(os.path.join(OUTPUT_DIR, filename))
    print(f"✓ {tablet_type} tablet screenshot ({W}x{H}) saved")


def generate_tablet_projects(tablet_type="7inch"):
    if tablet_type == "7inch":
        W, H = 1200, 1920
    else:
        W, H = 1600, 2560

    scale = W / 1080
    margin = int(60 * scale)

    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)

    draw_status_bar_tablet(draw, W)

    # Header
    for y in range(60, int(280*scale)):
        alpha = max(0, 1.0 - (y - 60) / (220*scale))
        c = int(230 * alpha + 255 * (1 - alpha))
        draw.line([0, y, W, y], fill=(c, c, c))

    draw.text((margin, int(120*scale)), "Projects", fill=ON_SURFACE, font=font_feat_title if tablet_type == "10inch" else font_large)
    draw.line([margin, int(190*scale), margin+int(180*scale), int(190*scale)], fill=PRIMARY, width=3)
    draw.text((margin, int(210*scale)), "A selection of projects I've built — from web apps to mobile and automation.", fill=ON_SURFACE_VARIANT, font=font_body)

    projects = [
        ("Portfolio Website", "Next.js portfolio with MDX blog, dark mode, SEO optimization", ["Next.js", "React", "TypeScript", "MDX"]),
        ("AI Trading Bot", "Automated cryptocurrency trading with ML predictions", ["Python", "TensorFlow", "Binance API"]),
        ("E-Commerce Platform", "Full-stack online store with payment processing", ["Flutter", "Firebase", "Stripe"]),
        ("Task Automation CLI", "CLI tool for automating dev workflows", ["Python", "Docker", "CI/CD"]),
        ("Real-time Chat App", "WebSocket chat with rooms and file sharing", ["Node.js", "Socket.io", "MongoDB"]),
        ("Weather Dashboard", "Interactive weather visualization with forecasts", ["React", "D3.js", "OpenWeather"]),
        ("Fitness Tracker", "Mobile app for workouts and nutrition", ["Flutter", "SQLite", "Charts"]),
        ("Blog CMS", "Headless CMS with markdown editor", ["FastAPI", "PostgreSQL", "S3"]),
    ]

    py = int(300 * scale)
    for i, (name, desc, tags) in enumerate(projects):
        card_h = int(160 * scale)
        # Two columns for 10-inch
        if tablet_type == "10inch" and i % 2 == 0:
            col = 0
            row = i // 2
            px = margin
        elif tablet_type == "10inch":
            col = 1
            row = i // 2
            px = W // 2 + 10
        else:
            col = 0
            row = i
            px = margin

        if tablet_type == "10inch":
            card_w = W // 2 - margin - 10
            if col == 0:
                draw_rounded_rect(draw, [px, py + row * (card_h+15), px+card_w, py + row*(card_h+15)+card_h], radius=16, outline=OUTLINE, width=2)
                draw.text((px+25, py + row*(card_h+15)+15), name, fill=ON_SURFACE, font=font_subtitle)
                draw.text((px+25, py + row*(card_h+15)+60), desc[:50], fill=ON_SURFACE_VARIANT, font=font_small)
                tx = px + 25
                for tag in tags[:3]:
                    tw = len(tag)*14+20
                    draw_rounded_rect(draw, [tx, py+row*(card_h+15)+card_h-40, tx+tw, py+row*(card_h+15)+card_h-8], radius=8, fill=SECONDARY_CONTAINER)
                    draw.text((tx+10, py+row*(card_h+15)+card_h-38), tag, fill=ON_SURFACE_VARIANT, font=font_tiny)
                    tx += tw + 8
            else:
                draw_rounded_rect(draw, [px, py + row*(card_h+15), px+card_w, py+row*(card_h+15)+card_h], radius=16, outline=OUTLINE, width=2)
                draw.text((px+25, py+row*(card_h+15)+15), name, fill=ON_SURFACE, font=font_subtitle)
                draw.text((px+25, py+row*(card_h+15)+60), desc[:50], fill=ON_SURFACE_VARIANT, font=font_small)
                tx = px + 25
                for tag in tags[:3]:
                    tw = len(tag)*14+20
                    draw_rounded_rect(draw, [tx, py+row*(card_h+15)+card_h-40, tx+tw, py+row*(card_h+15)+card_h-8], radius=8, fill=SECONDARY_CONTAINER)
                    draw.text((tx+10, py+row*(card_h+15)+card_h-38), tag, fill=ON_SURFACE_VARIANT, font=font_tiny)
                    tx += tw + 8
        else:
            draw_rounded_rect(draw, [margin, py, W-margin, py+card_h], radius=16, outline=OUTLINE, width=2)
            draw.text((margin+25, py+15), name, fill=ON_SURFACE, font=font_subtitle)
            draw.text((margin+25, py+60), desc[:60], fill=ON_SURFACE_VARIANT, font=font_small)
            tx = margin + 25
            for tag in tags[:3]:
                tw = len(tag)*14+20
                draw_rounded_rect(draw, [tx, py+card_h-40, tx+tw, py+card_h-8], radius=8, fill=SECONDARY_CONTAINER)
                draw.text((tx+10, py+card_h-38), tag, fill=ON_SURFACE_VARIANT, font=font_tiny)
                tx += tw + 8
            draw.text((W-margin-50, py+20), "→", fill=ON_SURFACE_VARIANT, font=font_icon)
            py += card_h + 15

    draw_nav_bar_tablet(draw, W, H, 1)

    filename = f"tablet_7inch_screenshot_2_projects.png" if tablet_type == "7inch" else f"tablet_10inch_screenshot_2_projects.png"
    img.save(os.path.join(OUTPUT_DIR, filename))
    print(f"✓ {tablet_type} tablet projects screenshot saved")


def generate_tablet_settings(tablet_type="7inch"):
    if tablet_type == "7inch":
        W, H = 1200, 1920
    else:
        W, H = 1600, 2560

    scale = W / 1080
    margin = int(60 * scale)

    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)

    draw_status_bar_tablet(draw, W)

    # Header
    for y in range(60, int(240*scale)):
        alpha = max(0, 1.0 - (y - 60) / (180*scale))
        c = int(230 * alpha + 255 * (1 - alpha))
        draw.line([0, y, W, y], fill=(c, c, c))

    draw.text((margin, int(120*scale)), "Settings", fill=ON_SURFACE, font=font_feat_title if tablet_type == "10inch" else font_large)
    draw.line([margin, int(190*scale), margin+int(210*scale), int(190*scale)], fill=PRIMARY, width=3)

    # Appearance
    sec_y = int(240*scale)
    draw.text((margin, sec_y), "Appearance", fill=ON_SURFACE, font=font_title)
    draw.line([margin, sec_y+50, margin+int(200*scale), sec_y+50], fill=PRIMARY, width=3)

    themes = [("System Default", "⚙", True), ("Light Mode", "☀", False), ("Dark Mode", "☾", False)]
    ty = sec_y + 70
    for label, icon, selected in themes:
        draw_rounded_rect(draw, [margin, ty, W-margin, ty+80], radius=16,
                         fill=SECONDARY_CONTAINER if selected else BG,
                         outline=PRIMARY if selected else OUTLINE, width=2 if selected else 1)
        draw.text((margin+40, ty+20), f"{icon}  {label}", fill=ON_SURFACE, font=font_subtitle)
        rx = W - margin - 80
        draw.ellipse([rx, ty+22, rx+36, ty+58], outline=PRIMARY if selected else OUTLINE, width=2)
        if selected:
            draw.ellipse([rx+8, ty+30, rx+28, ty+50], fill=PRIMARY)
        ty += 95

    # Language
    ty += 30
    draw.text((margin, ty), "Language", fill=ON_SURFACE, font=font_title)
    draw.line([margin, ty+50, margin+int(170*scale), ty+50], fill=PRIMARY, width=3)
    ty += 70

    langs = [("🇬🇧  English", True), ("🇹🇭  ภาษาไทย", False)]
    for label, selected in langs:
        draw_rounded_rect(draw, [margin, ty, W-margin, ty+80], radius=16,
                         fill=SECONDARY_CONTAINER if selected else BG,
                         outline=PRIMARY if selected else OUTLINE, width=2 if selected else 1)
        draw.text((margin+40, ty+20), label, fill=ON_SURFACE, font=font_subtitle)
        rx = W - margin - 80
        draw.ellipse([rx, ty+22, rx+36, ty+58], outline=PRIMARY if selected else OUTLINE, width=2)
        if selected:
            draw.ellipse([rx+8, ty+30, rx+28, ty+50], fill=PRIMARY)
        ty += 95

    # About
    ty += 40
    draw.text((margin, ty), "About", fill=ON_SURFACE, font=font_title)
    draw.line([margin, ty+50, margin+int(140*scale), ty+50], fill=PRIMARY, width=3)
    ty += 70

    draw_rounded_rect(draw, [margin, ty, W-margin, ty+260], radius=16, outline=OUTLINE, width=1)
    about_items = [("App Name", "Chaowalit Portfolio"), ("Developer", "Chaowalit Greepoke"), ("Version", "1.0.0"), ("Platform", "Android & iOS")]
    ay = ty + 20
    for label, value in about_items:
        draw.text((margin+30, ay), label, fill=ON_SURFACE_VARIANT, font=font_body)
        draw.text((margin+30, ay+32), value, fill=ON_SURFACE, font=font_body)
        ay += 65
        if ay < ty + 260 - 30:
            draw.line([margin+30, ay-10, W-margin-30, ay-10], fill=OUTLINE, width=1)

    draw_nav_bar_tablet(draw, W, H, 4)

    filename = f"tablet_7inch_screenshot_3_settings.png" if tablet_type == "7inch" else f"tablet_10inch_screenshot_3_settings.png"
    img.save(os.path.join(OUTPUT_DIR, filename))
    print(f"✓ {tablet_type} tablet settings screenshot saved")


if __name__ == "__main__":
    generate_app_icon()
    generate_feature_graphic()
    generate_tablet_screenshot("7inch")
    generate_tablet_screenshot("10inch")
    generate_tablet_projects("7inch")
    generate_tablet_projects("10inch")
    generate_tablet_settings("7inch")
    generate_tablet_settings("10inch")

    print(f"\n✅ All assets saved to {OUTPUT_DIR}/")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        if f.endswith('.png'):
            path = os.path.join(OUTPUT_DIR, f)
            size = os.path.getsize(path)
            img = Image.open(path)
            print(f"  {f}  ({img.size[0]}x{img.size[1]}, {size//1024}KB)")
