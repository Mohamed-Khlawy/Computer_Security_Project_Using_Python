import tkinter as tk
from tkinter import Canvas, PhotoImage, Tk, messagebox
import DES 
import Diffie_Helman
import SHA1


# canvas = Canvas(window, width=600, height=600, bg="white") 
def open_calculation_window(algorithm):
    calculation_window = tk.Toplevel(root)
    calculation_window.title("Perform Calculation")

    # num_parameters = 0

    label_names_Helman = ["P", "G", "User 1 Private", "User 2 Private"]
    label_names_DES    = ["Message", "Key"]
    label_names_SHA1   = ["Message"]

    file_name_Helman = 'Helman_Inputs.txt'
    file_name_DES    = 'DES_Inputs.txt'
    file_name_SHA1   = 'SHA1_Inputs.txt'

    # if algorithm == "Diffie_Helman":
    #     num_parameters = 4
    # elif algorithm == "SHA-1":
    #     num_parameters = 1
    # elif algorithm == "DES":
    #     num_parameters = 2
    # else:
    #     messagebox.showerror("Error", "Invalid algorithm")
    #     return

    labels = []
    entries = []
    canvas1 = Canvas(calculation_window, width=350, height=350, bg="white")
    canvas1.pack()
    img1= PhotoImage(file="Dec&Enc.png")
    #  calculation_window.mainloop()
    
    canvas1.create_image(170, 165, image=img1)
    # calculation_window.mainloop()

    # To read file and store its values in each line in a list, and retutn it
    def load_file_content(filename, entries):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

                return lines
                # for line in lines:
                #     entry = tk.Entry(calculation_window)
                #     entry.insert(0, line.strip())  # Strip to remove newline characters
                #     entry.pack()
                #     entries.append(entry)
        except FileNotFoundError:
            print(f"File not found: {filename}")


    # If the user choosed the Diffie_Helman algorithm
    if algorithm == "Diffie_Helman":
        # Load the Diffie_Helman inputs txt file and return its values
        file_lines = load_file_content(file_name_Helman, entries)

        # Loop through the parameter names given in the (label_names_Helman),
        # and the list returned from reading the algorithm inputs 
        for name, line in zip(label_names_Helman, file_lines):
            # Create a new label and pach it onto the canvas
            label = tk.Label(calculation_window, text=f"{name} :")
            label.pack()
            labels.append(label)

            # Create a new entry with the specified value for this parameter 
            # in the algorithm inputs file and pack it onto the canvas
            entry = tk.Entry(calculation_window)
            entry.insert(0, line.strip())  # Strip to remove newline characters
            entry.pack()
            entries.append(entry)

            # If we want to create a new entry without reading the input from file
            # entry = tk.Entry(calculation_window)
            # entry.pack()
            # entries.append(entry)

    # If the user choosed the SHA-1 algorithm
    elif algorithm == "SHA-1":
        # Load the SHA-1 inputs txt file and return its values
        file_lines = load_file_content(file_name_SHA1, entries)
        
        # Loop through the parameter names given in the (label_names_SHA1),
        # and the list returned from reading the algorithm inputs
        for name, line in zip(label_names_SHA1, file_lines):
            # Create a new label and pach it onto the canvas
            label = tk.Label(calculation_window, text=f"{name} :")
            label.pack()
            labels.append(label)

            # Create a new entry with the specified value for this parameter 
            # in the algorithm inputs file and pack it onto the canvas
            entry = tk.Entry(calculation_window)
            entry.insert(0, line.strip())  # Strip to remove newline characters
            entry.pack()
            entries.append(entry)

            # If we want to create a new entry without reading the input from file
            # entry = tk.Entry(calculation_window)
            # entry.pack()
            # entries.append(entry)

    # If the user choosed the DES algorithm
    elif algorithm == "DES":
        # Load the DES inputs txt file and return its values
        file_lines = load_file_content(file_name_DES, entries)
        
        # Loop through the parameter names given in the (label_names_DES),
        # and the list returned from reading the algorithm inputs
        for name, line in zip(label_names_DES, file_lines):
            # Create a new label and pach it onto the canvas
            label = tk.Label(calculation_window, text=f"{name} :")
            label.pack()
            labels.append(label)

            # Create a new entry with the specified value for this parameter 
            # in the algorithm inputs file and pack it onto the canvas
            entry = tk.Entry(calculation_window)
            entry.insert(0, line.strip())  # Strip to remove newline characters
            entry.pack()
            entries.append(entry)

            # If we want to create a new entry without reading the input from file
            # entry = tk.Entry(calculation_window)
            # entry.pack()
            # entries.append(entry)

    else:
        messagebox.showerror("Error", "Invalid algorithm")
        return

    def perform_calculation():
        #parameters = [entry.get() for entry in entries]  ===========================> changed

        try:
           
            result = None
            if algorithm == "Diffie_Helman":
                # Convert the parameters to int to be suitable for the algorithm
                parameters = [int(entry.get()) for entry in entries]   #===========================> changed
                result = Diffie_Helman.Diffie_Helman_algorithm(*parameters)
                

                result_window = tk.Toplevel(root)
                result_window.title("Diffie_Helman_Result")

                # Display each element of the tuple in a separate label   ===========================> changed
                key1, key2 = 0, 0
                for i, element in enumerate(result):
                    if i == 0:
                        key1 = element
                    if i == 1:
                        key2 = element
                    result_label = tk.Label(result_window,font=10,bg="coral", text=f"Key {i + 1}  =>  {element}")
                    result_label.pack()

                # Check if 2 keys is equal or not   ===========================> changed
                if key1 == key2:
                    result_label = tk.Label(result_window,font=10, text=f"Keys Have Been Exchanged Successfully")
                    result_label.pack()
                else:
                    result_label = tk.Label(result_window,font=10, text=f"Keys Have Not Been Exchanged Successfully")
                    result_label.pack()
            
            elif algorithm == "DES":
                parameters = [entry.get() for entry in entries]
                result = DES.DES_algorithm(*parameters)

                result_window = tk.Toplevel(root)
                result_window.title("DES_Result")

                # Display each element of the tuple in a separate label   ===========================> changed
                for i, element in enumerate(result):
                    if i == 0:
                        result_label = tk.Label(result_window,font=10,bg="light green", text=f"Ciphertext  =>  {element}")
                    if i == 1:
                        result_label = tk.Label(result_window,font=10,bg="light green", text=f"Plaintext After Description  =>  {element}")
                    result_label.pack()
            
            elif algorithm == "SHA-1":
                parameters = [entry.get() for entry in entries]
                result =SHA1.SHA_1_algorithm(*parameters)
                result_window = tk.Toplevel(root)
                result_window.title("SHA-1_Result")
                result_label = tk.Label(result_window,font =10,bg="light blue", text=f"Hash Value  =>  {result}")
                result_label.pack()
            
        except Exception as e:
            messagebox.showerror("Error", str(e))

        calculation_window.destroy()

    calculate_button = tk.Button(calculation_window, text="Calculate", command=perform_calculation)
    calculate_button.pack()
    calculation_window.mainloop()

root = tk.Tk()
canvas = Canvas(root, width=350, height=350, bg="white")
canvas.pack()
img = PhotoImage(file="Hacker.png")
canvas.create_image(170, 165, image=img)
root.title("Algorithm Executor")

x_label = tk.Label(text=f"Choose the appropriate algorithm : ",font=('Helvatical bold',14))
x_label.pack()

Diffie_Helman_button = tk.Button(root,bg="coral", text="Diffie_Helman",font=10, command=lambda: open_calculation_window("Diffie_Helman"))
Diffie_Helman_button.pack()

DES_button = tk.Button(root, text="DES",bg="light green",font=10, command=lambda: open_calculation_window("DES"))
DES_button.pack()

SHA_1_button = tk.Button(root, text="SHA-1",bg="light blue",font=10, command=lambda: open_calculation_window("SHA-1"))
SHA_1_button.pack()

root.mainloop()