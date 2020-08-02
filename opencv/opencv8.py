# blurring and reduicng noice ( a little )

# from file opencv7.py
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

    #types of blur
    # 1 kernel and 2D filer
    #kernel = np.ones((15,15), np.float32)/(15*15)
    #smooth = cv.filter2D(result, -1, kernel)

    # guassian blur
    #blur = cv.GaussianBlur(result, (15,15), 0)

    # median blur ( works best )
    median = cv.medianBlur(result, 15)

    # bilateral blur ( not so useful )
    #bilateral = cv.bilateralFilter(result, 15, 75, 75)


    #cv.imshow("frame" ,frame)
    #cv.imshow("mask" ,mask)
    cv.imshow("result" ,result)

    # showing all the blurring
    #cv.imshow("smooth" ,smooth)
    #cv.imshow("blur" ,blur)
    cv.imshow("median" ,median)
    #cv.imshow("bilateral" ,bilateral)







    if cv.waitKey(1) & 0xFF ==  ord('q'):
        break



cap.release()
cv.destroyAllWindows()
