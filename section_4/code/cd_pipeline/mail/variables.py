import os
import sys

to = os.environ['mailTo'] 
tokenPath = os.environ['GMAIL_TOKEN']
#tokenPath = os.environ['HOME'] + "/token.pickle"
mailSubject = os.environ['mailSubject'] #"Jenkins pipeline"
mailBody = os.environ['mailBody'] #"Started Jenkins pipeline for build {} and branch {}".format(os.environ["BUILD_NUMBER"], os.environ["BRANCH_NAME"])