from tkinter import *
from tkinter import ttk

TITLE = "Arial 14"
TEXT = "Arial 11"
# The title will be used for the main header for each page and text will be used for other things like buttons

class burger_order:
    ''' Will be used to process the order '''
    
    def burger_order(self, root):
        ''' Add the items that were chosen and put it on the screen '''
    
    def side_order(self, root):
        ''' Add the items that were chosen and put it on the screen '''
    
    def drink_order(self, root):
        ''' Add the items that were chosen and put it on the screen '''    

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
        
        self.frames["Main_menu"] = self.main_menu()
        self.frames["Create_burger"] = self.burger_creation()
        self.frames["Pick_side"] = self.side_selection()
        self.frames["Pick_drink"] = self.drinks_selection()
        self.frames["Ordering"] = self.order_menu()
        
        # Show inital frame
        self.show_frame("Main_menu")        
        
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise() # Move frame to top of stack
    
    def main_menu(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        
        # Main heading
        Label(frame, font=TITLE, text="Burger creation menu", bg="#6d9eeb").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Buttons for other menu
        Button(frame, text="Burger creation", bg="yellow", font=TEXT, command=lambda:
               self.show_frame("Create_burger")).grid(row=1, column=0)
        Button(frame, text="Side selection", bg="yellow", font=TEXT, command=lambda:
               self.show_frame("Pick_side")).grid(row=2, column=0)
        Button(frame, text="Drink selection", bg="yellow", font=TEXT, command=lambda:
               self.show_frame("Pick_drink")).grid(row=3, column=0)
        Button(frame, text="Order menu", bg="yellow", font=TEXT, command=lambda:
               self.show_frame("Ordering")).grid(row=4, column=0)            
        return frame
    
    def burger_creation(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        
        Label(frame, font=TITLE, text="Burger creation", bg="#ffd966").grid(row=0, columnspan=2,
                                                            padx=10, pady=10, sticky="nsew")
        Label(frame, font=TEXT, text="Meat options").grid(row=1, column=0)
        
        # Combobox for meat
        Meat_pick = ttk.Combobox(frame, state="readonly",
                                values=["Beef:$8", "Lamb:$8", "Chicken:$9", "Pork:$9", "vegaterian:$7"])
        Meat_pick.grid(row=1, column=1, pady=10)
        
        Label(frame, font=TEXT, text="Meat amount").grid(row=2, column=0)
        
        # Input box for meat amount
        self.a_box = Entry(frame)
        self.a_box.grid(row=2, column=1, pady=10)
        
        #if Entry > 3:
            #print("Pick a lower number")
        #elif Entry < 1:
            #print("If you want a meatless burger pick vegaterian")
        
        Label(frame, font=TEXT, text="Garnish 1").grid(row=3, column=0)
        # Combobox for Garnish
        Garnish_1 = ttk.Combobox(frame, state="readonly",
                                values=["Tomato:$4", "Onion:$4", "Lettuce:$3"])
        Garnish_1.grid(row=3, column=1, pady=10)
        
        Label(frame, font=TEXT, text="Garnish 2").grid(row=4, column=0)
        
        Garnish_2 = ttk.Combobox(frame, state="readonly",
                                values=["Tomato:$4", "Onion:$4", "Lettuce:$3"])
        Garnish_2.grid(row=4, column=1, pady=10)
        
        Label(frame, font=TEXT, text="Sauces").grid(row=5, column=0)
        # Combobox for Sauces
        sauces_pick = ttk.Combobox(frame, state="readonly",
                                values=["Mayo:$2", "Ketchup:$2", "Mustard:$2", "Apple sauce:$2"])
        sauces_pick.grid(row=5, column=1, pady=10)
        
        Button(frame, text="Back", bg="yellow", font=TEXT, command=lambda:
               self.show_frame("Main_menu")).grid(row=6, columnspan=2)
        
        return frame
    
    def side_selection(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        
        Label(frame, font=TITLE, text="Side selection", bg="#ffe599").grid(row=0, columnspan=2,
                                                             padx=10, pady=10, sticky="nsew")
        Label(frame, font=TEXT, text="Side options").grid(row=1, column=0)
        
        # Combobox for Sides
        Side_pick = ttk.Combobox(frame, state="readonly",
                             values=["Chips:$5", "Onion rings:$5", "salad:$4"])
        Side_pick.grid(row=1, column=1, pady=10)
        
        Label(frame, font=TEXT, text="Dips options").grid(row=2, column=0)
        
        # Combobox for Dips
        Dips_pick = ttk.Combobox(frame, state="readonly", values=["Ketchup:$2", "Aioli:$2"])
        Dips_pick.grid(row=2, column=1, pady=10)
        
        Button(frame, text="Back", bg="yellow", font=TEXT, command=lambda:
               self.show_frame("Main_menu")).grid(row=3, columnspan=2)        
        return frame
    
    def drinks_selection(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        
        Label(frame, font=TITLE, text="Drinks selection", bg="#f1c232").grid(row=0, columnspan=2,
                                                             padx=10, pady=10, sticky="nsew")
        Label(frame, font=TEXT, text="Drink options").grid(row=1, column=0)
        
        # Combobox for Drinks
        Drink_pick = ttk.Combobox(frame, state="readonly",
                                  values=["Tea:$4", "L&P:$4", "CokeCola:$4", "Sprite:$4"])
        Drink_pick.grid(row=1, column=1, pady=10)
        
        Label(frame, font=TEXT, text="Milkshake options").grid(row=2, column=0)
        
        # Combobox for Milkshakes
        Milkshake_pick = ttk.Combobox(frame, state="readonly",
                                  values=["Chocolate:$6", "strawberry:$6", "caramel:$6"])
        Milkshake_pick.grid(row=2, column=1, pady=10)
        
        Button(frame, text="Back", bg="yellow", font=TEXT, command=lambda:
               self.show_frame("Main_menu")).grid(row=3, columnspan=2)        
        return frame
    
    def order_menu(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        
        Label(frame, font=TITLE, text="Order menu", bg="#93c47d").grid(row=0, columnspan=2,
                                                             padx=10, pady=10, sticky="nsew")
        Label(frame, font=TEXT, text="Burger overview").grid(row=1, column=0)
        
        self.label_burger = Label(frame, font=TEXT, text="???").grid(row=1, column=1)
        
        Label(frame, font=TEXT, text="Side overview").grid(row=2, column=0)
        
        self.label_side = Label(frame, font=TEXT, text="???").grid(row=2, column=1)
        
        Label(frame, font=TEXT, text="Drinks overview").grid(row=3, column=0)
        
        self.label_drink = Label(frame, font=TEXT, text="???").grid(row=3, column=1)
        
        Label(frame, font=TEXT, text="Total").grid(row=4, column=0)
        
        self.label_total = Label(frame, font=TEXT, text="???").grid(row=4, column=1)
        
        Button(frame, text="Back", bg="yellow", font=TEXT, command=lambda:
               self.show_frame("Main_menu")).grid(row=5, columnspan=2)
        Button(frame, text="Finish order", bg="yellow", font=TEXT, command=self.quit).grid(row=6, columnspan=2)        
        return frame
    
    def burger_cost(self):
        #if Meat_pick == "Beef:$8":
        pass
    
    def side_cost(self):
        pass
    
    def drink_cost(self):
        pass
    
    def quit(self):
        ''' Close the window '''
        root.destroy()
        pass

root = Tk()
app = burger_maker(root)
root.mainloop()