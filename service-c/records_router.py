from fastapi import APIRouter
from services import RecordsService
from schemas import LocationName


records_service = RecordsService()

router = APIRouter(prefix="/records", tags=["records"])

@router.post("/")
def save_records():
    pass

@router.get("/")
def get_records():
    pass

@router.get("/count")
def get_records_count():
    pass

@router.get("/avg-temperature")
def get_avg_temperature():
    pass