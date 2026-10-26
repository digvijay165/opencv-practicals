"""
Practical 10: Edge detection using Canny
---------------------------------------------
Demonstrates cv2.Canny() to detect edges in an image, with a Gaussian
blur pre-processing step (common practice to reduce noise before edge
detection).
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
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges_low = cv2.Canny(blurred, 30, 90)
edges_high = cv2.Canny(blurred, 100, 200)

show("Original", img)
show("Blurred Gray", blurred)
show("Canny Edges (low thresholds)", edges_low)
show("Canny Edges (high thresholds)", edges_high)

cv2.imwrite(os.path.join(OUT_DIR, "10_canny_low.jpg"), edges_low)
cv2.imwrite(os.path.join(OUT_DIR, "10_canny_high.jpg"), edges_high)

close_all()
