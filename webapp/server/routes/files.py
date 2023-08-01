import os
import pandas as pd
import shutil
from flask import Blueprint, Response, request
from werkzeug.utils import secure_filename

from ml_models.neural_network import model_predict
from utils import allowed_file, pyaudio_featurize
from constants import (
    AUDIO_FILE_TARGET,
    CSV_FILE_TARGET,
    CSV_FILE_PATH
)

# Save File REST API as Blueprint
file_api = Blueprint("file_api", __name__)


@file_api.route("/upload", methods=["GET", "POST"])
def generate_csv():
    # only do this on a post request
    if request.method == "POST":
        files = request.files.getlist("file")

        # this is where we will temporarily store the audio files
        os.mkdir(AUDIO_FILE_TARGET)

        # this is where we will temporarily store the csv file
        os.mkdir(CSV_FILE_TARGET)

        # create a list of filenames
        filenames = []

        # create a list of predictions
        predictions = []

        if files:
            for file in files:
                # if not allowed file, skip the file
                if not allowed_file(file.filename):
                    print(f"{file.filename} not in correct format")
                    continue

                # save the file to the system
                filename = secure_filename(file.filename)
                audio_file_destination = os.path.join(
                    AUDIO_FILE_TARGET, filename
                )
                filenames.append(filename)
                file.save(audio_file_destination)

                # featurize  audio file into 170 features using pyAudioAnalysis
                features, labels = pyaudio_featurize(audio_file_destination)

                # reshape to row vector of proper shape
                features = features.reshape(-1, 1).T

                # get model prediction
                prediction = model_predict(features)

                # append to list of predictions
                predictions.append(prediction)

            prediction_df = pd.DataFrame(
                {"filename": filenames, "age": predictions}
            )

            # turn df into csv file
            prediction_df.to_csv(CSV_FILE_PATH)

            # open file so we can send back as a response
            csv_file = open(CSV_FILE_PATH, "r")
            return_csv_file = csv_file.read().encode("latin-1")
            csv_file.close()

            shutil.rmtree(CSV_FILE_TARGET)
            shutil.rmtree(AUDIO_FILE_TARGET)

            # return response to download csv file
            return Response(
                response=return_csv_file,
                mimetype="text/csv",
                headers={
                    "Content-disposition": "attachment; filename=csv_filename"
                },
                status=201,
            )

        # no files
        else:
            return Response("No file uploaded", 400)

    return Response("Error getting files", 400)
