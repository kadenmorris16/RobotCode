import tkinter as tk
import random
import threading
from speech import TTS

class Screen:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.canvas = tk.Canvas(self.root, bg="#dcdcdc")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.movePupilsId = None
        self.moveFigureId = None
        self.spiralId = None
        self.blinkId  = None
        self.nextBlinkId = None
        self.speech = TTS()

        self.drawEyes(0)
    
    def clear(self):
        if self.movePupilsId is not None:
            self.canvas.after_cancel(self.movePupilsId)
            self.movePupilsId = None
        if self.moveFigureId is not None:
            self.canvas.after_cancel(self.moveFigureId)
            self.moveFigureId = None
        if self.spiralId is not None:
            self.canvas.after_cancel(self.spiralId)
            self.spiralId = None
        if self.blinkId is not None:
            self.canvas.after_cancel(self.blinkId)
            self.blinkId = None
        if self.nextBlinkId is not None:
            self.canvas.after_cancel(self.nextBlinkId)
            self.nextBlinkId = None
        self.canvas.delete("all")
    
    def drawEyes(self, look):
        self.clear()
        screenHeight = self.canvas.winfo_screenheight()
        screenWidth = self.canvas.winfo_screenwidth()
        margin = 15
        face = self.canvas.create_oval(margin, margin, screenWidth - margin, screenHeight - margin, outline = "black", width = 5, tags = "face")

        eyeRadius = screenHeight/4
        leftEye = self.canvas.create_oval(screenWidth/2 - eyeRadius*2, screenHeight/2 - eyeRadius, screenWidth/2, screenHeight/2 + eyeRadius, outline = "black", fill = "white", tags = "leftEye")
        rightEye = self.canvas.create_oval(screenWidth/2, screenHeight/2 - eyeRadius, screenWidth/2 + eyeRadius*2, screenHeight/2 + eyeRadius, outline = "black", fill = "white", tags = "rightEye")

        pupilRadius = eyeRadius/2
        leftPupil = self.canvas.create_oval(screenWidth/2 - eyeRadius - pupilRadius, screenHeight/2 - eyeRadius + margin, screenWidth/2 - eyeRadius + pupilRadius, screenHeight/2 + eyeRadius - margin, outline = "black", fill = "black", tags = "leftPupil")
        rightPupil = self.canvas.create_oval(screenWidth/2 + eyeRadius - pupilRadius, screenHeight/2 - eyeRadius + margin, screenWidth/2 + eyeRadius + pupilRadius, screenHeight/2 + eyeRadius - margin, outline = "black", fill = "black", tags = "rightPupil")

        x1, y1, x2, y2 = self.canvas.bbox("face")
        topLid = self.canvas.create_arc(x1+margin, y1+margin, x2-margin, y2-margin, start=0, extent=180, outline="#dcdcdc", fill="#dcdcdc", tags="topLid")
        botLid = self.canvas.create_arc(x1+margin, y1+margin, x2-margin, y2-margin, start=0, extent=-180, outline="#dcdcdc", fill="#dcdcdc", tags="botLid")
        self.canvas.move("topLid", 0, -(self.canvas.winfo_screenheight() / 2))
        self.canvas.move("botLid", 0, self.canvas.winfo_screenheight() / 2)

        self.canvas.tag_raise("face")

        threading.Thread(target=self.nextBlink).start()

        if(look == 0): # move
            self.movePupils(0.5, 0.5)
        elif(look == 1): # up
            self.canvas.move("leftPupil", 0, (-1/3)*eyeRadius)
            self.canvas.move("rightPupil", 0, (-1/3)*eyeRadius)
        elif(look == 2): # right
            self.canvas.move("leftPupil", (2/3)*eyeRadius, 0)
            self.canvas.move("rightPupil", (2/3)*eyeRadius, 0)
        elif(look == 3): # down
            self.canvas.move("leftPupil", 0, (1/3)*eyeRadius)
            self.canvas.move("rightPupil", 0, (1/3)*eyeRadius)
        elif(look == 4): # left
            self.canvas.move("leftPupil", (-2/3)*eyeRadius, 0)
            self.canvas.move("rightPupil", (-2/3)*eyeRadius, 0)

    def nextBlink(self):
        t = random.randint(1000, 4000)
        self.nextBlinkId = self.canvas.after(t, lambda: self.blink(15))

    def blink(self, velo):
        self.canvas.move("topLid", 0, velo)
        self.canvas.move("botLid", 0, -velo)
        _, _, _, y2 = self.canvas.bbox("topLid")
        _, y1, _, _ = self.canvas.bbox("botLid")

        if y2 >= y1:
            velo *= -1
        elif y2 <= 0:
            self.nextBlink()
            return

        self.blinkId = self.canvas.after(10, lambda: self.blink(velo))

    def movePupils(self, xVelo, yVelo):
        self.canvas.move("leftPupil", xVelo, yVelo)
        self.canvas.move("rightPupil", xVelo, yVelo)
        ex1, ey1, ex2, ey2 = self.canvas.bbox("leftEye")
        px1, py1, px2, py2 = self.canvas.bbox("leftPupil")
        if px2 > ex2 or px1 < ex1:
            xVelo *= -1
        if py2 > ey2 or py1 < ey1:
            yVelo *= -1    
        self.movePupilsId = self.canvas.after(10, lambda: self.movePupils(xVelo, yVelo))

    def move(self):
        self.clear()
        x = self.canvas.winfo_screenwidth() / 2
        y = self.canvas.winfo_screenheight() / 2
        size = self.canvas.winfo_screenwidth() / 200
        head = self.canvas.create_oval(x - size*10, y - size*20 - size*30, x + size*10, y - size*30, outline = "black", tags = "figure")
        body = self.canvas.create_line(x, y, x, y - size*30, fill = "black", tags = "figure")
        leftArm = self.canvas.create_line(x, y - size*20, x - size*20, y + size*2, fill = "black", tags = "figure")
        rightArm = self.canvas.create_line(x, y - size*20, x + size*20, y + size*2, fill = "black", tags = "figure")
        leftLeg = self.canvas.create_line(x, y, x - size*12, y + size*32, fill = "black", tags = "figure")
        rightLeg = self.canvas.create_line(x, y, x + size*12, y + size*32, fill = "black", tags = "figure")
        leftFoot = self.canvas.create_line(x - size*12, y + size*32, x - size*12, y + size*36, fill = "black", tags = "figure")
        rightFoot = self.canvas.create_line(x + size*12, y + size*32, x + size*12, y + size*36, fill = "black", tags = "figure")

        self.moveFigure(3)

    def moveFigure(self, velo):
        self.canvas.move("figure", velo, 0)
        x1, _ , x2, _ = self.canvas.bbox("figure")
        if x2 > self.canvas.winfo_screenwidth() or x1 < 0:
            velo *= -1
        self.moveFigureId = self.canvas.after(10, lambda: self.moveFigure(velo))

    def printWordSpiral(self, word, fontSize, speak):
        self.clear()
        self.canvas.create_text(self.canvas.winfo_screenwidth() // 2, self.canvas.winfo_screenheight() // 2, text=word, font=("Helvetica", fontSize, "bold"), fill="black", tags="word")

        self.spiral(0, fontSize, fontSize)

        if speak:
            threading.Thread(target=self.speech.speak, args=(word,)).start()

    def spiral(self, angle, initialSize, currentSize):
        self.canvas.itemconfig("word", angle=angle, font=("Helvetica", currentSize, "bold"))
        if currentSize <= 5:
            currentSize = initialSize + 5
            angle = -30
        self.spiralId = self.canvas.after(100, lambda: self.spiral(angle + 30, initialSize, currentSize - 5))

    def printText(self, textContent, fontSize, speak):
        self.clear()
        self.canvas.create_text(self.canvas.winfo_screenwidth()//2, self.canvas.winfo_screenheight()//2, text=textContent, font=("Helvetica", fontSize), fill="black")
        
        if speak:
            threading.Thread(target=self.speech.speak, args=(textContent,)).start()


def run(root):
    global DIRECTION
    display = Screen(root)
    text = "Hey there! My name is Bobby."
    word = "Go Bobcats!"
    armMovement = {'t', 'y', 'u', 'i', 'o', 'p', 'f', 'g', 'h', 'j', 'k', 'l'}
    DIRECTION = 1

    def on_key_press(event):
        global DIRECTION

        #TEST KEYS
        if event.char == '1':
            display.move()
        elif event.char == '2':
            display.printText(text, 20, True)
        elif event.char == '3':
            display.printWordSpiral(word, 150, True)
        elif event.char == '4':
            display.drawEyes(0)
        elif event.char == '5':
            display.drawEyes(1)
        elif event.char == '6':
            display.drawEyes(2)
        elif event.char == '7':
            display.drawEyes(3)
        elif event.char == '8':
            display.drawEyes(4)
        elif event.char == '9':
            display.drawEyes(5)

        # WHEELS
        elif event.char == 'w': # Moving forward
            display.move()
        elif event.char == 's': # Moving backward
            display.move()
        elif event.char == 'a': # Turning left
            display.drawEyes(2)
        elif event.char == 'd': # Turning right
            display.drawEyes(4)
        
        elif event.char == '-': # Changing direction
            DIRECTION *= -1
            print("proj3_threads: direction =", DIRECTION)

        # HEAD & WAIST
        elif event.char == 'z': # Moving waist
            if DIRECTION == 1:
                display.drawEyes(2)
            else:
                display.drawEyes(4)
        elif event.char == ',': # Turning head
            if DIRECTION == 1:
                display.drawEyes(2)
            else:
                display.drawEyes(4)
        elif event.char == '.': # Tilting head
            if DIRECTION == 1:
                display.drawEyes(1)
            else:
                display.drawEyes(3)

        # ARMS
        elif event.char in armMovement:
            display.drawEyes(5)

    display.root.bind('<KeyPress>', on_key_press)

    display.root.mainloop()

if __name__ == "__main__":
    run()