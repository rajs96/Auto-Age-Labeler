import numpy as np
from constants import MODEL, FEATURE_SELECTOR, SCALER, CLASS_NAMES


def model_predict(input: np.ndarray):
    """Given input array of featurized audio, returns model prediction
    Args:
        -- input (numpy array) input to put in machine learning model
    Returns:
        -- prediction (str) age category based on featurized audio
    """

    # make sure we get in a numpy matrix for the features
    assert isinstance(input, np.ndarray)
    # feature selection
    features = FEATURE_SELECTOR.transform(input)

    # standard scale the data
    features = SCALER.transform(features)

    # gets an array of the probability that the speaker
    # belongs to a particular class
    prediction_probs = MODEL.predict(features)

    # gets the index of the highest probability
    prediction_index = np.argmax(prediction_probs)

    # get the class label based on the index
    prediction = CLASS_NAMES[prediction_index]

    return prediction
