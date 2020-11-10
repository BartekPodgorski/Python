import cv2
import this
print(this)
videos = ["C:/Users/user/Desktop/film2.avi",
          "C:/Users/user/Desktop/Python_Main/Python/obiekt/Film/test.avi"]
names_window = ["orginal", "our"]
cap = [cv2.VideoCapture(i) for i in videos]


frames = [None] * len(videos)
ret = [None] * len(videos)

while True:

    for i, c in enumerate(cap):
        if c is not None:
            ret[i], frames[i] = c.read()
    for i, f in enumerate(frames):
        if ret[i] is True:
            cv2.imshow(names_window[i], frames[i])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


for c in cap:
    if c is not None:
        c.release()

cv2.destroyAllWindows()

