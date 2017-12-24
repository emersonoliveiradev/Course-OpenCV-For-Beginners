#In this program, we will use OpenCV warpaffine function to transform
#a triangle in an image to another triangle as shown in the above figure.

import cv2
import numpy as np

# Read image
source = cv2.imread("images/person.jpg",1);

# Createmask/ warp matrix
warpMat = np.float32([[1.2, 0.2, 2],[-0.3, 1.3, 1]])

# Another mask/warp matrix
warpMat2 = np.float32([[1.2, 0.3, 2],[0.2, 1.3, 1]])

# Use warp affine
result = cv2.warpAffine(source, warpMat,(int(1.5*source.shape[0]),
         int(1.4*source.shape[1])), None, flags=cv2.INTER_LINEAR,
         borderMode=cv2.BORDER_REFLECT_101 )

result2 = cv2.warpAffine(source, warpMat2, (int(1.5*source.shape[0]),
          int(1.4*source.shape[1])), None, flags=cv2.INTER_LINEAR,
          borderMode=cv2.BORDER_REFLECT_101)

# Display images
cv2.imshow("Original",source)
cv2.imshow("Result", result)
cv2.imshow("Result2", result2)
cv2.waitKey(0)