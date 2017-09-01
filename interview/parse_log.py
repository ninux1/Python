#!/usr/bin/env python

import json


def parse_logfile(file):
    with open(file, 'r') as f:
        rf = f.read()
        f.seek(0)
        p_dict = json.load(f)
        with open('foo.txt', 'w') as wp:
            wp.write(rf)

    #p_dict = json.loads(rf)
    #print(p_dict['colors'][0]['color'])

    json_str = json.dumps(p_dict)
    print(json_str[2])

    with open('bar.json', 'w') as fp:
        json.dump(p_dict, fp)

parse_logfile('colors.json')