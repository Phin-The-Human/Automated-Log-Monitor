# Base image
FROM python:3.9-slim

# Set the working directory in the container 
WORKDIR /app

# Copy the application files into the container
COPY src/ ./src/
COPY logs/ ./logs/
COPY requirements.txt ./
COPY .env ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Expose the port your application uses
EXPOSE 8080

# Define the command to run your application
CMD ["python", "src/main.py"]