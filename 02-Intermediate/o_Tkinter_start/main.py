import tkinter

window = tkinter.Tk()
window.title("First time here!!")
window.minsize(500, 300)

# Label
label = tkinter.Label(text="I am a Label", font=(
    "Arial", 24, "italic", "bold"))
label.pack(side="left")

window.mainloop()
