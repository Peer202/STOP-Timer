from menu.page import MenuPage
from menu.running import EnlargerRunningPage
import time
# TODO
# Make TeststripStartPage functional

class TestStripLinearPage(MenuPage):
    def __init__(self,menu):
        self.menutitle = "Test Strip Mode Linear"
        self.page_handles_mode = False
        self.mainmenu = menu
        self.parameters = [
            ["mi:",1,1],
            ["dt:",1,1],
            ["st:",5,1]
        ]
        self.selected_parameter_index = 0
        self.update_menu_screens()

    def update_menu_screens(self):
        self.screens = [["",""],["",""]]
        self.screens[0][0] = self.menutitle
        self.screens[1][0] = self.menutitle

        for i,param in enumerate(self.parameters):
            param_string = param[0] + str(param[1])
            self.screens[0][1] = self.screens[0][1] + param_string

            if(i == self.selected_parameter_index):
                # parameter should not be there on second page
                self.screens[1][1] = self.screens[1][1] + (" "*len(param_string))
            else:
                self.screens[1][1] = self.screens[1][1] + param_string

            
    # User Interaction Handlers
    def on_increment(self):
        param = self.parameters[self.selected_parameter_index]
        self.parameters[self.selected_parameter_index][1] = param[1] + param[2]
        self.update_menu_screens()


    def on_decrement(self):
        param = self.parameters[self.selected_parameter_index]
        new_param_value = param[1] - param[2]
        if(new_param_value > 0):
            self.parameters[self.selected_parameter_index][1] = new_param_value
            self.update_menu_screens()

    def on_select(self):
        
        if(self.selected_parameter_index == len(self.parameters) - 1):
            self.selected_parameter_index = 0
        else:
            self.selected_parameter_index = self.selected_parameter_index + 1
        self.mainmenu.debug_print(self.selected_parameter_index)
        self.update_menu_screens()
        

    def on_start(self):
        # Initiate a new subpage and push to menu Holder object#
        self.mainmenu.force_new_menu_layer(
            TestStripStartPage(self.mainmenu,
            min=self.parameters[0] [1],
            dt=self.parameters[1] [1],
            steps= self.parameters[2] [1]
            )
        )

    def on_mode(self):
        pass

    def on_view(self):
        pass

    def on_time_select(self,time_selected):
        pass


class TestStripStartPage ():
    def __init__(self,menu,min,dt,steps):
        self.menutitle = "Press Start to Begin next Step"
        self.page_handles_mode = True
        self.mainmenu = menu
        #self.mainmenu.debug_print(str(min)+ " " + str(max)+ " " + str(steps))
        #Step Calculcationb
        self.current_step_index = 0
        self.enlarger_on_duration = float(dt)
        self.min = min
        self.vis_steps = []
        for i in range(steps):
            self.vis_steps.append(round(min + (self.enlarger_on_duration * i),1))
        

        self.mainmenu.debug_print(self.vis_steps)
        self.update_menu_screens()

    def update_menu_screens(self):
        self.screens = [["",""],["",""]]
        self.screens[0][0] = self.menutitle
        self.screens[1][0] = self.menutitle

        for i,step in enumerate(self.vis_steps):
            step_string = str(step)
            self.screens[0][1] = self.screens[0][1] + step_string

            if(i == self.current_step_index):
                # parameter should not be there on second page
                self.screens[1][1] = self.screens[1][1] + (" "*len(step_string))
            else:
                self.screens[1][1] = self.screens[1][1] + step_string

            
    # User Interaction Handlers
       

    def on_start(self):
        # Start Enlarger for x seconds, move onto next step
        # self.mainmenu.hardware.on_for_sec(self.enlarger_on_duration)
        if(self.current_step_index == 0):
            running_page_object = EnlargerRunningPage(self.mainmenu,self.min,self.on_enlarger_done)
        else:
            running_page_object = EnlargerRunningPage(self.mainmenu,self.enlarger_on_duration, self.on_enlarger_done)

        self.mainmenu.force_new_menu_layer(running_page_object)

    def on_enlarger_done(self):

        if(self.current_step_index == len(self.vis_steps) - 1):
            self.current_step_index = 0
        else:
            self.current_step_index = self.current_step_index + 1
        
        self.update_menu_screens()

    def on_mode(self):
        # Mode => Kill Testprintpage and go back to param page
        # Destrucing the Object
        self.mainmenu.remove_menu_layer(self)
        