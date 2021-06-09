import cv2
import os
from windowcapture import WindowCapture
import pyautogui

winname = input("请输入视窗名字：")
wincap = WindowCapture(winname)
screenshot = wincap.get_screenshot()
cv2.imwrite('temp.jpg', screenshot)
print("Done Screen Shot")

