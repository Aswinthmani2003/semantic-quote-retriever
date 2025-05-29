# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run Streamlit on port 8080 (required by Cloud Run)
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
