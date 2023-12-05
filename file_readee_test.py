import tkinter as tk

def load_file_content(filename, entries):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                entry = tk.Entry(root)
                entry.insert(0, line.strip())  # Strip to remove newline characters
                entry.pack()
                entries.append(entry)
    except FileNotFoundError:
        print(f"File not found: {filename}")

# Create the Tkinter window
root = tk.Tk()
root.title("Read File to Entries")

# List to store Entry widgets
entries = []

# Load file content to entries (replace 'your_file.txt' with your actual file name)
load_file_content('Helman_Inputs.txt', entries)

# Start the Tkinter event loop
root.mainloop()
