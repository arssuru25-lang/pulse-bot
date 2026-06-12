import smtplib
from email.mime.text import MIMEText

def send_alert(subject, body):

    sender = "ars.suru786@gmail.com"
    receiver = "ars.suru786@gmail.com"

    password = "qarhyvvjjcmubten"

    msg = MIMEText(body)

    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)