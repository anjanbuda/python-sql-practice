import tkinter as tk

def convert_temp():
    Fahrenheit = float(entry.get())  # same as input()
    Celsius = (Fahrenheit - 32) * 5/9  # same formula
    result_label.config(text=f"The Temp is : {Celsius:0.2f}°C")

# Create main window
root = tk.Tk()
root.title("Fahrenheit to Celsius Converter")

# Label
label = tk.Label(root, text="Enter the temperature in Fahrenheit:")
label.pack()

# Entry box
entry = tk.Entry(root)
entry.pack()

# Button
button = tk.Button(root, text="Convert", command=convert_temp)
button.pack()

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
