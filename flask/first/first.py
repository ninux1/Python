#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)


@app.route('/')
def task_structure():
    return "Task Server works here"

if __name__ == '__main__':
    app.run(port=5005)