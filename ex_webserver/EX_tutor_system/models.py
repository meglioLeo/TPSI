from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Vehicle model: stores vehicle information, including its plates, portales and timestamps.
class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True) # Primary key
    license_plate = db.Column(db.String(20), nullable=False, unique=True) # License plate number
    portal_id = db.Column(db.Integer, db.ForeignKey('portals.id'), nullable=False) # Foreign key to portals table
    timestamp_in = db.Column(db.DateTime, nullable=False) # Timestamp of entry
    timestamp_out = db.Column(db.DateTime) # Timestamp of exit (can be NULL until the vehicle exits)
    portal = db.relationship('Portal', backref=db.backref('vehicles', lazy=True)) # Relationship to Portal
    
    def __repr__(self):
        return f"<Vehicle {self.license_plate} entered at {self.timestamp_in}>"
    
# Portal model: stores information about a detection portal (location/ID).
class Portal(db.Model):
    __tablename__ = 'portals'
    id = db.Column(db.Integer, primary_key=True) # Primary key
    portal_id = db.Column(db.String(20), unique=True, nullable=False) # Portal ID (unique)
    location = db.Column(db.String(100), nullable=False) # Location of the portal (optional)
    def __repr__(self):
        return f"<Portal {self.portal_id} located at {self.location}>"