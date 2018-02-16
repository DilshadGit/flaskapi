from flask import Flask, jsonify 
from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse, abort, Api, Resource
from flask import request, render_template, url_for


app = Flask(__name__)
api = Api(app)



def abort_if_contact_doesnt_exist(contact_id):
    if contact_id not in Contact:
        abort(404, message="Contact {} doesn't exist".format(contact_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


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

	# shows a single todo item and lets you delete a todo item
	def get(self, contact_id):
		abort_if_contact_doesnt_exist(contact_id)
		return Contact[contact_id]

	def delete(self, contact_id):
		abort_if_contact_doesnt_exist(contact_id)
		del Contact[contact_id]
		return '', 204

	def put(self, contact_id):
		args = parser.parse_args()
		task = {'task': args['task']}
		Contact[contact_id] = task
		return task, 201


# shows a list of all todos, and lets you POST to add new tasks
class ContactList(Resource):
    def get(self):
        return Contact

    def post(self):
        args = parser.parse_args()
        contact_id = int(max(Contact.keys()).lstrip('contact')) + 1
        contact_id = 'contact%i' % contact_id
        Contact[contact_id] = {'task': args['task']}
        return Contact[contact_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(ContactList, '/contacts')
api.add_resource(Contact, '/contacts/<contact_id>')
 

if __name__ == '__main__':
	app.run(debug=True)
