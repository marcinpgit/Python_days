import smtplib
from secrets import *
from email.mime.text import MIMEText

temat = "Wiadomość od Marcina"
tresc = " to jest treść mojej wiadomości ółżźęą"

wiadomosc = MIMEText(tresc, _charset="utf-8")
wiadomosc['Subject'] = temat
wiadomosc['From'] = moj_login
wiadomosc['To'] = moj_login

mailer = smtplib.SMTP("smtp.gmail.com", 587)
mailer.ehlo()
mailer.starttls()
mailer.login(moj_login, moje_haslo)

mailer.sendmail(moj_login, moj_login, wiadomosc.as_string())

mailer.quit()
