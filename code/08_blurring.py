"""
Practical 8: Blurring images using Gaussian Blur and Median Blur
------------------------------------------------------------------------
Demonstrates:
  - cv2.GaussianBlur()
  - cv2.medianBlur()
A little salt-and-pepper noise is added first so the effect of each
blur (especially median blur, which is great at removing that kind of
noise) is clearly visible.
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


def add_salt_and_pepper(image, amount=0.02):
    noisy = image.copy()
    h, w = image.shape[:2]
    n_pixels = int(amount * h * w)

    # Salt (white) noise
    ys = np.random.randint(0, h, n_pixels)
    xs = np.random.randint(0, w, n_pixels)
    noisy[ys, xs] = [255, 255, 255]

    # Pepper (black) noise
    ys = np.random.randint(0, h, n_pixels)
    xs = np.random.randint(0, w, n_pixels)
    noisy[ys, xs] = [0, 0, 0]

    return noisy


noisy_img = add_salt_and_pepper(img)

gaussian_blur = cv2.GaussianBlur(noisy_img, (7, 7), sigmaX=0)
median_blur = cv2.medianBlur(noisy_img, 7)

show("Original", img)
show("Noisy Image", noisy_img)
show("Gaussian Blur", gaussian_blur)
show("Median Blur", median_blur)

cv2.imwrite(os.path.join(OUT_DIR, "08_noisy.jpg"), noisy_img)
cv2.imwrite(os.path.join(OUT_DIR, "08_gaussian_blur.jpg"), gaussian_blur)
cv2.imwrite(os.path.join(OUT_DIR, "08_median_blur.jpg"), median_blur)

close_all()
