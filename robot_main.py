from threading import Thread
import key_controller
import screen

if __name__ == "__main__":  
    Thread(target=screen.run).start() # start screen in seperate thread
    key_controller.run() # start key controller