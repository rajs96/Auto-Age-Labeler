from flask import Flask, render_template,request,Response
import time
import os
from config import Development
from utils import allowed_file

app = Flask(__name__)

# Define the allowed extensions for the file
ALLOWED_EXTENSIONS = ['mp3']

# Define root path for the application
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/audiofile',methods=['POST'])
def download_csv():
    """Takes in uploaded files and creates a csv with associated
    age labels
    """
    print(request.method)
    if request.method == 'POST':


        #target = os.path.join(APP_ROOT,app.config['UPLOAD_FOLDER'])
        file = request.files['file']
        if file and allowed_file(file.filename):
            return Response("successfully got file",201)
            time.sleep(5)
        else:
            return Response("wrong file type",404)

    return Response("something went wrong",404)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
