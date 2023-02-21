import RPi.GPIO as GPIO
import numpy as np
import math
from time import sleep

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

# Constants
GPIO_X = [18, 23, 24, 25]
GPIO_Y = [12, 16, 20, 21]
DELTA_T = 0.1
SEQ = [[1,0,0,0],
			 [1,1,0,0],
			 [0,1,0,0],
			 [0,1,1,0],
			 [0,0,1,0],
			 [0,0,1,1],
			 [0,0,0,1],
			 [1,0,0,1]]

def takeStep(motor, direction, seqStep):
	if motor == 'X':
		pins = GPIO_X
	elif motor == 'Y':
		pins = GPIO_Y

	for index in range(4):
		pin = pins[index]
		GPIO.output(pin,SEQ[seqStep][index])

	sleep(DELTA_T)

	if direction == 1:
		if seqStep == 7:
			return 0
		else:
			return seqStep + 1
	else:
		if seqStep == 0:
			return 7
		else :
			return seqStep - 1

def main():
	# Setup
	for pin in GPIO_X:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,False)
	for pin in GPIO_Y:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,False)

	seqStepX = 0

	for i in range(10):
		print(seqStepX)
		seqStepX = takeStep('X',1,seqStepX)


	for index in range(4):
		GPIO.output(GPIO_X[index], False)
		GPIO.output(GPIO_Y[index], False)
	print('Finished')

if __name__ == "__main__":
	main()