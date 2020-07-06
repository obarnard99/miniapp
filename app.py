from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Running on %s' % request.host


if __name__ == '__main__':
    app.run()
