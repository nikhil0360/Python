# Login Automation using Selenium 

## Why ? 
My Brother is a Freelancer [Photographer](https://www.instagram.com/sanchey.agarwal/), and a [music](https://www.instagram.com/ministry.of.music/) enthusiatic. 
He currently manages 3 instagram account, and those who use instagram web knows the pain of login in 
and out switch accounts. People might say he can use two different web browser, but lets be real...
one has to be true to its browser.

So he asked if I can do something.  
and Guess what, python has the solution.

### Task 

Automate instagram login process, such that clicking a file would open his account.

## Requirements 

* ``` pip3 install selenium ```
* You also need to downlaod webdriver for your browser, I have used chrome and you can get it from here : [chromedriver](https://chromedriver.chromium.org/downloads)
* you need to move the chromedriver to your ```/usr/local/bin```

### here is the [SOURCE]("instagram_automation.py") CODE
All you need to do is change the user name and password in the script.

Now to make the file a clickable you need to do the following.

* Change the file extension from .py to .command
* and excecute the following command on the terminal ```chmod + x filename.command```, this make the file executeable
* You need to add shebang line at top of the script i.e ```#!/usr/bin/env python3```


Thats all you need to do, you can also automate LMS, Facebook, and what not. (But be careful where you store the files, as it contains your passwords )




