# https://stackoverflow.com/questions/36817133/identifying-the-range-of-a-color-in-hsv-using-opencv

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True:

    _, frame = cap.read()
    frame = cv.resize(frame, (0, 0), fx = 0.4, fy = 0.4)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    min = np.array([30, 50, 50])
    max = np.array([90, 200, 200])

    mask = cv.inRange(hsv, min, max)
    result = cv.bitwise_and(frame, frame, mask = mask)

    #cv.imshow("frame" ,frame)
    cv.imshow("mask" ,mask)
    cv.imshow("result" ,result)

    if cv.waitKey(1) & 0xFF ==  ord('q'):
        break



cap.release()
cv.destroyAllWindows()
