"""
Practical 7: Thresholding (Binary threshold)
------------------------------------------------
Demonstrates converting a grayscale image to a binary image using
cv2.threshold() with the THRESH_BINARY type (and a couple of related
types for comparison).
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
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Basic binary threshold
thresh_val, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
print("Threshold value used:", thresh_val)

# Inverted binary threshold (for comparison)
_, binary_inv = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Otsu's automatic thresholding (bonus comparison)
otsu_val, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("Otsu threshold value:", otsu_val)

show("Original", img)
show("Grayscale", gray)
show("Binary Threshold", binary)
show("Binary Inverted Threshold", binary_inv)
show("Otsu Threshold", otsu)

cv2.imwrite(os.path.join(OUT_DIR, "07_gray.jpg"), gray)
cv2.imwrite(os.path.join(OUT_DIR, "07_binary_threshold.jpg"), binary)
cv2.imwrite(os.path.join(OUT_DIR, "07_binary_inv_threshold.jpg"), binary_inv)
cv2.imwrite(os.path.join(OUT_DIR, "07_otsu_threshold.jpg"), otsu)

close_all()
