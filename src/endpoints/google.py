
from fastapi import HTTPException
from fastapi import APIRouter
from src.models.google import GoogleCoordinates, GoogleVideoCoordinates, GoogleVideo
from src.utils.folder_util import checkIfFolderExistsAndCreateIfNot, deleteFileIfItExists, deleteAllFilesInFolder, deleteAllFoldersInFolder
import validators
import src.utils.get_video_data as get_video_data
import src.utils.gdownload_util as gdownload
from fastapi.responses import StreamingResponse

router = APIRouter(
    prefix="/google",
    tags=["Google Geojson"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_root():
    return {"Google Endpoint"}



@router.post("/machinelearning")
async def read_root(googleVideo: GoogleVideo):
    modelInput = googleVideo.dict()
    if validators.url(modelInput['video_link'].strip()) != True:
        raise HTTPException(
            status_code=404, detail="Video URL is not valid.")
   
   
   
    newPath = get_video_data.get_google_video_for_processing( modelInput['video_link'])
    
    def iterfile():  
        with open(newPath, mode="rb") as file_like:  
            yield from file_like  

    return StreamingResponse(iterfile(), media_type="video/mp4")
