import csv

from flask import Flask,render_template,request
from models import *
from settings import *

app = Flask(__name__)

app.config['SERVER_NAME'] = FLASK_SERVER_NAME
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

def main():
    f = open('Dinners.csv')
    reader = csv.reader(f)

    for Title, EventDate, Description, HostedBy, ContactPhone, Address, Country, Latitude, Longitude in reader:

        Dinner = Dinner(Title=Title,EventDate=EventDate,Description=Description,
                        HostedBy=HostedBy,ContactPhone=ContactPhone,Address=Address, Country=Country,
                        Latitude=Latitude, Longitude=Longitude)
        db.session.add(Dinner)
    
    db.session.commit()


    if __name__ == '__main__':
        with app.app_context():
            main()