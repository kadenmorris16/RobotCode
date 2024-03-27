from threading import Thread
import key_controller
import proj3_threads

if __name__ == "__main__":  
    key_controller.run() # start key controller
    Thread(target=proj3_threads.run).start() # start screen in seperate thread