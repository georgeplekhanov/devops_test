FROM python:3.11-slim

# Directory where application will be located inside container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy bash scripts for entrypoint and initialization
COPY entrypoint.sh /entrypoint.sh
COPY app.py init.sh .

# Make scripts executable
RUN chmod +x /entrypoint.sh /app/init.sh

# Set entrypoint script for container
ENTRYPOINT ["/entrypoint.sh"]
