
import pandas
import smtplib
import datetime as dt
import random


today_month = dt.datetime.now().month
today_day = dt.datetime.now().day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today in birthdays_dict:
    print("ho")
    birthday_person = birthdays_dict[today]
    nr = random.randint(1,3)
    with open(file=f"letter_templates/letter_{nr}.txt") as file:
        filedata = file.read()
        filedata = filedata.replace('[NAME]', birthday_person['name'])
    my_gmail = XXXX
    my_gpass = XXXX
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=XXXX, password=XXXX)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=my_gmail,
            msg=f'Subject: Happy Birthday\n\n{filedata}'
        )


