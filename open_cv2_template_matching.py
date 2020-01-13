import cv2
import numpy as np


img = "images/A_lot.jpg"
tmplt = "images/S_lot.jpg"

gray_image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
image = cv2.imread(img, cv2.IMREAD_COLOR)
template = cv2.imread(tmplt, cv2.IMREAD_GRAYSCALE)

w, h = template.shape[::-1]

# cv2.imshow("Image", image)
cv2.imshow("Gray Image", gray_image)
cv2.imshow("Template", template)

res = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

cv2.imshow("Detected", image)

# print(loc)
# print(len(loc))
# print(loc[0].shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
