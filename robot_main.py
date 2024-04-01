from threading import Thread
from multiprocessing import Process
import key_controller
import screen
import tkinter as tk

if __name__ == "__main__":  
    root=tk.Tk()
    Thread(target=screen.run, args=(root,)).start() # start screen in seperate thread
    target=key_controller.run(root) # start key controller
    root.mainloop()