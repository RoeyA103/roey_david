from fastapi import FastAPI

from routes import router

app = FastAPI(title="Service B data cleaner")

app.include_router(router=router)