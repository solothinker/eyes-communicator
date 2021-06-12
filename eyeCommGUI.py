#Making the GUI using TKinter
import os
import cv2
import dlib
import time
import threading
import numpy   as np
import tkinter as tk
from PIL import Image, ImageTk
##from eyeTrackerVideoClass import eyesRects
import eyeTrackerVideoClass
count = 0
class eyeComm(eyeTrackerVideoClass.eyesRects):
    def __init__(self,path='.\\'):
        eyeTrackerVideoClass.eyesRects.__init__(self)
        self.os = os
        self.path = path
        self.makingDir()
              
        self.root = tk.Tk()
        self.root.title("eye-Comm")
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        
        self.panel = tk.Label(self.root)  # initialize image panel
        self.panel.pack(anchor=tk.SE,side=tk.BOTTOM, fill='none', expand=tk.FALSE)#(padx=10, pady=100)
         
        self.wButton = 10
        self.hButton = 3        
        self.width   = self.root.winfo_screenwidth()
        self.height  = self.root.winfo_screenheight()
        self.root.geometry('%sx%s' % (int(self.width/2), int(self.height/2)))
        
        self._btnState = 'Play'
        self.playPauseBTN = tk.Button(self.root,text='Play',   command=self.playMe, bg='green',   width=self.wButton, height=self.hButton)
        self.playPauseBTN.place( relx=0.5,  rely=1.0, anchor=tk.S )
##
##        self.btnLeft   = tk.Button(self.root,text="Left",   command=lambda: self.BottonPress(self.leftLookPath),   width=self.wButton, height=self.hButton)
##        self.btnCenter = tk.Button(self.root,text="Center", command=lambda: self.BottonPress(self.centerLookPath), width=self.wButton, height=self.hButton)
##        self.btnRight  = tk.Button(self.root,text="Right",  command=lambda: self.BottonPress(self.rightLookPath),  width=self.wButton, height=self.hButton)
##
##        
##        self.btnLeft.place(   relx=0.35, rely=1.0, anchor=tk.SW)
##        self.btnCenter.place( relx=0.5,  rely=1.0, anchor=tk.S )
##        self.btnRight.place(  relx=0.65, rely=1.0, anchor=tk.SE)
        self.imageLoad()
        
    def playMe(self):

        if self.playPauseBTN['text'] == 'Stop':
            self.playPauseBTN['text'] = 'Play'
            self.playPauseBTN['bg'] = 'green'
           
        else:
            self.playPauseBTN['text'] = 'Stop'
            self.playPauseBTN['bg'] = 'red'
            self.BottonPress()
            
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
##        print(self.img.dtype)
        cv2image = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGBA)
        cv2image = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=cv2image)
        self.panel.imgtk = imgtk
        self.panel.config(image=imgtk)
        self.root.after(10, self.imageLoad)
        
    def BottonPress(self): 
        # saving the image data in Left folder when Left button press
        global count
        print(count,'Bingo')
        count += 1
        
        if count>=10:
            self.root.after_cancel(self._btnState)
            self.playMe()
            count = 0
        else:
            self._btnState = self.root.after(30, self.BottonPress)
        
##        path = path
##        print(path+'\\'+self.filename)
##        self.cv2.imwrite(path+'\\'+self.filename,self.img)
      
    def destructor(self):
        self.root.destroy()
        self.windClose()

        

gui = eyeComm()
gui.root.mainloop()

