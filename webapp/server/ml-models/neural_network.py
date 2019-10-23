from keras.models import load_model
import pickle
# Load in the model using absolute path
model = load_model(os.path.abspath("./model1.h5"))
# make the prediction function
model._make_predict_function()

# Load in feature selector using absolute path
feature_selector = pickle.load(open(os.path.abspath("feature_selector.pkl"),
    'rb'),encoding='latin1')

# Load in Standard scaler using absolute path
scaler = pickle.load(open(os.path.abspath("standard_scaler.pkl"),
    "rb"),encoding='latin1')

def model_predict(filename):
