# This contains different image gradients and edge detection

# this is what wiki has to say about gradients and edge detection
'''
An image gradient is a directional change in the intensity or color in an image.
The gradient of the image is one of the fundamental building blocks in
image processing. For example, the Canny edge detector uses image gradient
for edge detection
'''

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True:

    _, frame = cap.read()
    frame = cv.resize(frame, (0, 0), fx = 0.4, fy = 0.4)

    # gradients

    # this is default cv.CV_64F
    laplacian = cv.Laplacian(frame, cv.CV_64F)
                            # format    x  y    kernel size
    sobelx = cv.Sobel(frame, cv.CV_64F, 1 , 0 , ksize = 5)
    sobely = cv.Sobel(frame, cv.CV_64F, 0 , 1 , ksize = 5)
    sobelxy = cv.Sobel(frame, cv.CV_64F, 1 , 1 , ksize = 5)


    # edge detection ( there are many, we will use canny )

    canny = cv.Canny(frame, 200, 200)

    cv.imshow("frame" ,frame)

    '''
    cv.imshow("laplacian",laplacian)
    cv.imshow("sobelx",sobelx)
    cv.imshow("sobely",sobely)
    cv.imshow("sobelxy",sobelxy)
    '''

    cv.imshow("canny",canny)

    if cv.waitKey(1) & 0xFF ==  ord('q'):
        break



cap.release()
cv.destroyAllWindows()
