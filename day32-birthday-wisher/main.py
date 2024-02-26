import smtplib

# Outlook smtp smtp.live.com

my_email = 'ziriamanda@gmail.com'
password = 'qtnydxglyshyfcex'


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()     # Secure connection and encrypt email
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="ziriamanda@outlook.com",
                        msg="Subject:Hello \n\n This is the body of email")
    connection.close()
