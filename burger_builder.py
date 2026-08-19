from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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
        Label(frame, font=TITLE, text="Burger creation menu", bg="#6d9eeb").grid(row=0, column=0, ipadx=44, pady=10, sticky="nsew")
        
        # Buttons for other menu
        Button(frame, text="Burger creation", bg="yellow", font=TEXT, command=lambda:
               self.show_frame("Create_burger")).grid(row=1, column=0, padx=10, pady=10)
        Button(frame, text="Side selection", bg="yellow", font=TEXT, command=lambda:
               self.show_frame("Pick_side")).grid(row=2, column=0, padx=10, pady=10)
        Button(frame, text="Drink selection", bg="yellow", font=TEXT, command=lambda:
               self.show_frame("Pick_drink")).grid(row=3, column=0, padx=10, pady=10)
        Button(frame, text="Order menu", bg="yellow", font=TEXT, command=lambda:
               self.show_frame("Ordering")).grid(row=4, column=0, padx=10, pady=10)            
        return frame
    
    def burger_creation(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        
        Label(frame, font=TITLE, text="Burger creation", bg="#ffd966").grid(row=0, columnspan=2, ipadx=70,
                                                            pady=10, sticky="nsew")
        Label(frame, font=TEXT, text="Meat options").grid(row=1, column=0)
        
        # Combobox for meat
        self.Meat_pick = ttk.Combobox(frame, state="readonly",
                                values=["Beef:$8", "Lamb:$8", "Chicken:$9", "Pork:$9", "vegaterian:$7"])
        self.Meat_pick.grid(row=1, column=1, pady=10)
        
        Label(frame, font=TEXT, text="Meat amount: 1-3").grid(row=2, column=0)
        
        # Input box for meat amount
        self.a_box = Entry(frame)
        self.a_box.grid(row=2, column=1, pady=10)
        
        Label(frame, font=TEXT, text="Garnish 1").grid(row=3, column=0)
        # Combobox for Garnish
        self.Garnish_1 = ttk.Combobox(frame, state="readonly",
                                values=["Tomato:$4", "Onion:$4", "Lettuce:$3"])
        self.Garnish_1.grid(row=3, column=1, pady=10)
        
        Label(frame, font=TEXT, text="Garnish 2").grid(row=4, column=0)
        
        self.Garnish_2 = ttk.Combobox(frame, state="readonly",
                                values=["Tomato:$4", "Onion:$4", "Lettuce:$3"])
        self.Garnish_2.grid(row=4, column=1, pady=10)
        
        Label(frame, font=TEXT, text="Sauces").grid(row=5, column=0)
        # Combobox for Sauces
        self.sauces_pick = ttk.Combobox(frame, state="readonly",
                                values=["Mayo:$2", "Ketchup:$2", "Mustard:$2", "Apple sauce:$2"])
        self.sauces_pick.grid(row=5, column=1, pady=10)
        
        Button(frame, text="Back", bg="yellow", font=TEXT, command=lambda:
               self.show_frame("Main_menu")).grid(row=6, columnspan=2)
        
        return frame
    
    def side_selection(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        
        Label(frame, font=TITLE, text="Side selection", bg="#ffe599").grid(row=0, columnspan=2,
                                                             ipadx=74, pady=10, sticky="nsew")
        Label(frame, font=TEXT, text="Side options").grid(row=1, column=0)
        
        # Combobox for Sides
        self.Side_pick = ttk.Combobox(frame, state="readonly",
                             values=["Chips:$5", "Onion rings:$5", "salad:$4"])
        self.Side_pick.grid(row=1, column=1, pady=10)
        
        Label(frame, font=TEXT, text="Dips options").grid(row=2, column=0)
        
        # Combobox for Dips
        self.Dips_pick = ttk.Combobox(frame, state="readonly", values=["Ketchup:$2", "Aioli:$2"])
        self.Dips_pick.grid(row=2, column=1, pady=10)
        
        Button(frame, text="Back", bg="yellow", font=TEXT, command=lambda:
               self.show_frame("Main_menu")).grid(row=3, columnspan=2)        
        return frame
    
    def drinks_selection(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        
        Label(frame, font=TITLE, text="Drinks selection", bg="#f1c232").grid(row=0, columnspan=2,
                                                             ipadx=67, pady=10, sticky="nsew")
        Label(frame, font=TEXT, text="Drink options").grid(row=1, column=0)
        
        # Combobox for Drinks
        self.Drink_pick = ttk.Combobox(frame, state="readonly",
                                  values=["Tea:$4", "L&P:$4", "CokeCola:$4", "Sprite:$4"])
        self.Drink_pick.grid(row=1, column=1, pady=10)
        
        Label(frame, font=TEXT, text="Milkshake options").grid(row=2, column=0)
        
        # Combobox for Milkshakes
        self.Milkshake_pick = ttk.Combobox(frame, state="readonly",
                                  values=["Chocolate:$6", "strawberry:$6", "caramel:$6"])
        self.Milkshake_pick.grid(row=2, column=1, pady=10)
        
        Button(frame, text="Back", bg="yellow", font=TEXT, command=lambda:
               self.show_frame("Main_menu")).grid(row=3, columnspan=2)        
        return frame
    
    def order_menu(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        
        Label(frame, font=TITLE, text="Order menu", bg="#93c47d").grid(row=0, columnspan=2, ipadx=40,
                                                             padx=40, pady=10, sticky="nsew")
        Label(frame, font=TEXT, text="Burger overview").grid(row=1, column=0)
        # Shows the cost of the burger
        self.label_burger = Label(frame, font=TEXT, text="")
        self.label_burger.grid(row=1, column=1)
        
        Label(frame, font=TEXT, text="Side overview").grid(row=2, column=0)
        # Shows the cost of the side
        self.label_side = Label(frame, font=TEXT, text="")
        self.label_side.grid(row=2, column=1)
        
        Label(frame, font=TEXT, text="Drinks overview").grid(row=3, column=0)
        # Shows the cost of the drink
        self.label_drink = Label(frame, font=TEXT, text="")
        self.label_drink.grid(row=3, column=1)
        
        Button(frame, text="Back", bg="yellow", font=TEXT, command=lambda:
               self.show_frame("Main_menu")).grid(row=4, columnspan=2)
        Button(frame, text="Burger cost process", bg="yellow", font=TEXT, command=self.burger_cost).grid(row=5, columnspan=2)
        Button(frame, text="Side cost process", bg="yellow", font=TEXT, command=self.side_cost).grid(row=6, columnspan=2)
        Button(frame, text="Drink cost process", bg="yellow", font=TEXT, command=self.drink_cost).grid(row=7, columnspan=2)
        Button(frame, text="Finish order", bg="yellow", font=TEXT, command=self.quit).grid(row=8, columnspan=2)
        return frame
    
    def burger_cost(self):
        burger_Total = 0
        
        if self.Meat_pick.get() == "Beef:$8":
            burger_Total += 8
        elif self.Meat_pick.get() == "Lamb:$8":
            burger_Total += 8
        elif self.Meat_pick.get() == "Chicken:$9":
            burger_Total += 9
        elif self.Meat_pick.get() == "Pork:$9":
            burger_Total += 9
        elif self.Meat_pick.get() == "vegaterian:$7":
            burger_Total += 7
        
        if self.a_box.get() == "1":
            burger_Total += 0
        elif self.a_box.get() == "2":
            burger_Total += 3
        elif self.a_box.get() == "3":
            burger_Total += 6
        else:
            burger_Total += 0
        
        if self.Garnish_1.get() == "Tomato:$4":
            burger_Total += 4
        elif self.Garnish_1.get() == "Onion:$4":
            burger_Total += 4
        elif self.Garnish_1.get() == "Lettuce:$3":
            burger_Total += 3
        
        if self.Garnish_2.get() == "Tomato:$4":
            burger_Total += 4
        elif self.Garnish_2.get() == "Onion:$4":
            burger_Total += 4
        elif self.Garnish_2.get() == "Lettuce:$3":
            burger_Total += 3        
        
        if self.sauces_pick.get() == "Mayo:$2":
            burger_Total += 2
        elif self.sauces_pick.get() == "Ketchup:$2":
            burger_Total += 2
        elif self.sauces_pick.get() == "Mustard:$2":
            burger_Total += 2
        elif self.sauces_pick.get() == "Apple sauce:$2":
            burger_Total += 2
        
        self.label_burger.configure(text=burger_Total)
    
    def side_cost(self):
        side_Total = 0
        
        if self.Side_pick.get() == "Chips:$5":
            side_Total += 5
        elif self.Side_pick.get() == "Onion rings:$5":
            side_Total += 5
        elif self.Side_pick.get() == "salad:$4":
            side_Total += 4
        
        if self.Dips_pick.get() == "Ketchup:$2":
            side_Total += 2
        elif self.Dips_pick.get() == "Aioli:$2":
            side_Total += 2
        
        self.label_side.configure(text=side_Total)
    
    def drink_cost(self):
        drink_Total = 0
        
        if self.Drink_pick.get() == "Tea:$4":
            drink_Total += 4
        elif self.Drink_pick.get() == "L&P:$4":
            drink_Total += 4
        elif self.Drink_pick.get() == "CokeCola:$4":
            drink_Total += 4
        elif self.Drink_pick.get() == "Sprite:$4":
            drink_Total += 4
        
        if self.Milkshake_pick.get() == "Chocolate:$6":
            drink_Total += 6
        elif self.Milkshake_pick.get() == "strawberry:$6":
            drink_Total += 6
        elif self.Milkshake_pick.get() == "caramel:$6":
            drink_Total += 6
        
        self.label_drink.configure(text=drink_Total)
    
    def quit(self):
        ''' Close the window '''
        root.destroy()

root = Tk()
app = burger_maker(root)
root.mainloop()