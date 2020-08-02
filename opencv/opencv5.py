import numpy as np
import cv2 as cv

img1 = cv.imread("sample.jpeg")
img2 = cv.imread("logo2.png")

#add = img1 + img1
# will not work for differnt sizes

#add = cv.add(img1, img1)
# add each value of pixel and if value > 255 --> value = 255

#add = cv.addWeighted(img1, 0.6, img1, 0.6, 0)
# value1 * weight1 + value2 * weight 2

#cv.imshow("add", add)

# # # # # # #

# challenge - add a mask image of equation on the flat lay image

rows, cols, channel = img2.shape
roi = img1[0:rows, 0:cols]
cv.imshow("roi", roi)
# direct super impose

# giving mask to equation image
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 220, 255, cv.THRESH_BINARY_INV)
cv.imshow("mask equation", mask)

mask_inv = cv.bitwise_not(mask)
cv.imshow("mask_inv equation", mask_inv)

img_bg = cv.bitwise_and(roi, roi, mask = mask_inv)
cv.imshow("img_bg", img_bg)

img_fg = cv.bitwise_and(img2, img2, mask = mask)
cv.imshow("img_fg", img_fg)

add_mask = cv.add(img_fg, img_bg)
cv.imshow("final mask", add_mask)

img1[0:rows, 0:cols] = add_mask
cv.imshow("final output", img1)


cv.waitKey(0)
cv.destroyAllWindows()
