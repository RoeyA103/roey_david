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

def export_results(df: pd.DataFrame) -> list[dict]:
  return df.to_dict(orient='records')
