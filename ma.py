from flask_marshmallow import Marshmallow
from models import *

ma = Marshmallow()


class DinnerSchema(ma.Schema):
    class Meta:
        fields = ("Title", "EventDate", "Description", "HostedBy",
                  "ContactPhone", "Address", "Country", "Latitude", "Longitude")

        model = Dinner


class RSVPSchema(ma.Schema):
    class Meta:
        fields = ("RsvpID", "DinnerID", "AttendeeName")

        model = RSVP
