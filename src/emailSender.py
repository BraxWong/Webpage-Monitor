import yagmail

emailAddress = input("Please input your email address: ")
password = input("Please input your password: ")
body = "Hello there from Yagmail"

yag = yagmail.SMTP(emailAddress, password)
yag.send(
    to=emailAddress,
    subject="Yagmail test with attachment",
    contents=body, 
)
