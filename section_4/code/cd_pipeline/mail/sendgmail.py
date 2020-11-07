from __future__ import print_function
import httplib2
import pickle
import base64
import os.path
from abc import ABC, abstractmethod
from shutil import copyfile
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
'https://www.googleapis.com/auth/gmail.send']

class MailMessage(ABC):
    @abstractmethod
    def create_message(self):
        pass
    
    def authenticate(self, credentials_file=None, token_file=None):
        """Authenticate to Gmail API. If it's the first time to authenticate,
           you must provide credentials file obtained from Google Cloud
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.

        # If a token file is given by parameter, use it
        if token_file and not os.path.isfile('token.pickle'):
            if os.path.isfile(token_file): 
                copyfile(token_file, 'token.pickle')
            else:
                raise Exception("Your token file at path {} was not found".format(token_file))

        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            elif not credentials_file:
                raise Exception("If it is the first time you authenticate, you must provide credentials file")
            elif not os.path.isfile(credentials_file):
                raise Exception("The credentials file you provided in path {} was not found".format(credentials_file))
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        self.creds = creds

    def logoff(self):
        if os.path.exists('token.pickle'):
            os.remove('token.pickle')
        
        if hasattr(self, 'creds'):
            delattr(self, 'creds')

    def send(self):
        if not hasattr(self, 'creds'):
            raise Exception("You must authenticate before sending mail !!")

        service = build('gmail', 'v1', credentials=self.creds)

        # Call the Gmail API
        results = service.users().messages().send(userId='me', body=self.message).execute() # pylint: disable=maybe-no-member

        print(results)


class TextMailMessage(MailMessage):
    def __init__(self, toAddress, mailSubject, MailBody):
        self.message = self.create_message(toAddress, mailSubject, MailBody)

    def create_message(self, to, subject, message_text):
        message = MIMEText(message_text)
        message['to'] = to
        message['subject'] = subject
        return {
            'raw': base64.urlsafe_b64encode(message.as_string().encode('utf-8')).decode('utf-8')
        }