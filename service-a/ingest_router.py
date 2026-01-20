from fastapi import APIRouter
from services import IngestService ,send_to_service_b
from schemas import LocationName


ingests = IngestService()

router = APIRouter(prefix="/ingest", tags=["ingest"])

@router.post("/")
def get_records(location_name:LocationName):
    ingest = ingests.ingest_weather_for_location(location_name.model_dump()['location_name'])
    response = send_to_service_b(ingest)
    return response