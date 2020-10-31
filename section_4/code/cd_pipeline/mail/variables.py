import os

to = "stavco9@gmail.com"
tokenPath = os.environ['GMAIL_TOKEN']
#tokenPath = os.environ['HOME'] + "/token.pickle"
mailSubject = "Jenkins pipeline"
mailBody = "Started Jenkins pipeline for build {} and branch {}".format(os.environ["BUILD_NUMBER"], os.environ["BRANCH_NAME"])