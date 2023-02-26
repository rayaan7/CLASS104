#types of digital images = binary - 0(black) & 1(white) Grayscale - monochrome and Colored - three banned monochrome data. Also called channels.
import cv2
img = cv2.imread("butterfly.jpg")
cv2.imshow("Display Image",img)
#cv2.waitKey(0)
print(img)

grey_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("grayscale",grey_img)
print(grey_img)
cv2.waitKey(0)