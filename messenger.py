# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:33:04 2020

@author: HP
"""
import webbrowser
#import os
#os.environ['DISPLAY'] = ':1.1'
import pyautogui
import time



#name=input("Enter person name to send message: ").lower()
#message=input("enter mssage to be send:")
#no_of_times=int(input("How many times to send:"))
#goto website
#click on search

def send_msg(name,message,no_of_times):
    webbrowser.open('https://www.instagram.com/', new=2)
    time.sleep(10)
    pyautogui.click(940,128)
    #search for name
    pyautogui.typewrite(name)
    time.sleep(5)
    #click on first result
    pyautogui.click(961,160)
    time.sleep(5)
    #click on message
    pyautogui.click(1027,208)
    time.sleep(5)
    #click on message box
    for i in range(0,no_of_times):
        pyautogui.click(961,982)
        pyautogui.typewrite(message)
        pyautogui.click(1363,980)
    print('Done')
'''
if no_of_times==0:
    send_msg(name,message,no_of_times=1)
else:
    send_msg(name,message,no_of_times)
'''
