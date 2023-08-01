import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
AUDIO_FILE_TARGET = os.path.join(APP_ROOT, "voice-samples")
CSV_FILE_TARGET = os.path.join(APP_ROOT, "predictions")
ALLOWED_EXTENSIONS = ["mp3"]
