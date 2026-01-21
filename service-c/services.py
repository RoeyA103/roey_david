import requests
from datetime import datetime
from dotenv import load_dotenv
from os import getenv
import json
from db import pool
load_dotenv()

class RecordsService():

    def save_records(data: list[dict]):
        try:
            conn = pool.get_connection()
            cursor = conn.cursor()
            #fiil your code here!!!----------
            query = """
                insert into weather_records (
                    timestamp,
                    location_name,
                    country,
                    latitude,
                    longitude,
                    temperature,
                    wind_speed,
                    humidity,
                    temperature_category,
                    wind_category)
                values (
                    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s
                );
            """
            for item in data:
                values = item.values()
                cursor.execute(query, values)
            conn.commit()
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
    


