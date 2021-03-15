import json
import static.scripts.functions as func
from flask import Flask, redirect, render_template, request
from flask_bootstrap import Bootstrap
import helper as h

app = Flask(__name__)
bootstrap = Bootstrap(app)

SECRET_KEY = 'json'

@app.route('/')
def index():
    form = h.FormGender()
    txt = "static/scripts/MOCK_DATA.json"
    with open(txt) as text:
        v = json.load(text)
        func.single_digit(v)
        gender = func.single_digit(v) 
    return render_template('index.html', json=v, gender=gender, form=form)

@app.route('/genders', methods=['GET', 'POST'])
def gender_choice():
    for i in request.form:
        print(i)
        # return render_template('genders.html')


if __name__ == '__main__':
    app.run(debug=True)


    