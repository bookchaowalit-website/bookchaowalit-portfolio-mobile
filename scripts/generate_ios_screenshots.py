#!/usr/bin/env python3
"""Generate App Store Connect iPhone screenshots (6.7"/6.9", 1290x2796)
from the existing Android mockups in screenshots/, via scale-to-fit +
letterbox (no distortion, no cropping) rather than redrawing every screen
at a new aspect ratio.

Run generate_screenshots.py (root) first to refresh the source PNGs.
"""

from PIL import Image
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(SCRIPT_DIR, "..", "screenshots")
OUT_DIR = os.path.join(SRC_DIR, "ios")
os.makedirs(OUT_DIR, exist_ok=True)

TARGET_W, TARGET_H = 1290, 2796  # Apple's required 6.7"/6.9" iPhone screenshot size

SOURCE_FILES = [
    "phone_screenshot_1_home.png",
    "phone_screenshot_2_projects.png",
    "phone_screenshot_3_detail.png",
    "phone_screenshot_4_settings.png",
    "phone_screenshot_5_about.png",
    "phone_screenshot_6_dark_mode.png",
]


def main():
    for fname in SOURCE_FILES:
        src_path = os.path.join(SRC_DIR, fname)
        img = Image.open(src_path).convert("RGB")
        w, h = img.size

        scale = TARGET_W / w
        new_w, new_h = TARGET_W, round(h * scale)
        resized = img.resize((new_w, new_h), Image.LANCZOS)

        # Sample the source's own top-left background color so the
        # letterbox blends in seamlessly instead of showing a hard border.
        bg_color = img.getpixel((2, 2))

        canvas = Image.new("RGB", (TARGET_W, TARGET_H), bg_color)
        paste_y = (TARGET_H - new_h) // 2
        canvas.paste(resized, (0, paste_y))

        out_name = fname.replace("phone_screenshot_", "ios_iphone67_")
        out_path = os.path.join(OUT_DIR, out_name)
        canvas.save(out_path)
        print(f"✓ {out_name} ({TARGET_W}x{TARGET_H}, content {new_w}x{new_h})")


if __name__ == "__main__":
    main()
