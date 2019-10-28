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
        audio_file_target = os.path.join(APP_ROOT,'voice-samples')
        os.mkdir(audio_file_target)

        # this is where we will temporarily store the csv file
        csv_file_target = os.path.join(APP_ROOT,'predictions')
        os.mkdir(csv_file_target)

        # create a list of filenames
        filenames = list()

        # create a list of predictions
        predictions = list()

        if files:
            for file in files:
                # if not allowed file, skip the file
                if not allowed_file(file.filename):
                    print(f'{file.filename} not in correct format')
                    continue

                # save the file to the system
                filename = secure_filename(file.filename)
                audio_file_destination = os.path.join(audio_file_target,filename)
                filenames.append(filename)
                file.save(audio_file_destination)

                # featurize the audio file into 170 features using pyAudioAnalysis
                features, labels = pyaudio_featurize(audio_file_destination)

                # reshape to row vector of proper shape
                features = features.reshape(-1,1).T

                # get model prediction
                prediction = model_predict(features)

                # append to list of predictions
                predictions.append(prediction)

            prediction_df = pd.DataFrame({'filename':filenames,'age':predictions})
            print(prediction_df)
            csv_filename = 'predictions.csv'
            csv_file_path = os.path.join(csv_file_target,csv_filename)


            # turn df into csv file
            prediction_df.to_csv(csv_file_path)


            # open file so we can send back as a response
            csv_file = open(csv_file_path,'r')
            return_csv_file = csv_file.read().encode('latin-1')
            csv_file.close()

            shutil.rmtree(csv_file_target)
            shutil.rmtree(audio_file_target)

            # return response to download csv file
            return Response(response=return_csv_file,mimetype='text/csv',
                            headers={
                            'Content-disposition':'attachment; filename=csv_filename'
                            },
                            status=201)



        # no files
        else:
            return Response("No file uploaded",400)

        # now make the dataframe

        # remove the directory of files
        shutil.rmtree(target)


    return Response("Error getting files",400)
