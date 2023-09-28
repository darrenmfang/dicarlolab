import cv2
import numpy as np
image = cv2.imread(r"C:\Users\darre\OneDrive\Documents\test\picoshells.png") #just put in the file path
output = image.copy()
cv2.imshow("input", image)
cv2.waitKey()
cv2.destroyAllWindows()
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Find circles
arr = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.3, 40, 0, 300, 20, 0, 50) #Or your to cautious in your pickup of circles
# If some circle is found
circles = arr[0]
count = 0
for circle in circles:
   if circle is not None: #I think you need to move your for loop not totally sure gl :) 
      i = 0
      x = 0
      y = 0
      r = 0
      while i < len(circle):    
         circles[count][i] = np.round(circle[i]).astype("int")
         temp = circles[count][i]
         if i == 0:
            x = int(temp)
         if i == 1:
            y = int(temp)
         if i == 2:
            r = int(temp)
         i += 1
      cv2.circle(output, (x, y), r, (0, 0, 255), 2)
      count += 1
print(circles)
print(count)
cv2.imshow("circle",output)
cv2.waitKey(0)
cv2.destroyAllWindows()