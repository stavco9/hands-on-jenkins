import os
import sys

to = sys.argv[1] #"stavco9@gmail.com"
tokenPath = os.environ['GMAIL_TOKEN']
#tokenPath = os.environ['HOME'] + "/token.pickle"
mailSubject = sys.argv[2] #"Jenkins pipeline"
mailBody = sys.argv[3] #"Started Jenkins pipeline for build {} and branch {}".format(os.environ["BUILD_NUMBER"], os.environ["BRANCH_NAME"])