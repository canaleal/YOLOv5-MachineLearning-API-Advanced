from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from src.routes.api import router as api_router

app = FastAPI(
    title="Custom YOLOV5 Machine Learning API",
    description="""Obtain object value out of image
    and return image and json result""",
    version="0.0.2",
)

origins = [
    "http://localhost",
    "http://localhost:8000",
     "http://localhost:8080",
    "https://amdcapstone.netlify.app/",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"Geojson Utility API"}
