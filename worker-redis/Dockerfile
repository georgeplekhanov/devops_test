FROM python:3.11-slim

# Create log directory
RUN mkdir -p /var/log/worker
# Directory where application will be located inside container
WORKDIR /app

# Disable python output buffering
# Allows to show logs in real time
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN python -m pip install --no-cache-dir redis

# Copy worker script to container
COPY worker_redis.py .

# Run worker
CMD ["python", "worker_redis.py"]
