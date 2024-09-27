import tkinter as tk
from tkinter import ttk

# Function to add a new dropdown and input field on top of the "Add More" button
def add_dropdown_and_input():
    # Create a new row with dropdown and input field
    row_frame = tk.Frame(container_frame)
    
    # Dropdown for name with options "Chrome" and "Code"
    dropdown = ttk.Combobox(row_frame, values=["Chrome", "Code"], state="readonly")
    dropdown.set("Chrome")  # Set default value
    dropdown.pack(side="left", padx=5)

    # Input field for path
    path_entry = tk.Entry(row_frame, width=40)
    path_entry.pack(side="left", padx=5)

    # Pack the new row at the top (before the add_button)
    row_frame.pack(fill="x", pady=5)

    # Re-pack the Add More button to ensure it stays at the bottom
    add_button.pack_forget()
    add_button.pack(pady=10)

# Create the main window
window = tk.Tk()
window.title("Dynamic Form")

# Create a container frame for all rows
container_frame = tk.Frame(window)
container_frame.pack(pady=5, padx=10)

# First row frame with dropdown and input field
first_row_frame = tk.Frame(container_frame)

# First dropdown for name with options "Chrome" and "Code"
dropdown = ttk.Combobox(first_row_frame, values=["Chrome", "Code"], state="readonly")
dropdown.set("Chrome")  # Set default value
dropdown.pack(side="left", padx=5)

# First input field for path
path_entry = tk.Entry(first_row_frame, width=40)
path_entry.pack(side="left", padx=5)

# Pack the first row into the container
first_row_frame.pack(fill="x", pady=5)

# Button to add additional dropdown and input field
add_button = tk.Button(window, text="Add More", command=add_dropdown_and_input)
add_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
