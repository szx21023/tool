from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # 允許跨域

@socketio.on("connect")
def handle_connect():
    print("有客戶端連接了！")

@socketio.on("message")
def handle_message(msg):
    print(f"收到訊息: {msg}")
    send(f"Server received: {msg}", broadcast=True)  # 廣播訊息

@socketio.on("disconnect")
def handle_disconnect():
    print("客戶端已斷線")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)

