from .settings import db


class Profile(db.Model):
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

	def save(self):
	    db.session.add(self)
	    db.session.commit()

	@staticmethod
	def get_all():
	    return Profile.query.all()

	def delete(self):
	    db.session.delete(self)
	    db.session.commit()
		

	def __repr__(self):
		return '<Profile %r>'% self.username
