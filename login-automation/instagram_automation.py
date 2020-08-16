#!/usr/bin/env python3

# pip3 install selenium
# mv chromedriver /usr/local/bin
# chmod + x instagram_automation.py


username = "username"
password = "password"
from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
chrome.get('https://instagram.com')

sleep(2)

username = chrome.find_element_by_xpath('//input[@name=\"username\"]')
username.send_keys(username)

password = chrome.find_element_by_xpath('//input[@name=\"password\"]')
password.send_keys(password)

btn = chrome.find_element_by_xpath('//button[@type="submit"]')
btn.click()
