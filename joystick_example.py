#
# Example code cobbled together for gamepad testing
#
# uses pygame, which isn't great on slower rPi...
#

import pygame

# Initialize Pygame
pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Check for available joysticks
joystick_count = pygame.joystick.get_count()
print(f"Number of joysticks detected: {joystick_count}")

# Find a Logitech game controller (you might need to adjust the name)
logitech_joystick = None
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    name = joystick.get_name()
    print(f"Joystick {i}: {name}")
    if "Logitech" in name:
        logitech_joystick = joystick
        print(f"Found Logitech joystick: {name}")
        break

if not logitech_joystick:
    print("No Logitech joystick found. Please connect one and try again.")
    pygame.quit()
    exit()

# Get the number of axes on the joystick
axes = logitech_joystick.get_numaxes()
print(f"Number of axes: {axes}")
joystick_values = [0.0] * axes

buttons = logitech_joystick.get_numbuttons()
print(f"Number of buttons: {buttons}")
joystick_buttons = [False] * buttons

hats = logitech_joystick.get_numhats()
print(f"Number of hats: {hats}")
hat_state = (0, 0)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if hasattr(event, 'joy'):
            if event.joy == logitech_joystick.get_id():
                if event.type == pygame.JOYAXISMOTION:
                    axis_index = event.axis
                    axis_value = event.value
                    joystick_values[axis_index] = axis_value
                elif event.type == pygame.JOYBUTTONDOWN:
                    button_index = event.button
                    joystick_buttons[button_index] = True
                elif event.type == pygame.JOYBUTTONUP:
                    button_index = event.button
                    joystick_buttons[button_index] = False

                hat_state = logitech_joystick.get_hat(0)

                for i in range(0,axes):
                    print(f"{joystick_values[i]:.3f} ", end = '')
                print()

                for i in range(0,buttons):
                    print(f"{joystick_buttons[i]} ", end = '')
                print()

                print(f"{hat_state} ", end = '')
                print()
                print('--------')

    # You can add other game logic here, like updating a display based on joystick input

# Quit Pygame
pygame.quit()