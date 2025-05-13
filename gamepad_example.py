#
# gamepad_example using inputs https://github.com/zeth/inputs
#
from inputs import get_gamepad

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


while True:
	events = get_gamepad()
	for event in events:
		if event.ev_type == 'Absolute':
			joystick[event.code] = event.state
			#print(event.ev_type, event.code, event.state)
		if event.ev_type == 'Key':
			button[event.code] = event.state
			#print(event.ev_type, event.code, event.state)

		print(joystick)
		print(button)
		print('-----')


