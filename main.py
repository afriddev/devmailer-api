from fastapi import FastAPI
import smtplib
import random
app = FastAPI()
# --- root of The Server ----#
@app.get("/")
async def root():
    return{"EmailServerApi":{
        "version":"1.1.2",
        "status":"running",
        "server":"https://emailapi-tgbc.onrender.com"
    },
           "help":"/help",
           "default OTP Preferences":"/defaultOTPPreferences",
            "Custom Message" :"/CustomHelp"         
                       }
# --- Custom Message Details route ---#
@app.get('/CustomHelp')
async def Custom():
    return {
        "version":"1.1.2",
        "Format":"server/Custom/Email/subject/message",
        "Usage":"server/Custom/xyzemail@gmail.com/Hello/hello this is afrid"
    }
# --- Custom MessageSend Route ----#
@app.get('/Custom/{to}/{subjct}/{body}')
async def CustomMessage(to:str,subject:str,body:str):
    status = ""
    try:
        emailServer = smtplib.SMTP_SSL()
        emailServer.login("369afrid@gmail.com","mvws tzoq cdsf viiu")
        message = f"""From: EmailAPI <369afrid@gmail.com>
To: {to}
Subject: {subject}
{body}
"""
        emailServer.sendmail(to,'369afrid@gmail.com',message)
        status = "success"
    except:
        status = "error"
    
    return{
        "status":status,
        "subject":subject,
        "body":body
    }


# --- default emailSettings route ----#
@app.get("/defaultOTPPreferences")
async def defaultOTPPreferences():
    return {
        "Otp":"100000 - 999999",
        "Subject":"OTP",
        "Body":"To Login Your Verification Code Is 123456"
    }
# --- server hep route ----#
@app.get("/help")
async def help():
    return{
    "SendOTPWithDefaultSettings":{
        "url":"server/SendEmail/xyz@gmail.com",
        "otp":"default",
        "subject":"default",
        "body":"default"
    },
    "SendOTPCustom":{
        "url":"server/SendEmail/xyz@gmail.com/123456",
        "subject":"default",
        "body":"default"
    },
     "SendOTPCustomSubject":{
        "url":"server/SendEmail/xyz@gmail.com/123456/Example Subject",
        "body":"default"
    },
     "SendOTPCustomBody":{
        "url":"server/SendEmail/xyz@gmail.com/123456/Example Subject/your verification code : 123456",
    },
    "Custom Message":{
        "url":"server/Custom/xyzemail@gmail.com/hello/hi this is afrid"

    }
    }

# --- send email by using only email ----#
@app.get("/SendEmail/{email}")
async def sendEmail(email:str):
    status = ""
    otp = random.randint(100000,999999)
    message = f"""From: EmailAPI <369afrid@gmail.com>
To: {email}
Subject: OTP
To Login Your Verification Code iS {otp}
"""
    try:
        email_server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        email_server.login("369afrid@gmail.com","mvws tzoq cdsf viiu")
        email_server.sendmail("369afrid@gmail.com",email,message)
        status = "success"
    except :
        status = "error"
    return {
        "status":status,
        "email":email,
        "otp":otp
    }

# --- send email by using email and your custom OTP ----#
@app.get("/SendEmail/{email}/{otp}")
async def sendEmail(email:str,otp:int):
    status = ""
    message = f"""From: EmailAPI <369afrid@gmail.com>
To: {email}
Subject: OTP
To Login Your Verification Code iS {otp}
"""
    try:
        email_server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        email_server.login("369afrid@gmail.com","mvws tzoq cdsf viiu")
        email_server.sendmail("369afrid@gmail.com",email,message)
        status = "success"
    except :
        status = "error"
    return {
        "status":status,
        "email":email,
        "otp":otp
    }

# --- send email by using email,OTP and custom subject ----#
@app.get("/SendEmail/{email}/{otp}/{subject}")
async def sendEmail(email:str,otp:int,subject:str):
    status = ""
    message = f"""From: EmailAPI <369afrid@gmail.com>
To: {email}
Subject: {subject}
To Login Your Verification Code iS {otp}
"""
    try:
        email_server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        email_server.login("369afrid@gmail.com","mvws tzoq cdsf viiu")
        email_server.sendmail("369afrid@gmail.com",email,message)
        status = "success"
    except :
        status = "error"
    return {
        "status":status,
        "email":email,
        "otp":otp
    }

# --- send email by using email,OTP,subject and custom body ----#
@app.get("/SendEmail/{email}/{otp}/{subject}/{body}")
async def sendEmail(email:str,otp:int,subject:str,body:str):
    status = ""
    message = f"""From: EmailAPI <369afrid@gmail.com>
To: {email}
Subject: {subject}
{body}
"""
    try:
        email_server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        email_server.login("369afrid@gmail.com","mvws tzoq cdsf viiu")
        email_server.sendmail("369afrid@gmail.com",email,message)
        status = "success"
    except :
        status = "error"
    return {
        "status":status,
        "email":email,
        "otp":otp
    }