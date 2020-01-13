import cv2
import numpy as np
import matplotlib.pyplot as plt


img = "images/bookpage.jpg"

image = cv2.imread(img, cv2.IMREAD_COLOR)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", image)
cv2.imshow("Gray Image", gray_image)

retval, threshold = cv2.threshold(image, 12, 255, cv2.THRESH_BINARY)

cv2.imshow("Image After Simple Threshold", threshold)

retval_inv, threshold_inv = cv2.threshold(image, 12, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Image After Inverse Simple Threshold", threshold_inv)

gray_retval, gray_threshold = cv2.threshold(gray_image, 12, 255, cv2.THRESH_BINARY)

cv2.imshow("Gray Image After Simple Threshold", gray_threshold)

gray_retval_inv, gray_threshold_inv = cv2.threshold(
    gray_image, 12, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Gray Image After Inverse Simple Threshold", gray_threshold_inv)

gauss_gray = cv2.adaptiveThreshold(
    gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow("Gray Image After Gaussian Threshold", gauss_gray)

gauss_gray_inv = cv2.adaptiveThreshold(
    gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 115, 1)

cv2.imshow("Gray Image After Inverse Gaussian Threshold", gauss_gray_inv)

mean_gray = cv2.adaptiveThreshold(
    gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow("Gray Image After Mean Threshold", mean_gray)

mean_gray_inv = cv2.adaptiveThreshold(
    gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 115, 1)

cv2.imshow("Gray Image After Inverse Mean Threshold", mean_gray_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()
