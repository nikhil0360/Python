# object motion seperator using MOG ( some algorithm )
# this will easily detect any changes from a image, so we can
# solve the images which has find the difference really fast and easily

import numpy as np
import cv2 as cv

img1 = cv.imread("diff1b.png")
img2 = cv.imread("diff2b.png")

img1 = cv.resize( img1, (0,0), fx = 0.1 , fy = 0.1 )
img2 = cv.resize( img2, (0,0), fx = 0.1 , fy = 0.1 )

subtractor = cv.createBackgroundSubtractorMOG2()

mask = subtractor.apply(img1)
mask = subtractor.apply(img2)


result = cv.bitwise_and(img2, img2, mask = mask)
result = cv.addWeighted(img1, 0.5, result, 0.5, 0)

cv.imshow("orignal", img1)
cv.imshow("orignal2", img2)
cv.imshow("mask", mask)
cv.imshow("result", result)


cv.waitKey(0)
cv.destroyAllWindows()
