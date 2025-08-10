FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Copy project files
COPY . .

# Fix line endings for Windows compatibility
RUN sed -i 's/\r$//' entrypoint.sh

# Make entrypoint executable
RUN chmod +x entrypoint.sh

EXPOSE 8001

# Use CMD instead of ENTRYPOINT for better compatibility
CMD ["./entrypoint.sh"]