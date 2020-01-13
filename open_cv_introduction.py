import cv2
import numpy as np
import matplotlib.pyplot as plt


img = "images/watch.jpg"

# SAME: 0 = cv2.IMREAD_GRAYSCALE
# image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
image = cv2.imread(img, 0)

# SAME: 1 = cv2.IMREAD_COLOR
# image = cv2.imread(img, cv2.IMREAD_COLOR)
# image = cv2.imread(img, 1)

# SAME: -1 = cv2.IMREAD_UNCHANGED
# image = cv2.imread(img, cv2.IMREAD_UNCHANGED)
# image = cv2.imread(img, -1)


# Show in cv2 window
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save
# cv2.imwrite("images/gray_watch.jpg", image)


# Show in matplotlib window
# plt.imshow(image, cmap="gray", interpolation="bicubic") # For gray
# plt.imshow(image)                                       # For BGR
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))      # For RGB

# plt.show()
