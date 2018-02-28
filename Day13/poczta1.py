import smtplib
from secrets import *

adresat = moj_login

mailer = smtplib.SMTP("smtp.gmail.com", 587)

mailer.ehlo()

mailer.starttls()

mailer.login(moj_login, moje_haslo)

temat = "Hello from Marcin"
wiadomosc = " to jest moja wiadomosc"

tresc = temat + wiadomosc

mailer.sendmail(moj_login, adresat, tresc)

mailer.quit()