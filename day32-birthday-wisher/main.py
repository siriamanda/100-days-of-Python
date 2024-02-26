import datetime as dt
import random
import smtplib

my_email = 'ziriamanda@gmail.com'
password = 'qtnydxglyshyfcex'

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:

    with open("quotes.txt", "r") as quotes:
        quotes_list = quotes.readlines()
        random_quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()     # Secure connection and encrypt email
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
        to_addrs="ziriamanda@outlook.com",
        msg=f"Subject:You can do this \n\n {random_quote}")
        connection.close()








# import smtplib

# Outlook smtp smtp.live.com

# my_email = 'ziriamanda@gmail.com'
# password = 'qtnydxglyshyfcex'


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()     # Secure connection and encrypt email
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="ziriamanda@outlook.com",
#                        msg="Subject:Hello \n\n This is the body of email")
#     connection.close()

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# print(year)

# print(date_of_birth)




