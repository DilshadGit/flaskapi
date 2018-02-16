from flask import Flask, request, jsonify
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


# create empty dic
contacts = [
		{
			'full_name': 'Dilshad Abdulla', 
			'address': 'Ursula Gould Way', 
			'city': 'London', 
			'postcode': 'E14 7FX'
		},
		{
			'full_name': 'Tom David', 
			'address': '12 Londoan Road', 
			'city': 'Cambridge', 
			'postcode': 'CM1 3AA'
		}
	]

# this function check if the server is running and works
@app.route('/', methods=['GET'])
def check():
	return jsonify({'signal': 'It work!'})

# display all (list) of contact  
@app.route('/contacts', methods=['GET'])
def show_list():
	return jsonify({'contacts': contacts})


# display one user detail address
@app.route('/contact/<string:city>', methods=['GET'])
def show_detail(city):
	contact_list = [contact for contact in contacts if contact['city'] == city]
	return jsonify({'contact': contact_list[0]})

# create or add new contact detail
@app.route('/contact', methods=['POST'])
def add_contact():
	contact = {
		'full_name': request.json['full_name'], 
		'address': request.json['address'],
		'city': request.json['city'],
		'postcode': request.json['postcode']
	}
	contacts.append(contact)
	return jsonify({'contacts': contacts})

@app.route('/contact/<string:full_name>', methods=['PUT'])
def update(full_name):
	contacts = [contact for contact in contacts if contact['full_name'] == full_name]
	conacts[0]['full_name'] = request.json['full_name']
	conacts[1]['address'] = request.json['address']
	conacts[2]['city'] = request.json['city']
	conacts[3]['postcode'] = request.json['postcode']
	return jsonify({'contact': contacts[0], 'contacts': contact[1], 'contacts': contact[2], 'contacts': contact[3]})


if __name__ == '__main__':
	app.run(debug=True, port=8001)
