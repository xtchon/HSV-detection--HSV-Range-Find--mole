import cv2
import numpy as np
import os
import win32gui, win32ui, win32con
from time import time
from windowcapture import WindowCapture
from Scan import ProcessImg

def empty(x):#不做事
    pass

#获取输入
winname = input("请输入游戏视窗名：")
lower = input("请输入3个初始hsv lower:")
upper= input("请输入3个初始hsv upper:")
size = float(input("(>0;1为原始大小)\n请输入输出视窗大小倍率:"))
low = [int(n) for n in lower.split()] 
up  = [int(n) for n in upper.split()]

#绑定视窗
wincap = WindowCapture(winname) #获取对应视窗截图
if winname != 'None' and winname != 'Top':
    win = win32gui.FindWindow(None, winname)
elif winname == 'Top':
    win = win32gui.GetForegroundWindow()
loop_time = time()

while(True):
    if winname != 'None':
        window_rect = win32gui.GetWindowRect(win)#实时获取视窗位置大小
        winx = window_rect[0] #视窗右上角x坐标
        winy = window_rect[1] #视窗右上角y坐标
        winw = window_rect[2] - winx #视窗宽度
        winh = window_rect[3] - winy #视窗高度

    screenshot = wincap.get_screenshot() #实时获取截图
    found = ProcessImg(screenshot,low,up,size) #对截图进行处理 

    # debug the loop rate 显示FPS
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv2.waitKey(1) == ord('q'):#按住键盘q来退出程序
        cv2.destroyAllWindows()
        break

print('End')

