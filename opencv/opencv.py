import cv2 as cv
import numpy as np
#import matplotlib.pyplot as plt

img = cv.imread("test.jpeg", cv.IMREAD_GRAYSCALE)
# 0 for IMREAD_GRAYSCALE
# 1 for IMREAD_COLOR
# -1 FOR IMREAD_UNCHANGED

cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite("test1.png", img)
