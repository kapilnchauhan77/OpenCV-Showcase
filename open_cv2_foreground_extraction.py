import cv2
import numpy as np
import matplotlib.pyplot as plt

img = "images/IMG_0701-02.jpg"

image = cv2.imread(img, cv2.IMREAD_COLOR)
resized_image = cv2.resize(image,
                           (int(image.shape[1] * 0.35),
                            int(image.shape[0] * 0.35)),
                           interpolation=cv2.INTER_AREA)

cv2.imshow("Image", resized_image)

mask = np.zeros(resized_image.shape[:-1], np.uint8())

bgmodel = np.zeros((1, 65), np.float64())
fgmodel = np.zeros((1, 65), np.float64())

# Use matplotlib to find the coords, BTW, it is y, x not x, y
Face_Image = resized_image[65:290, 840:1095, :]

cv2.imshow("Face", Face_Image)

cv2.rectangle(resized_image, (840, 65), (1095, 290), 3)

cv2.waitKey(0)
cv2.destroyAllWindows()

face_rect = (840, 65, 231, 290)

grabcut = cv2.grabCut(resized_image, mask, face_rect, bgmodel,
                      fgmodel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
mask3 = np.where((mask == 3) | (mask == 1), 0, 1).astype("uint8")

resized_image_out = resized_image*mask3[:, :, np.newaxis]
resized_image = resized_image*mask2[:, :, np.newaxis]

cv2.imshow("Grab Cut", resized_image)
cv2.imshow("Grab Cut Inverse", resized_image_out)


resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
plt.imshow(resized_image)
plt.colorbar()
plt.show()
