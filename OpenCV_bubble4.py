import numpy as np
import argparse
import cv2

def fill_holes(imInput, threshold):
    """
    The method used in this function is found from
    https://www.learnopencv.com/filling-holes-in-an-image-using-opencv-python-c/

    """

    # Threshold.
    th, thImg = cv2.threshold(imInput, threshold, 255, cv2.THRESH_BINARY_INV)

    # Copy the thresholded image.
    imFloodfill = thImg.copy()

    # Get the mask.
    h, w = thImg.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)

    # Floodfill from point (0, 0).
    cv2.floodFill(imFloodfill, mask, (0,0), 255)

    # Invert the floodfilled image.
    imFloodfillInv = cv2.bitwise_not(imFloodfill)

    # Combine the two images.
    imOut = thImg | imFloodfillInv

    return imOut

if __name__ == "__main__":
    # Extract arguments from the command line.
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True, help = "Path to the image.")
    args = vars(ap.parse_args())

    # Load the image.
    image = cv2.imread(args["image"])
    image = cv2.resize(image, (1064, 1064))
    cv2.imshow("Original image", image)
    image = 255 - image
    # Convert the image into grayscale image.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imshow("Blurred", blurred)

    # Fille the "holes" on the image.
    filled = fill_holes(blurred, 220)
    cv2.imshow("Filled", filled)

    # Find circles by the Hough transfermation.
    circles = cv2.HoughCircles(filled, cv2.HOUGH_GRADIENT, 1, 20, param1 = 25, param2 = 10, minRadius = 0, maxRadius = 20)

    # Draw circles on the original image.
    if circles is not None:
        for i in range(circles.shape[1]):
            c = circles[0, i]

            cv2.circle( image, (c[0], c[1]), c[2], (0, 255, 0), 2)
            print("i = %d, r = %f" % (i, c[2]))

        cv2.imshow("Marked", image)
    else:
        print("circle is None")

    # Block the execution.
    cv2.waitKey(0)
    cv2.destroyAllWindows()