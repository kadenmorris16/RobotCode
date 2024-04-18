import serial
import math
import pyttsx3
import time
#import key_controller

engine = pyttsx3.init()
#k_c = key_controller.run()

#Old method, probably won't work
def calculateAngle(distances, closest, opposite):
    dx = distances[opposite] - distances[closest]
    dy = distances[(opposite + 1) % 4] - distances[closest]
    angle = math.degrees(math.atan2(dy, dx))
    return angle

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

    if(closest == target):
        print("FACING TARGET")
        #move(d_after, target)
    elif(closest == findOppositeAnchor(target)):
        print("FACING OPPOSITE")



# Not very elegant but avoids doing trig, might need to rework after testing
def move(distances, anchor):
    last_distance = distances[anchor]
    current_distance = last_distance

    #In theory, should exit loop once the distance between the anchor and robot begins to increase again
    while(current_distance <= last_distance):
        # move robot forward 0.5m
        last_distance = current_distance
        current_distance = getSerialData()[anchor]
        time.sleep(0.5)

# Returns an array of anchor distances
def getSerialData():
    ser = serial.Serial('COM5',115200)
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
                    #print("Distance to Anchor 0: " + split[1]) #Distance measured in meters with two decimal places (ex: 2.39)
                    if(len(split) > 4):
                        distances = [float(split[1]), float(split[2]), float(split[3]), float(split[4])]
                        all_distances[got_data] = distances
                        got_data += 1
                    # print("Distance to Anchor 1: " + split[2])
                    # print("Distance to Anchor 2: " + split[3])
                    # print("Distance to Anchor 3: " + split[4])
        except:
            print("Error found while decoding, skipping line...")
    final_dist = [0, 0, 0, 0]
    for i in range(4):
        total = all_distances[0][i] + all_distances[1][i] + all_distances[2][i]
        final_dist[i] = total / 3.0
    print(final_dist)
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
    angle = determineAngle(distances, getSerialData(), closest)

    # Correct angle to face (anchor or a specific direction?)
    initial_direction = ""
    if angle < -45 and angle >= -135:
        initial_direction = "Facing up"
    elif angle >= 45 and angle < 135:
        initial_direction = "Facing down"
    elif angle >= 135 or angle < -135:
        initial_direction = "Facing left"
    else:
        initial_direction = "Facing right"

    # Move out of boundary 
    move(distances, closest)

    # Announce "exited"
    engine.say("Exited")
    engine.runAndWait()


# Test code
run()

        
        
            
    
    