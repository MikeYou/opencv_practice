import cv2 as cv
import numpy as np
import os

good_input = "iiimg/linked_bean/"
img_size = 1064
path = os.path.join(good_input)
img_list = os.listdir(path)
goodbeans_path = "./output/auto_thed_canny_linkedbeans/" + str(1)+".jpg"
ind = 430
for i in img_list:

    img = cv.imread(os.path.join(path, i))

    img = cv.resize(img, (img_size, img_size))


    blank = np.zeros(img.shape, dtype="uint8")
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
    #blur = cv.medianBlur(gray, 5)
    thed = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
        cv.THRESH_BINARY, 11, 2)
    #ret, thed = cv.threshold(blur,0,255,cv.THRESH_OTSU)


    canny = cv.Canny(thed, 0,255)

    contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    cv.drawContours(blank, contours, -1, (0,255,0), 1)
    img_name = str(ind) + ".jpg"
    goodbeans_path = "./output/auto_thed_canny_linkedbeans/" + str(ind) + ".jpg"
    ind = ind + 1
    cv.imwrite(goodbeans_path, blank)