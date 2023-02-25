import math
import numpy as np
from time import sleep

import RPi.GPIO as GPIO

class StepperMotor:

	SEQ = [[1,0,0,0],
		 [1,1,0,0],
		 [0,1,0,0],
		 [0,1,1,0],
		 [0,0,1,0],
		 [0,0,1,1],
		 [0,0,0,1],
		 [1,0,0,1]]

	def __init__(self, name, pins):

		print('init')

		GPIO.setwarnings(False)
		GPIO.cleanup()
		GPIO.setmode(GPIO.BCM)

		self.pos = 0
		self.name = name
		self.pins = pins

	def step(self, direction):
		for index in range(4):
			GPIO.output(self.pins[index],StepperMotor.SEQ[self.pos][index])
			#print(StepperMotor.SEQ[self.pos][index])

		if direction == 'cw':
			if self.pos == len(StepperMotor.SEQ)-1:
				self.pos = 0
			else:
				self.pos += 1
		elif direction == 'ccw':
			if self.pos == 0:
				self.pos = len(StepperMotor.SEQ)-1
			else :
				self.pos -= 1

	def __exit__(self):
		print('\nInside __exit__')
		for index in range(4):
			GPIO.output(self.pins[index], 0)






