import logging
import os
import redis

# Get environment variables
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))
REDIS_CHANNEL = os.getenv("REDIS_CHANNEL")
# Log file location
LOG_FILE = "/var/log/worker/worker-redis.log"

# Configure logging with stdout and file writing
logging.basicConfig(
    # Set log level to INFO
    level=logging.INFO,
    # Set log format to message only
    format="%(message)s",
    # Add file and stream handlers
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(),
    ],
)

# Create redis client
client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
# Create pubsub connection
pubsub = client.pubsub()
# Subscribe to channel for messages
pubsub.subscribe(REDIS_CHANNEL)

# Listen for messages
for message in pubsub.listen():
    # Check type of message
    if message["type"] == "message":
        logging.info("Worker received task")
        logging.info("Processing task...")
