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
eye['EyeLeftRight'] = {}
eye['EyeLeftRight']['channel'] = 0
eye['EyeLeftRight']['value'] = 0.0
eye['EyeLeftRight']['max'] = 1744*4 
eye['EyeLeftRight']['min'] = 1248*4

eye['EyesUpDown'] = {}
eye['EyesUpDown']['channel'] = 1
eye['EyesUpDown']['value'] = 0.0
eye['EyesUpDown']['max'] = 1248*4
eye['EyesUpDown']['min'] = 1744*4

eye['LeftUpperEyeLid'] = {}
eye['LeftUpperEyeLid']['channel'] = 2
eye['LeftUpperEyeLid']['value'] = 0.0
eye['LeftUpperEyeLid']['max'] = 1056*4 
eye['LeftUpperEyeLid']['min'] = 2000*4

eye['LeftLowerEyeLid'] = {}
eye['LeftLowerEyeLid']['channel'] = 3
eye['LeftLowerEyeLid']['value'] = 0.0
eye['LeftLowerEyeLid']['max'] = 944*4
eye['LeftLowerEyeLid']['min'] = 1648*4

eye['RightUpperEyeLid'] = {}
eye['RightUpperEyeLid']['channel'] = 4
eye['RightUpperEyeLid']['value'] = 0.0
eye['RightUpperEyeLid']['max'] = 1104*4
eye['RightUpperEyeLid']['min'] = 2000*4

eye['RightLowerEyeLid'] = {}
eye['RightLowerEyeLid']['channel'] = 5
eye['RightLowerEyeLid']['value'] = 0.0
eye['RightLowerEyeLid']['max'] = 1248*4
eye['RightLowerEyeLid']['min'] = 2000*4


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


		if button['BTN_TL'] == 0:
			setEye('EyeLeftRight', joystick['ABS_X'] / 32768.0)
			setEye('EyesUpDown', joystick['ABS_Y'] / 32768.0)
		else:
			setEye('LeftUpperEyeLid', joystick['ABS_X'] / 32768.0)
			setEye('LeftLowerEyeLid', joystick['ABS_Y'] / 32768.0)

		if button['BTN_TR'] == 1:
			setEye('RightUpperEyeLid', joystick['ABS_RX'] / 32768.0)
			setEye('RightLowerEyeLid', joystick['ABS_RY'] / 32768.0)


