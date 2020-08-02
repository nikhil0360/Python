#opencv 2
# can now recoginse face and eyes ( left and right separete boxes )
# I optimise it by searching eyes inside the face detection, this
# reduces the search are to detect eyes : )

import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("eyes.xml")



cap = cv.VideoCapture(0) # 0 for web cam

while True:
    retval, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)



    faces = face_cascade.detectMultiScale(gray)

    if faces != ():
        boxes = faces.tolist()

        for box in boxes:
            cv.rectangle(frame, (box[0],box[1]) , (box[2]+ box[0],box[3]+box[1]), (0, 255, 0) , 5 )
            roi_gray = gray[ box[1]:box[1]+box[3], box[0]:box[0]+box[2] ]
            roi_color = frame[ box[1]:box[1]+box[3], box[0]:box[0]+box[2] ]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            if eyes != ():
                small_boxes = eyes.tolist()

                for box in small_boxes:
                    cv.rectangle(roi_color, (box[0],box[1]) , (box[2]+ box[0],box[3]+box[1]), (0, 0, 255) , 3 )




    half = cv.resize(frame, (0, 0), fx = 0.5, fy = 0.5)
    cv.imshow("video cam", half)
    #cv.imshow("video cam gray", gray)



    if cv.waitKey(1) & 0xFF ==  ord('q'):
        break

cap.release()
cv.destroyAllWindows()
