# Use a lightweight Python image
FROM python:3.11-slim AS base

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy all backend files
COPY . .

# Expose Django port
EXPOSE 8000

# Default command (development)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
