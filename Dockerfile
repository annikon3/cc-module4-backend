# Used ChatGPT for this DockerFile, then edited the given code a little. 
# Prompt: "I have Docker Desktop installed. How do I use Docker in an existing python project?"

# COMMANDS TO BUILD AND RUN
# docker build -t my-flask-app .
# docker run -p 8080:8080 my-flask-app

# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside the container
EXPOSE 8080

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

