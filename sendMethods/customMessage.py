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





class sendCustom:
    def __init__(self,**userData):
        #init toEmail for useage
        self.toEmail = userData["toEmail"]
        self.fromTitle = userData["fromTitle"]
        self.fromEmail = userData["fromEmail"]
        self.subject = userData["subject"]
        self.body = userData["body"]
        self.passkey = userData["passkey"]
        
        """
        init sendcore for message for

        """
        
        sendCore = messageCore(
           fromTitle=self.fromTitle,
           fromEmail=self.fromEmail,
           toEmail=self.toEmail,
           subject=self.subject,
           body=self.body
        )
        self.message = sendCore.messageBody()
        
        
    def customMessage(self):
      
        """
        smtpLib init

        """
        serverInit = smtpLib(self.toEmail,self.message,self.fromEmail,
        
        self.passkey)
        messageFromServer = serverInit.sendEmail()
        if(messageFromServer == "sendEmaiLSuccess"):
            return "sendEmailSuccess"
        elif(messageFromServer == "wrongCredentials"):
            return "wrongCredentials"
        else:
            return "sendEmailFailed"

    

        


        
        
    




