from flask import Blueprint, Response, request
from . import APP_ROOT, ALLOWED_EXTENSIONS
from ml_models.neural_network import model_predict
from werkzeug.utils import secure_filename
from utils import allowed_file, pyaudio_featurize
import os
import pandas as pd
import shutil

# Save File REST API as Blueprint
file_api = Blueprint('file_api',__name__)


@file_api.route('/upload',methods=['GET','POST'])
def generate_csv():
    # only do this on a post request
    if request.method == 'POST':
        files = request.files.getlist("file")
        print(files)

        # this is where we will temporarily store the files
        target = os.path.join(APP_ROOT,'voice-samples')

        #if it's not already there, add it
        if not os.path.isdir(target):
            os.mkdir(target)

        # create a list of filenames
        filenames = list()

        # create a list of predictions
        predictions = list()
        if files:
            for file in files:
                if allowed_file(file.filename):
                    # save the file to the system
                    filename = secure_filename(file.filename)
                    destination = os.path.join(target,filename)
                    filenames.append(filename)
                    file.save(destination)

                    # featurize the audio file into 170 features using pyAudioAnalysis
                    features, labels = pyaudio_featurize(destination)

                    # reshape to row vector of proper shape
                    features = features.reshape(-1,1).T

                    # get model prediction
                    prediction = model_predict(features)

                    # append to list of predictions
                    predictions.append(prediction)

        # now make the dataframe
        prediction_df = pd.DataFrame({'filename':filenames,'age':predictions})

        print(prediction_df)

        # remove the directory of files
        shutil.rmtree(target)



        return Response("Got list of files",201)
    return Response("Error getting files",400)
