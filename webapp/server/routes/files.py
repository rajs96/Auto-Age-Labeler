from flask import Blueprint, Response, request
from . import APP_ROOT, ALLOWED_EXTENSIONS

# Save File REST API as Blueprint
file_api = Blueprint('file_api',__name__)



@file_api.route('/upload',methods=['GET','POST'])
def generate_csv():
    # only do this on a post request
    if request.method == 'POST':
        files = request.files.getlist("file")
        print(files)

        # this is where we will temporarily store the files
        target = os.path.join(APP_ROOT,app.config['UPLOAD_FOLDER'])

        # if it's not already there
        if not os.path.isdir(target):
            os.mkdir(target)

        return Response("Got list of files",201)
    return Response("Error getting files",400)
