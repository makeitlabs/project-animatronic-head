#
# head control
#
from inputs import get_gamepad
import maestro

debug = False

# windows
servoController = maestro.Controller('COM6')

# linux
# servoController = maestro.Controller()

joystick = {}
joystick['ABS_X'] = 0
joystick['ABS_Y'] = 0
joystick['ABS_RX'] = 0
joystick['ABS_RY'] = 0
joystick['ABS_Z'] = 0
joystick['ABS_RZ'] = 0
joystick['ABS_HAT0X'] = 0
joystick['ABS_HAT0Y'] = 0

button = {}
button['BTN_THUMBL'] = 0
button['BTN_THUMBR'] = 0
button['BTN_WEST'] = 0
button['BTN_EAST'] = 0
button['BTN_NORTH'] = 0
button['BTN_SOUTH'] = 0
button['BTN_START'] = 0
button['BTN_SELECT'] = 0
button['BTN_TL'] = 0
button['BTN_TR'] = 0

# to-do... reverse? trim? midpoint?

# value is -1.0 to 1.0
# max, min are servo timings 0.25us (as per maestro.py)

eye = {}
eye['LeftEye'] = {}
eye['LeftEye']['channel'] = 0
eye['LeftEye']['value'] = 0.0
eye['LeftEye']['max'] = 9000 
eye['LeftEye']['min'] = 3000

eye['RightEye'] = {}
eye['RightEye']['channel'] = 1
eye['RightEye']['value'] = 0.0
eye['RightEye']['max'] = 9000 
eye['RightEye']['min'] = 3000

eye['LeftEyeLid'] = {}
eye['LeftEyeLid']['channel'] = 2
eye['LeftEyeLid']['value'] = 0.0
eye['LeftEyeLid']['max'] = 9000 
eye['LeftEyeLid']['min'] = 3000

eye['RightEyeLid'] = {}
eye['RightEyeLid']['channel'] = 3
eye['RightEyeLid']['value'] = 0.0
eye['RightEyeLid']['max'] = 9000 
eye['RightEyeLid']['min'] = 3000

eye['EyesUpDown'] = {}
eye['EyesUpDown']['channel'] = 4
eye['EyesUpDown']['value'] = 0.0
eye['EyesUpDown']['max'] = 9000 
eye['EyesUpDown']['min'] = 3000

def setEye(item, value):
	global eye
	global servoController
	global debug

	normalized = (value + 1.0) / 2.0
	target = round(eye[item]['min'] + (eye[item]['max'] - eye[item]['min']) * normalized)
	if debug:
		print(f"Set {item} {value} {target}")
	servoController.setTarget(eye[item]['channel'], target)

while True:
	events = get_gamepad()
	for event in events:
		if event.ev_type == 'Absolute':
			joystick[event.code] = event.state
			#print(event.ev_type, event.code, event.state)
		if event.ev_type == 'Key':
			button[event.code] = event.state
			#print(event.ev_type, event.code, event.state)

		if debug:
			print(joystick)
			print(button)
			print('-----')

		setEye('LeftEye', joystick['ABS_X'] / 32768.0)

		setEye('RightEye', joystick['ABS_RX'] / 32768.0)

		if button['BTN_TL'] == 0:
			setEye('LeftEyeLid', joystick['ABS_Y'] / 32768.0)
		else:
			setEye('EyesUpDown', joystick['ABS_Y'] / 32768.0)			

		setEye('RightEyeLid', joystick['ABS_RY'] / 32768.0)


