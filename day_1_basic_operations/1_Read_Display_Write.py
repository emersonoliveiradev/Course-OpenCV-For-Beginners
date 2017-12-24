import cv2

# Read the file "image.jpg".
imageName = "Images/sample.jpg"

# Load image
image = cv2.imread(imageName, cv2.IMREAD_COLOR)

#Verification
if image is None:  # Check for invalid input
    print("Could not open or find the image")

#Convert color image to gray
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display image
# Create a window for display.
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE) 
cv2.namedWindow("gray image", cv2.WINDOW_NORMAL)

# Show our image inside it.
cv2.imshow("image", image)
cv2.imshow("gray image", grayImage)

# Save image
cv2.imwrite("Images/result.jpg", image) 
cv2.imwrite("Images/result_gray.jpg", grayImage)  

# Wait for a keystroke in the window
cv2.waitKey(0)  
cv2.destroyAllWindows()