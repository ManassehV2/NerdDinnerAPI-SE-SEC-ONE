from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Dinner(db.Model):
    __tablename__ = "dinners"
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
    __tablename__ = "rsvps"
    RsvpID = db.Column(db.Integer, primary_key=True)
    DinnerID = db.Column(db.Integer, db.ForeignKey(
        "dinners.DinnerID"), nullable=False)
    AttendeeName = db.Column(db.String, nullable=False)
