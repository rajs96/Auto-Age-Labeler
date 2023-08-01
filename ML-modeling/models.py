# necessary imports
from keras.layers import Dense, Dropout
from keras.models import Model, Sequential
from keras import optimizers


def baseline_model(output_classes=8):
    """Returns a very simple keras classification model
    """
    model = Sequential()
    model.add(Dense(20, activation="relu"))
    model.add(Dropout(0.25))
    model.add(Dense(output_classes, activation="softmax"))

    model.compile(
        loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"]
    )
    return model

    #


def create_model(dropout=0.2, learning_rate=0.01, output_classes=8):
    """Returns a Keras classification NN that can be wrapped by sklearn

    Args:
        optimizer -- the optimizer you want to use for the NN
        dropout -- the dropout (1-keep_prob) for the NN
        learning_rate -- tunable learning rate parameter for SGD
        momentum -- tunable momentum parameter for optimizer
        ouput_classes - number of output classes in the model

    Returns:
        model -- neural network classifier
    """

    # create the model
    model = Sequential()
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(dropout))
    model.add(Dense(256, activation="relu"))
    model.add(Dropout(dropout))
    model.add(Dense(256, activation="relu"))
    model.add(Dropout(dropout))
    model.add(Dense(128, activation="relu"))
    model.add(Dense(output_classes, activation="softmax"))

    model_opt = optimizers.Adam(lr=learning_rate)

    # compile the model with optimizer, metrics
    model.compile(
        loss="categorical_crossentropy", optimizer=model_opt, metrics=["accuracy"]
    )

    return model
