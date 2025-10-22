from tkinter import *  # type: ignore
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
FONT = ("", 12, "bold")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_input.delete(0, END)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, str(password))
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_to_file():
    website = website_input.get()
    login = login_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": login,
            "password": password
        }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Something is Empty",
                            message="Please fill all the fields for correct validation of data.")
    else:
        try:
            with open(
                    "02-INTERMEDIATE/ie_Password_Manager/passwords.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating with new data
                data.update(new_data)

        except FileNotFoundError:
            with open("02-INTERMEDIATE/ie_Password_Manager/passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("02-INTERMEDIATE/ie_Password_Manager/passwords.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:

            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- SEARCH BY WEBSITE ------------------------------- #


def search_by_webiste():
    website = website_input.get()

    with open("02-INTERMEDIATE/ie_Password_Manager/passwords.json") as data_file:
        data = json.load(data_file)

        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Website not Found",
                                 message="Website has not been found in passwords.json\nTry to exactly match the webiste name and CAPITAL LETTERS!")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=0)

# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="02-Intermediate/ie_Password_Manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1, sticky="e")

login_label = Label(text="Email/Username:", font=FONT)
login_label.grid(column=0, row=2, sticky="e")

password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3, sticky="e")

# Entry
website_input = Entry()
website_input.grid(column=1, row=1, sticky="ew", padx=(4, 0))
website_input.focus()

login_input = Entry()
login_input.grid(column=1, row=2, columnspan=2, sticky="ew", padx=(4, 0))
login_input.insert(END, "example@gmail.com")

password_input = Entry()
password_input.grid(column=1, row=3, sticky="ew", padx=(4, 0))

# Buttons
search_website = Button(text="Search", font=FONT, command=search_by_webiste)
search_website.grid(column=2, row=1, sticky="ew", padx=(6, 0))

generate_password = Button(text="Generate Password",
                           font=FONT, command=password_generator)
generate_password.grid(column=2, row=3, sticky="w", padx=(6, 0))

Add_to_file = Button(text="Add", font=FONT, command=save_to_file)
Add_to_file.grid(column=1, row=4, columnspan=2, sticky="ew", pady=(6, 0))


window.mainloop()
