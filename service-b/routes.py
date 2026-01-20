from fastapi import APIRouter
from pydantic import BaseModel
import json

from models import DataResponse
from clean_data import load_df

router = APIRouter()

@router.get('/')
def root():
    return {"status": "healthy"}

@router.post('/clean')
def clean_data(data: DataResponse ):
    dataframe = load_df(json.dumps(data.data))
    return json.dumps(data.data)
