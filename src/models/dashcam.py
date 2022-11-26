from pydantic import BaseModel, validator
from typing import Optional


class DashcamVideo(BaseModel):
    video_link: str

    @validator("video_link", pre=True, always=True)
    def check_recording_link(cls, recording_link):
        assert recording_link != '', "Recording Link cannot be empty."
        return recording_link