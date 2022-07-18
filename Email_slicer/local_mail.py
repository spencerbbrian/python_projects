#Send an email to a localhosty port
import os, smtplib
from dotenv import load_dotenv

load_dotenv()
email_address = os.getenv('email_address')
password = os.getenv('password')

with smtplib.SMTP('localhost',1025) as smtp:

    subject = 'Grab dinner this weekend'
    body = 'How about dinner at 6pm this Saturday?'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(email_address, email_address, msg)