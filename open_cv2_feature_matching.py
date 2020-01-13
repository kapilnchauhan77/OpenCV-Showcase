import cv2
import numpy as np
import matplotlib.pyplot as plt


img = "images/opencv-feature-matching-image.jpg"
tmplt = "images/opencv-feature-matching-template.jpg"

image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
template = cv2.imread(tmplt, cv2.IMREAD_GRAYSCALE)

orb = cv2.ORB_create()

kp1, desp1 = orb.detectAndCompute(image, None)
kp2, desp2 = orb.detectAndCompute(template, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(desp1, desp2)
matches = sorted(matches, key=lambda x: x.distance)
# print(len(matches))

image3 = cv2.drawMatches(image, kp1, template, kp2, matches[:10], None, flags=2)

plt.imshow(image3)
plt.show()
