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

    kernel = np.ones((5, 5), np.uint8())

    erosion = cv2.erode(mask, kernel, iterations=1)
    cv2.imshow("Erosion Mask", erosion)

    dialation = cv2.dilate(mask, kernel, iterations=1)
    cv2.imshow("Dialation Mask", dialation)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)  # Removes false positives
    cv2.imshow("Opening Morphology Mask", opening)

    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)  # Removes false negatives
    cv2.imshow("Closing Morphology Mask", closing)

    # It is the difference between input image and Opening of the image
    # tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
    # cv2.imshow("Tophat Morphology Mask", tophat)

    # It is the difference between the closing of the input image and input image.
    # blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
    # cv2.imshow("Blackhat Morphology Mask", blackhat)

    res = cv2.bitwise_and(frame, frame, mask=erosion)
    cv2.imshow("Erosion Image", res)

    res = cv2.bitwise_and(frame, frame, mask=dialation)
    cv2.imshow("Dialation Image", res)

    res = cv2.bitwise_and(frame, frame, mask=opening)
    cv2.imshow("Opening Morphology Image", res)

    res = cv2.bitwise_and(frame, frame, mask=closing)
    cv2.imshow("Closing Morphology Image", res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:  # Escape Key
        break

cv2.destroyAllWindows()
cap.release()
