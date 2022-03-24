import cv2 as cv
import numpy as np


img = cv.imread("iiimg/linked_bean/430.jpg")

img = cv.resize(img, (1064, 1064))
cv.imshow("Cats", img)

#img = cv.resize(img, (1064, 1064))
blank = np.zeros(img.shape, dtype="uint8")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
#blur = cv.medianBlur(gray, 5)
thed = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv.THRESH_BINARY, 11, 2)
#ret, thed = cv.threshold(blur,0,255,cv.THRESH_OTSU)
cv.imshow("Cats", thed)

canny = cv.Canny(thed, 0,255)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# 計算總共有幾個輪廓 contours
print(f"{len(contours)} contour(s) found!")
# 畫出當前所有的 contours
cv.drawContours(img, contours, -1, (255,0,0), 1)
cv.imshow("Contours Drawn on img", img)
# 標示 contours
cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow("Contours Drawn on blank", blank)
cv.waitKey(0)