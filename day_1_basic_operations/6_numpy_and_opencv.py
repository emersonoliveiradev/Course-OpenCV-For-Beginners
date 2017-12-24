import numpy as np
import cv2

img = cv2.imread("../Images/soccer.jpg", 1)
cv2.imshow("Show image", img)
cv2.waitKey(0)
print(img.shape)

#Copy an image
img_copy = img.copy()
cv2.imshow("Show copy image", img_copy)
cv2.waitKey(0)

#Crop a retangular image
img_cropped = img[300:500, 300:750]
cv2.imshow("Show cropped image", img_cropped)
cv2.waitKey(0)

#Return the numbers of rows
print(img.shape[0])

#Return the numbers of columns
print(img.shape[1])

#Return the numbers of channels
print(img.shape[2])

cv2.destroyAllWindows()