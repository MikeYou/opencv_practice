import cv2 as cv
import numpy as np
img = cv.imread("iiimg/271720617_635628024414665_7847353730942105711_n.jpg")
img = cv.resize(img, (1064, 1064))
cv.imshow("Cats", img)

cv.waitKey(0)
cv.destroyAllWindows()

