import smtplib
import secrets

# definuje dane do logowania
adresat = secrets.login
nadawca = secrets.login
haslo = secrets.haslo

# tworzenie silnika
mailer = smtplib.SMTP('smtp.gmail.com', 587)
# witam sie z serwerem
mailer.ehlo()

# włączyć szyfrowanie
mailer.starttls()

# loguję się
mailer.login(nadawca, haslo)

temat = "Subject: Hello from Marcin\n"
wiadmosc = "To jest tresc wiadomosci"
tresc = temat + wiadmosc

# wysyłam
mailer.sendmail(nadawca, adresat, tresc)
print("Wysłano maila")

mailer.quit()