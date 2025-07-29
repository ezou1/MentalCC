import os
from dotenv import load_dotenv

load_dotenv()

def load_credentials():
    DEVICE_ID = os.getenv("DEVICE_ID")
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    return DEVICE_ID, EMAIL, PASSWORD
