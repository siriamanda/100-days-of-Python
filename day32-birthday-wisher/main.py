import datetime as dt
import pandas as pd
import random
import smtplib

now = dt.datetime.now()
today = (now.month, now.day)

birthday_file = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in birthday_file.iterrows()}

my_email = 'ziriamanda@gmail.com'
password = 'qtnydxglyshyfcex'

if today in birthdays_dict:

    random_number = random.randint(1,3)
    with open(f"./letter_templates/letter_{random_number}.txt", "r") as random_letter:
        personalised_letter = random_letter.read().replace("[NAME]", birthdays_dict[today]['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure connection and encrypt email
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ziriamanda@outlook.com",
            msg=f"Subject:Happy Birthday \n\n {personalised_letter}")







