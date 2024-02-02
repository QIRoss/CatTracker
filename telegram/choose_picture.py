import os
import glob

def choose_picture():
    base_dir = "../yolov5/runs/detect/"

    subdirectories = [d for d in glob.glob(os.path.join(base_dir, '*')) if os.path.isdir(d)]

    most_recent_folder = max(subdirectories, key=os.path.getmtime, default=None)

    if most_recent_folder is not None:
        video_files = glob.glob(os.path.join(most_recent_folder, 'prints/cat', '*.jpg'))

        most_recent_video = max(video_files, key=os.path.getmtime, default=None)

        label_files = glob.glob(os.path.join(most_recent_folder, 'labels', '*.txt'))
        most_recent_label = max(label_files, key=os.path.getmtime, default=None)

        # print("Most recent folder:", most_recent_folder)
        # print("Most recent 'video_feedY.jpg' file:", most_recent_video)
    else:
        # print("No folders found in the base directory.")
        1

    return most_recent_video, most_recent_label