#!/usr/bin/env python


from business import Weather
from flask import Flask, request
from json2html import *


app = Flask('__name__')


@app.route('/wapi', methods=['GET'])
def get_weather_info():

    if request.args:
       wdate = request.args.get('date')
       wcity = request.args.get('city')
       wstate = request.args.get('state')
       ret = Weather(wdate, wcity, wstate)
       if ret:
          return json2html.convert(json=ret.winfo)
       else:
          return "Date is mandatory while requesting weather info"
    else:
        return "Plz refer to the rest API guide for appropriate url args"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
