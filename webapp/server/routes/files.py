from flask import Blueprint, Response, request
from . import APP_ROOT, ALLOWED_EXTENSIONS

# Save File REST API as Blueprint
file_api = Blueprint('file_api',__name__)



@file_api.route('/upload',methods=['GET','POST'])
def generate_csv():
    if request.method == 'POST':
        files = request.files.getlist("file")
        print("we got here!")
        print(files)
        return Response("Got list of files",201)
    return Response("Error getting files",400)
