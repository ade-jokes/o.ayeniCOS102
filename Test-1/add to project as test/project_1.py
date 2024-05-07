import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk

def calculate_bill(all_entries, item_vars, item_prices):
    total_bill = 0
    for var, entry in zip(item_vars, all_entries):
        item = var.get()
        quantity = entry.get()
        if item and quantity.isdigit():
            total_bill += item_prices[item] * int(quantity)
    messagebox.showinfo("Total Bill", f"Your total bill is: ₦{total_bill:,}")

def clear_fields(all_entries):
    for entry in all_entries:
        entry.delete(0, tk.END)
    messagebox.showinfo("Cleared", "All fields have been cleared.")

def create_dropdown_and_entry(parent, var, label_text, y_position):
    label = tk.Label(parent, text=label_text)
    label.place(x=20, y=y_position)

    dropdown = tk.OptionMenu(parent, var, *item_prices.keys())
    dropdown.place(x=200, y=y_position)

    entry = tk.Entry(parent)
    entry.place(x=400, y=y_position)

    return entry

def function(item_vars, item_prices):
    order_window = tk.Toplevel()
    order_window.title("Place your order")
    order_window.resizable(False, False)

    item_frame = tk.Frame(order_window)
    item_frame.pack()

    # Define variables for dropdown selections
    rice_var, side_dish_var, soup_var, swallow_var, protein_var, beverage_var = item_vars

    # Create dropdown menus and entry fields for quantities
    all_entries = [
        create_dropdown_and_entry(item_frame, rice_var, "Rice/Pasta", 150),
        create_dropdown_and_entry(item_frame, side_dish_var, "Side Dish", 230),
        create_dropdown_and_entry(item_frame, soup_var, "Soup/Swallow", 310),
        create_dropdown_and_entry(item_frame, swallow_var, "Swallow", 390),
        create_dropdown_and_entry(item_frame, protein_var, "Protein", 470),
        create_dropdown_and_entry(item_frame, beverage_var, "Beverage", 550)
    ]

    # Create a button to calculate the total bill
    calculate_button = tk.Button(
        order_window, text="Calculate Bill", command=lambda: calculate_bill(all_entries, item_vars, item_prices), state=tk.DISABLED)
    calculate_button.pack(pady=20)

    # Create a button to clear the input fields
    clear_button = tk.Button(order_window, text="Clear Fields", command=lambda: clear_fields(all_entries))
    clear_button.pack(pady=20)

# Initialize the list of all entry fields
all_entries = []

# Define item prices
item_prices = {
    "Jollof Rice": 350,
    "Coconut Fried Rice": 350,
    "Jollof Spaghetti": 350,
    "Savory Beans": 350,
    "Roasted Sweet Potatoes": 300,
    "Fried Plaintains": 150,
    "Mixed Vegetables Salad": 150,
    "Boiled Yam": 150,
    "Eba": 100,
    "Poundo Yam": 100,
    "Semo": 100,
    "Atama Soup": 450,
    "Egusi Soup": 450,
    "Sweet Chilli Chicken": 1100,
    "Grilled Chicken Wings": 400,
    "Fried Beef": 400,
    "Fried Fish": 400,
    "Boiled Egg": 200,
    "Sauteed Sausages": 200,
    "Water": 200,
    "Glass Drink (35cl)": 150,
    "PET Drinks (35cl)": 150,
    "Glass/Canned Malt": 500,
    "Fresh Yo": 600,
    "Pineapple Juice": 350,
    "Manjo Juice": 350,
    "Zobo Drink": 350,
}

# Define variables for dropdown selections
rice_var = tk.StringVar()
side_dish_var = tk.StringVar()
soup_var = tk.StringVar()
swallow_var = tk.StringVar()
protein_var = tk.StringVar()
beverage_var = tk.StringVar()

# Create the main window
window = tk.Tk()
window.geometry('736x1139')

# Add the image to the canvas
img = ImageTk.PhotoImage(file="abi.png", master=window)
canvas = tk.Canvas(window, width=736, height=1139)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=img, anchor="nw")

# Create the menu section
canvas.create_text(300, 10, text="Menu", font = "times 28 bold italic underline ")

# Create the Rice/Pasta section
canvas.create_text(200,50, text="Rice/Pasta", font = "times 20 italic ")

# Add the Rice/Pasta items
canvas.create_text(200,90, text="Jollof Rice   N350", font = "Arial 12 italic")
canvas.create_text(200,130, text="Coconut Fried Rice   N350", font = "Arial 12 italic")
canvas.create_text(200,170, text="Jollof Spagetti   N350", font = "Arial 12 italic")

# Create the Side Dishes section
canvas.create_text(200,220, text="Side Dishes ", font = "times 20 italic ")

# Add the Side Dishes items
canvas.create_text(200,270, text="Savoury Beans   N350", font = "Arial 12 italic")
canvas.create_text(200,320, text="Roasted Sweet Potatoes   N300", font = "Arial 12 italic")
canvas.create_text(200,370, text="Fried Plaintains   N150", font = "Arial 12 italic")
canvas.create_text(200,420, text="Mixed Vegetables Salad   N150", font = "Arial 12 italic")
canvas.create_text(200,470, text="Boiled Yam   N150", font = "Arial 12 italic")

# Create the Soups and Swallow section
canvas.create_text(200,520, text="Soup/Swallow", font = "times 20 italic ")

# Add the Soups and Swallow items
canvas.create_text(200,570, text="Eba    N100", font = "Arial 12 italic")
canvas.create_text(200,600, text="Poundo Yam   N100", font = "Arial 12 italic")
canvas.create_text(200,635, text="Semo    N100", font = "Arial 12 italic")
canvas.create_text(200,670, text="Atama Soup   N450", font = "Arial 12 italic")
canvas.create_text(200,700, text="Egusi Soup   N450", font = "Arial 12 italic")

# Create the Protein section
canvas.create_text(450,50, text="Protein", font = "times 20 italic ",)

# Add the Protein items
canvas.create_text(450,90, text="Sweet chill Chicken   N1100", font = "Arial 12 italic")
canvas.create_text(450,130, text="Grilled Chicken Wings   N400", font = "Arial 12 italic",)
canvas.create_text(450,170, text="Fried Beef   N400", font = "Arial 12 italic")
canvas.create_text(450,210, text="Fried Fish   N400 ", font = "Arial 12 italic ")
canvas.create_text(450,250, text="Boiled Egg   N200", font = "Arial 12 italic")
canvas.create_text(450,290, text="Sauteed Sausages   N200", font = "Arial 12 italic")

# Create the Beverages section
canvas.create_text(450,330, text="BEVERAGE", font = "times 20 italic")

# Add the Beverages items
canvas.create_text(450,370, text="Water   N200", font = "Arial 12 italic")
canvas.create_text(450,410, text="Glass Drink(35cl)   N150", font = "Arial 12 italic")
canvas.create_text(450, 450, text="PET Drinks(35cl)   N150", font=("Arial", 12, "italic"))
canvas.create_text(450, 490, text="Glass/Canned Malt   N500", font=("Arial", 12, "italic"))
canvas.create_text(450, 530, text="Fresh Yo   N600", font=("Arial", 12, "italic"))
canvas.create_text(450, 570, text="Pineapple Juice   N350", font=("Arial", 12, "italic"))
canvas.create_text(450, 610, text="Manjo Juice   N350", font=("Arial", 12, "italic"))
canvas.create_text(450, 650, text="Zobo Drink   N350", font=("Arial", 12, "italic"))

# Create the Enjoy text
canvas.create_text(300,750, text="Enjoy", font=('Helvetica 26 bold italic'))

# Create the button with the function command
button = tk.Button(window, text="Click me!", command=lambda: function(
    (rice_var, side_dish_var, soup_var, swallow_var, protein_var, beverage_var), item_prices))

button.place(x=600, y= 730)

# Start the main loop
window.mainloop()