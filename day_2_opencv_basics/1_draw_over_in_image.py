import numpy as np
import cv2
from copy import copy

img = cv2.imread("images/person.jpg")


#Draw a line
#cv2.line ( image, starting point , end point , color , line thickness, line type)
imgLine = img.copy()
cv2.line(imgLine, (300, 200), (400, 180), (0, 255,0), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow("image_line", imgLine)
cv2.waitKey(0)


# Draw a circle
#cv2.circle ( image, center, radius, color of border, line thickness / fill type, line type)
imgCircle = img.copy()
cv2.circle(imgCircle, (250, 200), 50, (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow("image_circle", imgCircle)
cv2.waitKey(0)


#Draw an ellipse
#cv2.ellipse ( image, center, axes lengths, rotation degree of ellipse, starting angle , ending angle, color, line thickness / fill type, line type)
img_ellipse = img.copy()
cv2.ellipse(img_ellipse, (360, 200), (100, 170), 45, 0, 360, (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)
cv2.ellipse(img_ellipse, (360, 200), (100, 170), 135, 0, 360, (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow("image_ellipse", img_ellipse)
cv2.waitKey(0)


# Draw a rectangle
#cv2.rectangle ( image, upper left corner vertex, lower right corner vertex, line thickness / fill type, line type)
img_rectangle = img.copy()
cv2.rectangle(img_rectangle, (150, 55), (300, 355), (0, 255, 0), thickness=2, lineType=cv2.LINE_8)
cv2.imshow("image_rectangle", img_rectangle)
cv2.waitKey(0)


#Put text into image
#cv2.putText ( image, text, starting point of text, font type, font scale, color, linetype )

imgText = img.copy()
cv2.putText(imgText, "An person", (155, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow("text", imgText)
cv2.waitKey(0)