# app/crypto.py
from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("ENC_KEY")
fernet = Fernet(KEY)

def encrypt(text: str) -> str:
    return fernet.encrypt(text.encode()).decode()

def decrypt(token: str) -> str:
    return fernet.decrypt(token.encode()).decode()


