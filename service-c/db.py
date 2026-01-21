from mysql.connector import pooling
from dotenv import load_dotenv
from os import getenv

load_dotenv()

host = getenv("SQL_HOST","localhost")
user = getenv("SQL_USER","root")
password = getenv("SQL_PASS","123")
database = getenv("DATABASE","weather_records_db")

pool = pooling.MySQLConnectionPool(
    pool_name="mypool",      
    pool_size=5,             
    pool_reset_session=True, 
    host=host,
    user=user,
    password=password,
    database=database
)

conn = pool.get_connection()
print("Connection successful:", conn.is_connected())
conn.close()