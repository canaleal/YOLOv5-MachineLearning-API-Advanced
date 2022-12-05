
from ast import Pass
import logging
import src.utils.folder_util as folder_util
import src.utils.gdownload_util as gdownload_util
import src.utils.geojson_util as geojson_util

import src.service.google_drive as google_drive

import validators
import subprocess


import logging
import os
import urllib.request

def increase_stride(path, stride):
  # Get the size of the file in bytes
  file_size = os.path.getsize(path)

  # Calculate the number of times to increase the stride by 10
  num_increases = file_size // 100000000

  # Increase the stride by 10 the specified number of times
  for _ in range(num_increases):
    stride += 5

  return stride


# * Paths for project
data_folder_path = 'src/data'
video_save_path = f'{data_folder_path}/video.mp4'

# * Output save path
runs_folder_path = 'C:/Users/alexc/Documents/MachineLearning/yolov5/runs/detect'
output_folder_path = 'C:/Users/alexc/Documents/MachineLearning/yolov5/output'

def callSubProcess(command):
    subprocess.call(command, shell=True)


def get_google_video_for_processing(video_link=''):
    try:

        folder_util.checkIfFolderExistsAndCreateIfNot(data_folder_path)
        # * Download the file and load the raw data
        file_id = gdownload_util.download_drive_file(
            raw_url=video_link, save_path_url=video_save_path)
        
     

        # * Create the subprocess
        stride = increase_stride(video_save_path, 1)
        detect_python_path = 'C:/Users/alexc/Documents/MachineLearning/yolov5/detect.py'
        process = f'python {detect_python_path} --source {video_save_path} --vid-stride {stride} --conf-thres {0.4}'
        callSubProcess(process)

        # * Get the output
        path = f'{runs_folder_path}/exp/video.mp4v'
        
        newPath = f'{output_folder_path}/video-codec.mp4'
        newPathCompressed = f'{output_folder_path}/video-codec-comp.mp4'
            
            
        # * Create ffmpeg process
        callSubProcess(f'ffmpeg -y -i {path} -map 0 -c copy {newPath}')
        callSubProcess(f'ffmpeg -y -i {newPath} -vcodec  libx264  {newPathCompressed}')
        #callSubProcess(f'ffmpeg -y -i {newPathCompressed} -map 0 -c copy {newPath}')
        
          # * Delete all files (input, output)
        folder_util.deleteAllFilesInFolder(data_folder_path)
        folder_util.deleteAllFoldersInFolder(runs_folder_path)
        
        
        # * Upload to Google Drive
        print(file_id)

        # with open(newPath, "rb") as videoFile:
        #     video_data = videoFile.read()
        #     response = google_drive.save_video_to_google_drive(file_id, newPath, video_data)
        #     print(response.text)
           
        return newPathCompressed
      

    except Exception as e:
        logging.error(e)
        return e

