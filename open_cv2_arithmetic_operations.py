import cv2
import numpy as np

img1 = "images/IMG_0701.jpg"
img2 = "images/IMG_0701-02.jpg"


image1 = cv2.imread(img1, cv2.IMREAD_COLOR)

scale_percent = 35  # percent of original size
width = int(image1.shape[1] * scale_percent / 100)
height = int(image1.shape[0] * scale_percent / 100)
dim = (width, height)
resized1 = cv2.resize(image1, dim, interpolation=cv2.INTER_AREA)


image2 = cv2.imread(img2, cv2.IMREAD_COLOR)

scale_percent = 35  # percent of original size
width = int(image2.shape[1] * scale_percent / 100)
height = int(image2.shape[0] * scale_percent / 100)
dim = (width, height)
resized2 = cv2.resize(image2, dim, interpolation=cv2.INTER_AREA)

# resized_add = resized1 + resized2
# resized_add = cv2.add(resized1, resized2)
resized_add = cv2.add(resized1//2, resized2//2)
# resized_add = cv2.addWeighted(resized1, 0.3, resized2, 0.7, 0)
# resized_sub = resized1 - resized2
# resized_sub = cv2.subtract(resized1, resized2)
resized_sub = cv2.subtract(resized1//2, resized2//2)

cv2.imshow("Image-Added", resized_add)
cv2.imshow("Image-Substracted", resized_sub)
cv2.imshow("Image-1", resized1)
cv2.imshow("Image-2", resized2)
cv2.waitKey(0)
cv2.destroyAllWindows()
