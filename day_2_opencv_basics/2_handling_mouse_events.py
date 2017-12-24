import cv2
import math

'''
This program shows how highgui enables us to take mouse inputs. In this
code we use mouse input to draw a circle on an image. The mouse is dragged 
from the center to one of the points on the circumference. ‘c’ can be 
pressed to remove the drawn circles. '''

# Lists to store the points
center = []
circumference = []

'''
drawCircle the callback function is called when there is a mouse event like 
left click ( indicated by EVENT_LBUTTONDOWN ). The coordinates relative to 
the namedWindow is captured by this function in the variables (x,y). The 
function records the points of the circle’s center and a point on the 
circumference, hence allowing us to draw the desired circle on the image.
'''


def drawCircle(action, x, y, flags, userdata):
    # Referencing global variables
    global center, circumference
    # Action to be taken when left mouse button is pressed
    if action == cv2.EVENT_LBUTTONDOWN:
        center = [(x, y)]
        # Mark the center
        cv2.circle(source, center[0], 1, (255, 255, 0), 2, cv2.LINE_AA);

    # Action to be taken when left mouse button is released
    elif action == cv2.EVENT_LBUTTONUP:
        circumference = [(x, y)]
        # Calculate radius of the circle
        radius = math.sqrt(math.pow(center[0][0] - circumference[0][0], 2)
                           + math.pow(center[0][1] - circumference[0][1], 2))
        # Draw the circle
        cv2.circle(source, center[0], int(radius), (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow("Window", source)


source = cv2.imread("images/person.jpg", 1)
# Make a dummy image, will be useful to clear the drawing
dummy = source.copy()
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawCircle)
k = 0
# loop until escape character is pressed
while k != 27:

    cv2.imshow("Window", source)
    cv2.putText(source, "Choose center, and drag, Press ESC to exit and c to clear", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (255, 255, 255), 2);
    k = cv2.waitKey(20) & 0xFF
    # Another way of cloning
    if k == 99:
        source = dummy.copy()

cv2.destroyAllWindows()
