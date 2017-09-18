#!/usr/bin/env python


from business import Weather
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from json2html import *


app = Flask('__name__')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Plz enter the date for weather info :', validators=[validators.required()])


@app.route('/weather', methods=['GET', 'POST'])
def main():
    form = ReusableForm(request.form)
    print(form.errors)
    obj = None
    if request.method == 'POST':
        wdate = request.form['name']
        city = request.form['city']
        state = request.form['state']
        if form.validate():
            obj = Weather(str(wdate), city, state)
        else:
            flash('All the form fields are required. ')

    if obj:
        return json2html.convert(json = obj.winfo)
    else:
        return render_template('form.html', form=form)


@app.route('/wapi', methods=['GET'])
def get_weather_info():
    wdate = request.args.get('date')
    wcity = request.args.get('city')
    wstate = request.args.get('state')
    ret = Weather(wdate, wcity, wstate)
    return json2html.convert(json=ret.winfo)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
