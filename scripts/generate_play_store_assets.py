#!/usr/bin/env python3
"""Generate Google Play Store graphics for Chaowalit Portfolio app."""

from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = "/home/bookchaowalit/book-everything/solo-empire/domains/product/engineering/book-dev/book-apps/portfolio/bookchaowalit-portfolio-mobile/play-store-assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Colors - B&W monochrome design system
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY_DARK = (30, 30, 30)
GRAY_MID = (100, 100, 100)
GRAY_LIGHT = (200, 200, 200)
GRAY_BG = (245, 245, 245)

def get_font(size, bold=False):
    """Get a font, falling back to default if needed."""
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for path in font_paths:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def generate_app_icon():
    """Generate 512x512 app icon."""
    size = 512
    img = Image.new('RGB', (size, size), BLACK)
    draw = ImageDraw.Draw(img)
    
    # Draw a subtle border
    border = 20
    draw.rounded_rectangle([border, border, size-border, size-border], radius=80, outline=GRAY_MID, width=3)
    
    # Draw "C" initial
    font = get_font(280, bold=True)
    text = "C"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (size - text_w) // 2 - bbox[0]
    y = (size - text_h) // 2 - bbox[1] - 20
    draw.text((x, y), text, fill=WHITE, font=font)
    
    # Draw small dot accent
    dot_size = 24
    draw.ellipse([size//2 - dot_size//2, size - 80, size//2 + dot_size//2, size - 80 + dot_size], fill=WHITE)
    
    img.save(os.path.join(OUTPUT_DIR, "app-icon-512.png"))
    print("✓ App icon generated: app-icon-512.png")

def generate_feature_graphic():
    """Generate 1024x500 feature graphic."""
    width, height = 1024, 500
    img = Image.new('RGB', (width, height), BLACK)
    draw = ImageDraw.Draw(img)
    
    # Draw subtle grid pattern
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=GRAY_DARK, width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=GRAY_DARK, width=1)
    
    # Draw accent line
    draw.rectangle([60, 180, 68, 320], fill=WHITE)
    
    # Title text
    font_title = get_font(56, bold=True)
    draw.text((90, 180), "Chaowalit", fill=WHITE, font=font_title)
    
    font_subtitle = get_font(48, bold=False)
    draw.text((90, 250), "Portfolio", fill=GRAY_LIGHT, font=font_subtitle)
    
    # Tagline
    font_tag = get_font(22, bold=False)
    draw.text((90, 320), "Mobile Apps  •  Projects  •  Skills", fill=GRAY_MID, font=font_tag)
    
    # Decorative elements on right
    for i, y in enumerate([100, 160, 220, 280, 340]):
        box_w = 120 + (i % 3) * 30
        draw.rounded_rectangle([width - box_w - 60, y, width - 60, y + 40], radius=8, outline=GRAY_MID, width=2)
    
    img.save(os.path.join(OUTPUT_DIR, "feature-graphic-1024x500.png"))
    print("✓ Feature graphic generated: feature-graphic-1024x500.png")

def generate_phone_screenshot(variant=1):
    """Generate 1080x1920 phone screenshot mockup."""
    width, height = 1080, 1920
    img = Image.new('RGB', (width, height), WHITE)
    draw = ImageDraw.Draw(img)
    
    # Status bar
    draw.rectangle([0, 0, width, 80], fill=GRAY_BG)
    font_small = get_font(28)
    draw.text((40, 25), "9:41", fill=BLACK, font=font_small)
    draw.text((width - 120, 25), "100%", fill=BLACK, font=font_small)
    
    # App bar
    draw.rectangle([0, 80, width, 200], fill=WHITE)
    font_app = get_font(36, bold=True)
    draw.text((40, 115), "Portfolio", fill=BLACK, font=font_app)
    draw.line([(0, 200), (width, 200)], fill=GRAY_LIGHT, width=2)
    
    if variant == 1:
        # Hero section
        draw.rectangle([0, 200, width, 600], fill=GRAY_BG)
        font_name = get_font(64, bold=True)
        draw.text((60, 280), "Chaowalit", fill=BLACK, font=font_name)
        draw.text((60, 360), "Greepoke", fill=BLACK, font=font_name)
        
        font_role = get_font(32)
        draw.text((60, 460), "Full-Stack Developer & Solopreneur", fill=GRAY_MID, font=font_role)
        
        # Accent bar
        draw.rectangle([60, 540, 200, 548], fill=BLACK)
        
    elif variant == 2:
        # Skills section
        draw.rectangle([0, 200, width, 300], fill=WHITE)
        draw.rectangle([60, 230, 68, 280], fill=BLACK)
        font_section = get_font(40, bold=True)
        draw.text((90, 230), "Skills", fill=BLACK, font=font_section)
        
        # Skill chips
        skills = ["Flutter", "Dart", "Next.js", "React", "TypeScript", "Python", "Node.js", "Cloudflare"]
        x, y = 60, 340
        font_chip = get_font(28)
        for skill in skills:
            bbox = draw.textbbox((0, 0), skill, font=font_chip)
            w = bbox[2] - bbox[0] + 40
            if x + w > width - 60:
                x = 60
                y += 70
            draw.rounded_rectangle([x, y, x + w, y + 50], radius=25, outline=GRAY_MID, width=2)
            draw.text((x + 20, y + 10), skill, fill=BLACK, font=font_chip)
            x += w + 15
    
    elif variant == 3:
        # Projects section
        draw.rectangle([0, 200, width, 300], fill=WHITE)
        draw.rectangle([60, 230, 68, 280], fill=BLACK)
        font_section = get_font(40, bold=True)
        draw.text((90, 230), "Projects", fill=BLACK, font=font_section)
        
        # Project cards
        projects = [
            ("Portfolio Mobile App", "Flutter • Dart • iOS/Android"),
            ("Web Platform", "Next.js • React • TypeScript"),
            ("Automation System", "Python • Cloudflare Workers"),
        ]
        y = 340
        font_proj = get_font(32, bold=True)
        font_tech = get_font(24)
        for name, tech in projects:
            draw.rounded_rectangle([60, y, width - 60, y + 180], radius=16, outline=GRAY_LIGHT, width=2)
            draw.text((90, y + 30), name, fill=BLACK, font=font_proj)
            draw.text((90, y + 80), tech, fill=GRAY_MID, font=font_tech)
            # Arrow
            draw.text((width - 120, y + 60), "→", fill=GRAY_MID, font=font_tech)
            y += 220
    
    elif variant == 4:
        # Contact section
        draw.rectangle([0, 200, width, 300], fill=WHITE)
        draw.rectangle([60, 230, 68, 280], fill=BLACK)
        font_section = get_font(40, bold=True)
        draw.text((90, 230), "Contact", fill=BLACK, font=font_section)
        
        contacts = [
            ("Email", "bookchaowalit@gmail.com"),
            ("GitHub", "github.com/bookchaowalit"),
            ("Website", "bookchaowalit.com"),
        ]
        y = 340
        font_label = get_font(28, bold=True)
        font_value = get_font(24)
        for label, value in contacts:
            draw.rounded_rectangle([60, y, width - 60, y + 120], radius=12, outline=GRAY_LIGHT, width=2)
            draw.text((90, y + 20), label, fill=BLACK, font=font_label)
            draw.text((90, y + 60), value, fill=GRAY_MID, font=font_value)
            y += 150
    
    # Bottom nav bar
    draw.rectangle([0, height - 100, width, height], fill=GRAY_BG)
    draw.line([(0, height - 100), (width, height - 100)], fill=GRAY_LIGHT, width=2)
    font_nav = get_font(22)
    nav_items = ["Home", "Projects", "Skills", "Contact"]
    nav_width = width // len(nav_items)
    for i, item in enumerate(nav_items):
        x = nav_width * i + nav_width // 2 - 30
        draw.text((x, height - 70), item, fill=GRAY_MID if i > 0 else BLACK, font=font_nav)
    
    img.save(os.path.join(OUTPUT_DIR, f"phone-screenshot-{variant}-1080x1920.png"))
    print(f"✓ Phone screenshot {variant} generated: phone-screenshot-{variant}-1080x1920.png")

def generate_tablet_screenshot(size_name, width, height):
    """Generate tablet screenshot mockup."""
    img = Image.new('RGB', (width, height), WHITE)
    draw = ImageDraw.Draw(img)
    
    # Status bar
    draw.rectangle([0, 0, width, 60], fill=GRAY_BG)
    
    # App bar
    draw.rectangle([0, 60, width, 150], fill=WHITE)
    font_app = get_font(32, bold=True)
    draw.text((40, 85), "Portfolio", fill=BLACK, font=font_app)
    draw.line([(0, 150), (width, 150)], fill=GRAY_LIGHT, width=2)
    
    # Hero section
    draw.rectangle([0, 150, width, 400], fill=GRAY_BG)
    font_name = get_font(52, bold=True)
    draw.text((50, 200), "Chaowalit Greepoke", fill=BLACK, font=font_name)
    font_role = get_font(28)
    draw.text((50, 280), "Full-Stack Developer & Solopreneur", fill=GRAY_MID, font=font_role)
    draw.rectangle([50, 340, 180, 348], fill=BLACK)
    
    # Content grid (2 columns)
    font_section = get_font(32, bold=True)
    draw.rectangle([50, 430, 56, 470], fill=BLACK)
    draw.text((75, 430), "Skills", fill=BLACK, font=font_section)
    
    skills = ["Flutter", "Dart", "Next.js", "React", "TypeScript", "Python"]
    font_chip = get_font(22)
    x, y = 50, 500
    for skill in skills:
        bbox = draw.textbbox((0, 0), skill, font=font_chip)
        w = bbox[2] - bbox[0] + 30
        if x + w > width - 50:
            x = 50
            y += 55
        draw.rounded_rectangle([x, y, x + w, y + 40], radius=20, outline=GRAY_MID, width=2)
        draw.text((x + 15, y + 8), skill, fill=BLACK, font=font_chip)
        x += w + 10
    
    img.save(os.path.join(OUTPUT_DIR, f"tablet-{size_name}-{width}x{height}.png"))
    print(f"✓ Tablet screenshot generated: tablet-{size_name}-{width}x{height}.png")

if __name__ == "__main__":
    print("Generating Google Play Store assets...\n")
    
    generate_app_icon()
    generate_feature_graphic()
    
    # Phone screenshots (4 variants)
    for i in range(1, 5):
        generate_phone_screenshot(i)
    
    # Tablet screenshots
    generate_tablet_screenshot("7inch", 1200, 1920)  # 7-inch tablet
    generate_tablet_screenshot("10inch", 1600, 2560)  # 10-inch tablet
    
    print(f"\n✓ All assets saved to: {OUTPUT_DIR}")
    print("\nUpload these to Google Play Console:")
    print("  • app-icon-512.png → App icon")
    print("  • feature-graphic-1024x500.png → Feature graphic")
    print("  • phone-screenshot-1-1080x1920.png through 4 → Phone screenshots")
    print("  • tablet-7inch-1200x1920.png → 7-inch tablet screenshots")
    print("  • tablet-10inch-1600x2560.png → 10-inch tablet screenshots")
