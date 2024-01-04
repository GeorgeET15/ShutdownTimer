import tkinter as tk
from tkinter import messagebox
import os

def shutdown_timer():
    try:
        minutes = int(entry.get())
        seconds = minutes * 60
        os.system(f'shutdown -s -t {seconds}')
        messagebox.showinfo("Shutdown Timer", f"Shutdown initiated in {minutes} minutes.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def cancel_timer():
    os.system('shutdown -a')  # Abort the shutdown
    messagebox.showinfo("Shutdown Timer", "Shutdown canceled.")

# Create the main window
root = tk.Tk()
root.title("Shutdown Timer")
root.geometry("300x200")  # Increased height to accommodate the Cancel Timer button
root.resizable(False, False)
root.configure(bg="#101418")
#icon_path = "C:/Users/IRONM/Desktop/ShutdownTimer/App.ico"  # Replace with the path to your icon file
#root.iconbitmap(icon_path)

# Set a different font
font_style = ("Helvetica", 12, "bold")

# Create and place GUI elements
label = tk.Label(root, text="Enter minutes:", font=font_style, bg="#101418", fg="#ffffff")
label.pack(pady=10)

entry = tk.Entry(root, font=font_style, bg="#17202a", fg="#ffffff", insertbackground="#ffffff", selectbackground="#3399ff", borderwidth=0)
entry.pack(pady=10)

start_button = tk.Button(root, text="Start Shutdown", command=shutdown_timer, font=font_style, bg="#3498db", fg="#ffffff", padx=10, pady=5, activebackground="#2980b9")
start_button.pack(pady=10)

cancel_button = tk.Button(root, text="Cancel Timer", command=cancel_timer, font=font_style, bg="#e74c3c", fg="#ffffff", padx=10, pady=5, activebackground="#c0392b")
cancel_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
