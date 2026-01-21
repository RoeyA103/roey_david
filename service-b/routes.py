from fastapi import APIRouter
from pydantic import BaseModel
import json
from models import DataResponse, Forecast
from clean_data import load_df, temperature_catagory, wind_status, export_results
from services import send
router = APIRouter()

@router.get('/')
def root():
    return {"status": "healthy"}

@router.post('/clean')
def clean_data(data: DataResponse ):
    for item in data.data:
        Forecast.model_validate(item)
    dataframe = load_df(data.data)
    dataframe = temperature_catagory(dataframe)
    dataframe = wind_status(dataframe)
    results = export_results(dataframe)
    first_result = results[0]
    send_status = send(results)
    return {
        'sent to service c': send_status,
        'example results': first_result
        }
