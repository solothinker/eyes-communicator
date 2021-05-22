import cv2
import dlib

img = cv2.imread('Lenna.PNG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
detector = dlib.get_frontal_face_detector()
rects = detector(gray, 1)

topX    = rects[0].left()
topY    = rects[0].top()
bottomX = rects[0].right()
bottomY  = rects[0].bottom()

print(rects)
print(topX,topY,bottomX,bottomY)

img = cv2.rectangle(img, (topX,topY), (bottomX,bottomY), (255,0,0),2)

cv2.imshow('rect',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
