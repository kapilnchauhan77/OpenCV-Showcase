import cv2
import numpy as np


# video = "videos/people-walking.mp4"

# cv2.VideoCapture(video) # for Video

# Webcam
cap = cv2.VideoCapture(0)

# Save Webcam feed
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("videos/output.avi", fourcc, 20.0, (640, 480))

while 1:
    ret, frame = cap.read()

    gry = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Webcam", frame)

    out.write(frame)

    cv2.imshow("Gray", gry)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
