#!/usr/bin/env python

from time import sleep
import os
import RPi.GPIO as GPIO
import time
import subprocess
from random import randint

# setups ports for speakers
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

# setup port for digital read in from Person interrupt
GPIO.setup(18, GPIO.IN)

init = True

# an array of the ports
ports = [4, 5, 22, 27]
print(ports)
        
while True:
	if (init == True):
		print "Initializing for 5 seconds"
		init =False
		sleep(5)

	# Read the value to see if anyone has walked by
	input_value = 0 #init to 0 then read
	input_value = GPIO.input(18)
	print("Read Radar Input As: " + str(input_value))
	if(input_value == 1):
	#if (1 == 1):
		
		#------------------------- Witches --------------------------
		# set to port 4 (speaker 1) and turn on the GPIO port for the speaker
		port = 4
		GPIO.output(port, True)

		# play witches, print and create song play command
		song = "/home/pi/halloween/witch1.mp3"
		reccmd = ["/usr/bin/mpg321", "-q", song]
		p = subprocess.Popen(reccmd, stdout=subprocess.PIPE)
		while (p.poll() == None):
			sleep(.3)

		# turn off the port (can't have more than one port on or the speakers will be in parallel)
		GPIO.output(port, False)
		sleep(3)
		
        #------------------------- Background1 --------------------------
		# set to port 5 (speaker 2) and turn on the GPIO port for the speaker
		port = 5
		GPIO.output(port, True)

		# play Crow, print and create song play command
		song = "/home/pi/halloween/howl.mp3"
		reccmd = ["/usr/bin/mpg321", "-q", song]
		p = subprocess.Popen(reccmd, stdout=subprocess.PIPE)
		while (p.poll() == None):
			sleep(.3)
		
		# turn off the port (can't have more than one port on or the speakers will be in parallel)
		GPIO.output(port, False)
		sleep(1)

		#------------------------- Baby Doll --------------------------
		# set to port 22 (speaker 3) and turn on the GPIO port for the speaker
		port = 22
		GPIO.output(port, True)

		# play Baby Doll1, print and create song play command
		song = "/home/pi/halloween/babydoll1.mp3"
		reccmd = ["/usr/bin/mpg321", "-q", song]
		p = subprocess.Popen(reccmd, stdout=subprocess.PIPE)
		while (p.poll() == None):
			sleep(.3)
		
        # play Baby Doll2, print and create song play command
		song = "/home/pi/halloween/babydoll2.mp3"
		reccmd = ["/usr/bin/mpg321", "-q", song]
		p = subprocess.Popen(reccmd, stdout=subprocess.PIPE)
		while (p.poll() == None):
			sleep(.3)
			
		# turn off the port (can't have more than one port on or the speakers will be in parallel)
		GPIO.output(port, False)
		sleep(1)

		#------------------------- Background2 --------------------------
		# set to port 27 (speaker 2) and turn on the GPIO port for the speaker
		port = 27
		GPIO.output(port, True)

		# play Crow, print and create song play command
		song = "/home/pi/halloween/crow.mp3"
		reccmd = ["/usr/bin/mpg321", "-q", song]
		p = subprocess.Popen(reccmd, stdout=subprocess.PIPE)
		while (p.poll() == None):
			sleep(.3)
		
		# turn off the port (can't have more than one port on or the speakers will be in parallel)
		GPIO.output(port, False)
		sleep(1)

		#------------------------- Skeleton --------------------------
		# set to port 27 (speaker 4) and turn on the GPIO port for the speaker
		port = 27
		GPIO.output(port, True)

		# play skeleton2, print and create song play command
		song = "/home/pi/halloween/skeleton2.mp3"
		reccmd = ["/usr/bin/mpg321", "-q", song]
		p = subprocess.Popen(reccmd, stdout=subprocess.PIPE)
		while (p.poll() == None):
			sleep(.3)
		
        # play skeleton scream, print and create song play command
		song = "/home/pi/halloween/babydollscream.mp3"
		reccmd = ["/usr/bin/mpg321", "-q", song]
		p = subprocess.Popen(reccmd, stdout=subprocess.PIPE)
		while (p.poll() == None):
			sleep(.3)
			
		# turn off the port (can't have more than one port on or the speakers will be in parallel)
		GPIO.output(port, False)
		sleep(1)

        #------------------------- Background2 --------------------------
		# set to port 5 (speaker 2) and turn on the GPIO port for the speaker
		port = 5
		GPIO.output(port, True)

		# play Crow, print and create song play command
		song = "/home/pi/halloween/creepy1.mp3"
		reccmd = ["/usr/bin/mpg321", "-q", song]
		p = subprocess.Popen(reccmd, stdout=subprocess.PIPE)
		while (p.poll() == None):
			sleep(.3)
		
        # turn off the port (can't have more than one port on or the speakers will be in parallel)
		GPIO.output(port, False)
		sleep(1)
	
	#Wait 3 seconds to lokk for movement
	sleep(3)