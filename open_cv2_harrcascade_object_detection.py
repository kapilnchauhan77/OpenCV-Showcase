import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")

# Custom made phone cascade
phone_cascade = cv2.CascadeClassifier('haarcascades/phone_cascade.xml')

cap = cv2.VideoCapture(0)

while 1:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    phone = phone_cascade.detectMultiScale(gray, 10, 10)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

        roi = frame[y: y + h, x: x + w]
        roi_gray = gray[y: y + h, x: x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        for ex, ey, ew, eh in eyes:
            cv2.rectangle(roi, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)

    for x, y, w, h in phone:
        print("Found One!!!")
        cv2.putText(frame, "Kapil's phone", (x-w, y-h), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (11, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("Image", frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
