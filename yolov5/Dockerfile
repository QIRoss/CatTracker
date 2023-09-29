# Use the official Python image as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Install system dependencies (libgl1-mesa-glx is the missing library)
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Copy the application code into the container
COPY . .

# Install the required dependencies (if any)
RUN pip install -r requirements.txt

# Define the command to run the object detection script with the specified arguments
CMD ["python", "detect.py", "--weights", "runs/train/exp/weights/last.pt", "--img", "720", "--conf", "0.80", "--source", "http://streaming_service:5000/video_feed", "--save-crop", "--save-txt"]