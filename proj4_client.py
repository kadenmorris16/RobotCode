# Client Program

import socket
import pickle
import pyttsx3
import platform
import subprocess

engine = pyttsx3.init()

def main():
    
    token = "your turn"
    port = 9000
    if(platform.system() == 'Linux'):
        host = subprocess.check_output(['hostname', '-I']).decode().strip() # Linux
    else:
        host = str(socket.gethostbyname(socket.gethostname())) # Windows

    #host = "192.168.43.81"
    server_ip = "192.168.1.236" #MANUAL INPUT

    print("Client starting on " + host)

    #server = (server_ip, port)
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((server_ip, port))
    print("Connected to server.")

    lines = ["Hi, you look familiar.", "I am from Montana, where are you from?", 
             "Me too, I am from the room we are in currently in Bozeman, Montana.", "Tango.", 
             "What are the odds. Two robots run into to each other from the same state, and the same town, and the same room, with the same name?"]

    count = 0
    
    while True:
        msg = clientSocket.recv(1024)
        msg = pickle.loads(msg)

        if (msg == token):
            print(lines[count])
            engine.say(lines[count])
            engine.runAndWait()
            
            if(count == len(lines) - 1):
                data = pickle.dumps("EOF")
                clientSocket.sendall(data)
                break
            else:
                count+=1
                data = pickle.dumps(token)
                clientSocket.sendall(data)

    print("Client done")      

main()