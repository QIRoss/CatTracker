# Use the official Python image as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Install system dependencies (libgl1-mesa-glx is the missing library)
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Copy the application code into the container
COPY . .

# Install the required Python dependencies
RUN pip install -r requirements.txt

# Expose the port that Flask will run on
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python", "app.py"]