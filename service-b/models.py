from pydantic import BaseModel

class DataResponse(BaseModel):
    data: list[dict]