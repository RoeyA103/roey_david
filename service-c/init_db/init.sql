-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS weather_records_db;

USE weather_records_db;

-- Create contacts table
CREATE TABLE IF NOT EXISTS weather_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME ,
    location_name  VARCHAR(100),
    country  VARCHAR(100),
    latitude  FLOAT,
    longitude  FLOAT,
    temperature  FLOAT,
    wind_speed  FLOAT,
    humidity INT,
    temperature_category  VARCHAR(100),
    wind_category VARCHAR(100)

);

ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123';
FLUSH PRIVILEGES;


