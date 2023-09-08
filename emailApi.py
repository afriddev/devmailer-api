import uvicorn
from fastapi import FastAPI
from sendMethods import send
from model import emailRequestModel
from server import defaultEmail
import re
regexEmailPattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
emailAPI = FastAPI()
@emailAPI.get("/")
def root():
    return {
        "server": "working ..."
    }
@emailAPI.post("/sendEmail/")
def test(data: emailRequestModel):
    if (re.fullmatch(regexEmailPattern, data.toEmail)):
        if (data.passkey != None and data.fromEmail != defaultEmail):
            return {
                "message": "under Maintence .."
            }
        else:
            if (data.fromEmail != defaultEmail and data.passkey == None):
                return {
                    "message":"passkeyrequired"
                }
            elif(data.fromEmail == defaultEmail):
                try:
                    sendInit = send(toEmail=data.toEmail,
                                    fromEmail=data.fromEmail,
                                    fromTitle=data.title,
                                    subject=data.subject,
                                    body=data.body
                                    )
                    sendInit.sendMessage()
                    json = {
                        "message": "success",
                        "title": data.title,
                        "fromEmail": data.fromEmail,
                        "toEmail": data.toEmail,
                        "subject": data.subject,
                        "body":data.body
                    }
                    return json
                except:
                    return {
                        "message": "serverError"
                    }
            else:
                return{
                    "message":"serverError"
                }
    else:
        return {
            "message": "wrongEmail"
        }


if __name__ == "__main__":
    uvicorn.run("emailApi:emailAPI", reload=True)
