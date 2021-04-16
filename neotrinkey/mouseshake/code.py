# This exmaple uses the Adafruit Neo Trinkey - SAMD21 USB Key with 4 NeoPixels
# It turns all 4 LEDs to rred when touch 1 is touched, blue for touch 2 and yellow for both

import board
import touchio
import neopixel
import time
import usb_hid
from adafruit_hid.mouse import Mouse

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4,auto_write=True)
pixels.brightness = .1

touch_pad_1 = board.TOUCH1
touch_pad_2 = board.TOUCH2
touch1 = touchio.TouchIn(touch_pad_1)
touch2 = touchio.TouchIn(touch_pad_2)

RED = (255,0,0)
NONE = (0,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

max_shake_minutes = 1
move_distance = 100
mouse_pause = .5
loop_sleep = .5

active_state = False;
active_time = 0;

mouse = Mouse(usb_hid.devices)

pixels.fill(NONE)

while True:
    if touch1.value or touch2.value:
        active_state = not active_state
        if active_state:
            pixels.fill(RED)
            active_time = time.monotonic()
        else:
            pixels.fill(NONE)
    if active_state:
        mouse.move(x=move_distance)
        time.sleep(mouse_pause)
        mouse.move(x=-1 * move_distance)
        time.sleep(mouse_pause)
        elapsed = time.monotonic() - active_time
        if elapsed >= (max_shake_minutes * 60):
            active_state = False
            active_time = 0
            pixels.fill(NONE)
    else:
        time.sleep(loop_sleep)
    

