from fastapi import APIRouter
from services import IngestService ,send_to_service_b


locations =  ["Tel Aviv", "Gaza", "Teheran", "Beirut", "Damascus"]


ingests = IngestService(locations)

router = APIRouter(prefix="/ingest", tags=["ingest"])

@router.get("/")
def get_records():
    ingest = ingests.ingest_weather_for_locations()
    send_to_service_b(ingest)
    return {"message":"The data was successfully transferred"}