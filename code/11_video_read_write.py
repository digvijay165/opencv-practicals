"""
Practical 11: Reading and writing video files
----------------------------------------------------
Demonstrates:
  - cv2.VideoCapture()  : open/read a video file frame by frame
  - cv2.VideoWriter()   : write processed frames out to a new video file
A simple grayscale conversion is applied to each frame as an example
of frame-by-frame processing while reading/writing.
"""

import os
import cv2
from display_helper import show, close_all
from utils_generate_assets import generate_sample_video, VIDEO_PATH

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
os.makedirs(OUT_DIR, exist_ok=True)

if not os.path.exists(VIDEO_PATH):
    generate_sample_video()

cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    raise IOError(f"Could not open video file: {VIDEO_PATH}")

fps = cap.get(cv2.CAP_PROP_FPS) or 20
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out_path = os.path.join(OUT_DIR, "11_output_grayscale.avi")
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# isColor=False because we are writing single-channel grayscale frames
writer = cv2.VideoWriter(out_path, fourcc, fps, (width, height), isColor=False)

frame_count = 0
first_frame_saved = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    writer.write(gray_frame)

    show("Video Playback (grayscale)", gray_frame, wait=1)

    if not first_frame_saved:
        cv2.imwrite(os.path.join(OUT_DIR, "11_sample_frame_original.jpg"), frame)
        cv2.imwrite(os.path.join(OUT_DIR, "11_sample_frame_gray.jpg"), gray_frame)
        first_frame_saved = True

    frame_count += 1

cap.release()
writer.release()
close_all()

print(f"Processed {frame_count} frames.")
print("Input video:", VIDEO_PATH)
print("Output (grayscale) video saved to:", out_path)
