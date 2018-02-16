from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


models = Flask(__name__)
api = Api(models)


POSTGRES = {
	'user': 'dilmac',
	'pw': 'admin123',
	'db': 'flaskapi',
	'host': 'localhost',
	'port': '5432',
}

# access to the DB                                    username, password 
models.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' %POSTGRES

# I got some warning on python shell ('SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and)
models.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(models)


class Contact(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(100))
	last_name = db.Column(db.String(100))
	username = db.Column(db.String(120), unique=True)
	email = db.Column(db.String(120), unique=True)


	def __init__(self, first_name, last_name, username, email):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.email = email
		

	def __repr__(self):
		return '<Contact %r>'% self.username


if __name__ == '__main__':
	models.run(debug=True)
