import cv2 as cv
import numpy as np
img = cv.imread("iiimg/IMG_1673.jpg")
img = cv.resize(img, (1064, 1064))
cv.imshow("Cats", img)
dst = 255 - img
cv.imshow("dst", dst)
cv.waitKey(0)
cv.destroyAllWindows()

