from threading import Thread
import key_controller
import screen

if __name__ == "__main__":  
    key_controller.run() # start key controller
    Thread(target=screen.run).start() # start screen in seperate thread