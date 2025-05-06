from flask import Flask, request, jsonify
from tasks import add

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add_task():
    data = request.get_json()
    x = data.get("x", 0)
    y = data.get("y", 0)
    task = add.delay(x, y)
    return jsonify({"task_id": task.id}), 202
