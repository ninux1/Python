#!/usr/bin/env python

from flask import Flask, url_for, request
import json

app = Flask(__name__)


@app.route('/')
def api_root():
    return "Welcome to Article Rest Service"


@app.route('/articles')
def api_articles():
    return "List of  " + url_for('api_articles')


@app.route('/articles/<articled>')
def api_article(articled):
    return "You are reading " + articled


@app.route('/messages', methods = ['POST'])
def api_post():
    if request.headers['Content-Type'] == 'text/html':
        return "Text is " + request.data

    elif request.headers['Content-Type'] == 'application/json, charset=utf-8':
        return request.data


    else:
        return 'Unsupported media type ' + request.headers['Content-Type']

if __name__ == '__main__':
    app.run()
