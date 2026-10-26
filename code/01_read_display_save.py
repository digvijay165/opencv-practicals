"""
Practical 1: Reading, displaying and saving images
----------------------------------------------------
Demonstrates:
  - cv2.imread()   : read an image from disk
  - cv2.imshow()   : display it in a window
  - cv2.waitKey()  : wait for a keypress
  - cv2.destroyAllWindows() : close all windows
  - cv2.imwrite()  : save an image to disk
"""

import os
import cv2
from display_helper import show, close_all
from utils_generate_assets import generate_sample_image, IMAGE_PATH

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
os.makedirs(OUT_DIR, exist_ok=True)

# Make sure we have an input image to work with
if not os.path.exists(IMAGE_PATH):
    generate_sample_image()

# 1. Read the image from disk
img = cv2.imread(IMAGE_PATH)
if img is None:
    raise FileNotFoundError(f"Could not read image at {IMAGE_PATH}")

print("Image shape (H, W, Channels):", img.shape)

# 2. Display the original image
show("Original Image", img)

# 3. Save a copy of the image (demonstrates cv2.imwrite)
save_path = os.path.join(OUT_DIR, "01_saved_copy.jpg")
cv2.imwrite(save_path, img)
print("Saved image to:", save_path)

# 4. Close all open windows
close_all()
