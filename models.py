from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Dinner(db.Model):
    __tablename__ = "Dinners"
    DinnerID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String, nullable=False)
    EventDate = db.Column(db.DateTime, nullable=False)
    Description = db.Column(db.String, nullable=True)
    HostedBy = db.Column(db.String, nullable=False)
    ContactPhone = db.Column(db.String, nullable=True)
    Address = db.Column(db.String, nullable=False)
    Country = db.Column(db.String, nullable=False)
    Latitude = db.Column(db.Float, nullable=False)
    Longitude = db.Column(db.Float, nullable=False)

class RSVP(db.Model):
    __tablename__ = "RSVPs"
    RsvpID = db.Column(db.Integer, primary_key=True)
    DinnerID = db.Column(db.Integer, db.ForeignKey("Dinners.DinnerID"), nullable=False)
    AttendeeName = db.Column(db.String, nullable=False)


