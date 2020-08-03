# Guesture gaming 🎮

<div> <<img src="https://media.giphy.com/media/fteWMYaoLv118WOvDS/giphy.gif"/> </div>   


Opencv has many options to make guesture gaming possible,  
here i have used color detection and object motion tracking to make my  
controls for any game which can be played using arrows keys 
( I have used [pyautogui](https://pyautogui.readthedocs.io/en/latest/) for simulate keypress ).

Color can be detected by a ```inRange( frame, lower_bound, upper_bound)``` funtion, where frame is  
image or video feed, lower_bound and upper_bound are value of lower and upper limit of color  
you want to track. ( here it is green )

after this, we find the contours in the selected color, and find the center of the contour shape.  
Then using the center position in the frame, we can decide which action to take.

here is the [source code](guesture_gaming.py)
