import cv2
import dlib
import numpy as np
import time

#-----------------------------------------------------
# Eyes masking index
##eyes = np.arange(36,48).tolist()
##eyes.append(28)
eyes = [0,16,24,19]
imgHeight,imgWidth = 300,100
##ref = [27,30]
#-----------------------------------------------------

vc = cv2.VideoCapture(0,cv2.CAP_DSHOW) # to remove [ WARN:1] terminating async callback warning
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
# Activating camera
while(True):
    ret, img = vc.read()
    img = cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    for i, rect in enumerate(rects):
        pts = []
        shape = predictor(gray,rect)
        
        for ii in eyes:
            x,y = shape.part(ii).x,shape.part(ii).y
            pts.append([x,y])
        pts[2][0] = pts[1][0]
        pts[3][0] = pts[0][0]
        # fixing the window size
        pts[0][1] = pts[1][1] = max(pts[0][1],pts[1][1])
        pts[2][1] = pts[3][1] = max(pts[2][1],pts[3][1])

        #Cropping the needful shape
        img2 = img[pts[3][1]:pts[1][1],pts[0][0]:pts[1][0]]
        img2 = cv2.resize(img2,(imgHeight,imgWidth))
##        pts = np.array(pts,np.int32)
##        img = cv2.polylines(img,[pts],True,(0,255,0),2)

        cv2.imshow('Eye Tracking',img2)
    time.sleep(0.001)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#closing the camera and windows
vc.release()
cv2.destroyAllWindows()
