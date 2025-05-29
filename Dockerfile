# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Streamlit-specific environment variable
ENV PYTHONUNBUFFERED=1

# Run app on port 8080 for GCP
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
