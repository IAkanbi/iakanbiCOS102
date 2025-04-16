import tkinter as tk
from tkinter import messagebox


def price_message(number):
    # Create a window to show the price
    window = tk.Toplevel(root)
    window.title("Delivery Price")
    window.geometry("400x200")
    label_1 = tk.Label(window, text=f"Price of delivery is N{number}")
    label_1.pack()


def submit():
    weight = weight_entry.get()
    location = location_entry.get().strip().lower()  # Convert to lowercase and remove whitespace

    try:
        weight_number = float(weight)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid weight (numbers only)")
        return

    # Check locations
    if location in ["ibeju lekki", "ibeju-lekki"]:
        if weight_number >= 10:
            price_message(5000)
        else:
            price_message(3500)
    elif location == "epe":
        if weight_number >= 10:
            price_message(10000)
        else:
            price_message(5000)
    else:
        messagebox.showerror("Error", "We do not deliver to this location.")


# Creating main window
root = tk.Tk()
root.title("Simi Services")
root.geometry("400x200")

# Location Entry and label
location_label = tk.Label(root, text="Location (Ibeju-Lekki or Epe)")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

# Weight Entry and Label
weight_label = tk.Label(root, text="Weight of Package (in Kg)")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# Check Price Button
submit_button = tk.Button(root, text="Check Price", command=submit)
submit_button.pack()
submit_button.config(bg="green",fg="white")

root.mainloop()