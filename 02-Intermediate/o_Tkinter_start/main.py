from tkinter import *

window = Tk()
window.title("First time here!!")
window.minsize(500, 300)


def button_clicked():
    label.config(text=input_type.get())


# Label
label = Label(text="I am a Label", font=(
    "Arial", 24, "italic", "bold"))
label.pack()
# label["text"] = "New Text"
# label.config(text="New Text")

# Button
button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry

input_type = Entry(width=10)
input_type.pack()
window.mainloop()
