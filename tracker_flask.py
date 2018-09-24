from flask import Flask, render_template, url_for, flash, redirect
from forms import CallsignForm
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

############################ CONFIGURATIONS ############################
app = Flask(__name__)
## SECRET KEY
app.config['SECRET_KEY'] = '4fe839481f42a8b603a8d5aa7223997b'


############################## DATABASE SETUP ##############################
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


## TABLES
class Callsign(db.Model):
    """
    All of our callsigns that we collected from the user in the beginning
    """
    id = db.Column(db.Integer, primary_key=True)
    callsign = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f"CallsignList('{self.id}', '{self.callsign}')"


class BalloonPosition(db.Model):
    """
    Every row shall contain timestamp, callsign, latitude, longitude, altitude
    """
    timestamp = db.Column(db.Float, nullable=False, default=datetime.utcnow)

    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)
    callsign = db.Column(db.String(10), db.ForeignKey('callsign.callsign'), nullable=False, primary_key=True)

    def __repr__(self):
        return f"""
        BalloonPosition('{self.timestamp}',
                        '{self.callsign}',
                        '{self.latitude}',
                        '{self.longitude}',
                        '{self.altitude}')
                """

class GroundStation(db.Model):
    """
    Collecting all of our ground station position data
    """
    timestamp = db.Column(db.Float, nullable=False, default=datetime.utcnow, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)

    pitch = db.Column(db.Float)
    yaw = db.Column(db.Float)


    def __repr__(self):
        return f"""
        BalloonPosition('{self.timestamp}',
                        '{self.latitude}',
                        '{self.longitude}',
                        '{self.altitude}',
                        '{self.pitch}',
                        {self.yaw}')
                """

################################# ROUTES #####################################
@app.route("/")
@app.route("/status")
def home():
    return render_template('status.html', position=position)


@app.route("/collection", methods=['GET', 'POST'])
def collection():
    form = CallsignForm()
    if form.validate_on_submit():
        flash(f'Created objects for {form.Callsign.data}!', 'success')
        return redirect(url_for('status'))
    return render_template('callsigns.html', form=form)


############################## EXECUTION ###################################

if __name__ == "__main__":
    app.run(debug=True)
