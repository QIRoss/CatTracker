# Use the official Python image as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install the required dependencies
RUN pip install -r requirements.txt

# Define the command to run the Telegram bot
CMD ["python", "telegram.py"]
