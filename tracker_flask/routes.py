from flask import render_template, url_for, flash, redirect
from tracker_flask import app, db
from tracker_flask.forms import CallsignForm
from tracker_flask.models import Callsign, BalloonPosition, GroundStation
import serial

position = {}

ser = serial.Serial("/dev/cu.usbmodem1421", 9600)
posit = ser.read(36).decode('utf-8')
posit = posit.split(',')
position['latitude'] = posit[0]
position['longitude'] = posit[1]
position['altitude'] = posit[2]

@app.route("/")
@app.route("/home")
def home():
    return render_template('status.html', position=position)


@app.route("/setup", methods=["GET", "POST"])
def setup():
    form = CallsignForm()
    if form.validate_on_submit():
        # If everything looks good, then create an instance of the form in db
        callsign = Callsign(callsign=form.callsign.data)
        db.session.add(callsign)
        db.session.commit()

        # Then tell the user that everything's okay
        flash(f'Successfully added callsign {form.callsign.data}!','success')
        return redirect(url_for('home'))
    return render_template('setup.html', title='setup callsigns', form=form)
