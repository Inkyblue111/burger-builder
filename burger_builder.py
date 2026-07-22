from tkinter import *
from tkinter import ttk

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
        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nsew")
        
        # Dictionary to hold the frames and keys use to create the frame
        self.frames = {}
        self.frames["Menu"] = self.main_menu()
        self.frames["Create_burger"] = self.burger_creation()
        self.frames["Pick_side"] = self.side_selection()
        self.frames["Pick_drink"] = self.drinks_selection()
        self.frames["Ordering"] = self.order_menu()
        
        # Show inital frame
        self.show_frame("menu")
        
        def frame_show(self, name):
            frame = self.name[name]
            frame.tkraise() # Move frame to top of stack
        
        def main_menu(self):
            frame = Frame(self.container)
            frame.grid(row=0, column=0, sticky="nsew")
            
            # Main heading
            Label(frame, font=TITLE, text="Burger creation menu").grid(row=0, padx=10, pady=10, sticky="nsew")
            
            # Buttons for other menu
            Button(frame, text="Burger creation", bg="yellow", font=TEXT, command=lambda:
                   self.show_frame("Create_burger")).grid(row=1, column=0)
            return frame
        
        def burger_creation(self):
            
            pass
        
        def sides_selection(self):
            Label(frame, font=TITLE, text="Side selection").grid(row=0, columnspan=2,
                                                                 padx=10, pady=10, sticky="nsew")
            Label(frame, font=TEXT, text="Side options").grid(row=1, column=0)
            
            # Combobox
            Side_pick = ttk.Combobox(root, state="readonly",
                                 values=["Chips", "Onion rings", "salad"])
            Side_pick.grid(row=1, column=1, pady=20)
            pass
        
        def drinks_selection(self):
            Label(frame, font=TITLE, text="Drinks selection").grid(row=0, columnspan=2,
                                                                 padx=10, pady=10, sticky="nsew")
            Label(frame, font=TEXT, text="Drink options").grid(row=1, column=0)
            
            # Combobox
            drink_pick = ttk.Combobox(root, state="readonly",
                                      values=["Tea", "L&P", "Coke Cola", "Sprite"])
            drink_pick.grid(row=1, column=1, pady=20)            
            pass
        
        def order_menu(self):
            
            pass

root = Tk()
app = burger_maker(root)
root.mainloop()