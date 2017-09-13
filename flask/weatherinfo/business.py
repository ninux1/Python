#!/usr/bin/env python

import requests
from datetime import date
from datetime import timedelta


class Weather():
    def __init__(self, strdate):
        self.api_key = '463a6360cd5c47209a51ab56217d1a93'
        self.base_url = 'https://api.weatherbit.io/v2.0/history/daily?'
        self.city = 'Irvine'
        self.state = 'CA'
        self.amp = '&'
        self.strcity = 'city='
        self.strstate = 'state='
        self.str_start_date = 'start_date='
        self.str_end_date = 'end_date='
        self.str_key = 'key='
        self.sep = ','
        self.start_date = None
        self.end_date = self.parse_date(strdate)
        self.leest = self.fetch_weather_info()

    def parse_date(self, strdate):
        l = strdate.split('-')
        print(int(l[2]), int(l[1]), int(l[0]))
        #year = int(strdate[:-4])
        #month = int(strdate[4:-2])
        #day = int(strdate[6:])
        dateformat = date(int(l[0]), int(l[1]), int(l[2]))
        return dateformat

    def fetch_weather_info(self):
        i = 7
        urllist = []
        while i:
            self.start_date = self.end_date - timedelta(days=1)
            url_elements = [self.strcity, self.city, self.sep, self.state, self.amp, self.str_start_date,
                            str(self.start_date), self.amp, self.str_end_date, str(self.end_date),
                            self.amp, self.str_key, self.api_key]
            url = ''.join([self.base_url, ''.join(url_elements)])
            urllist.append(url)
            self.end_date = self.start_date
            i -= 1
        return urllist
