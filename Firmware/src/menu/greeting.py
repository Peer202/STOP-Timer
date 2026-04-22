from menu.page import MenuPage

class GreetingsPage (MenuPage):
    def __init__(self):
        self.screens = [
            ["STOP! Timer","V0.1 by P.P."],["STOP  Timer","V0.1 by P.P."]
            ]
        self.update_menu_screens()
    def update_menu_screens(self):
        pass
