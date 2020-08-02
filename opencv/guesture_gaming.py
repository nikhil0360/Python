# detecting the contour
# improve opencv8.py using erosion, dilation and median blur
# blurring and reduicng noice ( a little )
# works great with my green cloth and toy


# from file opencv7.py
import numpy as np
import cv2 as cv
import imutils
import pyautogui as gui

cap = cv.VideoCapture(0)

while True:

    _, frame = cap.read()

    frame = cv.resize(frame, (0, 0), fx = 0.3, fy = 0.3)
    height, width = frame.shape[:2]
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    min = np.array([30, 50, 50])
    max = np.array([90, 200, 200])

    mask = cv.inRange(hsv, min, max)
    mask = cv.medianBlur(mask, 15)
    mask = cv.erode(mask, None, iterations=2)
    mask = cv.dilate(mask, None, iterations=2)

    #cv.imshow("mask", mask)

    result = cv.bitwise_and(frame, frame, mask = mask)

    # contour detection
    cnts = cv.findContours(mask, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        M = cv.moments(c)
        cX = int(M["m10"] / M["m00"] + 0.00001)
        cY = int(M["m01"] / M["m00"] + 0.00001)

        if cX > 2*width//3:
            gui.press('left')
            #print("left")

        elif cX < width//3:
            gui.press('right')
            #print("right")

        elif cY > 2*height//3:
            gui.press('down')

        elif cY < height//3:
            gui.press('up')

        cv.circle(frame, (cX, cY), 7, (255, 255, 255), -1)

    cv.rectangle(frame, (width//3, 0 ) , (2*width//3, height), (255, 255, 255) , 3 )
    cv.rectangle(frame, (width//3, height//3 ) , (2*width//3, 2*height//3), (255, 255, 255) , 3 )
    #types of blur
    # 1 kernel and 2D filer
    #kernel = np.ones((15,15), np.float32)/(15*15)
    #smooth = cv.filter2D(result, -1, kernel)

    # guassian blur
    #blur = cv.GaussianBlur(result, (15,15), 0)

    # median blur ( works best )
    #median = cv.medianBlur(result, 15)

    # bilateral blur ( not so useful )
    #bilateral = cv.bilateralFilter(result, 15, 75, 75)


    #cv.imshow("frame" ,frame)
    #cv.imshow("mask" ,mask)


    #cv.imshow("result" ,result)
    frame = cv.flip(frame, 1)
    cv.imshow("frame" ,frame)

    # showing all the blurring
    #cv.imshow("smooth" ,smooth)
    #cv.imshow("blur" ,blur)
    #cv.imshow("median" ,median)
    #cv.imshow("bilateral" ,bilateral)

    if cv.waitKey(1) & 0xFF ==  ord('q'):
        break



cap.release()
cv.destroyAllWindows()
