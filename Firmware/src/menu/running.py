import time
# TODO
# Just the Screen thats showing while the Enlarger is on for a given duration
#   Make Enlarger Countdown
#   Be able to stop enlarger
#   Handle adding and removing EnlargerRunning Page
#   Cancel by pressing Mode or start
class EnlargerRunningPage():
    def __init__(self,menu,duration,enlarger_callback=None):
        self.screens = [["Enlarger",""],["Enlarger",""]]
        self.page_handles_mode = True
        self.start_ticks = time.ticks_ms()
        self.duration_ms = duration * 1000
        self.menu = menu
        self.menu.hardware.switch_on()
        self.callback = enlarger_callback
        self.abortflag = False
        self.update_menu_screens()

    def update_menu_screens(self):
        # check for 
        _time_passed = time.ticks_diff(time.ticks_ms(),self.start_ticks)
        self.menu.debug_print(self.duration_ms - _time_passed)
        if(self.duration_ms <= _time_passed or self.abortflag):
            # Countdown has run out
            self.menu.hardware.switch_off()
            self.screens[0][1] = "Run Out"
            self.menu.remove_menu_layer(self)
            if(self.callback != None):
                self.callback()
            self.menu.start_lockout_time = time.time()
        else:
            self.screens[0][1] = "Time Left: " + str(round((self.duration_ms - _time_passed)/1000,1))

    # User Interaction Handlers

    def on_increment(self):
        pass

    def on_decrement(self):
        pass

    def on_select(self):
        pass

    def on_start(self):
        self.abortflag = True

    def on_mode(self):
        self.abortflag = True

    def on_view(self):
        pass

    def on_focus(self):
        pass

    def on_time_select(self,time_selected):
        pass

