# NOTE: Sobel and laplacian is not work properly with this webcam

import cv2
import numpy as np

# Webcam
cap = cv2.VideoCapture(0)

while 1:
    _, frame = cap.read()

    cv2.imshow("Original Frame", frame)

    # CV_64F means float64, it is the default and there is no need there
    # laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    # sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    # sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    # cv2.imshow("Laplacian Frame", laplacian)
    # cv2.imshow("Sobel X Frame", sobelx)
    # cv2.imshow("Sobel Y Frame", sobely)

    edges = cv2.Canny(frame, 50, 50)
    # edges = cv2.Canny(frame, 100, 200)
    cv2.imshow('Edges', edges)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
