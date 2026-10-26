"""
Practical 6: Image rotation using getRotationMatrix2D and warpAffine
--------------------------------------------------------------------------
Demonstrates rotating an image about its center by an arbitrary angle.
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
(h, w) = img.shape[:2]
center = (w // 2, h // 2)


def rotate(image, angle, scale=1.0):
    M = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(image, M, (w, h))


rotated_45 = rotate(img, 45)
rotated_90 = rotate(img, 90)
rotated_180 = rotate(img, 180)
rotated_scaled = rotate(img, 30, scale=0.7)

show("Original", img)
show("Rotated 45 deg", rotated_45)
show("Rotated 90 deg", rotated_90)
show("Rotated 180 deg", rotated_180)
show("Rotated 30 deg + Scaled 0.7x", rotated_scaled)

cv2.imwrite(os.path.join(OUT_DIR, "06_rotated_45.jpg"), rotated_45)
cv2.imwrite(os.path.join(OUT_DIR, "06_rotated_90.jpg"), rotated_90)
cv2.imwrite(os.path.join(OUT_DIR, "06_rotated_180.jpg"), rotated_180)
cv2.imwrite(os.path.join(OUT_DIR, "06_rotated_30_scaled.jpg"), rotated_scaled)

close_all()
