from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.session import create_db_and_tables
from api.v1.api import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup database
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"Hello": "World"}