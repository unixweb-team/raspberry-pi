#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

StepPins = [17,22,23,24]
 
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
# Set to 1 or 2 for clockwise
# Set to -1 or -2 for anti-clockwise
 
# Read wait time from command line
WaitTime = int(sys.argv[2])/float(1000)
 
# Initialise variables
StepCounter = 0
 
# Start main loop
# Repeats until amount of steps is reached
for i in range(int(sys.argv[3]):  
 
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
