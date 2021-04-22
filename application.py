from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_restplus import Api, Resource, fields

from settings import *
from models import *
from ma import *


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS


db.init_app(app)
ma = Marshmallow(app)

api = Api(app, version='1.0', title='NerdDinner API',
          description='A simple NerdDinner API')


dinner_schema = DinnerSchema()
dinners_schema = DinnerSchema(many=True)

rsvp_schema = RSVPSchema()
rsvps_schema = RSVPSchema(many=True)


# Model required by flask_restplus for expect
dinner = api.model("Dinner", {
    'Title': fields.String('Name of the Dinner'),
    'EventDate': fields.DateTime,
    'Description': fields.String,
    'HostedBy': fields.String,
    'ContactPhone': fields.String,
    'Address': fields.String,
    'Country': fields.String,
    'Latitude': fields.Float,
    'Longitude': fields.Float
})


@api.route('/api/dinners/<int:id>')
class dinnerResource(Resource):
    def get(self, id):
        '''
        Show a single dinner
        '''
        dinner = Dinner.query.filter_by(DinnerID=id).first()
        return dinner_schema.dump(dinner)

    @api.expect(dinner)
    @api.response(204, 'Dinner successfully updated.')
    def put(self, id):
        """
        Updates a dinner.
        """
        dinner = Dinner.query.filter_by(DinnerID=id).first()

        dinner.Title = request.json['Title']
        dinner.EventDate = request.json['EventDate']
        dinner.Description = request.json['Description']
        dinner.HostedBy = request.json['HostedBy']
        dinner.ContactPhone = request.json['ContactPhone']
        dinner.Address = request.json['Address']
        dinner.Country = request.json['Country']
        dinner.Latitude = request.json['Latitude']
        dinner.Longitude = request.json['Longitude']

        db.session.add(dinner)
        db.session.commit()

        return dinner_schema.dump(dinner)

    @api.response(204, 'Dinner successfully deleted.')
    def delete(self, id):
        """
        Deletes Dinner.
        """
        dinner = Dinner.query.filter_by(DinnerID=id).first()
        if dinner is None:
            return None, 404
        db.session.delete(dinner)
        db.session.commit()
        return None, 204


@api.route('/api/dinners')
class dinnersResource(Resource):

    def get(self):
        """
        Get all the Dinners
        """
        dinners = Dinner.query.all()
        return dinners_schema.dump(dinners)

    @api.expect(dinner)
    def post(self):
        """
        Create a new Dinner
        """
        new_dinner = Dinner()
        new_dinner.Title = request.json['Title']
        new_dinner.EventDate = request.json['EventDate']
        new_dinner.Description = request.json['Description']
        new_dinner.HostedBy = request.json['HostedBy']
        new_dinner.ContactPhone = request.json['ContactPhone']
        new_dinner.Address = request.json['Address']
        new_dinner.Country = request.json['Country']
        new_dinner.Latitude = request.json['Latitude']
        new_dinner.Longitude = request.json['Longitude']

        db.session.add(new_dinner)
        db.session.commit()

        return dinner_schema.dump(new_dinner)
