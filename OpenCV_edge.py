import cv2


original_img=cv2.imread("iiimg/IMG_1673.jpg")
original_img = cv2.resize(original_img, (1064, 1064))
cv2.imshow("1", original_img)
print("  Edge detection in the Original images  ")
#We will find the edges in the image as below
Edge_Org=cv2.Canny(original_img,150,175)
cv2.imshow("2", Edge_Org)
cv2.waitKey(0)
cv2.destroyAllWindows()