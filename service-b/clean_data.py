import pandas as pd
import numpy as np

def load_df(data:list[dict]) -> pd.DataFrame:
  df = pd.DataFrame(data)
  return df

def temperature_catagory(df: pd.DataFrame) -> pd.DataFrame:
  df['temperature_catagory'] = pd.cut(
    df["temperature"],
    bins=[-np.inf,18,25,np.inf],
    labels=["cold","moderate","hot"]
  )
  return df

def wind_status(df: pd.DataFrame) -> pd.DataFrame:
  df['wind_status'] = pd.cut(
    df["wind_speed"],
    bins=[0,10,np.inf],
    labels=["calm","windy"]
  )
  
  return df

if __name__ == "__main__":
  data = [
{
  "timestamp": "2026-01-19 00:00:00",
  "location_name": "Tel Aviv",
  "country": "Israel",
  "latitude": 32.08088,
  "longitude": 34.78057,
  "temperature": 12.8,
  "wind_speed": 3.1,
  "humidity": 92
},
{
  "timestamp": "2026-01-19 01:00:00",
  "location_name": "Tel Aviv",
  "country": "Israel",
  "latitude": 32.08088,
  "longitude": 34.78057,
  "temperature": 12.8,
  "wind_speed": 4.1,
  "humidity": 90
},
{
  "timestamp": "2026-01-19 02:00:00",
  "location_name": "Tel Aviv",
  "country": "Israel",
  "latitude": 32.08088,
  "longitude": 34.78057,
  "temperature": 12.8,
  "wind_speed": 5,
  "humidity": 91
},
{
  "timestamp": "2026-01-19 03:00:00",
  "location_name": "Tel Aviv",
  "country": "Israel",
  "latitude": 32.08088,
  "longitude": 34.78057,
  "temperature": 12.3,
  "wind_speed": 4.9,
  "humidity": 91
},
{
  "timestamp": "2026-01-19 04:00:00",
  "location_name": "Tel Aviv",
  "country": "Israel",
  "latitude": 32.08088,
  "longitude": 34.78057,
  "temperature": 11.9,
  "wind_speed": 4.6,
  "humidity": 95
}]
  df = load_df(data)
  df = temperature_catagory(df)
  df = wind_status(df)
  print(df[['temperature_catagory','wind_status']].head(5))