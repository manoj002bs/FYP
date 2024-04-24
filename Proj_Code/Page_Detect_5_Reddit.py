import cv2
import numpy as np
import pytesseract
import imutils
from imutils import contours, perspective
filef = 'Input_Images\Book_1.jpg'
image = cv2.imread(filef)

# Convert image to grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
 
# Use canny edge detection
edges = cv2.Canny(gray,50,150,apertureSize=3)
 
# Apply HoughLinesP method to
# to directly obtain line end points
lines = cv2.HoughLinesP(
            edges, # Input edge image
            1, # Distance resolution in pixels
            np.pi/180, # Angle resolution in radians
            threshold=600, # Min number of votes for valid line
            minLineLength=600, # Min allowed length of line
            maxLineGap=30 # Max allowed gap between line for joining them
            )
 
lines_list = []
# Iterate over points
for points in lines:
      # Extracted points nested in the list
    x1,y1,x2,y2=points[0]
    # Draw the lines joing the points
    # On the original image
    cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)
    # Maintain a simples lookup list for points
    lines_list.append([(x1,y1),(x2,y2)])
     
# Save the result image
cv2.imwrite(filef[:-4]+'_line.jpg',image)