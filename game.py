import tkinter as tk
from tkinter import messagebox
import time

def check_speed():
    try:
        speed = float(entry_speed.get())  # Get the speed from the input box

        if 70 < speed < 75:
            messagebox.showwarning("Warning", "You are going too fast!")
        elif speed >= 75:
            messagebox.showerror("Fine", "You were speeding! You've been fined!")
            reset_game()
        else:
            messagebox.showinfo("Good Speed", "You're good, no issues.")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def reset_game():
    entry_speed.delete(0, tk.END)  # Clear the entry field
    label_result.config(text="Enter your speed to begin!")

# Set up the GUI window
window = tk.Tk()
window.title("Speed Check Game")

# Add a label
label = tk.Label(window, text="How fast are you going (in mph)?")
label.pack(pady=10)

# Add a text entry box for speed input
entry_speed = tk.Entry(window)
entry_speed.pack(pady=10)

# Add a button to check the speed
check_button = tk.Button(window, text="Check Speed", command=check_speed)
check_button.pack(pady=10)

# Add a label to display results
label_result = tk.Label(window, text="Enter your speed to begin!")
label_result.pack(pady=20)

# Run the application
window.mainloop()
