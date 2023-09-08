import smtplib
from .defaultUtils import defaultEmail,defaultPasskey
from .serverUtils import smtpGmail,smtpPort

class smtpLib:
    def __init__(self,email,message,fromEmail,fromEmailPassword):
        self.email = email
        self.message = message,
        self.fromEmail = fromEmail ,
        self.fromEmailPasskey = fromEmailPassword 
       
    def sendEmail(self):
        try:
            email_server = smtplib.SMTP_SSL(smtpGmail,smtpPort)
            try:
                email_server.login(self.fromEmail[0],self.fromEmailPasskey)
                email_server.sendmail(self.fromEmail,self.email,self.message[0])
            
                return "emailSendSuccess"
            except:
                return "wrongCredentials"
            

        except Exception as error:
            print(error)
            return "emailSendFailed"
            

