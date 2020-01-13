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

    # Smoothing / blurring code

    # Simple Smoothing
    kernel = np.ones((10, 10), np.float64())/255
    smoothed = cv2.filter2D(res, -1, kernel)

    cv2.imshow("10,10 Smoothed Frame", smoothed)

    kernel = np.ones((15, 15), np.float64())/255
    smoothed = cv2.filter2D(res, -1, kernel)

    cv2.imshow("15,15 Smoothed Frame", smoothed)

    # Gaussian Blurring
    gauss_blur = cv2.GaussianBlur(res, (15, 15), 0)

    cv2.imshow("15,15 Gaussian Smoothed Frame", gauss_blur)

    # Median Blurring
    median_blur = cv2.medianBlur(res, 15)

    cv2.imshow("15,15 Median Smoothed Frame", median_blur)

    # Bilateral Blurring
    bilateral_blur = cv2.bilateralFilter(res, 15, 75, 75)

    cv2.imshow("15,15 Bilateral Smoothed Frame", bilateral_blur)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:  # Escape Key
        break

cv2.destroyAllWindows()
cap.release()
