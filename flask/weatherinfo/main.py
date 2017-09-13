#!/usr/bin/python

from business import Weather
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask import jsonify
import json


app = Flask('__name__')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Plz enter the date for weather info :', validators=[validators.required()])


@app.route('/', methods=['GET', 'POST'])
def main():
    form = ReusableForm(request.form)
    print(form.errors)
    obj = None
    if request.method == 'POST':
        wdate = request.form['name']
        if form.validate():
            flash('The Date you entered is ' + wdate)
            obj = Weather(str(wdate))

        else:
            flash('All the form fields are required. ')
    if obj:
        return jsonify(obj.leest)
    else:
        return render_template('form.html', form=form)


@app.route('/winfo/<string:dat>', methods=['GET'])
def get_weather_info(dat):
    ret = Weather(dat)
    return jsonify(ret.leest)


if __name__ == '__main__':
    app.run(port=7000)