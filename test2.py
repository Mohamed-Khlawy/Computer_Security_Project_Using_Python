import tkinter as tk
from tkinter import messagebox

def open_calculation_window(operation):
    calculation_window = tk.Toplevel(root)
    calculation_window.title("Perform Calculation")

    label = tk.Label(calculation_window, text="Enter the equation:")
    label.pack()

    entry = tk.Entry(calculation_window)
    entry.pack()

    def perform_calculation():
        equation = entry.get()
        try:
            result = None
            if operation == "Sum":
                result = eval(equation)
            elif operation == "Multiply":
                result = eval(equation)
            elif operation == "Division":
                result = eval(equation)
            else:
                messagebox.showerror("Error", "Invalid operation")
                calculation_window.destroy()
                return

            result_window = tk.Toplevel(root)
            result_window.title("Result")
            result_label = tk.Label(result_window, text=f"Result: {result}")
            result_label.pack()

        except Exception as e:
            messagebox.showerror("Error", str(e))

        calculation_window.destroy()

    calculate_button = tk.Button(calculation_window, text="Calculate", command=perform_calculation)
    calculate_button.pack()


root = tk.Tk()
root.title("Calculator")

sum_button = tk.Button(root, text="Sum", command=lambda: open_calculation_window("Sum"))
sum_button.pack()

multiply_button = tk.Button(root, text="Multiply", command=lambda: open_calculation_window("Multiply"))
multiply_button.pack()

division_button = tk.Button(root, text="Division", command=lambda: open_calculation_window("Division"))
division_button.pack()

root.mainloop()