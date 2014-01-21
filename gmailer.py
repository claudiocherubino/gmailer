import argparse
import smtplib

from datetime import datetime
from email.mime.text import MIMEText

GOOGLE_SMTP_SERVER = 'smtp.gmail.com'
TLS_PORT = 587


def smtp_login(username, password, server=GOOGLE_SMTP_SERVER, port=TLS_PORT):
  server = smtplib.SMTP(server, port)
  server.starttls()
  server.login(username, password)
  return server

def create_email(sender, recipient, subject, body):
  message = MIMEText(body, 'html')
  message['Subject'] = subject
  message['From'] = sender
  message['To'] = recipient
  return message


# configure and parse command-line parameters
parser = argparse.ArgumentParser(description='Send emails using a Google account.')
parser.add_argument('user', help='Google account used to send emails')
parser.add_argument('password', help='Password to authenticate the Google account')
parser.add_argument('to', metavar='recipient',
    help='Recipient email address')
parser.add_argument('file', type=argparse.FileType('r'),
    help='Location of the file containing the markup to send')
parser.add_argument('--subject',
    help='Email subject')
args = parser.parse_args()

# set the email subject if it is not provided
if not args.subject:
	args.subject = 'Gmailer test - ' + str(datetime.now())

# login to the Google SMTP server
server = smtp_login(args.user, args.password)

# create the email message
email_body = args.file.read()
email = create_email(
    sender=args.user, recipient=args.to, subject=args.subject, body=email_body)

try:
  server.sendmail(args.user, args.to, email.as_string())
  print "Email sent successfully"
except smtplib.SMTPException as e:
  print "Unable to send email: " + e

