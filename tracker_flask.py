from flask import Flask, render_template, url_for, flash, redirect
from forms import CallsignForm
from flask_sqlalchemy import SQLAlchemy

## flask application configurations
app = Flask(__name__)

app.config['SECRET_KEY'] = '4fe839481f42a8b603a8d5aa7223997b'

# Setting up our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Callsigns(db.Model):
    """
    All of our callsigns that we collected from the user in the beginning
    """
    id = db.Column(db.Integer, primary_key=True)
    callsign = db.Column(db.String(10), unique=True, nullable=False)

class Position(db.Model):
    """
    Every row shall contain timestamp, callsign, latitude, longitude, altitude
    """
    timestamp = db.Column(db.Float, nullable=False)
    callsign = db.Column(db.String(10), unique=True, nullable=False, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)

class GroundStation(db.Model):
    """
    Collecting all of our ground station position data
    """
    timestamp = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)
    
    pitch = db.Column(db.Float)
    yaw = db.Column(db.Float)



position = [
    {
        'latitude': '0',
        'longitude': '0',
        'timestamp': '0',
        'callsign': '0',
    },
    {
        'latitude': '1',
        'longitude': '1',
        'timestamp': '1',
        'callsign': '1',
    }
]

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




if __name__ == "__main__":
    app.run(debug=True)
