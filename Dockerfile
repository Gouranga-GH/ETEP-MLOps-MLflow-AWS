# Use the official Python image as the base image, specifying version 3.8 with the "slim-buster" variant
# This variant is a minimal Debian-based image which helps to reduce the image size.
FROM python:3.8-slim-buster

# Update the package list and install the AWS CLI inside the container
# The `-y` flag automatically answers 'yes' to prompts and runs the command non-interactively.
RUN apt update -y && apt install awscli -y

# Set the working directory inside the container to `/app`
# This is where all your application files will reside and be executed.
WORKDIR /app

# Copy the contents of the current directory (where the Dockerfile is located) to the `/app` directory in the container
# This includes your application code and any other necessary files.
COPY . /app

# Install the Python packages listed in `requirements.txt`
# The `requirements.txt` file should contain all the dependencies your application needs.
RUN pip install -r requirements.txt

# Define the command to run your application using Python 3
# This will execute `app.py` when the container starts.
CMD ["python3", "app.py"]
