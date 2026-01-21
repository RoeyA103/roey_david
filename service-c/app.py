from fastapi import FastAPI
import uvicorn
from records_router import router
from dotenv import load_dotenv
from os import getenv
from services import RecordsService

load_dotenv()

host = getenv("SERVICE_HOST","localhost")
port = int(getenv("SERVICE_PORT",8001))

app = FastAPI()

@app.lifespan()
def init_db():
    RecordsService.init_db()

@app.get("/")
def root():
    return {"message":"runnig"}

app.include_router(router)

if __name__=="__main__":
    uvicorn.run("app:app",host=host,port=port,reload=True)