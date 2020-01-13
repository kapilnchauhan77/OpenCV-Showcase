import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while 1:

    _, frame = cap.read()

    cv2.imshow("Frame", frame)

    # hsv = hue saturation value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow("HSV", hsv)

    # lower_not_skin = np.array([30, 0, 0])
    # upper_not_skin = np.array([255, 255, 255])

    # mask = cv2.inRange(hsv, lower_not_skin, upper_not_skin)

    # lower_red = np.array([150, 150, 0])
    # upper_red = np.array([180, 255, 255])

    # mask = cv2.inRange(hsv, lower_red, upper_red)

    lower_green = np.array([20, 150, 130])
    upper_green = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)

    cv2.imshow("Mask", mask)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Final Frame", res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:  # Escape Key
        break

cv2.destroyAllWindows()
cap.release()
