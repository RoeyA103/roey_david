from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def root():
    return {"status": "healthy"}

@router.post('/clean')
def clean_data(data: str):
    return {"data recieved": data}
