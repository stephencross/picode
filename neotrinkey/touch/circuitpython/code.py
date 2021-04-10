# This exmaple uses the Adafruit Neo Trinkey - SAMD21 USB Key with 4 NeoPixels
# It turns all 4 LEDs to rred when touch 1 is touched, blue for touch 2 and yellow for both


import board
import touchio
import neopixel
import time

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

while True:
    if touch1.value and touch2.value:
        pixels.fill(YELLOW)
    else:
        if touch1.value:
            pixels.fill(RED)
        elif touch2.value:
            pixels.fill(BLUE)
        else:
            pixels.fill(NONE)
    time.sleep(0.05)
    