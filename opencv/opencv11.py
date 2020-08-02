# template matching

import cv2 as cv
import numpy as np

img_rgb = cv.imread('img_for_template.png')

img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

template = cv.imread('template.png',0)
w, h = template.shape[::-1]
print(template.shape)

# matchTemplate function
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)



for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

img_rgb = cv.resize(img_rgb, (0,0),  fx = 0.4, fy = 0.4)
res = cv.resize(res, (0,0),  fx = 0.4, fy = 0.4)


cv.imshow('Detected',img_rgb)
cv.imshow('res',res)


cv.waitKey(0)
cv.destroyAllWindows()

# result with my templates are not good, because the netflix logo look same as
# other logos (because of the white circle)
