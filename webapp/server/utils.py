# Python script to featurize the audio
# essentially a data preprocessing script

# import required modules
import pickle
import os
import json
import numpy as np
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
from constants import ALL_FEATURES

from typing import Any


def stats(matrix: np.ndarray) -> np.ndarray:
    """Compute the mean, std dev, max, and median of matrix
    Args:
        matrix -- matrix of values
    Returns:
        output (numpy array) array of five statistical values
    """
    mean = np.mean(matrix)
    std = np.std(matrix)
    maxv = np.amax(matrix)
    minv = np.amin(matrix)
    median = np.median(matrix)

    output = np.array([mean, std, maxv, minv, median])

    return output


def convert_mono(filename: str) -> str:
    """Converts filename into mono
    Args:
        filename -- name of the file to be converted
    Returns:
        mono - file converted to mono form
    """
    mono = filename[0:-4] + "_mono.wav"
    os.system("ffmpeg -i %s -ac 1 %s" % (filename, mono))
    return mono


def pyaudio_featurize(file):
    # use pyaudioanalysis library to export features
    # exported as file[0:-4].json
    filename = file
    mono = convert_mono(filename)
    [Fs, x] = audioBasicIO.readAudioFile(mono)
    F = audioFeatureExtraction.stFeatureExtraction(
        x, Fs, 0.050 * Fs, 0.025 * Fs
    )
    os.remove(mono)

    data = {"features": F[0].tolist()}

    jsonfile = open(filename[0:-4] + ".json", "w")
    json.dump(data, jsonfile)
    jsonfile.close()
    jsonfile = file[0:-4] + ".json"
    g = json.load(open(jsonfile))
    features = np.array(g["features"])

    # now go through all the features and get statistical features for array
    new_features = []
    labels = []

    for i in range(len(features)):
        tfeature = stats(features[i])
        for j in range(len(tfeature)):
            new_features.append(tfeature[j])
            if j == 0:
                labels.append("mean " + ALL_FEATURES[i])
            elif j == 1:
                labels.append("std " + ALL_FEATURES[i])
            elif j == 2:
                labels.append("max " + ALL_FEATURES[i])
            elif j == 3:
                labels.append("min " + ALL_FEATURES[i])
            elif j == 4:
                labels.append("median " + ALL_FEATURES[i])

    new_features = np.array(new_features)
    os.remove(jsonfile)

    return new_features, labels


def allowed_file(filename: str) -> bool:
    """Function to determine if file is in the extensions allowed by the pgm.

    Args:
        filename (str) -- the name of the file
    """
    return "." in filename and filename.rsplit(".", 1)[1] in ['mp3']


def load_object(filename: str) -> Any:
    """Helper to load objects with pickle module."""
    return pickle.load(open(filename, "rb"), encoding="latin1")
