import static.scripts.functions as func
from flask import Flask, redirect, render_template, request
from flask_bootstrap import Bootstrap
import helper as helper

app = Flask(__name__)
bootstrap = Bootstrap(app)

SECRET_KEY = 'json'

@app.route('/')
def index():
    form = helper.FormGender()    
    file_json = func.read_file()
    func.single_digit(file_json)
    gender = func.single_digit(file_json) 
    return render_template('index.html', json=file_json, gender=gender, form=form)

@app.route('/genders', methods=['GET', 'POST'])
def gender_choice():
    form = helper.FormGender(request.form)
    print("olaaa")
    if request.method == 'POST' and form.validate():
        gender = form.choice_switcher.data
        return print(gender)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


    