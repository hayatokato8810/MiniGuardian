import atexit
from StepperMotor import StepperMotor

motor1 = StepperMotor('Yaw',  [18, 23, 24, 25])
motor2 = StepperMotor('Pitch',[12, 16, 20, 21])

def main():
	print("Starting")

	for i in range(2000):
		motor1.step('cw')
	for i in range(480):
		motor1.step('ccw')

def cleanup():
	motor1.__exit__()
	motor2.__exit__()
atexit.register(cleanup)

if __name__ == "__main__":
	main()