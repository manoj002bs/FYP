import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('Input_Images\Book_1_left.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours from left to right
contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])

# Calculate the midline
midline_x = (cv2.boundingRect(contours[-1])[0] + cv2.boundingRect(contours[0])[0]) // 2

# Split the image into left and right
left_page = image[:, :midline_x]
right_page = image[:, midline_x:]

# Draw contours on the original image
image_contours = image.copy()
cv2.drawContours(image_contours, contours, -1, (0, 255, 0), 2)

# Display the original image with contours
plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(image_contours, cv2.COLOR_BGR2RGB)), plt.title('Original with Contours')
plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(right_page, cv2.COLOR_BGR2RGB)), plt.title('Right Page')
plt.show()
