from flask import Flask
import os
import requests
import redis

app = Flask(__name__)

# Get environment variables
WORKER_URL = os.getenv("WORKER_URL")
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))
REDIS_CHANNEL = os.getenv("REDIS_CHANNEL")

# Create redis client for appication
def redis_client():
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

@app.route("/")
def home():
    return "App is running"

@app.route("/task")
def send_task():
    try:
        r = requests.get(WORKER_URL, timeout=5)
        return f"Worker response: {r.text}"
    except Exception as e:
        return f"Error contacting worker: {str(e)}"


@app.route("/task-redis")
def send_task_redis():
    try:
        # Get redis client connection
        client = redis_client()
        # Publish message to channel
        client.publish(REDIS_CHANNEL, "process-task")
        # Return response to user with http
        return "Task published to Redis"
    except Exception as e:
        return f"Error publishing task to Redis: {str(e)}"
