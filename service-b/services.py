import requests
from dotenv import load_dotenv
import os

load_dotenv()

SERVICE_C_URL = os.getenv("SERVICE_C_URL")

def send(data:list[dict])->requests.Response:
    try:
        response = requests.post(url=SERVICE_C_URL, data=data).json
    except:
        response = "service c not implemented yet"
    return response
