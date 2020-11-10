import cv2

cap = cv2.VideoCapture(
    "C:/Users/user/Desktop/Python_Main/Python/obiekt/Film/test.avi")

while(cap.isOpened()):
    ret, frame = cap.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0XFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
