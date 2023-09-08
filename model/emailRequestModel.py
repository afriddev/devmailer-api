
from pydantic import BaseModel,Field
import sys
sys.path.append("..")
from server import defaultEmail
from sendMethods import sendDefault




class emailRequestModel(BaseModel):
    fromEmail:str | None = defaultEmail
    toEmail:str 
    title:str | None = sendDefault.defaultFromTitle
    subject:str | None =sendDefault.defaultSubject
    body:str | None = sendDefault.defaultBody
    passkey:str | None = None


