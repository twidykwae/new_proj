from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.session import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup database
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}