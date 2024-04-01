from threading import Thread
from multiprocessing import Process
import key_controller
import screen

if __name__ == "__main__":  
    Process(target=screen.run).start() # start screen in seperate thread
    Process(target=key_controller.run).start() # start key controller