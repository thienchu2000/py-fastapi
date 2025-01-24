from typing import Union
from fastapi import FastAPI
import uvicorn
import asyncio
from routers import routers
from config.firebase import conected_firebase

app = FastAPI()


routers.routers(app)

@app.on_event("startup")
async def on_startup():
    await conected_firebase()
    print("Firebase connected successfully!")

if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
