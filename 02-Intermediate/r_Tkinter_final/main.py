from tkinter import *  # type: ignore

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


def miles_to_km():
    to_miles = float(input_miles.get())
    label_output.config(text=to_miles*1.6)


# Inputs
input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)

# Text/Outputs

label = Label(text="Miles")
label.grid(column=2, row=0)

label = Label(text="is equal to")
label.grid(column=0, row=1)

label_output = Label(text="0", width=10)
label_output.grid(column=1, row=1)

label = Label(text="Km")
label.grid(column=2, row=1)

# Button

button = Button(text="Caculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
