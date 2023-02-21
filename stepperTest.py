import RPi.GPIO as GPIO
import numpy as np
import math
from time import sleep

GpioPinsX = [18, 23, 24, 25]
GpioPinsY = [12, 16, 20, 21]

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

time = 0.001

for pin in GpioPinsX:
	print(pin)

print()

for pin in GpioPinsY:
	print(pin)