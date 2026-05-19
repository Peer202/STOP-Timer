# Imports
from menu.page import MenuPage
from Firmware.src.menu.teststriplinear import TestStripLinearPage
from menu.greeting import GreetingsPage
from menu.focus import FocusPage

# CONSTANTS
DISPLAY_RATIO = 3 # Show page 1 n times before showing Page Page 2 once

class MenuHolder:
    # Main Menu Objects. Holds all Pages as Children and controls Program Flow

    def __init__(self,hardware_object,debug=False) -> None:
        self.MenuPages = [
            TestStripLinearPage(self)
        ]
        self.CurPageIndex = 0
        self.debug = debug
        self.hardware = hardware_object
        self.hardware.pass_menu(self)

        self.screen_page_index = 0
        self.screen_counter = 0
        self.Menu_layers = [] # stack of menu Objects, the one at 0 is displayed and gets interacted with
        self.force_new_menu_layer(GreetingsPage())

    def update_screen(self):
        # Called every X Seconds
        self.hardware.clear_disp()
        if(self.screen_counter <= DISPLAY_RATIO):
            _screen_page_index = 0
            self.screen_counter = self.screen_counter + 1

        if(self.screen_counter > DISPLAY_RATIO):
            _screen_page_index = 1
            self.screen_counter = 0

        print("Menu Layers: " + str(self.Menu_layers))
        for i,row in enumerate(self.Menu_layers[0].screens[_screen_page_index]):
            self.hardware.print_to_disp(i,row)

    def next_menu_page(self):
        if(self.CurPageIndex == (len(self.MenuPages) - 1)):
            self.CurPageIndex = 0
        else:
            self.CurPageIndex = self.CurPageIndex + 1
        
        self.Menu_layers = [self.MenuPages[self.CurPageIndex]]
        self.debug_print("PageIndex changed:" + str(self.CurPageIndex) )
        self.Menu_layers[0].update_menu_screens()

        self.update_screen()
        #redraw Screen
    
    def force_new_menu_layer(self,pageobject):
        # used by children to set normally unavailable pages
        self.Menu_layers.insert(0,pageobject)
        self.Menu_layers[0].update_menu_screens()
        self.update_screen()
    
    def remove_menu_layer(self,pageobject):
        self.Menu_layers.remove(pageobject)
        self.update_screen()

    def debug_print(self,msg):
        if(self.debug):
            print(msg)

    def add_menu_page(self,MenuPageObject):
        self.MenuPages.append(MenuPageObject)

    # User Interaction Handlers

    def on_increment(self):
        self.Menu_layers[0].on_increment()
        print("on_increment")

    def on_decrement(self):
        self.Menu_layers[0].on_decrement()
        print("on_decrement")

    def on_select(self):
        self.Menu_layers[0].on_select()
        print("on_select")
    
    def on_start(self):
        self.Menu_layers[0].on_start()
        print("on_start")

    def on_mode(self):
        self.Menu_layers[0].on_mode()
        if(not self.Menu_layers[0].page_handles_mode):
            self.next_menu_page()
        print("on_mode")

    def on_view(self):
        self.Menu_layers[0].on_view()
        print("on_view")

    def on_focus(self):
        #self.Menu_layers[0].on_focus()
        self.force_new_menu_layer(FocusPage)
        print("on_focus")

    def on_time_select(self,time_selected):
        print("time_selected: " + str(time_selected))
-