import cv2
import dlib
import numpy as np

#-----------------------------------------------------
# Eyes masking index
#for left eyes from 36 to 41
#for right eyes from 42 to 47
left = np.arange(36,42).tolist()
right = np.arange(42,48).tolist()
#-----------------------------------------------------
vc = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
# Activating camera
while(True):
    ret, img = vc.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    for i, rect in enumerate(rects):
        shape = predictor(gray,rect)
        for ii in range(shape.num_parts):
            x,y = shape.part(ii).x,shape.part(ii).y   
            img = cv2.circle(img,(x,y),2,(255,0,0),-1)
    cv2.imshow('Eye Tracking',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#closing the camera and windows
vc.release()
cv2.destroyAllWindows()
