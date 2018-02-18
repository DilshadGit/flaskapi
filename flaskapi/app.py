from flask import jsonify, request, abort 

from config.settings import app

from config.models import Profile


# app = Falsk(__name__)



profiles = [
		{
			'first_name': 'Dilshad', 
			'last_name': 'Abdulla', 
			'username': 'dilmac', 
			'email': 'dilmac@gmail.com'
		},
		{
			'first_name': 'Admin', 
			'last_name': 'SubAdmin', 
			'username': 'adminsub', 
			'email': 'admin@gmail.com'
		}
	]

@app.route('/', methods=['GET'])
def check():
	return jsonify({'signal': 'Welcome to Flast API'}, {'profiles': profiles})


@app.route('/add', methods=['POST', 'GET'])
def add():
	if request.method == 'POST':
		profile = str(request.data.get('first_name', 'last_name', 'username', 'email'))
		if contact:
			profile = Contact(
								first_name=first_name,
								last_name=last_name,
								username=username,
								email=email)
			profile.save()
			response = jsonify({
					'id': profile.id,
					'first_name': profile.first_name,
					'last_name': profile.last_name,
					'username': profile.last_name,
					'email': profile.email
				})
			response.status_code = 201
			return response

		else:
			# Get
			profiles = Contact.get_all()
			output = []

			for profile in profiles:
				obj = {
					'id': profile.id,
					'first_name': profile.first_name,
					'last_name': profile.last_name,
					'username': profile.last_name,
					'email': profile.email
				}
				output.append(obj)
			response = jsonify(output)
			response.status_code = 200
			return response



@app.route('/list/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def contact_view(id, **kwargs):
	profile = Contact.query.filter_by(id=id).first()

	if not profile:
		abort(404)

	if request.method == 'PUT':
		profile = str(request.data.get('first_name', 'last_name', 'username', 'email'))

		profile.first_name = first_name
		profile.last_name = last_name
		profile.username = username
		profile.email = email
		profile.save()

		response = jsonify({
				'id': profile.id,
				'first_name': profile.first_name,
				'last_name': profile.last_name,
				'username': profile.last_name,
				'email': profile.email
			})
		response.status_code = 200
		return response

	# if request is delete    
	elif request.method == 'DELETE':
	        profile.delete()
	        return {"message": "profile {} deleted successfully".format(profile.id)}, 200
	else:
	    # GET
	    response = jsonify({
	        'id': profile.id,
			'first_name': profile.first_name,
			'last_name': profile.last_name,
			'username': profile.last_name,
			'email': profile.email
	    })

	    response.status_code = 200
	    return response



if __name__ == '__main__':
	app.run(debug=True)
