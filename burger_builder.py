from tkinter import *

TITLE = "Arial 14"
TEXT = "Arial 11"
# The title will be used for the main header for each page and text will be used for other things like buttons

class burger_maker:
    ''' Will be used to make the order '''
    def __init__(self, root):
        # Main menu
        self.root = root
        self.root.title("Burger Builder")
        
        # Container for frames
        self.container = frame(self.root)
        self.container.grid(row=0, column=0, sticky="nsew")
        
        # Dictionary to hold the frames and keys use to create the frame
        self.frames = {}
        self.frames["menu"] = self.main_menu()
        self.frames["create_burger"] = self.burger_creation()
        self.frames["pick_side"] = self.side_selection()
        self.frames["pick_drink"] = self.drinks_selection()
        self.frames["ordering"] = self.order_menu()
        
        # Show inital frame
        self.show_frame("menu")
        
        def main_menu(self):
            
            pass
        
        def burger_creation(self):
            pass
        
        def side_selection(self):
            pass
        
        def drinks_selection(self):
            pass
        
        def order_menu(self):
            pass