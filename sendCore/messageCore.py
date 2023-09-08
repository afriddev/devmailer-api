import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from server import defaultUtils



class messageCore:
    def __init__(self,fromTitle,fromEmail,toEmail,subject,body):
        self.fromTitle =  fromTitle 
        self.fromEmail = fromEmail
        self.toEmail = toEmail
        self.subject = subject
        self.body = body 


   
    def messageBody(self):
        message = f"""From: {self.fromTitle} <{ self.fromEmail }>
To: {self.toEmail}
Subject: {self.subject}
{self.body}
"""
        
        return message