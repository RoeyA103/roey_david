import requests
from datetime import datetime
from dotenv import load_dotenv
from os import getenv
import json
from db import pool
load_dotenv()

class RecordsService():

    def save_records():
        try:
            conn = pool.get_connection()
            cursor = conn.cursor()
            #fiil your code here!!!----------
        except:
            pass

        finally:
            cursor.close()
            conn.close()

    def get_records():
        try:
            conn = pool.get_connection()
            cursor = conn.cursor()
            #fiil your code here!!!----------
        except:
            pass

        finally:
            cursor.close()
            conn.close()

    def get_records_count():
        try:
            conn = pool.get_connection()
            cursor = conn.cursor()
            #fiil your code here!!!----------
        except:
            pass

        finally:
            cursor.close()
            conn.close()

    def get_avg_temperature():
        try:
            conn = pool.get_connection()
            cursor = conn.cursor()
            #fiil your code here!!!----------
        except:
            pass

        finally:
            cursor.close()
            conn.close()
    
    
