# server.py
from dotenv import load_dotenv
import os

load_dotenv()

defaultEmail = os.getenv("DEFAULT_EMAIL")
defaultPasskey = os.getenv("DEFAULT_PASSKEY")
