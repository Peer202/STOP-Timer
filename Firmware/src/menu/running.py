import time
# TODO
# Just the Screen thats showing while the Enlarger is on for a given duration
#   Make Enlarger Countdown
#   Be able to stop enlarger
#   Handle adding and removing EnlargerRunning Page
#   Cancel by pressing Mode or start
class EnlargerRunningPage():
    def __init__(self,menu,duration):
        self.screens = [["Enlarger",""],["",""]]
        self.page_handles_mode = True
        self.start_ticks = time.ticks_ms()
        self.duration_ms = duration * 1000

    def update_menu_screens(self):
        # check for 
        _time_passed = time.ticks_diff(time.ticks_ms(),self.start_ticks)
        if(self.duration_ms <= _time_passed):
            # Countdown has run out

        # also used for countdown
    
    # User Interaction Handlers

    def on_increment(self):
        pass

    def on_decrement(self):
        pass

    def on_select(self):
        pass

    def on_start(self):
        pass

    def on_mode(self):
        pass

    def on_view(self):
        pass

    def on_focus(self):
        pass

    def on_time_select(self,time_selected):
        pass

