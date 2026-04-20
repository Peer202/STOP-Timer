#imports

import time
from machine import Pin, I2C
from i2c_lcd import i2c_lcd

#CONFIGS
INDICATOR_TIME_1 = 20
INDICATOR_TIME_2 = 19
INDICATOR_TIME_3 = 17

# PIN Definitions
# INPUTS

# OUTPUTS
PIN_INDICATOR_TIME_1 = Pin(19,Pin.OUT)
PIN_INDICATOR_TIME_2 = Pin(18,Pin.OUT)
PIN_INDICATOR_TIME_3 = Pin(17,Pin.OUT)
# Code

times = [0,0,0]
times_selected = 0


i2c = I2C(0)
d = i2c_lcd.Display(i2c)

# Clear the screen
d.clear()

# Write "Hello World" to the screen
d.write("Hello World")


time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico W!")
pinState = False
while(True):
    time.sleep(0.5)
    for pin in [PIN_INDICATOR_TIME_1,PIN_INDICATOR_TIME_2,PIN_INDICATOR_TIME_3]:
        pin.value(pinState)
    pinState = not pinState