from wtforms import Form, RadioField, SubmitField
import static.scripts.functions as func

class FormGender(Form): 
    file = func.read_file()
    gender = func.single_digit(file)
    for i in gender: 
        choice_switcher = RadioField('label', choices=gender)
        submit = SubmitField('Submit')

    


