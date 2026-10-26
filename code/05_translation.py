"""
Practical 5: Image translation (shifting) using warpAffine
----------------------------------------------------------------
Demonstrates shifting an image by (tx, ty) pixels using a translation
matrix and cv2.warpAffine().
"""

import os
import cv2
import numpy as np
from display_helper import show, close_all
from utils_generate_assets import generate_sample_image, IMAGE_PATH

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
os.makedirs(OUT_DIR, exist_ok=True)

if not os.path.exists(IMAGE_PATH):
    generate_sample_image()

img = cv2.imread(IMAGE_PATH)
(h, w) = img.shape[:2]

# Shift the image 80 px right and 50 px down
tx, ty = 80, 50
M = np.float32([[1, 0, tx],
                [0, 1, ty]])
translated = cv2.warpAffine(img, M, (w, h))

# Shift the image left and up (negative values)
tx2, ty2 = -60, -40
M2 = np.float32([[1, 0, tx2],
                  [0, 1, ty2]])
translated2 = cv2.warpAffine(img, M2, (w, h))

show("Original", img)
show("Translated (+80,+50)", translated)
show("Translated (-60,-40)", translated2)

cv2.imwrite(os.path.join(OUT_DIR, "05_translated_right_down.jpg"), translated)
cv2.imwrite(os.path.join(OUT_DIR, "05_translated_left_up.jpg"), translated2)

close_all()
