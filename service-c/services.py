import requests
from datetime import datetime
from dotenv import load_dotenv
from os import getenv
import json

load_dotenv()

service_b_url = getenv("SERVICE_B_URL","http://localhost:8000/clean")


class RecordsService():
    pass
    
