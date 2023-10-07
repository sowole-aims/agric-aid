# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for opencv
RUN apt-get update \
    && apt-get install -y --no-install-recommends libgl1-mesa-glx libglib2.0-0 libsm6 libxrender1 libxext6 libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define an environment variable to run the app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run app.py when the container launches
CMD ["flask", "run"]


