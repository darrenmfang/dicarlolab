import cv2
import numpy as np
image = cv2.imread('circle_ellipse_2.JPG')
output = image.copy()
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Find circles
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.3, 100)
# If some circle is found
if circles is not None:
   # Get the (x, y, r) as integers
   circles = np.round(circles[0, :]).astype("int")
   print(circles)
   # loop over the circles
   for (x, y, r) in circles:
      cv2.circle(output, (x, y), r, (0, 255, 0), 2)
# show the output image
cv2.imshow("circle",output)
cv2.waitKey(0)