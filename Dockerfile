# Use the official Python slim image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file first (to leverage Docker caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . .

# Ensure proper permissions (optional, for robust environments)
RUN chmod +x main.py

# Expose the server port
EXPOSE 8080

# Command to start the server
CMD ["python", "main.py"]
