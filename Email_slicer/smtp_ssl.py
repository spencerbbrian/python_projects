#This test is no longer possible because gmail no longer allows the use
#of app passwords
from fileinput import filename
import os, smtplib, imghdr
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()
email_address = os.getenv('email_address')
password = os.getenv('password')

msg = EmailMessage()
msg['Subject'] = 'Grab dinner this weekend?'
msg['From'] = email_address
msg['To'] = email_address
msg.set_content('How about dinner at 6pm this Saturday?')

with open(r'C:\Users\brian\Desktop\CCR\FULLSTACK_DEVELOPMENT\BACKEND\PYTHON\Projects\Email_slicer\mini.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
    # print(file_type)

msg.add_attachment(file_data, maintype='image',subtype=file_type,filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address,password)

    smtp.send_message(msg)