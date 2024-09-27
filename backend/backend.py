import subprocess
import os
import time
import tkinter as tk

# Function to get input and store in a variable
def get_input():
    user_input = input_entry.get()  # Retrieve input from entry field
    print(f"Input received: {user_input}")  # Store or print the value
    input_var.set(f"Stored: {user_input}")  # Update label with the stored input

# Create the main window
window = tk.Tk()
window.title("Input Storage GUI")

# Create an entry widget for input
label_key = tk.Label(window,text="Enter Value", )
label_key.pack()
input_entry = tk.Entry(window, width=300)
input_entry.pack(pady=10)

# Create a label to display the stored input
input_var = tk.StringVar()
input_label = tk.Label(window, textvariable=input_var)
input_label.pack(pady=10)

# Create a button to submit the input
submit_button = tk.Button(window, text="Submit", command=get_input)
submit_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()


# subprocess.run(["start","code"],shell=True)o
# filepath = input("enter the file path")
# url = input("enter your url")
# subprocess.run(['start',"chrome",url], shell=True)
# subprocess.run (["code", filepath], shell=True)
# time.sleep(4)
