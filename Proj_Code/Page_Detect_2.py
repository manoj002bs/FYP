import cv2
import numpy as np
from imutils.perspective import four_point_transform
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Load the input image from disk
input_image_path = 'Input_Images\Book_1.jpg'  # Replace with the path to your input image
frame = cv2.imread(input_image_path)

# You can adjust the scale if needed
scale = 0.5

# Font settings for text overlay
font = cv2.FONT_HERSHEY_SIMPLEX

# Constants for image dimensions
WIDTH, HEIGHT = frame.shape[1], frame.shape[0]

# Function to perform image processing
def image_processing(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    return threshold

# Function to detect and crop the document
def scan_detection(image):
    global document_contour

    document_contour = np.array([[0, 0], [WIDTH, 0], [WIDTH, HEIGHT], [0, HEIGHT]])

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, threshold = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.015 * peri, True)
            if area > max_area and len(approx) == 4:
                document_contour = approx
                max_area = area

    cv2.drawContours(frame, [document_contour], -1, (0, 255, 0), 3)

# Function to center text on the image
def center_text(image, text):
    text_size = cv2.getTextSize(text, font, 2, 5)[0]
    text_x = (image.shape[1] - text_size[0]) // 2
    text_y = (image.shape[0] + text_size[1]) // 2
    cv2.putText(image, text, (text_x, text_y), font, 2, (255, 0, 255), 5, cv2.LINE_AA)

# Perform document detection and cropping
scan_detection(frame)

# Display the input image
cv2.imshow("Input", cv2.resize(frame, (int(scale * WIDTH), int(scale * HEIGHT))))
cv2.waitKey(0)

# Crop the document
warped = four_point_transform(frame, document_contour.reshape(4, 2))

# Display the cropped document
cv2.imshow("Cropped Document", cv2.resize(warped, (int(scale * warped.shape[1]), int(scale * warped.shape[0]))))
cv2.waitKey(0)

# Perform image processing on the cropped document
processed = image_processing(warped)
processed = processed[10:processed.shape[0] - 10, 10:processed.shape[1] - 10]

# Display the processed document
cv2.imshow("Processed Document", cv2.resize(processed, (int(scale * processed.shape[1]), int(scale * processed.shape[0]))))
cv2.waitKey(0)

# Save the processed document image
output_image_path = 'scanned_document.jpg'  # Replace with the desired output path
cv2.imwrite(output_image_path, processed)
print(f'Scanned document saved as {output_image_path}')

# Perform OCR on the cropped document
ocr_text = pytesseract.image_to_string(warped)
print(f'OCR Text: {ocr_text}')

cv2.destroyAllWindows()
