from tkinter import *  # type: ignore

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


def miles_to_km():
    to_miles = int(input_miles.get())
    label_result.config(text=round(to_miles*1.609, 2))


# Inputs
input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)

# Text/Outputs

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_to_km = Label(text="Km")
label_to_km.grid(column=2, row=1)

label_result = Label(text="0", width=10)
label_result.grid(column=1, row=1)

# Button

button = Button(text="Caculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
