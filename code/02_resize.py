"""
Practical 2: Resizing images
------------------------------
Demonstrates cv2.resize() to:
  - scale an image up/down by a factor
  - resize to an exact (width, height)
"""

import os
import cv2
from display_helper import show, close_all
from utils_generate_assets import generate_sample_image, IMAGE_PATH

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
os.makedirs(OUT_DIR, exist_ok=True)

if not os.path.exists(IMAGE_PATH):
    generate_sample_image()

img = cv2.imread(IMAGE_PATH)
show("Original", img)

# Resize by scale factor (half size)
half = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
show("Resized - Half", half)
cv2.imwrite(os.path.join(OUT_DIR, "02_resized_half.jpg"), half)

# Resize by scale factor (double size)
double = cv2.resize(img, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)
show("Resized - Double", double)
cv2.imwrite(os.path.join(OUT_DIR, "02_resized_double.jpg"), double)

# Resize to an exact width/height
fixed = cv2.resize(img, (300, 300), interpolation=cv2.INTER_CUBIC)
show("Resized - 300x300", fixed)
cv2.imwrite(os.path.join(OUT_DIR, "02_resized_300x300.jpg"), fixed)

print("Original size:", img.shape[:2])
print("Half size:", half.shape[:2])
print("Double size:", double.shape[:2])
print("Fixed size:", fixed.shape[:2])

close_all()
