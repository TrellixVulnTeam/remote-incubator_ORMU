import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os

# Getting credentials for email address
email = os.environ.get('EMAIL_ID')
email_pass = os.environ.get('EMAIL_PASS')