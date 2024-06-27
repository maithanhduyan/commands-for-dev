from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # the /etc/hosts in docker containers doesn't like 127.0.0.1
    #  so use 0.0.0.0 instead.
    app.run(host="0.0.0.0")