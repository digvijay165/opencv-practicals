"""
Practical 9: Morphological operations (Tophat, Blackhat)
--------------------------------------------------------------
Demonstrates cv2.morphologyEx() with:
  - cv2.MORPH_TOPHAT  : difference between the input image and its
                        "opening" -> highlights small bright details
  - cv2.MORPH_BLACKHAT: difference between the "closing" of the input
                        image and the input image -> highlights small
                        dark details
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
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 13))

tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

# Also show basic erosion/dilation for context
erosion = cv2.erode(gray, kernel, iterations=1)
dilation = cv2.dilate(gray, kernel, iterations=1)

show("Original (Gray)", gray)
show("Tophat", tophat)
show("Blackhat", blackhat)
show("Erosion", erosion)
show("Dilation", dilation)

cv2.imwrite(os.path.join(OUT_DIR, "09_tophat.jpg"), tophat)
cv2.imwrite(os.path.join(OUT_DIR, "09_blackhat.jpg"), blackhat)
cv2.imwrite(os.path.join(OUT_DIR, "09_erosion.jpg"), erosion)
cv2.imwrite(os.path.join(OUT_DIR, "09_dilation.jpg"), dilation)

close_all()
