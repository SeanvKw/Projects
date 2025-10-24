import smtplib
# """smtplib.SMTP("smtp.gmail.com", port=587)"""
# password = "app password"
# my_email = "youremail@gmail.com"
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="randommail@gmail.com",
#         msg="Subject:Hello\n\nThats my program lol")

# current_date_time = dt.datetime.now()
# year = current_date_time.year
# month = current_date_time.month
# day_of_week = current_date_time.weekday()
# print(current_date_time, "\n", year, "\n", month, "\n", day_of_week)

# date_of_birth = dt.datetime(year=2006, month=2, day=3)
# print(date_of_birth)
# day_of_week = current_date_time.weekday()
# print(day_of_week)
# if day_of_week == 4:
#    print("yep it works!")

import datetime as dt
import random


password = "app password"
my_email = "youremail@gmail.com"
to_mail = "youremail@gmail.com"
current_date_time = dt.datetime.now()
day_of_week = current_date_time.weekday()
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    motivational_quotes = open(
        "02-Intermediate/j_SMTP/first_day/quotes.txt", "r").readlines()
    picked_quote = random.choice(motivational_quotes)
    if day_of_week == 4:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_mail,
            msg=f"Subject:Motivational Quote SMPT Project\n\n{picked_quote}"
        )
    else:
        print("Today is not the right date to send something so spicy!")
