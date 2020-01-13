import cv2
import numpy as np
import matplotlib.pyplot as plt

img = "images/watch.jpg"

image_for_mpl = cv2.imread(img, cv2.IMREAD_COLOR)

image = cv2.imread(img, cv2.IMREAD_COLOR)

px = image[155, 155]

image[450: 550, 250: 350] = [255, 255, 255]

# ROI = Region Of Image
ROI = image[250: 350, 50: 150]

image[0: 100, 0: 100] = ROI

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.cvtColor(image_for_mpl, cv2.COLOR_BGR2RGB)

plt.imshow(image)
plt.colorbar()
plt.show()
