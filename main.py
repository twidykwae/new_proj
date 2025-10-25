from fastapi import FastAPI
from db.session import create_db_and_tables

async def lifespan(app: FastAPI):
    print("Database starting")
    create_db_and_tables()
    print("Database ready")
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}