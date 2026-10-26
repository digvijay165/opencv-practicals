OpenCV Practicals - Deen Bandhu Singh
========================================

Folder contents
---------------
code/    - All Python source files (one file per practical, numbered 01-12),
           plus two small shared helper files:
             display_helper.py       - safe cv2.imshow()/waitKey()/destroyAllWindows() wrapper
             utils_generate_assets.py- generates the sample input image and sample input video
             build_pdf.py            - script used to generate the PDF report (documentation only)

assets/  - Sample input image (sample.jpg) and sample input video (sample_input.avi)
           used by the practicals. These are generated automatically by
           utils_generate_assets.py the first time any script is run, so the
           practicals are fully self-contained and do not depend on any
           external image/video file.

outputs/ - All output images/videos produced by running the scripts.

OpenCVPracticals_Report.pdf - PDF containing the full source code and the
           output screenshots for every practical.

How to run
----------
1. Install dependencies:
       pip install opencv-python numpy

2. From inside the "code" folder, run any script, e.g.:
       cd code
       python 01_read_display_save.py
       python 02_resize.py
       ...
       python 12_webcam_capture.py

   Each script will:
     - open a window showing the image/video using cv2.imshow()
     - wait for a keypress (cv2.waitKey())
     - close the window(s) (cv2.destroyAllWindows())
     - save its output image(s)/video(s) into the "outputs" folder

3. Practical 12 (webcam capture) needs a real webcam attached to your
   computer. If no webcam is found, it automatically falls back to running
   the same capture/write pipeline on the sample video so the code can
   still be verified end-to-end.

List of practicals
-------------------
 1. Reading, displaying and saving images
 2. Resizing images
 3. Flipping images (horizontal, vertical, both)
 4. Drawing shapes (lines, polygons) and adding text on images
 5. Image translation (shifting) using warpAffine
 6. Image rotation using getRotationMatrix2D and warpAffine
 7. Thresholding (Binary threshold)
 8. Blurring images using Gaussian Blur and Median Blur
 9. Morphological operations (Tophat, Blackhat)
10. Edge detection using Canny
11. Reading and writing video files
12. Capturing live video from webcam
