from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo


class CallsignForm(FlaskForm):
    """
    class CallsignForm
    ============

    Callsign Form accepts a callsign that is confirmed by the user to be
    correct by double entering it. On submit, then it will be validated
    and checked if there are there any duplicates, if there is, then raise
    an error
    """
    callsign = StringField('Callsign', validators=[DataRequired(), Length(min=1, max=10)])
    confirm_callsign = StringField('Confirm_Callsign', validators=[DataRequired(), Length(min=1, max=10), EqualTo('callsign')])
    # You can insert boolean logic here, think about it tho
    submit = SubmitField('Submit Callsign')


    def validate_callsign(self, callsign):
        """
        validate_callsign()
        ===================

        a method that checks if the callsign that we input is equal to the callsign that is retrieved by checking the database for the callsign that we just submitted
        """
        callsign = Callsign.query.filter_by(callsign=callsign.data).first()
        if callsign:
            raise ValidationError("That callsign is already in here! Choose another!")
