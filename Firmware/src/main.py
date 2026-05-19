#imports

import time
import machine
from machine import Pin
from lcd1602 import LCD1602
from menu.holder import MenuHolder

from rotary_irq_rp2 import RotaryIRQ
#CONSTANTS
UPDATE_RATE = 5 # Hz
DELAY_BETWEEN_FRAMES = 1/UPDATE_RATE #s
DEBOUNCE_DURATION = 500 #ms


# State Variables
Command_queue = []
times = [0,0,0]
times_selected = 0
encoder_last_value = 0
# PIN Definitions

# INPUTS

PIN_SWITCH_START = Pin(7,Pin.IN,Pin.PULL_UP)
PIN_SWITCH_MODE = Pin(6,Pin.IN,Pin.PULL_UP)
PIN_SWITCH_VIEW = Pin(5,Pin.IN,Pin.PULL_UP)

PIN_SWITCH_TIME_1 = Pin(8,Pin.IN,Pin.PULL_UP)
PIN_SWITCH_TIME_2 = Pin(9,Pin.IN,Pin.PULL_UP)
PIN_SWITCH_TIME_3 = Pin(10,Pin.IN,Pin.PULL_UP)

PIN_SWITCH_ENCODER_SELECT = Pin(4,Pin.IN,Pin.PULL_UP)
#PIN_SWITCH_ENCODER_A = Pin(2,Pin.IN,Pin.PULL_UP)
#PIN_SWITCH_ENCODER_B = Pin(3,Pin.IN,Pin.PULL_UP)

# OUTPUTS
PIN_INDICATOR_TIME_1 = Pin(15,Pin.OUT)
PIN_INDICATOR_TIME_2 = Pin(14,Pin.OUT)
PIN_INDICATOR_TIME_3 = Pin(13,Pin.OUT)

PIN_BACKLIGHT_ENABLE = Pin(27,Pin.OUT)

PIN_ENLARGER = Pin(12,Pin.OUT)


class HardwareInterface():
    def __init__(self):
        self.lcd = LCD1602.begin_4bit(rs=16, e=17, db_7_to_4=[26, 22, 19, 18])
        self.enlarger_on = False

    def pass_menu(self,menu_object):
        self.menu = menu_object

    def on_for_sec(self,on_duration):
        self.switch_on()
        time.sleep(on_duration)
        self.switch_off()

    def switch_on(self):
        print("Enlarger On")
        self.enlarger_on = True
        self.toggle_all_leds()
    
    def switch_off(self):
        print("Enlarger off")
        self.enlarger_on = False
        self.toggle_all_leds()

    def print_to_disp(self,row,row_text):
        self.lcd.write_text(0, row, row_text)

    def clear_disp(self):
        self.lcd.clear()    

    def on_time_select(self,pin):
        if(pin == PIN_SWITCH_TIME_1):
           t = 1
        if(pin == PIN_SWITCH_TIME_2):
           t = 2
        if(pin == PIN_SWITCH_TIME_3):
           t = 3
        self.menu.on_time_select(t)

    def toggle_all_leds(self):
        for pin in [PIN_INDICATOR_TIME_1,PIN_INDICATOR_TIME_2,PIN_INDICATOR_TIME_3]:
            pin.toggle()

def InputISR(pin):
    Command_queue.append(pin)

def Execute_from_Queue():
    global Command_queue
    if(len(Command_queue)==0):
        return
    irq_source = Command_queue[0]


    if(irq_source == PIN_SWITCH_MODE):
        menu.on_mode()

    if(irq_source == PIN_SWITCH_VIEW):
        menu.on_view()

    if(irq_source == PIN_SWITCH_ENCODER_SELECT):
        menu.on_select()
    if(irq_source == PIN_SWITCH_START):
        menu.on_start()

    Command_queue = []

def InputEncoder():
    global encoder_last_value
    _curr_value = encoder.value()
    #print(_curr_value)
    if(_curr_value > encoder_last_value):
        menu.on_increment()
        #print("Increment")
    if(_curr_value < encoder_last_value):
        menu.on_decrement()
        #print("decrement")
    else:
        print("Encoder intterupt, but Value has not changed")
    encoder_last_value = _curr_value

    
hardware = HardwareInterface()
menu = MenuHolder(hardware_object=hardware,debug=True)

encoder = RotaryIRQ(
    pin_num_clk=2,
    pin_num_dt=3,
    min_val=0,
    max_val=10,
    incr=1,
    reverse=True,
    range_mode=RotaryIRQ.RANGE_UNBOUNDED,
    pull_up=True
)
encoder.add_listener(InputEncoder)

# INPUT INTERRUPTS

#PIN_SWITCH_START.irq(trigger=Pin.IRQ_FALLING, handler=hardware.on_start)
#PIN_SWITCH_MODE.irq(trigger=Pin.IRQ_FALLING, handler=hardware.on_mode)
#PIN_SWITCH_VIEW.irq(trigger=Pin.IRQ_FALLING, handler=hardware.on_view)
#PIN_SWITCH_ENCODER_SELECT.irq(trigger=Pin.IRQ_FALLING, handler=hardware.on_select)

for pin in [PIN_SWITCH_START,PIN_SWITCH_MODE,PIN_SWITCH_VIEW,PIN_SWITCH_ENCODER_SELECT]:
    pin.irq(trigger=Pin.IRQ_FALLING, handler=InputISR)

for pin in [PIN_SWITCH_TIME_1,PIN_SWITCH_TIME_2,PIN_SWITCH_TIME_3]:
    pin.irq(trigger=Pin.IRQ_FALLING, handler=hardware.on_time_select)

#PIN_BACKLIGHT_ENABLE.on()

time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico W!")

while(True):
    print(Command_queue)
    Execute_from_Queue()
    #PIN_BACKLIGHT_ENABLE.toggle()
    time.sleep(DELAY_BETWEEN_FRAMES)
    menu.update_screen()


