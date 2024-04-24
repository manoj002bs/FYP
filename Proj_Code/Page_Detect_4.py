import cv2
import numpy as np
import pytesseract
import imutils
from imutils import contours, perspective

# Load the image
image = cv2.imread('book.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur the image slightly
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform edge detection
edges = cv2.Canny(blurred, 50, 200, 255)

# Find contours in the edge map
cnts = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = contours.sort_contours(cnts[0])[0]

# Loop over the contours individually
for (i, c) in enumerate(cnts):
    # If the contour is not sufficiently large, ignore it
    if cv2.contourArea(c) < 500:
        continue

    # Compute the rotated bounding box of the contour
    box = cv2.minAreaRect(c)
    box = cv2.boxPoints(box) if imutils.is_cv2() else cv2.cv.BoxPoints(box)
    box = np.array(box, dtype="int")

    # Order the points in the contour
    box = perspective.order_points(box)

    # Draw the bounding box on the image
    cv2.drawContours(image, [box.astype("int")], -1, (0, 255, 0), 2)

# Split the image using the coordinates of the bounding box
left_page = image[:, :int(image.shape[1] / 2)]
right_page = image[:, int(image.shape[1] / 2):]

# Use Tesseract to extract text
text_left = pytesseract.image_to_string(left_page)
text_right = pytesseract.image_to_string(right_page)

# Print the extracted text
print("Left Page Text:")
print(text_left)

print("\nRight Page Text:")
print(text_right)
