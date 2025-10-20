from tkinter import *  # type: ignore

window = Tk()
window.title("First time here!!")
window.minsize(height=300, width=500)
window.config(padx=250, pady=20)


def button_clicked():
    label.config(text=input_type.get())


# Label
label = Label(text="I am a Label", font=(
    "Arial", 24, "italic", "bold"))
label.grid(column=0, row=0)
# label["text"] = "New Text"
# label.config(text="New Text")

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=0, row=1)

button = Button(text="I'm Here Seeking Vengenace", command=button_clicked)
button.grid(column=0, row=2)
# Entry

input_type = Entry(width=10)
input_type.grid(column=0, row=3)
window.mainloop()
