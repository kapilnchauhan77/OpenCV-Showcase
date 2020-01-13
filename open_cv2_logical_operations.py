import cv2
import numpy as np

img1 = "images/Logo.png"
img2 = "images/IMG_0701-02.jpg"


image2 = cv2.imread(img2, cv2.IMREAD_COLOR)

scale_percent = 35  # percent of original size
width = int(image2.shape[1] * scale_percent / 100)
height = int(image2.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image2, dim, interpolation=cv2.INTER_AREA)

cv2.imshow("Starting Image", resized)

image1 = cv2.imread(img1, cv2.IMREAD_COLOR)

cv2.imshow("Logo_Unedited", image1)

rows, cols, channels = image1.shape

roi = resized[:rows, :cols]

cv2.imshow("ROI", roi)

gray_logo = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Logo", gray_logo)

ret, mask = cv2.threshold(gray_logo, 220, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Mask", mask)

mask_inv = cv2.bitwise_not(mask)

cv2.imshow("Mask_INV", mask_inv)

img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

cv2.imshow("Img_bg", img2_bg)

img1_fg = cv2.bitwise_and(image1, image1, mask=mask)

cv2.imshow("Img_fg", img1_fg)

dst = cv2.add(img2_bg, img1_fg)

cv2.imshow("Logo_Edited", dst)

resized[:rows, :cols] = dst

cv2.imshow("Final Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
