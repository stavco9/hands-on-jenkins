import os
import variables
from sendgmail import TextMailMessage

#CLIENT_CREDENTIALS = "client_secret_1058289137326-ic0f1jqsnik3qem9pnfktm8vpdrat9qk.apps.googleusercontent.com.json"
#TOKEN_FILE = "C:\\temp\\blabla"
TOKEN_FILE = variables.tokenPath
toAddress = variables.to
mailSubject = variables.mailSubject
mailBody = variables.mailBody

def main():
    mail = TextMailMessage(toAddress, mailSubject, mailBody)
    mail.authenticate(token_file=TOKEN_FILE)
    #mail.logoff()
    mail.send()

if __name__ == '__main__':
    main()