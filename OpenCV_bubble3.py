import cv2 as cv


def main():


    im = cv.imread("iiimg/IMG_1673.jpg")

    gray = cv.CreateImage(cv.GetSize(im), 8, 1)
    edges = cv.CreateImage(cv.GetSize(im), 8, 1)

    cv.CvtColor(im, gray, cv.CV_BGR2GRAY)
    cv.Canny(gray, edges, 50, 200, 3)
    cv.Smooth(gray, gray, cv.CV_GAUSSIAN, 9, 9)

    storage = cv.CreateMat(im.rows, 1, cv.CV_32FC3)

    cv.HoughCircles(edges, storage, cv.CV_HOUGH_GRADIENT, 2, gray.height/4, 200, 100)
    # Now, supposing it found circles, how do I extract the information?
    print(storage.r)



if __name__ == '__main__':
    main()