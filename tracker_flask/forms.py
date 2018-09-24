from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class CallsignForm(FlaskForm):
    callsignNumber = StringField('CS_NUMBER', validators=[DataRequired()])

    callsign = StringField('Callsign', validators=[DataRequired(), Length(min=1, max=10)])

    gps_active = BooleanField('Is the GPS connection good?')
    submit = SubmitField('Start Collection!')
