import cv2
import numpy as np

img = "images/opencv-corner-detection-sample.jpg"

image = cv2.imread(img, cv2.IMREAD_COLOR)

cv2.imshow("Image", image)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image", gray_image)

gray_image = np.float32(gray_image)

# corners = cv2.goodFeaturesToTrack(where, how_many_to_find, image_quality, minimum_distance_between_features)
corners = cv2.goodFeaturesToTrack(gray_image, 200, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (x, y), 3, 255, -1)

cv2.imshow("Image with corners", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
