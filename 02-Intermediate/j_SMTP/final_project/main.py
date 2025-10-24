import pandas
import smtplib
import random
import datetime as dt

PLACEHOLDER = "[NAME]"
password = "app password"
my_email = "youremail@gmail.com"
to_mail = "youremail@gmail.com"

current_date = (dt.datetime.now().day, dt.datetime.now().month)
data = pandas.read_csv("02-Intermediate/j_SMTP/final_project/birthdays.csv")
birthdays_dict = {(row["day"], row["month"])
                   : row for (index, row) in data.iterrows()}


if current_date in birthdays_dict:
    birthday_name = birthdays_dict[current_date]
    file_path = f"02-Intermediate/j_SMTP/final_project/letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace(PLACEHOLDER, birthday_name["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_mail,
            msg=f"Subject:Happy Birthday {birthday_name["name"]} \n\n{contents}")
