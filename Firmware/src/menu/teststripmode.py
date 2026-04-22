from menu.page import MenuPage

#TODO
# Make TeststripStartPage functional

class TestStripLinearPage (MenuPage):
    def __init__(self,menuholder):
        self.menutitle = "Test Strip Mode Linear"
        self.menuholder = menuholder
        self.parameters = [
            [" min: ",1,1],
            [" max: ",10,1],
            [" steps: ",10,1]
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
        self.parameters[self.selected_parameter_index][1] = param[1] - param[2]
        self.update_menu_screens()

    def on_select(self):
        print(self.selected_parameter_index)
        if(self.selected_parameter_index == len(self.parameters) - 1):
            self.selected_parameter_index = 0
        else:
            self.selected_parameter_index = self.selected_parameter_index + 1
        
        self.update_menu_screens()
        

    def on_start(self):
        # Initiate a new subpage and push to menu Holder object#
        self.menuholder.force_new_menu_page(
            TestStripStartPage(self,
            min=self.parameters[0] [1],
            max=self.parameters[1] [1],
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
    def __init__(self,testparampage,min,max,steps):
        self.menutitle = "Press Start to Begin next Step"
        self.testparampage = testparampage
        self.steps = [1, 2,3,4,5]
        self.current_step_index = 0
        self.update_menu_screens()
    
    def update_menu_screens(self):
        self.screens = [["",""],["",""]]
        self.screens[0][0] = self.menutitle
        self.screens[1][0] = self.menutitle

        for i,step in enumerate(self.steps):
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
        if(self.current_step_index == len(self.steps) - 1):
            self.current_step_index = 0
        else:
            self.current_step_index = self.current_step_index + 1
        
        self.update_menu_screens()



