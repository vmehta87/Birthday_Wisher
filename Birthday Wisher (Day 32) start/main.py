import smtplib
import datetime as dt
from random import choice


def send_email(text):
    my_email = '87vmehta.test@gmail.com'
    password = 'uznaelgyfuhxpgwz'

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='test.87vmehta@gmail.com',
            msg=f'Subject:email sent by coding\n\n{text}???')


now = dt.datetime.now()
if now.weekday() == 0:
    with open('quotes.txt', 'r') as quotes_file:
        quotes = quotes_file.readlines()
        quote = choice(quotes)
        send_email(quote)

