from fastapi import FastAPI, Depends
from core.database import get_db

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "thy co nguoi yeu chua :)?"}





