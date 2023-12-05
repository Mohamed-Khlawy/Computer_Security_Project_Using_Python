import tkinter as tk
from tkinter import messagebox
import DES 
import Diffie_Helman
import SHA1

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
            if operation == "Diffie_Helman":
                public1 = entry1.get()
                public2 = entry2.get()
                private1 = entry3.get()
                private2 = entry4.get()
                result = Diffie_Helman.Diffie_Helman_algorithm(public1, public2, private1, private2)
            elif operation == "DES":
                result = multiply_function(equation)
            elif operation == "SHA-1":
                result = division_function(equation)
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


def sum_function(equation):
    # Custom implementation for sum
    # You can replace this with your own logic
    numbers = [int(num) for num in equation.split("+")]
    return sum(numbers)


def multiply_function(equation):
    # Custom implementation for multiplication
    # You can replace this with your own logic
    numbers = [int(num) for num in equation.split("*")]
    result = 1
    for num in numbers:
        result *= num
    return result


def division_function(equation):
    # Custom implementation for division
    # You can replace this with your own logic
    numbers = [int(num) for num in equation.split("/")]
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result


root = tk.Tk()
root.title("Calculator")

sum_button = tk.Button(root, text="Sum", command=lambda: open_calculation_window("Diffie_Helman"))
sum_button.pack()

multiply_button = tk.Button(root, text="Multiply", command=lambda: open_calculation_window("DES"))
multiply_button.pack()

division_button = tk.Button(root, text="Division", command=lambda: open_calculation_window("SHA-1"))
division_button.pack()

root.mainloop()