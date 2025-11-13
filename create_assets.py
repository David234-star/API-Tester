# create_assets.py
import os
from PIL import Image, ImageDraw

# --- Configuration ---
ASSETS_DIR = "assets"
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
ICONS_DIR = os.path.join(ASSETS_DIR, "icons")

# Create directories if they don't exist
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(ICONS_DIR, exist_ok=True)

# --- 1. Generate background.png (512x512) ---


def create_background():
    """Creates a dark, tileable grid background."""
    print("Creating background.png...")
    img = Image.new('RGB', (512, 512), color='#0A0A1A')
    draw = ImageDraw.Draw(img)

    # Draw a subtle grid
    grid_color = '#1F1F3F'  # A very dark, subtle blue/purple
    for i in range(0, 512, 32):
        draw.line([(i, 0), (i, 512)], fill=grid_color, width=1)
        draw.line([(0, i), (512, i)], fill=grid_color, width=1)

    # Draw a fainter sub-grid
    sub_grid_color = '#10102A'
    for i in range(0, 512, 8):
        if i % 32 != 0:  # Avoid drawing over the main grid
            draw.line([(i, 0), (i, 512)], fill=sub_grid_color, width=1)
            draw.line([(0, i), (512, i)], fill=sub_grid_color, width=1)

    filepath = os.path.join(IMAGES_DIR, "background.png")
    img.save(filepath)
    print(f"Saved to {filepath}")

# --- 2. Generate light_mode.png (24x24) ---


def create_light_mode_icon():
    """Creates a simple sun icon for the light mode toggle."""
    print("Creating light_mode.png...")
    img = Image.new('RGBA', (24, 24), (0, 0, 0, 0))  # Transparent background
    draw = ImageDraw.Draw(img)

    icon_color = "#E0E0FF"  # Matches light text color for visibility

    # Central circle
    draw.ellipse((7, 7, 16, 16), fill=icon_color)

    # Rays
    draw.line((11.5, 2, 11.5, 5), fill=icon_color, width=2)  # N
    draw.line((11.5, 18, 11.5, 21), fill=icon_color, width=2)  # S
    draw.line((2, 11.5, 5, 11.5), fill=icon_color, width=2)  # W
    draw.line((18, 11.5, 21, 11.5), fill=icon_color, width=2)  # E

    draw.line((5, 5, 7, 7), fill=icon_color, width=2)  # NW
    draw.line((16, 16, 18, 18), fill=icon_color, width=2)  # SE
    draw.line((5, 18, 7, 16), fill=icon_color, width=2)  # SW
    draw.line((16, 7, 18, 5), fill=icon_color, width=2)  # NE

    filepath = os.path.join(ICONS_DIR, "light_mode.png")
    img.save(filepath)
    print(f"Saved to {filepath}")

# --- 3. Generate dark_mode.png (24x24) ---


def create_dark_mode_icon():
    """Creates a simple crescent moon icon for the dark mode toggle."""
    print("Creating dark_mode.png...")
    img = Image.new('RGBA', (24, 24), (0, 0, 0, 0))  # Transparent background
    draw = ImageDraw.Draw(img)

    icon_color = "#E0E0FF"

    # Draw a filled circle, then "cut out" a smaller circle to make a crescent
    draw.ellipse((6, 4, 20, 18), fill=icon_color)
    draw.ellipse((9, 4, 23, 18), fill=(0, 0, 0, 0))  # Transparent cutout

    filepath = os.path.join(ICONS_DIR, "dark_mode.png")
    img.save(filepath)
    print(f"Saved to {filepath}")


if __name__ == "__main__":
    create_background()
    create_light_mode_icon()
    create_dark_mode_icon()
    print("\nAll assets created successfully!")
