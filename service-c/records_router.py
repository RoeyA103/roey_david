from fastapi import APIRouter
from services import RecordsService

router = APIRouter(prefix="/records", tags=["records"])


@router.post("/")
def save_records(data):
    RecordsService.save_records(data)

@router.get("/")
def get_records():
    RecordsService.get_records()

@router.get("/count")
def get_records_count():
    RecordsService.get_records_count()

@router.get("/avg-temperature")
def get_avg_temperature():
    RecordsService.get_avg_temperature()