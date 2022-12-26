from flask import Flask
import socket

app = Flask(__name__)

VERSION = "V1"


@app.route('/')
def home():
    return socket.gethostname() + VERSION + "\n"


@app.route('/test')
def hostName():
    return "ingress test" + socket.gethostname() + "\n"


@app.route('/page')
def page():
    return "page " + socket.gethostname() + "\n"


@app.route('/version')
def ip():
    return VERSION


if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
