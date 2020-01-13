import cv2
import numpy as np

video = "videos/people-walking.mp4"

vid = cv2.VideoCapture(video)  # for Video
# vid = cv2.VideoCapture(0)  # for WebCam
fgbg = cv2.createBackgroundSubtractorMOG2()

while 1:
    _, frame = vid.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow("Original", frame)
    cv2.imshow("FG mask", fgmask)

    kernel = np.ones((5, 5), np.uint8())

    opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening Morphology Mask", opening)              # It worked best

    # closing = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow("Closing Morphology Mask", closing)

    # erosion = cv2.erode(fgmask, kernel, iterations=1)
    # cv2.imshow("Erosion Mask", erosion)

    # dialation = cv2.dilate(fgmask, kernel, iterations=1)
    # cv2.imshow("Dialation Mask", dialation)

    # res = cv2.bitwise_and(frame, frame, mask=fgmask)
    # cv2.imshow("FG Image", res)

    # res = cv2.bitwise_and(frame, frame, mask=opening)
    # cv2.imshow("Opening Morphology Image", res)

    # res = cv2.bitwise_and(frame, frame, mask=closing)
    # cv2.imshow("Closing Morphology Image", res)

    # res = cv2.bitwise_and(frame, frame, mask=erosion)
    # cv2.imshow("Erosion Image", res)

    # res = cv2.bitwise_and(frame, frame, mask=dialation)
    # cv2.imshow("Dialation Image", res)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()
vid.release()
