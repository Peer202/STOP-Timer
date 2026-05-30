from menu.running import EnlargerRunningPage
from menu.page import MenuPage

class LinearPrintPage(MenuPage):
    def __init__(self,menu):
        self.menutitle = "Linear Print Mode"
        self.page_handles_mode = False
        self.mainmenu = menu

        self.times = [1.0,1.0,1.0]
        self.diff = 1
        self.diff_index = 0
        self.selected_Time_index = 0
        self.anchorpositions = [0,6,12]
        
        self.update_menu_screens()

    def update_menu_screens(self):
        self.screens = [["",""],["",""]]
        self.screens[0][0] = self.menutitle
        self.screens[1][0] = self.menutitle

        try:
            self.mainmenu.hardware.led_all_off()
            self.mainmenu.hardware.led_index_on(self.selected_Time_index)
        except:
            pass

        line_positions = 0
        for i,time in enumerate(self.times):
            time_string = (" "*(self.anchorpositions[i] - line_positions)) + str(time)
            self.screens[0][1] = self.screens[0][1] + time_string
            line_positions = line_positions + len(time_string)

            if(i == self.selected_Time_index):
                # selected time should not be there on second page
                self.screens[1][1] = self.screens[1][1] + (" "*len(time_string))
            else:
                self.screens[1][1] = self.screens[1][1] + time_string

            
    # User Interaction Handlers
    def on_increment(self):
        self.times[self.selected_Time_index] = self.times[self.selected_Time_index] + self.diff
        #print(self.times)
        self.update_menu_screens()


    def on_decrement(self):
        self.times[self.selected_Time_index] = self.times[self.selected_Time_index] - self.diff
        #print(self.times)
        if(self.times[self.selected_Time_index] < 0):
            self.times[self.selected_Time_index] = 0
        self.update_menu_screens()

    def on_select(self):
        if(self.diff == 0.5):
            self.diff = 1

        if(self.diff == 1):
            self.diff = 0.5

        self.update_menu_screens()
        

    def on_start(self):
        # Initiate a new subpage and push to menu Holder object#
        running_page_object = EnlargerRunningPage(self.mainmenu,self.times[self.selected_Time_index])
        self.mainmenu.force_new_menu_layer(running_page_object)
        self.update_menu_screens()


    def on_mode(self):
        self.mainmenu.hardware.led_all_off()

    def on_view(self):
        pass

    def on_time_select(self,time_selected):
        self.selected_Time_index = time_selected
        
        self.update_menu_screens()
