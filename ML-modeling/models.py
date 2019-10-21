# necessary imports
from keras.layers import Dense,Dropout
from keras.models import Model,Sequential


def create_model(optimizer='adam',dropout=0.2,output_classes=8):
    """Returns a Keras classification NN that can be wrapped by sklearn

    Args:
        optimizer -- the optimizer you want to use for the NN
        dropout -- the dropout (1-keep_prob) for the NN
        ouput_classes - number of output classes in the model

    Returns:
        model -- neural network classifier
    """


    # create the model
    model = Sequential()
    model.add(Dense(128,activation='relu'))
    model.add(Dropout(dropout))
    model.add(Dense(256,activation='relu'))
    model.add(Dropout(dropout))
    model.add(Dense(256,activation='relu'))
    model.add(Dropout(dropout))
    model.add(Dense(256,activation='relu'))
    model.add(Dense(output_classes,activation='softmax'))

    # compile the model with optimizer, metrics
    model.compile(loss='categorical_crossentropy',optimizer=optimizer,
        metrics=['accuracy'])

    return model
