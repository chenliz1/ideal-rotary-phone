# Use an official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the app code
COPY app.py /app
COPY requirements.txt /app
COPY config.json /app
COPY templates /app/templates

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
