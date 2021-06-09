import cv2
import numpy as np

def empty(x):
    pass

path = input("输入图片名称： ")

cv2.namedWindow("TrackBars")#建立一个windows
cv2.resizeWindow("TrackBars",640,240)#设置大小
cv2.createTrackbar("HueMin","TrackBars",0,255,empty) #设置滑动条
cv2.createTrackbar("HueMax","TrackBars",255,255,empty)#初始值，最大值
cv2.createTrackbar("SatMin","TrackBars",0,255,empty)
cv2.createTrackbar("SatMax","TrackBars",255,255,empty)
cv2.createTrackbar("ValueMin","TrackBars",0,255,empty)
cv2.createTrackbar("ValueMax","TrackBars",255,255,empty)

while 1:
    img = cv2.imread(path)
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#把图片转为hsv
    h_min = cv2.getTrackbarPos("HueMin","TrackBars")#获取滑动条的数值
    h_max = cv2.getTrackbarPos("HueMax", "TrackBars")
    s_min = cv2.getTrackbarPos("SatMin", "TrackBars")
    s_max = cv2.getTrackbarPos("SatMax", "TrackBars")
    v_min = cv2.getTrackbarPos("ValueMin", "TrackBars")
    v_max = cv2.getTrackbarPos("ValueMax", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])#集合滑动条数值
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)#建立一个mask 根据对于imgHSV进行颜色筛选
    
    imgResult = cv2.bitwise_and(img, img, mask=mask)#利用mask对原图进行取块

    #kernel = np.ones((5,5), np.uint8)
    #imgGray = cv2.cvtColor(imgResult, cv2.COLOR_BGR2GRAY)#灰度化   
    #imgCanny = cv2.Canny(imgGray, 300, 0)#边缘detect
    #imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)#加粗边缘
    #imgEroded = cv2.erode(imgDialation, kernel, iterations=1)#边缘减粗

    #cv2.imshow("Org",img)
    #cv2.imshow("HSV",imgHSV)
    #cv2.imshow("Mask",mask)
    cv2.imshow("Masked",imgResult)
    #cv2.imshow("Canny",imgCanny)
    #cv2.imshow("dia",imgDialation)
    #cv2.imshow("ero",imgEroded)

    cv2.waitKey(1)
