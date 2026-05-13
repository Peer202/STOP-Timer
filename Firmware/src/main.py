#imports

import time
import machine
from machine import Pin
from lcd1602 import LCD1602
from menu.holder import MenuHolder
#CONFIGS
UPDATE_RATE = 2 # Hz
DELAY_BETWEEN_FRAMES = 1/UPDATE_RATE #s

# PIN Definitions

# INPUTS

PIN_SWITCH_START = Pin(7,Pin.IN,Pin.PULL_UP)
PIN_SWITCH_MODE = Pin(6,Pin.IN,Pin.PULL_UP)
PIN_SWITCH_VIEW = Pin(5,Pin.IN,Pin.PULL_UP)

PIN_SWITCH_TIME_1 = Pin(8,Pin.IN,Pin.PULL_UP)
PIN_SWITCH_TIME_2 = Pin(9,Pin.IN,Pin.PULL_UP)
PIN_SWITCH_TIME_3 = Pin(10,Pin.IN,Pin.PULL_UP)

PIN_SWITCH_ENCODER_SELECT = Pin(4,Pin.IN,Pin.PULL_UP)
#PIN_SWITCH_ENCODER_A = 
#PIN_SWITCH_ENCODER_B = 

# OUTPUTS
PIN_INDICATOR_TIME_1 = Pin(15,Pin.OUT)
PIN_INDICATOR_TIME_2 = Pin(14,Pin.OUT)
PIN_INDICATOR_TIME_3 = Pin(13,Pin.OUT)

PIN_BACKLIGHT_ENABLE = Pin(27,Pin.OUT)

PIN_ENLARGER = Pin(12,Pin.OUT)


class HardwareInterface():
    def __init__(self):
        self.lcd = LCD1602.begin_4bit(rs=16, e=17, db_7_to_4=[26, 22, 19, 18])

    def pass_menu(self,menu_object):
        self.menu = menu_object

    def on_for_sec(self,time):
        self.switch_on()
        time.delay(time)
        self.switch_off()

    def switch_on(self):
        print("Enlarger On")
    
    def switch_off(self):
        print("Enlarger off")

    def print_to_disp(self,row,row_text):
        self.lcd.write_text(0, row, row_text)

    def clear_disp(self):
        self.lcd.clear()    
    
    def on_increment(self,pin=None):
        self.menu.on_increment()

    def on_decrement(self,pin=None):
        self.menu.on_decrement()

    def on_select(self,pin=None):
        self.menu.on_select()
    
    def on_start(self,pin=None):
        self.menu.on_start()
        self.enlarger_on()
        time.sleep(3)
        self.enlarger_off()

    def on_mode(self,pin=None):
        self.menu.on_mode()

    def on_view(self,pin=None):
        self.menu.on_view()

    def on_focus(self,pin=None):
        self.menu.on_focus()

    def on_time_select(self,pin):
        if(pin == PIN_SWITCH_TIME_1):
           t = 1
        if(pin == PIN_SWITCH_TIME_2):
           t = 2
        if(pin == PIN_SWITCH_TIME_3):
           t = 3
        self.menu.on_time_select(t)
    
    def enlarger_on(self):
        PIN_ENLARGER.on()
        self.toggle_all_leds()

    def enlarger_off(self):
        PIN_ENLARGER.off()
        self.toggle_all_leds()

    def toggle_all_leds(self):
        for pin in [PIN_INDICATOR_TIME_1,PIN_INDICATOR_TIME_2,PIN_INDICATOR_TIME_3]:
            pin.toggle()
    


times = [0,0,0]
times_selected = 0
hardware = HardwareInterface()
menu = MenuHolder(hardware_object=hardware,debug=True)

# INPUT INTERRUPTS

PIN_SWITCH_START.irq(trigger=Pin.IRQ_FALLING, handler=hardware.on_start)
PIN_SWITCH_MODE.irq(trigger=Pin.IRQ_FALLING, handler=hardware.on_mode)
PIN_SWITCH_VIEW.irq(trigger=Pin.IRQ_FALLING, handler=hardware.on_view)
PIN_SWITCH_ENCODER_SELECT.irq(trigger=Pin.IRQ_FALLING, handler=hardware.on_select)

for pin in [PIN_INDICATOR_TIME_1,PIN_INDICATOR_TIME_2,PIN_INDICATOR_TIME_3]:
    pin.irq(trigger=Pin.IRQ_FALLING, handler=hardware.on_time_select)

#PIN_BACKLIGHT_ENABLE.on()

time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico W!")

while(True):
    
    #PIN_BACKLIGHT_ENABLE.toggle()
    time.sleep(DELAY_BETWEEN_FRAMES)
    menu.update_screen()


