from flask import Blueprint, Response
from . import APP_ROOT

# Save File REST API as Blueprint
file_api = Blueprint('file_api',__name__)

# Define the allowed extensions for the file
ALLOWED_EXTENSIONS = ['mp3']

@file_api.route('/test',methods=['GET','POST'])
def test_route():
    print("we got here")
    return Response("we got here",201)
