#!/usr/bin/env python

import json, requests
from datetime import date
from datetime import timedelta


class Weather():
    def __init__(self, strdate, city, state):
        self.api_key = '463a6360cd5c47209a51ab56217d1a93'
        self.base_url = 'https://api.weatherbit.io/v2.0/history/daily?'
        self.city = city
        self.state = state
        self.country = 'US'
        self.amp = '&'
        self.strcity = 'city='
        self.strstate = 'state='
        self.str_start_date = 'start_date='
        self.str_end_date = 'end_date='
        self.str_key = 'key='
        self.sep = ','
        self.start_date = None
        if strdate:
            self.end_date = self.parse_date(strdate)
        else:
            self.end_date = date(2017, 9, 20)
        self.winfo = self.fetch_weather_info()

    def parse_date(self, strdate):
        l = strdate.split('-')
        dateformat = date(int(l[0]), int(l[1]), int(l[2]))
        return dateformat


    def fetch_weather_info(self):
        i = 7
        counter = 0
        weather = {"city":self.city,
                   "state":self.state,
                   "country":self.country,
                   "data":[]
                  }

        while i:
           self.start_date = self.end_date - timedelta(days=1)
           url_elements = [self.strcity, self.city, self.sep, self.state, self.amp, self.str_start_date,
                             str(self.start_date), self.amp, self.str_end_date, str(self.end_date),
                             self.amp, self.str_key, self.api_key]
           url = ''.join([self.base_url, ''.join(url_elements)])
           resp = requests.get(url, stream=True)
           resp = resp.json()
           weather['data'].append({ "datetime":resp['data'][0]['datetime'],
                                    "max_wind_spd":resp['data'][0]['max_wind_spd'],
                                    "max_temp":resp['data'][0]['max_temp'],
                                    "min_temp":resp['data'][0]['min_temp'],
                                    "clouds":resp['data'][0]['clouds'] })

           self.end_date = self.start_date
           i -= 1
           counter+=1

        return weather