from flask import Flask
import socket

app = Flask(__name__)

VERSION = "V1"


@app.route('/')
def home():
    return socket.gethostname() + "\n"


@app.route('/name')
def hostName():
    return socket.gethostname()


@app.route('/version')
def ip():
    return VERSION


if __name__ == '__main__':
    app.run(debug=True)
