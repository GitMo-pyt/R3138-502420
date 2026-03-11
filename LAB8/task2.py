import cv2
import numpy as np

def video_proc():
    down_points = (640, 480)
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if 170 <= x + w // 2 <= 470 and 90 <= y + h // 2 <= 390:
                frame = cv2.rotate(frame, cv2.ROTATE_180)

        cv2.imshow('cam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()


video_proc()
cv2.waitKey(0)
cv2.destroyAllWindows()