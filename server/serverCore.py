import smtplib
from .defaultUtils import defaultEmail,defaultPasskey
from .serverUtils import smtpGmail,smtpPort

class smtpLib:
    def __init__(self,email,message,fromEmail,fromEmailPassword):
        self.email = email
        self.message = message,
        self.fromEmail = fromEmail ,
        self.fromEmailPasskey = fromEmailPassword 
        print("server_inti")
    def sendEmail(self):
        try:
            email_server = smtplib.SMTP_SSL(smtpGmail,smtpPort)
            email_server.login(self.fromEmail[0],self.fromEmailPasskey)
            email_server.sendmail(self.fromEmail,self.email,self.message[0])
            print("ok")
            return {
                "fromemail":self.fromEmail,
                "email":self.email,
                "body":self.message,
                "message":"success"
                
            }
        except Exception as error:
            print(error)
            return {
                "message":"smtperror"}
            

