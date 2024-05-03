import serial
import math
import pyttsx3
import time
from tango import Tango
import RPi.GPIO as GPIO

engine = pyttsx3.init()
tango = Tango()

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
THRESHOLD = 70 # Distance at which the robot stops for obstactle

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def getDistance():
    GPIO.output(TRIG, False)
    time.sleep(0.1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = time.time()
    timeout = time.time()
    while GPIO.input(ECHO) == 0:
        if(time.time() - timeout) > 3:
            print("Timeout occurred while receiving echo signal")
            return None
    while GPIO.input(ECHO) == 1:
        if(time.time() - timeout) > 3:
            print("Timeout occurred while receiving echo signal")
            return None
    print("New Reading:")
    pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

def findClosestAnchor(distances):
    closest = 0 #Closest anchor number
    lowest = 100
    index = 0
    for x in distances:
        if(x < lowest):
            lowest = x
    closest = distances.index(lowest)
    print("Anchor " + str(closest) + " is the closest.")
    return closest


#Currently assumes that anchors are positioned:
#     0  1
#     3  2
def findOppositeAnchor(closest):
    if(closest == 0):
        return 2
    elif(closest == 1):
        return 3
    elif(closest == 2):
        return 0
    elif(closest == 3):
        return 1
    
def determineAngle(d_before, d_after, target):
    # Calculate the changes in distances between anchors
    changes = [0, 0, 0, 0]
    for i in range(len(d_before)):
        changes[i] = d_after[i] - d_before[i]
    print(changes)
    sorted = changes.copy()
    sorted.sort()
    closest = changes.index(sorted[0])
    next = changes.index(sorted[1])
    print("Between anchors " + str(closest) + " and " + str(next))
    #Figure out the rest after testing

    if(closest == target): #Probably don't need to adjust
        print("FACING TARGET")
        move(d_after, target)
    elif(closest == findOppositeAnchor(target)): #Should do a ~180 degree turn
        print("FACING OPPOSITE")
        turn(3, 'r')
    elif(next == target): # Turn 45 degrees from closest
        turn(1, getDirection())
    else: # Target is in position 3, so do a 3/4 turn
        turn(2, getDirection())

def getDirection(target, closest):
    anchors = [0, 1, 2, 3]
    if(closest == 0 and target == 3):
        return 'r'
    elif(closest == 3 and target == 0):
        return 'l'
    else:
        if(target > closest):
            return 'r'
        elif(target < closest):
            return 'l'

def turn(rotations, direction):
    for i in range(rotations):
        if(direction == 'r'):
            tango.setServo(1, 5000)
            time.sleep(0.8)
            tango.reset(1)
        elif(direction == 'l'):
            tango.setServo(1, 7000)
            time.sleep(0.8)
            tango.reset(1)

def moveForward():
    if(getDistance() > THRESHOLD):
        tango.setServo(0, 5200)
        time.sleep(1.4)
        tango.reset(0)
    else:
        while(getDistance() < THRESHOLD):
            print("Something is blocking the way")
            time.sleep(1)
        moveForward()


# Not very elegant but avoids doing trig, might need to rework after testing
def move(distances, anchor):
    last_distance = distances[anchor]
    current_distance = last_distance

    #In theory, should exit loop once the distance between the anchor and robot begins to increase again
    for i in range(4):
        moveForward()
        last_distance = current_distance
        current_distance = getSerialData()[anchor]
        time.sleep(0.5)

# Returns an array of anchor distances
def getSerialData():
    ser = serial.Serial('/dev/ttyUSB0', 115200)
    ser.close()
    ser.open()
    distances = []
    all_distances = [[0], [0], [0]]
    got_data = 0
    while got_data < 3:

        data = ser.readline()
        try:
            data = data.decode()
            if(data[0] == '$'):
                if(data[1] != 'R'): #Range error check
                    split = data.split(',')
                    print(split)
                    if(len(split) > 4):
                        distances = [float(split[1]), float(split[2]), float(split[3]), float(split[4])]
                        all_distances[got_data] = distances
                        got_data += 1
        except:
            print("Error found while decoding, skipping line...")
    final_dist = [0, 0, 0, 0]
    for i in range(4):
        total = all_distances[0][i] + all_distances[1][i] + all_distances[2][i]
        final_dist[i] = total / 3.0
    print(final_dist)
    ser.close()
    return final_dist
                


def run():
    # Get initial serial data
    distances = getSerialData()

    # Find the closest anchor
    closest = findClosestAnchor(distances)
    #opposite = findOppositeAnchor(closest)

    # Announce the quadrant
    string = "I am in quadrant " + str(closest)
    engine.say(string)
    engine.runAndWait()

    # Figure out angle
    time.sleep(1)
    #Move forward slightly
    moveForward()
    determineAngle(distances, getSerialData(), closest)

    # Move out of boundary 
    move(distances, closest)

    # Announce "exited"
    engine.say("Exited")
    engine.runAndWait()


# Test code
#run()

        
        
            
    
    