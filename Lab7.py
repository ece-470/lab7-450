import RPi.GPIO as  GPIO
import time

# These are the pins we will be using.
# ENA-6, ENB-26, IN1-12, IN2-13, IN3-20, IN4-21
# wheel encoder right-CE0-8, left-CE1-7
ENA = 6
ENB = 26
IN1 = 12
IN2 = 13
IN3 = 20
IN4 = 21
CE0 = 8
CE1 = 7

#Functions to carry out movement of the robot
# 0 = GPIO.LOW  1 = GPIO.HIGH
def moveForward():
    print("Moving Forward...")
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)

def stop():
    print("Stopping...")
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.LOW)

def moveBackward():
    print("Moving Backward...")
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)

def pivotRight():
    print("Right Pivot...")
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)

def pivotLeft():
    print("Left Pivot...")
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)

# Sets the desired pin numbering system to BCM
GPIO.setmode(GPIO.BCM)

# Disables warnings in case the RPI.GPIO detects that a pin has been configured
# to something other than the default (input)
GPIO.setwarnings(False)

# Sets all the pins stated above as outputs
chan_list_out = [ENA,ENB,IN1,IN2,IN3,IN4]
chan_list_in = [CE0,CE1]
GPIO.setup(chan_list_out,GPIO.OUT)
GPIO.setup(chan_list_in,GPIO.IN)

# creates objects "p1" and "p2", sets ena and enb to 50 Hz, starts them at 20% duty cycle
p1 = GPIO.PWM(ENA,50)
p1.start(20)

p2 = GPIO.PWM(ENB,50)
p2.start(20)

rPrev = 0
rCnt = 0
lPrev = 0
lCnt = 0

while True:
	rCurr = GPIO.input(CE0)
	lCurr = GPIO.input(CE1)
	
	if(rCurr == 1 and rPrev == 0):
		rCnt += 1
	rPrev = rCurr
	if(lCurr == 1 and lPrev == 0):
		lCnt += 1
	lPrev = lCurr
	
	#time.sleep(1)
	print("Right wheel: ", rCnt, "\n")
	print("Left wheel: ", lCnt, "\n")



# Stops both the PWM outputs
p1.stop()
p2.stop()

# Cleans up the used resources
GPIO.cleanup()
