from flask import Flask
from flask_restplus import Api, Resource, fields
from flask_marshmallow import Marshmallow

from models import *
from settings import *

app = Flask(__name__)
app.config['SERVER_NAME'] = FLASK_SERVER_NAME
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)
ma = Marshmallow(app)

api = Api(app, version="1.0", title="NerdDinner API" ,description="NerdDinner provides an easy way for people to find and organize dinners online ")

ns = api.namespace("api", description="Dinner operations")

dinner = api.model("Dinner", {
    'DinnerID': fields.Integer(readonly=True, description='The Dinner unique identifier'),
    'Title': fields.String(required=True, description='The Dinner details'),
    'EventDate': fields.DateTime(required=True, description='The events date'),
    'Description': fields.String(required=True, description='The Dinner details'),
    'HostedBy': fields.String(required=True, description='The Dinner organizer name'),
    'ContactPhone': fields.String(required=True, description='The Dinner organizer phone number'),
    'Address': fields.String(required=True, description='The events address'),
    'Country': fields.String(required=True, description='The events country'),
    'Latitude': fields.Float(required=True, description='events place latitude'),
    'Longitude': fields.Float(required=True, description='events place longitude')

})

@ns.route("/")
class DinnerList(Resource):
    @ns.marshal_list_with(dinner)
    def get(self):
        '''List all dinners'''
        dinners = Dinner.query.all()
        return dinners

    @ns.expect(dinner)
    @ns.marshal_with(dinner, code=201)
    def post(self):
        ''' Create a new Dinner'''
        dinner = api.payload
        db.session.add(dinner)
        db.session.commit()
        return dinner, 201





if __name__ == '__main__':
    app.run(debug=True)
