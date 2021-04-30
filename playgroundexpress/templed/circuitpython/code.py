# Import Libraries
import board
import time
from adafruit_circuitplayground.express import cpx

# LED Settings
cpx.pixels.brightness = 0.2
cpx.pixels.auto_write = True
RED = (255,0,0)
NONE = (0,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

# Defaults
led_degree_delay = .1  # Seconds between LED degree display
led_tens_delay = 2. # Seconds between display tens and ones of temperature
measurement_delay = 10  # Seconds between temperature measurements

# led_temp - display temperature with LEDS.  First tens, and ones.   
def led_temp (temp_f):
    # Light an LED for each 10th dgree of temp, 72 degrees has 7 LEDs
    tens = int(abs(temp_f // 10)) * 10
    ones = int(abs(temp_f)) - tens 
    cpx.pixels.fill(NONE)
    print("Update LEDs display")
    # Display tens
    for x in range(tens / 10):
        cpx.pixels[x] = BLUE
        time.sleep(led_degree_delay)
    time.sleep(led_tens_delay)
    cpx.pixels.fill(NONE)
    # Display ones
    for x in range(ones):
        cpx.pixels[x] = YELLOW
        time.sleep(led_degree_delay)
    time.sleep(led_tens_delay)
    cpx.pixels.fill(NONE)
    
while True:
    # Take temperature measurement and convert for fahrenheit
    temperature_f = cpx.temperature * 1.8 + 32
    print(temperature_f)
    led_temp(temperature_f)
    time.sleep(measurement_delay)
