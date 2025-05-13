# project-animatronic-head
Creation of an animatronic head as a fun demo

## Prototype version

3D Printed head parts
https://www.thingiverse.com/thing:2781756
https://www.thingiverse.com/thing:2863069

Pololu Mini Maestro 18
https://www.pololu.com/product/1354

Raspberry Pi

Logitech F310 Game Pad
https://www.logitechg.com/en-us/products/gamepads/f310-gamepad.html

Python class for Maestro (which is where maestro.py came from)
https://github.com/FRC4564/Maestro

Also requires:

Pyserial 
https://github.com/pyserial/pyserial

If using Pygame to talk to gamepad...
Pygame 
https://www.pygame.org/news

If using Inputs to talk to gamepad...
Inputs
https://github.com/zeth/inputs


## Software Notes

- AI has been used to help write code for this project.
- Pygame on older/headless rPi is slow, using Inputs instead

## Eye Notes

- 5 servos
-- each eye (left/right)
-- each eyelid (left/right)
-- both eyes together (up/down)
