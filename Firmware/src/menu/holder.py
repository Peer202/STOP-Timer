# Imports
from menu.page import MenuPage
from menu.teststripmode import TestStripLinearPage
from menu.greeting import GreetingsPage

class MenuHolder:
    # Main Menu Objects. Holds all Pages as Children and controls Program Flow

    def __init__(self,switch_object,debug=False) -> None:
        self.MenuPages = []
        
        self.CurPageIndex = 0
        self.debug = debug

        self.switch = switch_object

        self.add_menu_page(TestStripLinearPage(self))

        self.screen_page_index = 0
        self.currentMenuPage = GreetingsPage()
        self.update_screen()

    def update_screen(self):
        # Called every X Seconds
        for row in self.currentMenuPage.screens[self.screen_page_index]:
            print(row)
        if(self.screen_page_index == 0):
            self.screen_page_index = 1
        else:
            self.screen_page_index = 0

    def next_menu_page(self):
        if(self.CurPageIndex == len(self.MenuPages) - 1):
            self.CurPageIndex = 0
            
        else:
            self.CurPageIndex = self.CurPageIndex + 1
        
        self.currentMenuPage = self.MenuPages[self.CurPageIndex]    
        self.debug_print("PageIndex changed:" + str(self.CurPageIndex) )
        self.currentMenuPage.update_menu_screens()

        self.update_screen()
        #redraw Screen
    
    def force_new_menu_page(self,pageobject):
        # used by children to set normally unavailable pages
        self.currentMenuPage = pageobject
        self.currentMenuPage.update_menu_screens()
        self.update_screen()
    
    def debug_print(self,msg):
        if(self.debug):
            print(msg)

    def add_menu_page(self,MenuPageObject):
        self.MenuPages.append(MenuPageObject)

    # User Interaction Handlers

    def on_increment(self):
        self.currentMenuPage.on_increment()
        print("on_increment")

    def on_decrement(self):
        self.currentMenuPage.on_decrement()
        print("on_decrement")

    def on_select(self):
        self.currentMenuPage.on_select()
        print("on_select")
    
    def on_start(self):
        self.currentMenuPage.on_start()
        print("on_start")

    def on_mode(self):
        self.currentMenuPage.on_mode()
        self.next_menu_page()
        print("on_mode")

    def on_view(self):
        self.currentMenuPage.on_view()
        print("on_view")

    def on_focus(self):
        self.currentMenuPage.on_focus()
        print("on_focus")

    def on_time_select(self,time_selected):
        print("time_selected: " + str(time_selected))
