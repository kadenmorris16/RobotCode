# Client Program

import socket
import sys
import random
import pickle
import time
import pyttsx3


engine = pyttsx3.init()


def main():
    server_ip = "192.168.1.64"
    token = "your turn"
    port = 6005
    host = '192.168.1.64'

    server = (server_ip, 6000)
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket.bind( (host,port) )

    lines = ["Hi, you look familiar.", "I am from Montana, where are you from?", 
             "Me too, I am from the room we are in currently in Bozeman, Montana.", "Tango.", 
             "What are the odds. Two robots run into to each other from the same state, and the same town, and the same room, with the same name?"]

    count = 0
    
    while True:
        (msg, addr) = clientSocket.recvfrom(1024)
        msg = pickle.loads(msg)

        if (msg == token):
            print(lines[count])
            engine.say(lines[count])
            engine.runAndWait()
            
            if(count == len(lines) - 1):
                data = pickle.dumps("EOF")
                clientSocket.sendto(data, server)
                break
            else:
                count+=1
                data = pickle.dumps(token)
                clientSocket.sendto(data, server)

    print("Client done")


        

main()

