import cv2
import numpy as np
image = cv2.imread(r"C:\Users\darre\OneDrive\Documents\test\image.png") #just put in the file path
output = image.copy()
cv2.imshow("input", image)
cv2.waitKey()
cv2.destroyAllWindows()
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Find circles
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.3, 100) #Or your to cautious in your pickup of circles
# If some circle is found
count = 0
if circles is not None: #I think you need to move your for loop not totally sure gl :) 
   # Get the (x, y, r) as integers
   circles = np.round(circles[0, :]).astype("int")
   print(circles)
   # loop over the circles
   for (x, y, r) in circles:
      count += 1
      cv2.circle(output, (x, y), r, (255, 255, 255), 5)
# show the output image
print(count)
cv2.imshow("circle",output)
cv2.waitKey(0)
cv2.destroyAllWindows()