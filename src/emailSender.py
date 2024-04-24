import smtplib

def sendEmail(emailAddress, password, subject, message):
    print("About to send email")
    message_bytes = message.encode('utf-8')
    text = f"Subject: {subject}\n\n{message_bytes.decode()}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    print("Logging in")
    server.login(emailAddress, password)
    print("Sending email")
    server.sendmail(emailAddress, emailAddress, text)
    server.quit()
