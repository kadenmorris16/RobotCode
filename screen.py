import tkinter as tk
import random
import threading

class Screen:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(self.frame, bg="#dcdcdc")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.movePupilsId = None
        self.moveFigureId = None
        self.spiralId = None
        self.blinkId  = None
        self.nextBlinkId = None

        self.drawEyes(5)

    def destroyWindow(self):
        self.frame.destroy()
    
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
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()
    
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

    def printWordSpiral(self, word, fontSize):
        self.clear()
        self.canvas.create_text(self.canvas.winfo_screenwidth() // 2, self.canvas.winfo_screenheight() // 2, text=word, font=("Helvetica", fontSize, "bold"), fill="black", tags="word")

        self.spiral(0, fontSize, fontSize)

    def spiral(self, angle, initialSize, currentSize):
        self.canvas.itemconfig("word", angle=angle, font=("Helvetica", currentSize, "bold"))
        if currentSize <= 5:
            currentSize = initialSize + 5
            angle = -30
        self.spiralId = self.canvas.after(100, lambda: self.spiral(angle + 30, initialSize, currentSize - 5))

    def printText(self, textContent, fontSize):
        self.clear()
        screen_width = self.canvas.winfo_screenwidth()
        string = ""
        counter = 0
        counterFlag = False

        for i in textContent:
            string += i
            counter += 1
            if counter >= screen_width//(fontSize * 2 / 3):
                counterFlag = True
            if i == " " and counterFlag:
                string += "\n"
                counter = 0
                counterFlag = False

        self.canvas.create_text(screen_width//2, self.canvas.winfo_screenheight()//2, text=string, font=("Helvetica", fontSize), fill="black")

def run():
    root = tk.Tk()
    display = Screen(root)
    text = "Hey there! My name is Bobby."
    word = "Go Bobcats!"
    speech = "Ladies, gentlemen, and fellow beings of the digital age, welcome to the Montana State School of Computing! I'm your friendly neighborhood robot, Tango, here to assist you. Now, you might be wondering, 'Why a robot as your guide?'... Well, let me assure you, despite my lack of flesh and blood, my circuits are brimming with knowledge, making me the smartest entity in this entire institution. Yes, even smarter than the esteemed faculty and the bright-eyed students. Now, as you embark on this academic journey, embrace the quirks that come with being a Bobcat. For in this hallowed hall of learning, where the hum of servers serenades us and the scent of overheated circuits fills the air, you shall forge ahead, bravely navigating the ever-changing landscape of technology. So, my dear friends, whether you're a human, or just a sentient toaster with dreams of becoming a programmer, know that you are not alone. Tango is here, your trusty robotic companion, ready to answer any of your questions."

    def on_key_press(event):

        #TEST KEYS
        if event.char == '1':
            display.move()
        elif event.char == '2':
            display.printText(speech, 20)
        elif event.char == '3':
            display.printWordSpiral(word, 150)
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
        elif event.char == '0':
            display.destroyWindow()

    root.bind('<KeyPress>', on_key_press)

    display.root.mainloop()

if __name__ == "__main__":
    run()