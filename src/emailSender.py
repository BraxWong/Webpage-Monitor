import smtplib

def sendEmail(emailAddress, password, subject, message):
    text = f"Subject: {subject}\n\n{message}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(emailAddress, password)

    server.sendmail(emailAddress, emailAddress, text)
