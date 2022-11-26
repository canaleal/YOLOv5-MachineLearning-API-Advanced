from pydantic import BaseModel, validator
from typing import Optional


class GoogleCoordinates(BaseModel):
    user_id: str
    coord_link: str

    @validator("user_id", pre=True, always=True)
    def check_id(cls, id):
        assert id != '', "ID cannot be empty."
        return id

    @validator("coord_link", pre=True, always=True)
    def check_coordinates_link(cls, coordinates_link):
        assert coordinates_link != '', "Coordinates Link cannot be empty."
        return coordinates_link



class GoogleVideo(BaseModel):
    user_id: str
    video_link: str
   

    @validator("user_id", pre=True, always=True)
    def check_id(cls, id):
        assert id != '', "ID cannot be empty."
        return id

    @validator("video_link", pre=True, always=True)
    def check_video_link(cls, video_link):
        assert video_link != '', "Video Link cannot be empty."
        return video_link

 

class GoogleVideoCoordinates(BaseModel):
    user_id: str
    video_link: str
    coord_link: str

    @validator("user_id", pre=True, always=True)
    def check_id(cls, id):
        assert id != '', "ID cannot be empty."
        return id

    @validator("video_link", pre=True, always=True)
    def check_video_link(cls, video_link):
        assert video_link != '', "Video Link cannot be empty."
        return video_link

    @validator("coord_link", pre=True, always=True)
    def check_coordinates_link(cls, coordinates_link):
        assert coordinates_link != '', "Coordinates Link cannot be empty."
        return coordinates_link
