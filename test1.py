import tkinter as tk
from tkinter import messagebox

def display_number():
    number = entry.get()
    messagebox.showinfo("Number Display", f"The entered number is: {number}")

def open_new_window():
    new_window = tk.Toplevel(root)
    label = tk.Label(new_window, text="New Window")
    label.pack()

root = tk.Tk()
root.title("Number Entry")

label = tk.Label(root, text="Enter a number:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button1 = tk.Button(root, text="Display Number", command=display_number)
button1.pack()

button2 = tk.Button(root, text="Open New Window", command=open_new_window)
button2.pack()

root.mainloop()