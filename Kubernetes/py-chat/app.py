from flask import Flask, render_template
from flask_socketio import SocketIO, send
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app)

# Route để phục vụ giao diện chat cho client
@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    with app.app_context():
        # Thực thi code cần application context
        print('Message: ' + msg)
        send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
