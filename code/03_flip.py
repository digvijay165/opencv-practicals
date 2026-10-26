"""
Practical 3: Flipping images (horizontal, vertical, both)
-------------------------------------------------------------
Demonstrates cv2.flip() with flip codes:
  1  -> horizontal flip (mirror left-right)
  0  -> vertical flip (upside-down)
 -1  -> both horizontal and vertical
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

horizontal_flip = cv2.flip(img, 1)
vertical_flip = cv2.flip(img, 0)
both_flip = cv2.flip(img, -1)

show("Horizontal Flip", horizontal_flip)
show("Vertical Flip", vertical_flip)
show("Both Flip", both_flip)

cv2.imwrite(os.path.join(OUT_DIR, "03_flip_horizontal.jpg"), horizontal_flip)
cv2.imwrite(os.path.join(OUT_DIR, "03_flip_vertical.jpg"), vertical_flip)
cv2.imwrite(os.path.join(OUT_DIR, "03_flip_both.jpg"), both_flip)

close_all()
