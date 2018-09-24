from flask import render_template, url_for, flash, redirect
from tracker_flask import app
from tracker_flask.forms import CallsignForm
from tracker_flask.models import Callsign, BalloonPosition, GroundStation


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
