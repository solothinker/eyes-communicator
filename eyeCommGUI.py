#Making the GUI using TKinter
import os
import cv2
import dlib
import time
import numpy   as np
import tkinter as tk
##from eyeTrackerVideoClass import eyesRects
import eyeTrackerVideoClass

class eyeComm(eyeTrackerVideoClass.eyesRects):
    def __init__(self,path='.\\'):
        eyeTrackerVideoClass.eyesRects.__init__(self)
        self.os = os
        self.path = path
        self.makingDir()
              
        self.root = tk.Tk()
        self.root.title("eye-Comm")
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
         
        self.wButton = 10
        self.hButton = 3        
        self.width   = self.root.winfo_screenwidth()
        self.height  = self.root.winfo_screenheight()
        self.root.geometry('%sx%s' % (int(self.width/2), int(self.height/2)))

        self.btnLeft   = tk.Button(self.root,text="Left",   command=lambda: self.BottonPress(self.leftLookPath),   width=self.wButton, height=self.hButton)
        self.btnCenter = tk.Button(self.root,text="Center", command=lambda: self.BottonPress(self.centerLookPath), width=self.wButton, height=self.hButton)
        self.btnRight  = tk.Button(self.root,text="Right",  command=lambda: self.BottonPress(self.rightLookPath),  width=self.wButton, height=self.hButton)

        
        self.btnLeft.place(   relx=0.35, rely=1.0, anchor=tk.SW)
        self.btnCenter.place( relx=0.5,  rely=1.0, anchor=tk.S )
        self.btnRight.place(  relx=0.65, rely=1.0, anchor=tk.SE)
        self.imageLoad()
        
        
    def makingDir(self):
        # making Data directory
        if not self.os.path.isdir(self.path+'Data'):
            self.os.mkdir(self.path+'Data')
        self.dataPath = self.path+'Data'

        # making Left moved eyes directory
        if not self.os.path.isdir(self.os.path.join(self.dataPath,'Left')):
            self.os.mkdir(self.os.path.join(self.dataPath,'Left'))
        self.leftLookPath = self.os.path.join(self.dataPath,'Left')

        # making Centered eyes directory
        if not self.os.path.isdir(self.os.path.join(self.dataPath,'Center')):
            self.os.mkdir(self.os.path.join(self.dataPath,'Center'))
        self.centerLookPath = self.os.path.join(self.dataPath,'Center')

        # making Right moved eyes directory
        if not self.os.path.isdir(self.os.path.join(self.dataPath,'Right')):
            self.os.mkdir(self.os.path.join(self.dataPath,'Right'))
        self.rightLookPath = self.os.path.join(self.dataPath,'Right')
        
    def imageLoad(self):
        self.camCapture()
        self.root.after(10, self.imageLoad)
        
    def BottonPress(self,path): 
        # saving the image data in Left folder when Left button press
        path = path
        print(path+'\\'+self.filename)
        self.cv2.imwrite(path+'\\'+self.filename,self.img)
      
    def destructor(self):
        self.root.destroy()
        self.windClose()

        

gui = eyeComm()
gui.root.mainloop()

