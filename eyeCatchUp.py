import cv2
import dlib

# reading the image
img = cv2.imread('Lenna.PNG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
detector = dlib.get_frontal_face_detector()

# detecting rect coordinate around face
rects = detector(gray, 1)

predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

for i, rect in enumerate(rects):
    shape = predictor(gray,rect)
    for ii in range(shape.num_parts):
        x,y = shape.part(ii).x,shape.part(ii).y   
        img = cv2.circle(img,(x,y),2,(255,0,0),-1)

    
cv2.imshow('rect',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
