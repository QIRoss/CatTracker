import os
import glob

def choose_picture():
    # Define the base directory
    base_dir = "yolov5/runs/detect/"

    # Get a list of all subdirectories in the base directory
    subdirectories = [d for d in glob.glob(os.path.join(base_dir, '*')) if os.path.isdir(d)]

    # Find the most recent subdirectory
    most_recent_folder = max(subdirectories, key=os.path.getmtime, default=None)

    if most_recent_folder is not None:
        # Find the most recent 'video_feedY.jpg' file in the most recent folder
        video_files = glob.glob(os.path.join(most_recent_folder, 'prints/cat', 'image*.jpg'))
        
        most_recent_video = max(video_files, key=os.path.getmtime, default=None)

        # print("Most recent folder:", most_recent_folder)
        # print("Most recent 'video_feedY.jpg' file:", most_recent_video)
    else:
        # print("No folders found in the base directory.")
        1

    return most_recent_video