#opencv 2 video capturing

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0) # 0 for web cam

while True:
    retval, frame = cap.read()

    frame = cv.resize(frame, (0, 0), fx = 0.5, fy = 0.5)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("video cam", half)
    cv.imshow("video cam gray", gray)


    if cv.waitKey(1) & 0xFF ==  ord('q'):
        break

cap.release()
cv.destroyAllWindows()
