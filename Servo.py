#!/usr/bin/python

#run from command line, the inputs are:
#./servo.py direction delay steps
#direction is given as a 1 or a -1, 1 is clockwise motion, and -1 is anti-clockwise motion
#delay is given as full numbers and then converted into milliseconds for example 1 or 5
#steps is given as a full number again, for example 5 or 100

import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

StepPins = [5,6,13,19]
 
# Set all pins as output
for pin in StepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)
 
#define the output sequence
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]
        
StepCount = len(Seq)
StepDir = int(sys.argv[1]) 
WaitTime = int(sys.argv[2])/float(1000)
Steps = int(sys.argv[3])

# StepDir set to 1 or 2 for clockwise
# STepDir set  to -1 or -2 for anti-clockwise
 
 
# Initialise variables
StepCounter = 0
 
# Start main loop
# Repeats until amount of steps is reached
for i in range(Steps):
 
  for pin in range(0,4):
    xpin=StepPins[pin]# Get GPIO
    if Seq[StepCounter][pin]!=0:
	  GPIO.output(xpin, True)
    else:
      GPIO.output(xpin, False)
 
  StepCounter += StepDir
 
  # If we reach the end of the sequence
  # start again
  if (StepCounter>=StepCount):
    StepCounter = 0
  if (StepCounter<0):
    StepCounter = StepCount+StepDir
 
  # Wait before moving on
  time.sleep(WaitTime)
