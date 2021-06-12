# image crop class
import cv2
import dlib
import numpy as np
import time
import datetime

eyes = [0,16,24,19]
imgHeight,imgWidth = 300,100

class eyesRects:
    
    def __init__(self):
        self.cv2 = cv2
        self.vc = self.cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.detector = dlib.get_frontal_face_detector()
        self.img = np.uint8(np.random.randint(0,255,size=(imgWidth,imgHeight,3)))
        self.predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    def camCapture(self):
        ret, img = self.vc.read()
        if ret:
            img = cv2.flip(img,1)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            rects = self.detector(gray, 1)
            
            for i, rect in enumerate(rects):
                pts = []
                shape = self.predictor(gray,rect)
                
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
                b,a,_ = img2.shape
                if a and b:
                    img2 = cv2.resize(img2,(imgHeight,imgWidth))
##                    cv2.imshow('Eye Tracking',img2)
                    self.img = img2
                    ts = datetime.datetime.now()
                    self.filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))


    def windClose(self):
        self.vc.release()
        self.cv2.destroyAllWindows()
        
    
if __name__=="__main__":
    eyesRects()
