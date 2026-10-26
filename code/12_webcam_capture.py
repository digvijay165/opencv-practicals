"""
Practical 12: Capturing live video from webcam
-----------------------------------------------------
Demonstrates cv2.VideoCapture(0) to grab frames live from the default
webcam, display them in a window, and save both a snapshot and a short
recorded clip. Press 'q' to stop recording early.

NOTE: This script needs an actual webcam attached to the computer it
runs on. If no webcam is found (e.g. on a headless server / cloud
sandbox), it prints a message and falls back to demonstrating the same
capture/write logic on the sample video created by
utils_generate_assets.py, so the code path can still be verified.
"""

import os
import cv2
import time
from display_helper import show, close_all
from utils_generate_assets import generate_sample_video, VIDEO_PATH

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
os.makedirs(OUT_DIR, exist_ok=True)

RECORD_SECONDS = 5


def run_webcam_capture():
    cap = cv2.VideoCapture(0)  # 0 = default webcam
    if not cap.isOpened():
        return False

    fps = cap.get(cv2.CAP_PROP_FPS) or 20
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) or 640
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) or 480

    out_path = os.path.join(OUT_DIR, "12_webcam_recording.avi")
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    writer = cv2.VideoWriter(out_path, fourcc, fps, (width, height))

    print("Recording from webcam... press 'q' to stop early.")
    start = time.time()
    snapshot_saved = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        writer.write(frame)
        show("Webcam Live Feed", frame, wait=1)

        if not snapshot_saved:
            cv2.imwrite(os.path.join(OUT_DIR, "12_webcam_snapshot.jpg"), frame)
            snapshot_saved = True

        if (time.time() - start) > RECORD_SECONDS:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    writer.release()
    close_all()
    print("Webcam recording saved to:", out_path)
    return True


def run_fallback_demo():
    """Used only when no physical webcam is available, so the
    capture -> display -> write pipeline can still be demonstrated
    end-to-end using the pre-generated sample video as a stand-in for
    a 'live' feed."""
    print("No webcam detected. Running the same capture/write pipeline "
          "on the sample video instead, so the logic can still be verified.")

    if not os.path.exists(VIDEO_PATH):
        generate_sample_video()

    cap = cv2.VideoCapture(VIDEO_PATH)
    fps = cap.get(cv2.CAP_PROP_FPS) or 20
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out_path = os.path.join(OUT_DIR, "12_webcam_recording_fallback.avi")
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    writer = cv2.VideoWriter(out_path, fourcc, fps, (width, height))

    snapshot_saved = False
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        writer.write(frame)
        show("Simulated Webcam Feed", frame, wait=1)
        if not snapshot_saved:
            cv2.imwrite(os.path.join(OUT_DIR, "12_webcam_snapshot_fallback.jpg"), frame)
            snapshot_saved = True

    cap.release()
    writer.release()
    close_all()
    print("Fallback 'webcam' recording saved to:", out_path)


if __name__ == "__main__":
    if not run_webcam_capture():
        run_fallback_demo()
