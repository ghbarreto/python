from wtforms import Form, RadioField, validators
import static.scripts.functions as func

class FormGender(Form):     
    choice_switcher = RadioField(
        'Choice?',
        [validators.Required()],
        choices=[('choice1', 'Choice One'), ('choice2', 'Choice Two')], default='choice1'
    )
