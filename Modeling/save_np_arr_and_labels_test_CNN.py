# we are writing this script to save the testing features in a .npy file
# for our CNN

import librosa
import pandas as pd
import numpy as np
import pickle

def windows(data,window_size):
    start = 0
    while start < len(data):
        yield start, start + window_size
        start+=(window_size/2)

# function to extract spectrogram from a list of
# mp3 files
def extract_features_spectrogram(parent_dir,file_list,bands=60, frames=41):
    log_specgrams = []
    labels = []
    window_size = 512*(frames-1)
    for f in file_list:
        path = parent_dir+'/'+f
        sound_clip,s = librosa.load(path)
        label = f
        for (start,end) in windows(sound_clip,window_size):
            if(len(sound_clip[start:end])==window_size):
                signal = sound_clip[start:end]
                melspec = librosa.feature.melspectrogram(signal,n_mels=bands)
                logspec = librosa.amplitude_to_db(melspec)
                logspec = logspec.T.flatten()[:,np.newaxis].T
                log_specgrams.append(logspec)
                labels.append(label)
                print("Featurized {}.".format(label))
    return (log_specgrams,labels)

# first load data from csv
df_test = pd.read_csv('audio_testing_data_cleaned.csv')
df_test = df_test[['filename','age']]
l = list(df_test['filename'])
# extract log-mel spectrogram features
features_test, labels_test = extract_features_spectrogram('../Data Wrangling/cv-valid-test',
                                                l)
np.save("testing_feature_arr.npy",features_test)

with open("testing_labels.pickle",'wb') as labels_write:
    pickle.dump(labels_test,labels_write)