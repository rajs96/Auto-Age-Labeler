from keras.models import load_model
import pickle
import numpy as np
import os
# Load in the model using absolute path
model = load_model(os.path.abspath("model1.h5"))
# make the prediction function
model._make_predict_function()

# Load in feature selector using absolute path
feature_selector = pickle.load(open(os.path.abspath("feature_selector.pkl"),
    'rb'),encoding='latin1')

# Load in Standard scaler using absolute path
scaler = pickle.load(open(os.path.abspath("standard_scaler.pkl"),
    "rb"),encoding='latin1')

class_names = ['teens','twenties','thirties','fourties','fifties','sixties',
    'seventies','eighties']


def model_predict(input):
    """Given input array of featurized audio, returns model prediction
    Args:
        -- input (numpy array) input to put in machine learning model
    Returns:
        -- prediction (str) age category based on featurized audio
    """

    # make sure we get in a numpy matrix for the features
    assert isinstance(input,np.ndarray)
    # feature selection
    features = feature_selector.transform(features)

    # standard scale the data
    features = scaler.transform(features)

    # gets an array of the probability that the speaker belongs to a particular class
    prediction_probs = model.predict(features)

    # gets the index of the highest probability
    prediction_index = np.argmax(prediction_probs)

    # get the class label based on the index
    prediction = class_names[prediction_index]

    return prediction
