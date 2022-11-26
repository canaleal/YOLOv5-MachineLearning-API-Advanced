import requests
import re
import os
import json
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')


def save_video_to_google_drive(video_id, video_path, video_data):
    file_stats = os.stat(video_path)
    print(file_stats.st_size)
    # url = f'https://www.googleapis.com/drive/v3/files/{video_id}?uploadType=media'
    # headers = {
    #     'Authorization': f'API {API_KEY}',
    #     'Content-Type': 'video/mp4',
    #     'Content-Length': f'{file_stats.st_size}',
    # }

    # resp = requests.request(
    #     "PUT",
    #     url,
    #     headers=headers,
    #     data=video_data
    # )
    
    
    
    videoData = {
        'name':'test.mp4',
        'mimeType': "video/mp4",
        'parents': ['1dBCZHO7lh055IgjeT9u3ojGh0Bg6LE4E'],
    };
    GOOGLE_UPLOAD_URL = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=resumable'
    uploadResponseVideoPost = requests.request(
        'POST',
        url = GOOGLE_UPLOAD_URL,
        headers = {
            'Authorization': f'API {API_KEY}',
            'Content-Type': 'application/json'
        },
        data = json.dumps(videoData),
    );  

    videoLocation = uploadResponseVideoPost


    
    # resp = requests.request(
    #     "GET",
    #     'https://api.publicapis.org/entries',
    #     # headers=headers,
    #     # data=video_data
    # )
      
      
    return videoLocation
