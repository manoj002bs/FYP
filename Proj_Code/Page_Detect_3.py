import cv2
import pytesseract

# Read the input image
input_image_path = 'Input_Images\Book_1.jpg'
image = cv2.imread(input_image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply any necessary preprocessing steps (e.g., thresholding, edge detection) to separate the two pages

# Example: Thresholding
_, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

# Find contours in the image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Assume that the first two contours correspond to the two pages
contour1, contour2 = contours[:2]

# Extract the two pages
x1, y1, w1, h1 = cv2.boundingRect(contour1)
x2, y2, w2, h2 = cv2.boundingRect(contour2)

page1 = image[y1:y1+h1, x1:x1+w1]
page2 = image[y2:y2+h2, x2:x2+w2]

# Save the separated pages (optional)
cv2.imwrite('page1.jpg', page1)
cv2.imwrite('page2.jpg', page2)

# Use Tesseract to extract text from each page
text_page1 = pytesseract.image_to_string(page1)
text_page2 = pytesseract.image_to_string(page2)

# Print or use the extracted text as needed
print("Text from Page 1:")
print(text_page1)

print("\nText from Page 2:")
print(text_page2)
