#Making the GUI using TKinter
import os
import cv2
import dlib
import time
import numpy   as np
import tkinter as tk


class eyeComm:
    def __init__(self,path='.\\'):
        
        self.os = os
        self.path = path
        self.makingDir()
              
        self.root = tk.Tk()
        self.root.title("eye-Comm")
         
        self.wButton = 10
        self.hButton = 3        
        self.width   = self.root.winfo_screenwidth()
        self.height  = self.root.winfo_screenheight()
        self.root.geometry('%sx%s' % (int(self.width/2), int(self.height/2)))

        self.btnLeft   = tk.Button(self.root,text="Left",   command=self.leftBottonPress,   width=self.wButton, height=self.hButton)
        self.btnCenter = tk.Button(self.root,text="Center", command=self.centerBottonPress, width=self.wButton, height=self.hButton)
        self.btnRight  = tk.Button(self.root,text="Right",  command=self.rightBottonPress,  width=self.wButton, height=self.hButton)

        
        self.btnLeft.place(   relx=0.35, rely=1.0, anchor=tk.SW)
        self.btnCenter.place( relx=0.5,  rely=1.0, anchor=tk.S )
        self.btnRight.place(  relx=0.65, rely=1.0, anchor=tk.SE)
        
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
        
    def leftBottonPress(self):
        # saving the image data in Left folder when Left button press
        print(self.leftLookPath)
        print('self.leftBottonPress')

    def centerBottonPress(self):
        # saving the image data in Center folder when Center button press
        print(self.centerLookPath)
        print('self.centerBottonPress')

    def rightBottonPress(self):
        # saving the image data in Right folder when Right button press
        print(self.rightLookPath)
        print('self.rightBottonPress')

gui = eyeComm()
gui.root.mainloop()
