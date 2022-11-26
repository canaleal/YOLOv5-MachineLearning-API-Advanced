from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

import validators
from pydantic import BaseModel, validator
from typing import Optional
from fastapi import HTTPException
import subprocess

from fastapi.responses import StreamingResponse
import logging
import os
import httpx
import urllib.request

def checkIfFolderExistsAndCreateIfNot(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def deleteFileIfItExists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def deleteAllFilesInFolder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            logging.error(e)


def deleteAllFoldersInFolder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        try:
            if os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            logging.error(e)

input_folder_path = 'input/video.mp4'
runs_folder_path = 'runs/detect'

def callSubProcess(command):
    subprocess.call(command, shell=True)
    
    
 


class VideoLink(BaseModel):
    video_link: str

    @validator("video_link", pre=True, always=True)
    def check_recording_link(cls, recording_link):
        assert recording_link != '', "Recording Link cannot be empty."
        return recording_link

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


@app.get("/")
def read_root():
    return {"Geojson Utility API"}


@app.post("/geotabMachinelearning")
async def read_root(videoLink: VideoLink):
    
    modelInput = videoLink.dict()
    if validators.url(modelInput['video_link'].strip()) != True:
        raise HTTPException(
            status_code=404, detail="Video URL is not valid.")
        
    urllib.request.urlretrieve(modelInput['video_link'], input_folder_path)
    folder_length = len(next(os.walk(runs_folder_path))[1])
   
    callSubProcess('python detect.py --source "C:\\Users\\alexc\\Documents\\MachineLearning\\yolov5\\input\\video.mp4" --conf-thres 0.4')
    
    path = runs_folder_path 
    newPath = runs_folder_path
    if(folder_length == 0):
        path +=  f'{path}/exp/video.mp4v'
        newPath = f'{newPath}/exp/video-codec.mp4'
    else:
        path = f'{path}/exp{folder_length + 1}/video.mp4v'
        newPath = f'{newPath}/exp{folder_length + 1}/video-codec.mp4'
        
        
    callSubProcess(f'ffmpeg -i  {path} -map 0 -c copy {newPath}')
    
    
    
    

    def iterfile():  
        with open(newPath, mode="rb") as file_like:  
            yield from file_like  

    return StreamingResponse(iterfile(), media_type="video/mp4")
                
    