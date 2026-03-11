import smtplib
from email.mime.text import MIMEText
import os

def send_email(to_email, summary):

    msg = MIMEText(summary)

    msg["Subject"] = "AI Sales Report"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = to_email

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login(
        os.getenv("EMAIL_USER"),
        os.getenv("EMAIL_PASS")
    )

    server.send_message(msg)
    server.quit()