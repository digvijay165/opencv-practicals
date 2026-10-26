"""
Practical 4: Drawing shapes (lines, polygons) and adding text on images
---------------------------------------------------------------------------
Demonstrates:
  - cv2.line()
  - cv2.rectangle()
  - cv2.circle()
  - cv2.polylines() / cv2.fillPoly()
  - cv2.putText()
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
canvas = img.copy()

# Line
cv2.line(canvas, (0, 0), (canvas.shape[1], canvas.shape[0]), (0, 255, 0), 3)

# Rectangle
cv2.rectangle(canvas, (30, 30), (200, 150), (255, 0, 0), 3)

# Circle
cv2.circle(canvas, (canvas.shape[1] - 100, 100), 60, (0, 0, 255), -1)

# Polygon (pentagon) using polylines
pts = np.array([[300, 400], [350, 320], [420, 350], [400, 430], [320, 450]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(canvas, [pts], isClosed=True, color=(0, 255, 255), thickness=3)

# Text
cv2.putText(canvas, "Drawing Demo - Deen Bandhu Singh", (20, canvas.shape[0] - 20),
            cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

show("Original", img)
show("Shapes and Text", canvas)

cv2.imwrite(os.path.join(OUT_DIR, "04_shapes_and_text.jpg"), canvas)

close_all()
