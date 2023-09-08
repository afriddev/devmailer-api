# importing default values from senddefault
from .sendDefault import *
import sys
sys.path.append("..")
# importing messaging core from snedCore
from sendCore import messageCore
# importing defaultEmail
from server import defaultEmail,defaultPasskey
#importing smtplib from serverCore
from server import smtpLib





class sendTest:
    def __init__(self,**userData):
        #init toEmail for useage
        self.toEmail = userData["toEmail"]
        """
        init sendcore for message for

        """
        
        sendCore = messageCore(
           fromTitle=defaultFromTitle,
           fromEmail=defaultEmail,
           toEmail=self.toEmail,
           subject=defaultSubject,
           body=defaultBody
        )
        self.message = sendCore.messageBody()
        print(self.message)
        
    def sendMessage(self):
      
        """
        smtpLib init

        """
        serverInit = smtpLib(self.toEmail,self.message,defaultEmail,defaultPasskey)
        serverInit.sendEmail()
        print("sendMessage")

        


        
        
    




