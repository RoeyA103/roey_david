from fastapi import APIRouter
from pydantic import BaseModel
import json

from models import DataResponse
from clean_data import load_df, temperature_catagory, wind_status

router = APIRouter()

@router.get('/')
def root():
    return {"status": "healthy"}

@router.post('/clean')
def clean_data(data: DataResponse ):
    dataframe = load_df(data.data)
    dataframe = temperature_catagory(dataframe)
    dataframe = wind_status(dataframe)
    #results = dataframe.head(1).to_dict()
    
    return {'example results': dataframe.head(1).to_dict(orient='records')}
