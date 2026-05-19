from menu.page import MenuPage

# TODO
# Add Countdown for safety Shutoff

class FocusPage(MenuPage):
    def __init__(self,menu):
        self.menutitle = "FOCUS ON"
        self.menu = menu
        self.page_handles_mode = False
        self.update_menu_screens()

    def update_menu_screens(self):
        self.screens = [["",""],["",""]]
        self.screens[0][0] = self.menutitle
        self.screens[1][0] = self.menutitle

        if(self.menu.hardware.enlarger_on):
            self.screens[0][1] = "ON"
            self.screens[1][0] = ""
        else:
            self.screens[0][1] = "OFF"
            self.screens[1][0] = ""

    def on_start(self):
        # Start Enlarger and Blink LEDs
        if(self.menu.hardware.enlarger_on):
            self.menu.hardware.switch_off()
        else:
            self.menu.hardware.switch_on()

        self.update_menu_screens()
    

    def on_mode(self):
        
        self.menu.hardware.switch_off() # make sure enlarger is off before object is destroyed

    def on_view(self):
        pass

    def on_time_select(self,time_selected):
        pass
