import os

from pathlib import Path
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO = Image.open(os.path.join(BASE_DIR, "assets/logo.png")).convert("RGBA")
LOGO_WIDTH, LOGO_HEIGHT = LOGO.size


def process(file):
    image = Image.open(file).convert("RGBA")
    file_name = file.name.split(".")[0]
    file_ext = "jpg"
    file_name = f"{file_name}.{file_ext}"
    margin = 500
    image_widht, image_height = image.size
    x = image_widht - LOGO_WIDTH - margin
    y = image_height - LOGO_HEIGHT - margin
    # LOGO.putalpha(100)
    copied_image = image.copy()
    copied_image.paste(LOGO, (x, y), LOGO)
    copied_image.save(os.path.join(BASE_DIR, f"assets/Watermarked/{file_name}"), format="png")


for child in Path(os.path.join(BASE_DIR, "assets/Test")).iterdir():
    if child.is_file():
        process(child)
