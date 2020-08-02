import numpy as np
import cv2 as cv


# image operations and ROI ( region of image )
img = cv.imread("sample.png", cv.IMREAD_COLOR)

img[100,100] = [255,255,255]
img[100:150, 100:200] = [255,255,255]
# its img[y1:y2, x1:x2] --> y,x


#print(img.shape)

# we can also copy and paste the pixel values, but make sure the no. of pixels
# are properly measured

cv.imshow("edited image", img)

cv.waitKey(0)
cv.destroyAllWindows()
