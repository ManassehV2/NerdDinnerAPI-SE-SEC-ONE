# Flask settings
FLASK_SERVER_NAME = 'localhost:8888'
FLASK_DEBUG = True  # Do not use debug mode in production

# SQLAlchemy settings
#SQLALCHEMY_DATABASE_URI = 'postgresql://xtdkkbutqwhxvv:d3938c8668b8307b5e6be45177a60e482ddb79e6c23deaa34231a63570940e80@ec2-34-247-118-233.eu-west-1.compute.amazonaws.com:5432/d19t4vr4el5ht4'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password01@localhost:5432/nerddinnerdb'
SQLALCHEMY_TRACK_MODIFICATIONS = False
