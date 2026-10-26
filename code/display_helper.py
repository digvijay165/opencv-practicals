"""
display_helper.py
------------------
Small shared helper so every practical can safely call cv2.imshow() /
cv2.waitKey() / cv2.destroyAllWindows() even when run on a machine or
server that has no display attached (e.g. while auto-testing).

On a normal computer with a screen, `show()` behaves exactly like the
standard cv2.imshow + cv2.waitKey(0) + cv2.destroyWindow() sequence and
a window will pop up as expected. If no display is available, the
GUI call is skipped so the script still runs to completion and still
saves its output image/video to disk.
"""

import cv2


def show(window_name, image, wait=0):
    """Display `image` in a window called `window_name`.

    wait=0  -> waits until any key is pressed (normal interactive use)
    wait>0  -> waits only `wait` milliseconds (useful for video frames)
    """
    try:
        cv2.imshow(window_name, image)
        cv2.waitKey(wait)
    except cv2.error:
        # No GUI backend / no display attached (headless environment).
        print(f"[display_helper] Could not open a window for "
              f"'{window_name}' (no display available). "
              f"The processed image/video was still saved to disk.")


def close_all():
    try:
        cv2.destroyAllWindows()
    except cv2.error:
        pass
