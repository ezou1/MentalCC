from config import load_credentials
from eeg import setup, register_kinesis
from controller import activate_push_action
import time

def callback(data):
    print(f"Callback")
    activate_push_action()

if __name__ == "__main__":
    # ENTER DETAILS HERE
    DEVICE_ID = "" 
    EMAIL = ""
    PASSWORD = ""
    
    print(load_credentials())
    setup(DEVICE_ID, EMAIL, PASSWORD)
    unsubscribe = register_kinesis("push", callback)
    print("Listening for 'push'...")
    time.sleep(60)
    unsubscribe()
    print("Logoff.")
