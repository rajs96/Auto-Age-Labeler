from flask import Blueprint, Response

# Save File REST API as Blueprint
file_api = Blueprint('file_api',__name__)

@file_api.route('/test',methods=['GET'])
def test_route():
    print("we got here")
    return Response("we got here",201)
