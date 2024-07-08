from fastapi import FastAPI
import uvicorn
from workout_api.routers import api_router

app = FastAPI(title='WorkoutApi')
app.include_router(api_router)