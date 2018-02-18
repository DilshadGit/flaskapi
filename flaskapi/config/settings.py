from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy


app = FlaskAPI(__name__)


POSTGRES = {
	'user': 'dilmac',
	'pw': 'admin123',
	'db': 'flaskapi',
	'host': 'localhost',
	'port': '5432',
}

# access to the DB                                    username, password 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' %POSTGRES

# I got some warning on python shell ('SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
