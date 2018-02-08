import cv2
import numpy as np

#cap = cv2.VideoCapture('boat.mp4')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(frame, 50, 50)

        im2, contours, heirarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if w>20 and h>20:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('original', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('output.png', frame)
            break

    else:
        break

cap.release()
cap.destroyAllWindows()
