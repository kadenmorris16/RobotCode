import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

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
    print("AAA")
    pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

while True:
    print(getDistance())
    time.sleep(1)

