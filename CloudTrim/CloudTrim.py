from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from google_drive_downloader import GoogleDriveDownloader as gdd 
import re 
import mimetypes
import time
import os

def to_seconds(timestamp):
    """
    take timestamp hrs:min:sec
    and return the value in second
    """
    hrs,mint,sec=timestamp.split(":")
    hrs2sec = hrs*60*60
    mint2sec = mint*60
    
    return hrs2sec + mint2sec +sec


def download_from_drive(link=None,ids=None,to_save=None):
    if link:
        try:
            pattern = r"/file/[a-zA-Z]*/([a-zA-Z0-9-_]*)/?.*"
            result = re.search(pattern,link)
            file_id = result.groups()[0]
        except:
            return False
    if ids:
        file_id = ids
    gdd.download_file_from_google_drive(file_id=file_id,dest_path=to_save)

def direct_download(url,to_save):
    os.system(f"wget -O {to_save} {url}")
    return True

def trim_video(path,start,end,export_path):
    """
    path --> string :: path of video to trim.
    start --> int (seconds):: start time to trim.
    end --> int (seconds):: end time to trim.
    export_path --> string :: path to save trimmed video
    
    trim video 
    take from `path`
    trim from `start` 2 `end`
    and save to `export_path`
    """
    if mimetypes.guess_type(path)[0].startswith('video'):
        ffmpeg_extract_subclip(path, start, end, targetname=export_path)
        return True
    else:
        raise TypeError("not a video")

def HandleTrim(url,start,end,isDrive):
    start = to_seconds(start)
    end = to_seconds(end)
    name=time.time()
    init_path = f"/manual/download/{name}.mkv"
    final_path = f"/manual/trimed/{name}.mkv"
    
    if isDrive == "on":
        if "drive" in url:
            download_from_drive(link=url, to_save=init_path)
        else:
            download_from_drive(ids=url, to_save=init_path)
    else:
        direct_download(url,to_save=init_path)
        
    trim_video(init_path,start,end,final_path)
    
    os.remove(init_path)
    return final_path
