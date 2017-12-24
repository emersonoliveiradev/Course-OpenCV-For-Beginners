import cv2
import numpy as np

# Read image
source = cv2.imread("Images/sample.jpg",1)

scalingFactor = 1/255.0

# Convert unsigned int to float
source = np.float32(source)
source = source * scalingFactor

#Convert back to unsigned int
source = source * (1.0/scalingFactor)
source = np.uint8(source)
print(source)