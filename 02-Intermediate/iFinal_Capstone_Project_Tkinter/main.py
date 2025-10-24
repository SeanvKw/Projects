import pandas
from tkinter import *  # type: ignore
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANG = ("Ariel", 40, "italic")
FONT_TRANSLATED = ("Ariel", 50, "bold")
picked_word = {}
to_learn = []
try:
    saved_data = pandas.read_csv(
        "02-Intermediate/j_Capstone_Project_Tkinter/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(
        "02-Intermediate/j_Capstone_Project_Tkinter/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = saved_data.to_dict(orient="records")
# Window Config
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


def next_card():
    global picked_word, timer
    window.after_cancel(timer)
    picked_word = random.choice(to_learn)

    canvas_flash.itemconfig(
        translation, text=picked_word["French"], fill='black')
    canvas_flash.itemconfig(language, text="French", fill='black')
    canvas_flash.itemconfig(create_img, image=card_front)

    timer = window.after(3000, func=flip)
# Function after "accept" button was clicked


def accept():
    to_learn.remove(picked_word)
    saved_data = pandas.DataFrame(to_learn)
    saved_data.to_csv(
        "02-Intermediate/j_Capstone_Project_Tkinter/data/words_to_learn.csv", index=False)
    next_card()

# Function after "decline" button was clicked


def declined():
    next_card()


def flip():
    canvas_flash.itemconfig(create_img, image=card_back)
    canvas_flash.itemconfig(language, text="English", fill='white')
    canvas_flash.itemconfig(
        translation, text=picked_word["English"], fill='white')


timer = window.after(3000, func=flip)
# Canvas Main Image


canvas_flash = Canvas(width=800, height=526,
                      highlightthickness=0, bg=BACKGROUND_COLOR)

card_front = PhotoImage(
    file="02-Intermediate/j_Capstone_Project_Tkinter/images/card_front.png")
card_back = PhotoImage(
    file="02-Intermediate/j_Capstone_Project_Tkinter/images/card_back.png")

create_img = canvas_flash.create_image(400, 263, image=card_front)
canvas_flash.grid(column=0, row=0, columnspan=2)

# Canvas Text

language = canvas_flash.create_text(
    400, 150, text="French", font=FONT_LANG)

translation = canvas_flash.create_text(
    400, 263, text="cos", font=FONT_TRANSLATED)

# Canvas Buttons Images

decline_image = PhotoImage(
    file="02-Intermediate/j_Capstone_Project_Tkinter/images/wrong.png")
accept_image = PhotoImage(
    file="02-Intermediate/j_Capstone_Project_Tkinter/images/right.png")

# Buttons
decline_button = Button(
    image=decline_image, highlightthickness=0, command=declined)
decline_button.grid(column=0, row=1)

accept_button = Button(
    image=accept_image, highlightthickness=0, command=accept)
accept_button.grid(column=1, row=1)
next_card()
window.mainloop()
