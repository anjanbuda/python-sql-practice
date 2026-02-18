'''
Assignment 1: Area of a Circle
Write a program that calculates the area of a circle given its radius.
The formula for the area of a circle is: Area = π * radius^2.
Take radius from user. Use π as 3.14
'''


# radius=float(input("enter the radius of the circle> "))
# area=3.14*radius*radius
# print("The area of the circle is:",area)

import tkinter as tk

def calculate_area():
    radius = float(entry.get())  # same logic as input()
    area = 3.14 * radius * radius  # same formula
    result_label.config(text="The area of the circle is: " + str(area))

# Create main window
root = tk.Tk()
root.title("Circle Area Calculator")

# Label
label = tk.Label(root, text="Enter the radius of the circle:")
label.pack()

# Entry box
entry = tk.Entry(root)
entry.pack()

# Button
button = tk.Button(root, text="Calculate Area", command=calculate_area)
button.pack()

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
