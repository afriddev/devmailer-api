import uvicorn
from fastapi import FastAPI
from sendMethods import sendTest


emailAPI = FastAPI()
@emailAPI.get("/")
def root():
    return{
        "server":"working ..."
    }

@emailAPI.get("/sendEmail/{email}")
def test(email:str):
    send = sendTest(toEmail = email)
    send.sendMessage()

    return {
        "email":email
    }







if __name__ == "__main__":
    uvicorn.run("emailApi:emailAPI",reload=True)