# TODO
# Make Refreshrate dependend on parameter


# Implement Printing Page
# Implement Enlarger Running Page


import keyboard
from menu.holder import MenuHolder
import time
import os
# CONFIG



# Setup

class SwitchObject():
    def __init__(self) -> None:
        pass

    def on_for_sec(self,time):
        self.switch_on()
        time.delay(time)
        self.switch_off()

    def switch_on(self):
        print("Enlarger On")
    
    def switch_off(self):
        print("Enlarger off")

switch = SwitchObject
menu = MenuHolder(switch_object=switch,debug=True)

keyboard.add_hotkey('space',menu.on_start)
keyboard.add_hotkey('m',menu.on_mode)
keyboard.add_hotkey('v',menu.on_view)
keyboard.add_hotkey('f',menu.on_focus)

keyboard.add_hotkey('up',menu.on_increment)
keyboard.add_hotkey('down',menu.on_decrement)
keyboard.add_hotkey('enter',menu.on_select)

keyboard.add_hotkey('1',lambda: menu.on_time_select(1))
keyboard.add_hotkey('2',lambda: menu.on_time_select(2))
keyboard.add_hotkey('3',lambda: menu.on_time_select(3))
# RUN


while(True):
    time.sleep(1)
    os.system('clear')
    menu.update_screen()
