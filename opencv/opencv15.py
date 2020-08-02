# object motion seperator using MOG ( some algorithm )
# this will easily detect any changes from a image, so we can
# solve the images which has find the difference really fast and easily

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
subtractor = cv.createBackgroundSubtractorMOG2()

while True:
    ret, frame  = cap.read()
    frame = cv.resize(frame, (0,0), fx = 0.4 , fy = 0.4)
    mask = subtractor.apply(frame)

    result = cv.bitwise_and(frame, frame, mask = mask)

    cv.imshow("orignal", frame)
    cv.imshow("result", result)


    if cv.waitKey(1) & 0xFF ==  ord('q'):
        break

cap.release()
cv.destroyAllWindows()
