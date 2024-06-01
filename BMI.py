import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = (weight / (height * height)) * 703
        bmi_as_int = int(bmi)
        messagebox.showinfo("BMI Result", f'Your BMI is {bmi_as_int}')
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")

# Create the main window
root = tk.Tk() # Initialize main window
root.title("BMI Calculator")

weight_label = tk.Label(root, text="Enter weight (lbs):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Enter height (inches):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

root.mainloop()