# Server Program

import socket
import pickle
import pyttsx3
import subprocess
import platform

engine = pyttsx3.init()

def main():
    token = "your turn"
    port = 9000
    if(platform.system() == 'Linux'):
        host = subprocess.check_output(['hostname', '-I']).decode().strip() # Linux
    else:
        host = str(socket.gethostbyname(socket.gethostname())) # Windows
    
    print("Server starting on " + host)

    #bind socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind( (host, port) )

    serverSocket.listen(1)
    connection, addr = serverSocket.accept()

    lines = ["Hi.", "I was just going to say the same thing about you. Where are you from?", "Me too. Bozeman, Montana", 
             "Me too, wow that is wild. What is your name?", "You're not going to believe this, but my name is Tango also.", 
             "Looking around this room I'd say pretty high."]

    string = ""
    count = 0
    
    while True:
        if(count == 0):
            print(lines[count])
            engine.say(lines[count])
            engine.runAndWait()
            count+=1
            data = pickle.dumps(token)
            connection.sendall(data)
            continue

        (msg, addr) = connection.recvfrom(1024)
        msg = pickle.loads(msg)
        
        if (msg == token):
            print(lines[count])
            engine.say(lines[count])
            engine.runAndWait()
            if(count == len(lines) - 1):
                #end connection
                break
            else:
                count +=1
            
            data = pickle.dumps(token)
            connection.sendall(data)
        elif(msg == "EOF"):
            print(lines[count])
            engine.say(lines[count])
            engine.runAndWait()
            break
        else:
            print("ERROR: recieved '" + msg + "' instead of token")

    print("Server Done")
    

main()