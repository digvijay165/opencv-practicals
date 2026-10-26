"""
build_pdf.py
------------
Generates OpenCVPracticals_Report.pdf containing, for each practical:
  - the practical title
  - the full source code
  - the resulting output image(s) ("screenshots" of the output, since
    imwrite() produces exactly what would appear in the imshow() window)

Not one of the graded practicals itself - a documentation helper.
"""

import os
import cv2
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Image,
                                 PageBreak, Preformatted, Table, TableStyle)
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIR = os.path.join(BASE, "code")
OUT_DIR = os.path.join(BASE, "outputs")
PDF_PATH = os.path.join(BASE, "OpenCVPracticals_Report.pdf")

styles = getSampleStyleSheet()
title_style = ParagraphStyle("TitleCustom", parent=styles["Title"], fontSize=22, spaceAfter=6)
subtitle_style = ParagraphStyle("SubtitleCustom", parent=styles["Normal"], fontSize=12,
                                 alignment=TA_CENTER, textColor=colors.grey)
heading_style = ParagraphStyle("HeadingCustom", parent=styles["Heading1"], fontSize=16,
                                spaceBefore=10, spaceAfter=8, textColor=colors.HexColor("#1a3d5c"))
subhead_style = ParagraphStyle("SubHead", parent=styles["Heading3"], fontSize=11,
                                spaceBefore=8, spaceAfter=4, textColor=colors.HexColor("#333333"))
body_style = styles["BodyText"]
code_style = ParagraphStyle("Code", parent=styles["Code"], fontSize=7.3, leading=9,
                             backColor=colors.HexColor("#f5f5f5"))
caption_style = ParagraphStyle("Caption", parent=styles["Normal"], fontSize=9,
                                alignment=TA_CENTER, textColor=colors.grey, spaceAfter=10)

# List of (practical_number, title, script_filename, [ (output_image_path, caption), ... ])
PRACTICALS = [
    (1, "Reading, Displaying and Saving Images", "01_read_display_save.py", [
        ("assets/sample.jpg", "Input image (read with cv2.imread)"),
        ("outputs/01_saved_copy.jpg", "Output: saved copy (cv2.imwrite)"),
    ]),
    (2, "Resizing Images", "02_resize.py", [
        ("assets/sample.jpg", "Original (640x480)"),
        ("outputs/02_resized_half.jpg", "Resized to half (320x240)"),
        ("outputs/02_resized_double.jpg", "Resized to double (1280x960)"),
        ("outputs/02_resized_300x300.jpg", "Resized to fixed 300x300"),
    ]),
    (3, "Flipping Images (Horizontal, Vertical, Both)", "03_flip.py", [
        ("assets/sample.jpg", "Original"),
        ("outputs/03_flip_horizontal.jpg", "Horizontal flip (flip code 1)"),
        ("outputs/03_flip_vertical.jpg", "Vertical flip (flip code 0)"),
        ("outputs/03_flip_both.jpg", "Both axes flip (flip code -1)"),
    ]),
    (4, "Drawing Shapes and Adding Text", "04_draw_shapes_text.py", [
        ("assets/sample.jpg", "Original"),
        ("outputs/04_shapes_and_text.jpg", "Line, rectangle, circle, polygon and text drawn"),
    ]),
    (5, "Image Translation using warpAffine", "05_translation.py", [
        ("assets/sample.jpg", "Original"),
        ("outputs/05_translated_right_down.jpg", "Translated +80px right, +50px down"),
        ("outputs/05_translated_left_up.jpg", "Translated -60px left, -40px up"),
    ]),
    (6, "Image Rotation using getRotationMatrix2D and warpAffine", "06_rotation.py", [
        ("assets/sample.jpg", "Original"),
        ("outputs/06_rotated_45.jpg", "Rotated 45 degrees"),
        ("outputs/06_rotated_90.jpg", "Rotated 90 degrees"),
        ("outputs/06_rotated_180.jpg", "Rotated 180 degrees"),
        ("outputs/06_rotated_30_scaled.jpg", "Rotated 30 degrees + scaled 0.7x"),
    ]),
    (7, "Thresholding (Binary Threshold)", "07_thresholding.py", [
        ("outputs/07_gray.jpg", "Grayscale conversion"),
        ("outputs/07_binary_threshold.jpg", "Binary threshold (T=127)"),
        ("outputs/07_binary_inv_threshold.jpg", "Binary inverted threshold"),
        ("outputs/07_otsu_threshold.jpg", "Otsu's automatic threshold"),
    ]),
    (8, "Blurring using Gaussian Blur and Median Blur", "08_blurring.py", [
        ("outputs/08_noisy.jpg", "Image with salt-and-pepper noise added"),
        ("outputs/08_gaussian_blur.jpg", "Gaussian Blur (7x7 kernel)"),
        ("outputs/08_median_blur.jpg", "Median Blur (kernel size 7)"),
    ]),
    (9, "Morphological Operations (Tophat, Blackhat)", "09_morphology.py", [
        ("outputs/09_tophat.jpg", "Tophat (Original - Opening)"),
        ("outputs/09_blackhat.jpg", "Blackhat (Closing - Original)"),
        ("outputs/09_erosion.jpg", "Erosion (for reference)"),
        ("outputs/09_dilation.jpg", "Dilation (for reference)"),
    ]),
    (10, "Edge Detection using Canny", "10_edge_detection.py", [
        ("outputs/10_canny_low.jpg", "Canny edges (thresholds 30, 90)"),
        ("outputs/10_canny_high.jpg", "Canny edges (thresholds 100, 200)"),
    ]),
    (11, "Reading and Writing Video Files", "11_video_read_write.py", [
        ("outputs/11_sample_frame_original.jpg", "Sample frame - original (from input video)"),
        ("outputs/11_sample_frame_gray.jpg", "Sample frame - grayscale (written to output video)"),
    ]),
    (12, "Capturing Live Video from Webcam", "12_webcam_capture.py", [
        ("outputs/12_webcam_snapshot_fallback.jpg",
         "Snapshot captured by the capture/write pipeline\n(no physical webcam available in this "
         "run environment, so the fallback path shown in the code was exercised;\n"
         "on a computer with a webcam attached, cv2.VideoCapture(0) is used instead)"),
    ]),
]


def add_cover_page(story):
    story.append(Spacer(1, 2 * inch))
    story.append(Paragraph("OpenCV Practicals", title_style))
    story.append(Paragraph("Image and Video Processing using Python & OpenCV", subtitle_style))
    story.append(Spacer(1, 0.5 * inch))
    info_data = [
        ["Submitted by:", "Deen Bandhu Singh"],
        ["Assignment:", "OpenCV Practicals"],
        ["Libraries used:", "OpenCV (cv2), NumPy"],
        ["Tools used:", "cv2.imshow(), cv2.waitKey(), cv2.destroyAllWindows()"],
    ]
    t = Table(info_data, colWidths=[1.8 * inch, 4 * inch])
    t.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 11),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, colors.HexColor("#dddddd")),
    ]))
    story.append(t)
    story.append(PageBreak())


def add_toc(story):
    story.append(Paragraph("Contents", heading_style))
    data = [["#", "Practical"]]
    for num, title, _, _ in PRACTICALS:
        data.append([str(num), title])
    t = Table(data, colWidths=[0.5 * inch, 5.5 * inch])
    t.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a3d5c")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#cccccc")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f7f7f7")]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(t)
    story.append(PageBreak())


def add_practical(story, num, title, script_filename, images):
    story.append(Paragraph(f"Practical {num}: {title}", heading_style))

    script_path = os.path.join(CODE_DIR, script_filename)
    with open(script_path, "r") as f:
        code_text = f.read()

    story.append(Paragraph(f"<b>File:</b> code/{script_filename}", body_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph("Source Code:", subhead_style))
    # Escape for Preformatted / reportlab XML parsing safety
    story.append(Preformatted(code_text, code_style))

    story.append(Spacer(1, 10))
    story.append(Paragraph("Output:", subhead_style))

    max_width = 5.6 * inch
    max_height = 3.3 * inch

    for img_rel_path, caption in images:
        img_path = os.path.join(BASE, img_rel_path)
        if not os.path.exists(img_path):
            continue
        im = cv2.imread(img_path)
        if im is None:
            continue
        h, w = im.shape[:2]
        scale = min(max_width / w, max_height / h, 1.0) if w and h else 1.0
        # Allow slight upscale for small images so they're legible
        scale = min(max_width / w, max_height / h)
        draw_w, draw_h = w * scale, h * scale

        story.append(Image(img_path, width=draw_w, height=draw_h))
        story.append(Paragraph(caption.replace("\n", "<br/>"), caption_style))

    story.append(PageBreak())


def main():
    doc = SimpleDocTemplate(
        PDF_PATH, pagesize=A4,
        leftMargin=0.6 * inch, rightMargin=0.6 * inch,
        topMargin=0.6 * inch, bottomMargin=0.6 * inch,
        title="OpenCV Practicals - Deen Bandhu Singh",
    )

    story = []
    add_cover_page(story)
    add_toc(story)

    for num, title, script_filename, images in PRACTICALS:
        add_practical(story, num, title, script_filename, images)

    doc.build(story)
    print("PDF generated at:", PDF_PATH)


if __name__ == "__main__":
    main()
