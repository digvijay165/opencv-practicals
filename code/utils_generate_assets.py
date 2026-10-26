"""
utils_generate_assets.py
-------------------------
Helper script used ONLY to generate the sample input image and sample
input video used by the other practicals. Run this once before running
the other scripts (it is also called automatically by 01_... and
11_... if the assets are missing).

This is not one of the graded practicals itself.
"""

import cv2
import numpy as np
import os

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

IMAGE_PATH = os.path.join(ASSETS_DIR, "sample.jpg")
VIDEO_PATH = os.path.join(ASSETS_DIR, "sample_input.avi")


def generate_sample_image(path=IMAGE_PATH, width=640, height=480):
    """Create a colourful synthetic image with shapes, gradient and text
    so that every OpenCV operation (thresholding, edges, morphology,
    blurring, etc.) has something meaningful to work on."""
    img = np.zeros((height, width, 3), dtype=np.uint8)

    # Background gradient
    for y in range(height):
        img[y, :, 0] = int(255 * y / height)          # Blue channel gradient
        img[y, :, 1] = 120
        img[y, :, 2] = int(255 * (1 - y / height))     # Red channel gradient

    # Shapes to give edges / contours for morphology & Canny
    cv2.rectangle(img, (50, 50), (250, 200), (255, 255, 255), -1)
    cv2.circle(img, (450, 130), 90, (0, 0, 0), -1)
    cv2.circle(img, (450, 130), 90, (255, 255, 255), 4)
    pts = np.array([[100, 350], [200, 260], [300, 350], [250, 430], [150, 430]], np.int32)
    cv2.fillPoly(img, [pts], (0, 255, 255))
    cv2.line(img, (350, 250), (600, 420), (255, 0, 255), 6)

    cv2.putText(img, "OpenCV Practicals", (150, 460), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imwrite(path, img)
    return path


def generate_sample_video(path=VIDEO_PATH, width=640, height=480, fps=20, seconds=3):
    """Create a short synthetic video (a bouncing circle) so the video
    read/write practical has an input file to work with even when no
    pre-recorded video is supplied."""
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    writer = cv2.VideoWriter(path, fourcc, fps, (width, height))

    total_frames = fps * seconds
    x, y = 50, height // 2
    dx = 8
    radius = 35

    for i in range(total_frames):
        frame = np.full((height, width, 3), (40, 40, 40), dtype=np.uint8)
        x += dx
        if x - radius < 0 or x + radius > width:
            dx = -dx
        cv2.circle(frame, (x, y), radius, (0, 165, 255), -1)
        cv2.putText(frame, f"Frame {i+1}/{total_frames}", (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        writer.write(frame)

    writer.release()
    return path


if __name__ == "__main__":
    print("Generated sample image:", generate_sample_image())
    print("Generated sample video:", generate_sample_video())
