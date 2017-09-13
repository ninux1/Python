#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello this is my flask microservice"


if __name__ == '__main__':
    app.run(port=10000)
