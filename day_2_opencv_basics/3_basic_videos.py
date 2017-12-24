import numpy as np
import cv2

cap = cv2.VideoCapture("videos/chaplin.mp4")

#Check if there is any video
if(cap.isOpened()==False):
    print("Error opening video!")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
    else:
        break

    #Break if pressioned ESC
    if cv2.waitKey(25) & 0xFF == 27:
        break

# When everything done, release the video capture object
cap.release()
cv2.destroyAllWindows()
