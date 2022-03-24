import cv2 as cv

capture = cv.VideoCapture("iiimg/IMG_1135.mov")

while True:
    isTrue, frame = capture.read()
    if isTrue:
        cv.imshow("Video", frame)

# 讀取過程中若按下 q 則離開
    #if cv.waitKey(27) & 0xFF == ord("q"):
        #break

# 持續讀取影片，直到讀取完畢
    #else:
        #break
capture.release()
cv.destroyAllWindows()