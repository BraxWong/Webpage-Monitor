import smtplib

def sendEmail(emailAddress, password):

    subject = "Skinport market has updated"
    message = "Hello. The skinport market has updated. Have a nice day"

    text = f"Subject: {subject}\n\n{message}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(emailAddress, password)

    server.sendmail(emailAddress, emailAddress, text)

    print("Verify email has been sent")
