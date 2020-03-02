import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time

class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        
        leftFrame = tkinter.Frame(window, width=600, height=600)
        leftFrame.grid(row=0, column=0, padx=10, pady=2)
        
        rightFrame = tkinter.Frame(window, width=200, height=600)
        rightFrame.grid(row=0, column=1, padx=10, pady=2)
         # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)
 
         # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(leftFrame, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()
 
        # Button that lets the user take a snapshot
        self.btn_snapshot=tkinter.Button(leftFrame, text="SNAPSHOT", width=25, height=3, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)
        
        moveleft_btn = tkinter.Button(rightFrame, text="Left", command=self.moveLeft, width=8, height=1)
        moveleft_btn.grid(column=0, row=0, padx=5, pady=5)
        #moveleft_btn.pack(side="bottom")
        
        moveright_btn = tkinter.Button(rightFrame, text="Right", command=self.moveRight, width=8, height=1)
        moveright_btn.grid(column=1, row=0, padx=5, pady=5)
        #moveright_btn.pack(side="bottom")
        
        moveup_btn = tkinter.Button(rightFrame, text="Up", command=self.moveUp, width=8, height=1)
        moveup_btn.grid(column=0, row=1, padx=5, pady=5)
        #moveup_btn.pack(side="top")
        
        movedown_btn = tkinter.Button(rightFrame, text="Down", command=self.moveDown, width=8, height=1)
        movedown_btn.grid(column=1, row=1, padx=5, pady=5)
        #movedown_btn.pack(side="top")
        
        moveforward_btn = tkinter.Button(rightFrame, text="Forward", command=self.moveForward, width=8, height=1)
        moveforward_btn.grid(column=0, row=2, padx=5, pady=5)
        #moveforward_btn.pack(side="bottom")
        
        movebackward_btn = tkinter.Button(rightFrame, text="Backward", command=self.moveBackward, width=8, height=1)
        movebackward_btn.grid(column=1, row=2, padx=5, pady=5)
        #movebackward_btn.pack(side="bottom")
        
        rollpos_btn = tkinter.Button(rightFrame, text="Roll +", command=self.rollPositive, width=8, height=1)
        rollpos_btn.grid(column=0, row=3, padx=5, pady=5)
        
        rollneg_btn = tkinter.Button(rightFrame, text="Roll -", command=self.rollNegative, width=8, height=1)
        rollneg_btn.grid(column=1, row=3, padx=5, pady=5)
        
        yawpos_btn = tkinter.Button(rightFrame, text="Yaw +", command=self.yawPositive, width=8, height=1)
        yawpos_btn.grid(column=0, row=4, padx=5, pady=5)
        
        yawneg_btn = tkinter.Button(rightFrame, text="Yaw -", command=self.yawNegative, width=8, height=1)
        yawneg_btn.grid(column=1, row=4, padx=5, pady=5)
        
        pitchpos_btn = tkinter.Button(rightFrame, text="Pitch +", command=self.pitchPositive, width=8, height=1)
        pitchpos_btn.grid(column=0, row=5, padx=5, pady=5)
        
        pitchneg_btn = tkinter.Button(rightFrame, text="Pitch -", command=self.pitchNegative, width=8, height=1)
        pitchneg_btn.grid(column=1, row=5, padx=5, pady=5)
 
         # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()
 
        self.window.mainloop()
        
        
 
    def snapshot(self):
         # Get a frame from the video source
        ret, frame = self.vid.get_frame()
 
        if ret:
             cv2.imwrite("sample-" + time.strftime("%d-%m-%Y_%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
 
    def update(self):
         # Get a frame from the video source
         ret, frame = self.vid.get_frame()
 
         if ret:
             self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
             self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
 
         self.window.after(self.delay, self.update)
         
         
         
         
    def moveLeft(self):
        print("Moving left")
    def moveRight(self):
        print("Moving right")
    def moveUp(self):
        print("Moving up")
    def moveDown(self):
        print("Moving down")
    def moveForward(self):
        print("Moving forward")
    def moveBackward(self):
        print("Moving backward")
    def rollPositive(self):
        print("Applying positive roll")
    def rollNegative(self):
        print("Applying negative roll")
    def yawPositive(self):
        print("Applying positive yaw")
    def yawNegative(self):
        print("Applying negative yaw")
    def pitchPositive(self):
        print("Applying positive pitch")
    def pitchNegative(self):
        print("Applying negative pitch")
 
 
class MyVideoCapture:
    def __init__(self, video_source=0):
         # Open the video source
         self.vid = cv2.VideoCapture(video_source)
         if not self.vid.isOpened():
             raise ValueError("Unable to open video source", video_source)

       # Get video source width and height
         self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
         self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
    def get_frame(self):
         if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
         else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
       if self.vid.isOpened():
            self.vid.release()



# Create a window and pass it to the Application object
App(tkinter.Tk(), "ASU - PSYCHE IMIS - 2019-2020")