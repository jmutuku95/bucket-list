'''app routes'''
from flask import request, jsonify, abort, make_response
from app.models import Bucketlist, User
from app import app


@app.route('/bucketlists/', methods=['POST', 'GET'])
def bucketlists():
    '''create bucketlist and get all bucketlists'''
    # Get the access token from the header
    auth_header = request.headers.get('Authorization')
    access_token = auth_header.split(" ")[1]

    if access_token:
        # Attempt to decode the token and get the User ID
        user_id = User.decode_token(access_token)
        if not isinstance(user_id, str):
            # Go ahead and handle the request, the user is authenticated

            if request.method == "POST":
                name = str(request.data.get('name', ''))
                if name:
                    bucketlist = Bucketlist(name=name, created_by=user_id)
                    bucketlist.save()
                    response = jsonify({
                        'id': bucketlist.id,
                        'name': bucketlist.name,
                        'date_created': bucketlist.date_created,
                        'date_modified': bucketlist.date_modified,
                        'created_by': user_id
                       })

                    return make_response(response), 201
            else:
                # GET all the bucketlists created by this user
                bucketlists = Bucketlist.query.filter_by(created_by=user_id)
                results = []

                for bucketlist in bucketlists:
                    obj = {
                        'id': bucketlist.id,
                        'name': bucketlist.name,
                        'date_created': bucketlist.date_created,
                        'date_modified': bucketlist.date_modified,
                        'created_by': bucketlist.created_by
                    }
                    results.append(obj)

                return make_response(jsonify(results)), 200
        else:
            # user is not legit, so the payload is an error message
            message = user_id
            response = {
                'message': message
                }
            return make_response(jsonify(response)), 401


@app.route('/bucketlists/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def bucketlist_manipulation(id, **kwargs):
    '''Retrieve bucketlist using it's id, edit bucketlist and delete
    bucketlist'''
    # get the access token from the authorization header
    auth_header = request.headers.get('Authorization')
    access_token = auth_header.split(" ")[1]

    if access_token:
        # Get the user id related to this access token
        user_id = User.decode_token(access_token)

        if not isinstance(user_id, str):
            # If the id is not a string(error), we have a user id
            # Get the bucketlist with the id specified from the URL (<int:id>)
            bucketlist = Bucketlist.query.filter_by(id=id).first()
            if not bucketlist:
                # There is no bucketlist with this ID for this User, so
                # Raise an HTTPException with a 404 not found status code
                abort(404)

            if request.method == "DELETE":
                # delete the bucketlist using our delete method
                bucketlist.delete()
                return {
                    "message": "bucketlist {} deleted".format(bucketlist.id)
                }, 200

            elif request.method == 'PUT':
                # Obtain the new name of the bucketlist from the request data
                name = str(request.data.get('name', ''))

                bucketlist.name = name
                bucketlist.save()

                response = {
                    'id': bucketlist.id,
                    'name': bucketlist.name,
                    'date_created': bucketlist.date_created,
                    'date_modified': bucketlist.date_modified,
                    'created_by': bucketlist.created_by
                    }
                return make_response(jsonify(response)), 200
            else:
                # Handle GET request, sending back the bucketlist to the user
                response = {
                    'id': bucketlist.id,
                    'name': bucketlist.name,
                    'date_created': bucketlist.date_created,
                    'date_modified': bucketlist.date_modified,
                    'created_by': bucketlist.created_by
                    }
                return make_response(jsonify(response)), 200
        else:
            # user is not legit, so the payload is an error message
            message = user_id
            response = {
                'message': message
                }
            # return an error response, telling the user he is Unauthorized
            return make_response(jsonify(response)), 401