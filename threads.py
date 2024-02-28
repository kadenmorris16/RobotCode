import tkinter as tk

class Screen:
    def __init__(self):
        self.name = "Rob"
        self.runUI()

    def runUI(self):
        root = tk.Tk()
        root.attributes('-fullscreen', True)

        c = tk.Canvas(root)
        c.pack(fill=tk.BOTH, expand=True)

        self.drawEyes(c)

        root.mainloop()
    
    def drawEyes(self, c):
        cHeight = c.winfo_reqheight()
        cWidth = c.winfo_reqwidth()
        height = cHeight/2 - cHeight/100
        width = cWidth/2 - cWidth/100
        lEye = c.create_oval(cWidth/2 - width, cHeight/2 -height, cWidth/2 +width, cHeight/2 +height)
        c.itemconfig(lEye, fill='red')


robot = Screen()