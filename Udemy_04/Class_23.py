# send e-mail SMTP with Python

import os
import pathlib
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

# data send and recipient
sender = os.getenv('FROM_EMAIL', '')
recipient = ''

# File path HTML
FILE_PATH_HTML = pathlib.Path(__file__).parent / 'Class_23.html'

# SMTP Settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Text Message
with open(FILE_PATH_HTML, 'r', encoding='utf-8') as file:
    texto_file = file.read()
    template = Template(texto_file)
    text_email = template.substitute(name='Joamir')

# Transform our message in MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = sender
mime_multipart['to'] = recipient
mime_multipart['subject'] = 'Assunto do teste Joamir'

body_email = MIMEText(text_email, 'html', 'utf-8')
mime_multipart.attach(body_email)

# Send Email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('Email enviado com sucesso')