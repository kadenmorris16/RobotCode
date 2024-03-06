# Server Program

import socket
import random
import sys
import csv
import pickle
import time
import pyttsx3


engine = pyttsx3.init()



def main():
    host = "192.168.1.64" # Server's IP
    token = "your turn"
    port = 6000
    print("Server starting on " + host)

    client = ("192.168.1.64", 6005)

    #bind socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind( (host, port) )

    lines = ["Hi.", "I was just going to say the same thing about you. Where are you from?", "Me too. Bozeman, Montana", 
             "Me too, wow that is wild. What is your name?", "You're not going to believe this, but my name is Tango also.", 
             "Looking around this room I'd say pretty high."]

    #serverSocket.listen(1)

    #accept new connection(s)
    #connection, addr = serverSocket.accept()

    string = ""
    count = 0
    
    while True:
        if(count == 0):
            print(lines[count])
            engine.say(lines[count])
            engine.runAndWait()
            count+=1
            data = pickle.dumps(token)
            serverSocket.sendto(data, client)
            continue

        (msg, addr) = serverSocket.recvfrom(1024)
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
            serverSocket.sendto(data, client)
        elif(msg == "EOF"):
            print(lines[count])
            engine.say(lines[count])
            engine.runAndWait()
            break
        else:
            print("ERROR: recieved '" + msg + "' instead of token")

    print("Server Done")
    

main()
