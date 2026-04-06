from flask import Flask

app = Flask(__name__)

@app.route("/process")
def process():
    print("Worker received task")
    print("Processing task...")
    return "Task completed"