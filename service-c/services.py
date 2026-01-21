import requests
from datetime import datetime
from dotenv import load_dotenv
from os import getenv
import json
from db import pool
from mysql.connector import Error

load_dotenv()

class RecordsService():
    @staticmethod
    def init_db():
        try:
            conn = pool.get_connection()
            cursor = conn.cursor()

            create_table_query = """
            CREATE TABLE IF NOT EXISTS weather_records (
                id INT AUTO_INCREMENT PRIMARY KEY,
                timestamp DATETIME,
                location_name VARCHAR(100),
                country VARCHAR(100),
                latitude FLOAT,
                longitude FLOAT,
                temperature FLOAT,
                wind_speed FLOAT,
                humidity INT,
                temperature_category VARCHAR(100),
                wind_category VARCHAR(100)
            );
            """

            cursor.execute(create_table_query)
            conn.commit()

            print("Table 'weather_records' created successfully.")

        except Error as e:
            print("Error while connecting to MySQL:", e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            

    @staticmethod
    def save_records(data):
        try:
            conn = pool.get_connection()
            cursor = conn.cursor()
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
        except Error as e:
            print("Error while connecting to MySQL:", e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            

    @staticmethod
    def get_records():
        try:
            conn = pool.get_connection()
            cursor = conn.cursor()
            #fiil your code here!!!----------
        except Error as e:
            print("Error while connecting to MySQL:", e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            
            
    @staticmethod
    def get_records_count():
        try:
            conn = pool.get_connection()
            cursor = conn.cursor()
            #fiil your code here!!!----------
        except Error as e:
            print("Error while connecting to MySQL:", e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            

    @staticmethod
    def get_avg_temperature():
        try:
            conn = pool.get_connection()
            cursor = conn.cursor()
            #fiil your code here!!!----------
        except Error as e:
            print("Error while connecting to MySQL:", e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            
    
    
