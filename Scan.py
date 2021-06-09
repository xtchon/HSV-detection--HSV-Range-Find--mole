import cv2
import numpy as np
import pyautogui
      
def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #边缘轮廓提取
    for cnt in contours:
        area = cv2.contourArea(cnt) #计算轮廓面积
        if area > 100: #面积大于100才画
            cv2.drawContours(imgResize,cnt,-1,(0,255,0),2,) #绘画边缘轮廓
            #peri  =cv2.arcLength(cnt,True) #边缘长度
            #approx = cv2.approxPolyDP(cnt,0.02*peri,True)#获得边缘的多边形拟合曲线
            #objCor = len(approx) #角数目
            #x,y,w,h=cv2.boundingRect(approx) #获取
            #r = int((w+h)/4)
            #cx = x+r
            #cy = y+r
            ####cv2.rectangle(目标图片,(左上角xy),(右下角xy),(颜色bgr),线粗-1为实心) #画矩形
            ####画绿色小人
            #cv2.circle(imgResize, (cx, cy), r, (0, 255, 0), 2) #画圆形
            #cv2.circle(imgResize, (int(cx+0.3*r), cy), int(0.2*r), (0,0,0), -1)
            #cv2.circle(imgResize, (int(cx-0.3*r), cy), int(0.2*r), (0,0,0), -1)
            #cv2.line(imgResize, (cx, cy+r), (cx, int(cy+2*r)), (0,255,0), 2) #画线条
            #cv2.line(imgResize, (cx, int(cy+1.2*r)), (cx-r, int(cy+1.6*r)), (0,255,0), 2)
            #cv2.line(imgResize, (cx, int(cy+1.2*r)), (cx+r, int(cy+1.6*r)), (0,255,0), 2)
            #cv2.line(imgResize, (cx, int(cy+2*r)), (cx+r, int(cy+2.2*r)), (0,255,0), 2)
            #cv2.line(imgResize, (cx, int(cy+2*r)), (cx-r, int(cy+2.2*r)), (0,255,0), 2)

def ProcessImg(screenshot,low,up,size):
    kernel = np.ones((5,5), np.uint8) #kernel=核心, 5x5矩阵, unit8=0~255 8bit

    global imgResize
    imgResize = cv2.resize(screenshot, (int(screenshot.shape[1]*size), int(screenshot.shape[0]*size)))#把截图放大缩小
    imgHSV=cv2.cvtColor(imgResize,cv2.COLOR_BGR2HSV)#把图片转为hsv

    lower = np.array([low])#集合滑动条数值
    upper = np.array([up])
    
    mask = cv2.inRange(imgHSV,lower,upper)#建立一个mask 根据对于imgHSV进行颜色筛选
    imgMasked = cv2.bitwise_and(imgResize, imgResize, mask=mask)#利用mask对原图进行取块
    
    imgGray = cv2.cvtColor(imgMasked, cv2.COLOR_BGR2GRAY)#灰度化
    imgCanny = cv2.Canny(imgGray, 300, 0)#边缘detect 300,0 越小越多细节
    
    imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)#加粗边缘 iterations加粗次数1
    imgEroded = cv2.erode(imgDialation, kernel, iterations=1)#边缘减粗 

    getContours(imgEroded) #对原图画边缘(使用减粗图片进行画边缘)

    #cv2.imshow("canny",imgCanny)#显示边缘图片
    #cv2.imshow("dia",imgDialation)#显示加粗图片
    #cv2.imshow("Erod",imgEroded)#显示减粗图片
    cv2.imshow("Scan",imgResize)
    
    return 0





    

