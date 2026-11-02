# Use Python base image
FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Run automated tests
CMD ["python", "-m", "pytest", "-v"]