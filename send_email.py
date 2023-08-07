import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "dannyveugelen@gmail.com"
password = "qccyazhxksvspboo"

receiver = "1982capoeira@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Portfolio App contact-me
Hi!
How are you?
Bye!
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message )
