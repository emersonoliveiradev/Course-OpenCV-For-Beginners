import cv2
import numpy as np

# In this program, we will use OpenCV getAffineTransform function
# to obtain the warping matrix using two triangles, one being the
# input triangle and the other being the output triangle

# Input triangle
inp = np.float32([[50, 50], [100, 100], [200, 150]])

# Output triangle
output = np.float32([[72, 51], [142, 101], [272, 136]])

# Another output triangle
output2 = np.float32([[77, 76], [152, 151], [287, 236]])

# Get the tranformation matrices
warpMat = cv2.getAffineTransform(inp, output)
warpMat2 = cv2.getAffineTransform(inp, output2)

# Display the matrices
print("Warp Matrix 1 : \n {} \n".format(warpMat))
print("Warp Matrix 2 : \n {} \n".format(warpMat2))