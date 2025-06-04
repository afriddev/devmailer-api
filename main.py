
"""

importing modules section start

"""
import uvicorn
from fastapi import FastAPI, Body, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError,HTTPException
from fastapi.responses import JSONResponse
from fastapi import Body
from sendMethods import send
from model import emailRequestModel
from server import defaultEmail, defaultPasskey
from sendMethods import sendCustom
import re
import requests as r
from fastapi.middleware.cors import CORSMiddleware
from db import logs_collection
from datetime import datetime

"""

importing modules section end

"""

"""

emailValidation Regex Pattern

"""
regexEmailPattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

"""

initalize fastapi

"""
app = FastAPI()
"""
cors config
"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


"""

422 Exception

"""
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            {
                "message":"wrongInput"
            }
            ),
    )
    
"""

404 Exception

"""
@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder(
            {
                "message":"wrongUrl"
            }
            ),
    )

"""

Root Of The EmailAPI

"""

@app.get("/")
def root():
    return {
        "message":{
            "serverStatus":"running",
            "version":"1.4.2"
        }
    }


@app.post("/sendEmail/")
def test(data: emailRequestModel, request: Request):
    client_host = request.client.host
    logs_collection.insert_one({
        "timestamp": datetime.utcnow(),
        "ip": client_host,
        "fromEmail": data.fromEmail,
        "toEmail": data.toEmail,
        "subject": data.subject,
        "body": data.body
    })
    if (re.fullmatch(regexEmailPattern,data.toEmail)):
        if (data.passkey != None and data.fromEmail != defaultEmail):

            try:
                json = {}
                sendInit = sendCustom(toEmail=data.toEmail,
                                fromEmail=data.fromEmail,
                                fromTitle=data.title,
                                subject=data.subject,
                                body=data.body,
                                passkey = data.passkey
                                )
                messageFromServer = sendInit.customMessage()
                if(messageFromServer == "sendEmailFailed" ):
                    json = {"message":"sendEmailFailed"}
                elif(messageFromServer == "wrongCredentials"):
                    json = {"message":"wrongCredentials"}
                elif(messageFromServer == "emailSendSuccess"):
                     json = {
                    "message": messageFromServer,
                    "title": data.title,
                    "fromEmail": data.fromEmail,
                    "toEmail": data.toEmail,
                    "subject": data.subject,
                    "body": data.body
                    }

                else:
                    return {"message":"serverError"}
                   
                return json
            except:
                return {
                    "message": "serverError"
                }

        else:
            if (data.fromEmail != defaultEmail and data.passkey == None):
                return {
                    "message": "passkeyrequired"
                }
            elif (data.fromEmail == defaultEmail):
                try:
                    json ={}
                    sendInit = send(toEmail=data.toEmail,
                                    fromEmail=data.fromEmail,
                                    fromTitle=data.title,
                                    subject=data.subject,
                                    body=data.body
                                    )
                    messageFromServer = sendInit.sendMessage()
                    if(messageFromServer == "emailSendSuccess"):
                    

                        json = {
                        "message": messageFromServer,
                        "title": data.title,
                        "fromEmail": data.fromEmail,
                        "toEmail": data.toEmail,
                        "subject": data.subject,
                        "body": data.body
                    }
                    elif(messageFromServer == "wrongCredentials"):
                        json = {"messsage":"wrongCredentials"}
                    elif(messageFromServer == "emailSendFailed"):
                        json = {"message":"emailSendFailed"}
                    else:
                        json = {"message":"serverError"}
                    return json
                except:
                    return {
                        "message": "serverError"
                    }
            else:
                return {
                    "message": "serverError"
                }
    else:
        return {
            "message": "wrongEmail"
        }


if __name__ == "__main__":
  uvicorn.run("main:app", reload=True)
