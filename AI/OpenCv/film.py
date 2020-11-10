import cv2
# we make variable
imageName = "C:/Users/user/Desktop/Python_Main/Python/obiekt/Film/test_image.jpg"
#We are readning our photo
image = cv2.imread(imageName)
#We show photo
cv2.imshow("My Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()