import pickle
from os.path import dirname, abspath, join
from keras.models import load_model


# WRITE PATHS
APP_ROOT = dirname(abspath(__file__))
AUDIO_FILE_TARGET = join(APP_ROOT, "voice-samples")
CSV_FILE_TARGET = join(APP_ROOT, "predictions")
CSV_FILE_PATH = join(CSV_FILE_TARGET, 'predictions.csv')

# MODELING
MODEL_PATH = join(APP_ROOT, "model_files")
MODEL = load_model(join(MODEL_PATH, 'model1.h5'))
FEATURE_SELECTOR = pickle.load(
    open(join(MODEL_PATH, "feature_selector.pkl"), "rb"), encoding="latin1"
)
SCALER = pickle.load(
    open(join(MODEL_PATH, "standard_scaler.pkl"), "rb"), encoding="latin1"
)
CLASS_NAMES = [
    "teens",
    "twenties",
    "thirties",
    "fourties",
    "fifties",
    "sixties",
    "seventies",
    "eighties",
]

# AUDIO FEATURES
ALL_FEATURES = [
    "zero crossing rate",
    "energy",
    "entropy of energy",
    "spectral centroid",
    "spectral spread",
    "spectral entropy",
    "spectral flux",
    "spectral rolloff",
    "mfcc1",
    "mfcc2",
    "mfcc3",
    "mfcc4",
    "mfcc5",
    "mfcc6",
    "mfcc7",
    "mfcc8",
    "mfcc9",
    "mfcc10",
    "mfcc11",
    "mfcc12",
    "mfcc13",
    "chroma1",
    "chroma2",
    "chroma3",
    "chroma4",
    "chroma5",
    "chroma6",
    "chroma7",
    "chroma8",
    "chroma9",
    "chroma10",
    "chroma11",
    "chroma12",
    "chroma deviation",
]
