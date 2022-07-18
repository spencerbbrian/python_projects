#This test is no longer possible because gmail no longer allows the use
#of app passwords
import os, smtplib
from dotenv import load_dotenv

load_dotenv()
email_address = os.getenv('email_address')
password = os.getenv('password')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    #Identifies mail serving we are using
    smtp.ehlo()
    #Encrypt traffic
    smtp.starttls()
    #Reidentify as an encrypted connection
    smtp.ehlo()

    smtp.login(email_address,password)

    subject = 'Grab dinner this weekend'
    body = 'How about dinner at 6pm this Saturday?'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(email_address, email_address, msg)