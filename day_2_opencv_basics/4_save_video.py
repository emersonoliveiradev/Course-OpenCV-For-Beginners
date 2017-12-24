import cv2
import numpy as np

#Create a VideoCapture object (Webcam)
cap = cv2.VideoCapture(-1)

if (cap.isOpened() == False):
  print("Unable your camera")


frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

#Create an object VideoWriter
out = cv2.VideoWriter('videos/output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

#Read and save the feed from webcam until ESC is pressed .
while(True):
    ret, frame = cap.read()
    if(ret == True):
        #Write the frame into the file 'output.avi'
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('frame',frame)
        # Press ESC on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Break the loop
    else:
        break

# When everything done, release the video capture and video write objects
cap.release()
out.release()
cv2.destroyAllWindows()