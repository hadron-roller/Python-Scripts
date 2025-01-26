import os
import base64
import json
import re
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# If modifying the SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail():
    """Authenticate the user with Gmail API and return the service object."""
    creds = None
    # The token file stores the user's access and refresh tokens, and is created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run.
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    # Build the Gmail API service object.
    service = build('gmail', 'v1', credentials=creds)
    return service

def create_message(sender, to, subject, body):
    """Create a message for the email."""
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg = MIMEText(body)
    message.attach(msg)

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    return {'raw': raw_message}

def send_message(service, sender, to, subject, body):
    """Send an email message via Gmail API."""
    try:
        message = create_message(sender, to, subject, body)
        message = service.users().messages().send(userId="me", body=message).execute()
        print('Message sent successfully! Message ID:', message['id'])
    except Exception as error:
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    service = authenticate_gmail()

    sender = "your-email@gmail.com"  # Replace with your email address
    to = "recipient-email@gmail.com"  # Replace with the recipient's email address
    subject = "Test Email"
    body = "This is a test email sent using Gmail API in Python."

    send_message(service, sender, to, subject, body)
