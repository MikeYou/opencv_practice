import cv2 as cv


img = cv.imread("iiimg/IMG_1673.jpg")

img = cv.resize(img, (1064, 1064))
dst = 255 - img
cv.imshow("dst", dst)
blur = cv.GaussianBlur(dst, (7,7), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Cats", canny)

cv.waitKey(0)