# Getting the data ready

## Feature extraction/engineering
In order to deal with audio data, we use a library called pyAudioAnalysis (developed by Theodoros Giannakopolous, Directory of Machine Learning at Behavioral Signals). If we look at the file "pyaudio_featurize.py", we can see the script that featurizes the audio data. It extracts 34 features that it calculates at 50ms intervals throughout the audio clip: then we take the mean, standard deviation, maximum, minimum, and median of those captured features throughout the clip. This feature engineering technique, as well as the code that featurizes the data, is adopted from [Jim Schwoebel's Voicebook](https://github.com/jim-schwoebel/voicebook).

## Audio features
There are a variety of spectral features that can be extracted from audio, which are mostly related to frequency and energy of the wave. Detailed descriptions of some of the features can be found [here](https://github.com/jim-schwoebel/voicebook/tree/master/chapter_3_featurization).

## Dealing with outliers
Since there are over 74,000 samples, and over 170 features, it would be difficult to find an efficient way to eliminate outliers. We will be using a deep neural network (reasons are discussed later), whose nonlinear activations **can make it easier to deal with outliers**, especially with a lot of data (although this isn't always the case).

## Large amount of features
We take five statistical measures of 34 audio features, which leaves us with 170 features. In the modeling folder, we'll discuss and test different ways of reducing dimensionality.
