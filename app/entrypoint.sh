#!/bin/bash

echo "Starting container..."
echo "Running initialization script..."
/app/init.sh
echo "Application started"

# Run gunicorn for production with 2 workers for parallel request
gunicorn --bind 0.0.0.0:5000 --workers 2 app:app
