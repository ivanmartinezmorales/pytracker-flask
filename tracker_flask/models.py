from tracker_flask import db
from datetime import datetime


## TABLES BOI ##
class Callsign(db.Model):
    """
    Callsign Table
    ==============
    All of our callsigns that we collected from the user in the beginning
    """
    id = db.Column(db.Integer, primary_key=True)
    callsign = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f"CallsignList('{self.id}', '{self.callsign}')"


class BalloonPosition(db.Model):
    """
    BalloonPosition Table
    =====================
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
    Ground Station Table
    ====================
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
