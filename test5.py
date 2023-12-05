import tkinter as tk
from tkinter import messagebox

def open_calculation_window(algorithm):
    calculation_window = tk.Toplevel(root)
    calculation_window.title("Perform Calculation")

    num_parameters = 0

    if algorithm == "Algorithm1":
        num_parameters = 4
    elif algorithm == "Algorithm2":
        num_parameters = 3
    elif algorithm == "Algorithm3":
        num_parameters = 2
    else:
        messagebox.showerror("Error", "Invalid algorithm")
        return

    labels = []
    entries = []

    for i in range(num_parameters):
        label = tk.Label(calculation_window, text=f"Enter parameter {i+1}:")
        label.pack()
        labels.append(label)

        entry = tk.Entry(calculation_window)
        entry.pack()
        entries.append(entry)

    def perform_calculation():
        parameters = [entry.get() for entry in entries]

        try:
            result = None
            if algorithm == "Algorithm1":
                result = algorithm1(*parameters)
            elif algorithm == "Algorithm2":
                result = algorithm2(*parameters)
            elif algorithm == "Algorithm3":
                result = algorithm3(*parameters)

            result_window = tk.Toplevel(root)
            result_window.title("Result")
            result_label = tk.Label(result_window, text=f"Result: {result}")
            result_label.pack()

        except Exception as e:
            messagebox.showerror("Error", str(e))

        calculation_window.destroy()

    calculate_button = tk.Button(calculation_window, text="Calculate", command=perform_calculation)
    calculate_button.pack()


def algorithm1(param1, param2, param3, param4):
    # Custom implementation for Algorithm1
    # You can replace this with your own logic
    return int(param1) + int(param2) + int(param3) + int(param4)


def algorithm2(param1, param2, param3):
    # Custom implementation for Algorithm2
    # You can replace this with your own logic
    return int(param1) + int(param2) + int(param3)


def algorithm3(param1, param2):
    # Custom implementation for Algorithm3
    # You can replace this with your own logic
    return int(param1) + int(param2)


root = tk.Tk()
root.title("Algorithm Executor")

algorithm1_button = tk.Button(root, text="Algorithm 1", command=lambda: open_calculation_window("Algorithm1"))
algorithm1_button.pack()

algorithm2_button = tk.Button(root, text="Algorithm 2", command=lambda: open_calculation_window("Algorithm2"))
algorithm2_button.pack()

algorithm3_button = tk.Button(root, text="Algorithm 3", command=lambda: open_calculation_window("Algorithm3"))
algorithm3_button.pack()

root.mainloop()