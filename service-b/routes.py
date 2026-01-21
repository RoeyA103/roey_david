from fastapi import APIRouter
from pydantic import BaseModel
import json

from models import DataResponse


router = APIRouter()

@router.get('/')
def root():
    return {"status": "healthy"}

@router.post('/clean')
def clean_data(data: DataResponse ):
    return data.data
