import cv2
import numpy as np

windowname = "My window"
image = np.zeros((512, 512, 3), np.uint8)

cv2.namedWindow(windowname)


def drawCircle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image, (x, y), 60, (0, 0, 255), -1)


cv2.setMouseCallback(windowname, drawCircle)

while(True):
    cv2.imshow(windowname, image)
    if cv2.waitKey(20) == 27:
        break

cv2.destroyAllWindows()


def main():
    while(True):
        cv2.imshow(windowname, image)
        if cv2.waitKey(0) == 27:
            break

    cv2.destroyAllWindows()


if __name__ == "__name__":
    main()
