from pydantic import BaseModel, Field

class DataResponse(BaseModel):
    data: list[dict]

class Forecast(BaseModel):
    timestamp: str = Field(max_length=20)
    location_name: str = Field(max_length=100)
    country: str = Field(max_length=100)
    latitude: float
    longitude: float
    temperature: float
    wind_speed: float
    humidity: int