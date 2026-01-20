import pandas as pd

def load_df(data:list[dict]) -> pd.DataFrame:
    df = pd.read_json(data)
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
    df = pd.DataFrame(data)
    print(df.head(5))