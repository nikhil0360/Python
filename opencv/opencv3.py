# this one is about drawing, and writing on an image.
# we can do that using pyplot, but cv has it so its great
# also, i have used PIL... it has ImageDraw but it needs to convert the cv
# image from BGR to RGB, which is some tedious process.

import cv2 as cv
import numpy as np

img = cv.imread("test.jpeg")

# line, rectangle, circle ( colors are in bgr )
thickness = 5
cv.line( img, (0,0), (150,150), (255,255,255), thickness)
# it is like : image, start coordinate, end , color , thickness
cv.rectangle( img, (30,24), (170,150), (255,0,0), thickness)
cv.circle( img, (200,200), 50, (0,255,0), -1)
# for fill use thickness = -1


# draw polygon shapes
pts = np.array([[100,200], [200,100], [150,300] ,[400,400]], np.int32)
cv.polylines(img, [pts], True, (0,255,0), thickness)


#drawing text ( can see the documentation for this for better help of arguments)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "Hello World", (500,500), font, 3, (0,0,0), thickness, cv.LINE_AA )


cv.imshow("drawing", img)
cv.waitKey(0)
cv.destroyAllWindows()

# thats all
