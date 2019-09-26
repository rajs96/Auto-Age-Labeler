# Getting the data ready

## Feature extraction/engineering
In order to deal with audio data, we use a library called pyAudioAnalysis (developed by Theodoros Giannakopolous, Directory of Machine Learning at Behavioral Signals). If we look at the file "pyaudio_featurize.py", we can see the script that featurizes the audio data. It extracts 34 features that it calculates at 50ms intervals throughout the audio clip: then we take the mean, standard deviation, maximum, minimum, and median of those captured features throughout the clip. This feature engineering technique, as well as the code that featurizes the data, is adopted from [Jim Schwoebel's Voicebook](https://github.com/jim-schwoebel/voicebook).

