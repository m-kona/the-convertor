from tkinter import *

window = Tk()

window.geometry("500x500")  # Setting screen size("width"x"height")
window.title("The Temperature Converter")

c_input = StringVar()
f_input = StringVar()
results = StringVar()

# Functions
def activate_celsius_converter():
    c_entry.configure(state="normal")
    celsius_to_fahrenheit_label.configure(state="normal")
    f_entry.configure(state="readonly")
    fahrenheit_to_celsius_label.configure(state="disabled")


def activate_fahrenheit_converter():
    f_entry.configure(state="normal")
    fahrenheit_to_celsius_label.configure(state="normal")
    c_entry.configure(state="readonly")
    celsius_to_fahrenheit_label.configure(state="disabled")


def clear():
    c_entry.configure(state="normal")
    f_entry.configure(state="normal")
    c_entry.delete(0, END)
    f_entry.delete(0, END)
    results.set(" ")
    # celsius_to_fahrenheit_label.configure(state="disabled")
    # fahrenheit_to_celsius_label.configure(state="disabled")


def conversion():
    get_number = float(c_entry.get())
    get_number_two = float(f_entry.get())
    f = get_number * 9/5 + 32  # Formulae for celsius to fahrenheit conversion
    c = (get_number_two - 32) * 5/9 # Formulae for fahrenheit to celsius conversion
    output = "Celsius To Fahrenheit = " + "\t" + str(f) + "\n" + "Fahrenheit To Celsius = " + "\t" + str(c)
    return results.set(output)


def exit_program():
    return window.destroy()


# Entry widget
c_entry = Entry(window, textvariable=c_input, state=DISABLED)
f_entry = Entry(window, textvariable=f_input, state=DISABLED)

# Label
results_label = Label(window, textvariable=results, bg="blue", width=50, height=10,)
celsius_to_fahrenheit_label = Label(window, text="Celsius To Fahrenheit", state=DISABLED)
fahrenheit_to_celsius_label = Label(window, text="Fahrenheit To Celsius", state=DISABLED)

# Button widgets
# Activation Buttons
activate_c_button = Button(window, text="Activate Celsius", command=activate_celsius_converter)
activate_f_button = Button(window, text="Activate Fahrenheit",
                           command=activate_fahrenheit_converter)

# Calculation Button
calc_conversion_button = Button(window, text="Calculate", command=conversion)

# Exit and Clear Buttons
exit_button = Button(window, text="Exit", command=exit_program)
clear_button = Button(window, text="Clear", command=clear)

# placing widgets
# Placing Labels
celsius_to_fahrenheit_label.place(x=10, y=40)
fahrenheit_to_celsius_label.place(x=10, y=90)
results_label.place(x=55, y=200)

# Placing text entries
c_entry.place(x=160, y=44)
f_entry.place(x=160, y=94)

# Placing Buttons
activate_c_button.place(x=340, y=40)
activate_f_button.place(x=340, y=90)
calc_conversion_button.place(x=200, y=150)
clear_button.place(x=150, y=400)
exit_button.place(x=300, y=400)

window.mainloop()