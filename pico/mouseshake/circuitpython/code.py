# MouseShake is a USS mouse the shakes the mouse pointer when active! This is a hardware solution to 
# keeping a computer from sleeping.  
# CirtvuitPython - Raspberry Pi Pico

# Libraries
import time
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse

# User settings
max_shake_minutes = 240
move_distance = 100
mouse_pause = .5
loop_sleep = .5

# Define components
# TODO: Adjust pin definitions for your board layout
led = digitalio.DigitalInOut(board.GP12)
led.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)
mouse = Mouse(usb_hid.devices)

# Inititalize variables
active_state = False;
active_time = 0;

# Initial LED state
led.value = False

while True:
    if button.value:
        active_state = not active_state
        if active_state:
            led.value = True
            active_time = time.time()
        else:
            led.value = False
    if active_state:
        mouse.move(x=move_distance)
        time.sleep(mouse_pause)
        mouse.move(x=-1 * move_distance)
        time.sleep(mouse_pause)
        elapsed = time.time()- active_time
        if elapsed >= (max_shake_minutes * 60):
            active_state = False
            active_time = 0
            led.value = False
    else:
        time.sleep(loop_sleep)