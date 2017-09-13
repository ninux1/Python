#!/usr/bin/python

from flask import Flask
from datetime import date
from business import Weather


app = Flask('__name__')


@app.route('/')
def main():
    return 'Welcome to Arcus Global Weather Service'


@app.route('/winfo/<string:dat>', methods=['GET'])
def get_weather_info(dat):
    csvobject = Weather(dat)
    return csvobject


if __name__ == '__main__':
    app.run(port=7000)