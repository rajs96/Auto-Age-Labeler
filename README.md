# Automatic Age Labeler for Voice Datasets

When creating machine learning models that incorporate voice, the age of the speaker
can bias datasets. The model might be detecting the difference in age rather
than the signal of interest. Thus, segmenting age can be used to build custom models
for speech recognition/acoustic object detection that are more accurate.

This application provides users an easy way of automatically labeling their voice
samples with the age category of the speaker. The user simply needs to attach mp3 files,
and press "upload" to download a CSV file with two columns: the filename, and the
age category.

This repository contains notebooks that detail the entire machine learning project,
including data preprocessing, exploratory data analysis, and modeling. It also
contains code for the web application, which can be run using Docker.

## Directory Structure
```bash
├── ML-modeling                      # Notebooks with Keras models/analysis
├── data-prep                        # Data Preprocessing
├── eda                              # Basic Exploratory Data Analysis
├── presentation-slides              # Presentation from NeuroLex demo day
├── result-reports                   # Result Reports from 2018
├── webapp                           # Code for Web Application
    ├── client                       # client-side code
    ├── nginx                        # Reverse proxy for routing
    ├── server                       # Backend code                
├── .gitignore                       # Only push necessary files
├── .travis.yml                      # For eventual testing, not used yet
├── Dockerrun.aws.json               # For eventual deployment, not used yet
├── README.md                        # Readme that details the repo
├── docker-compose.yml               # Necessary to run the app on user machine
```

## Running the Application with Docker
```bash
docker-compose up --build
# now the app is running on localhost:4000
```

## References
- [Jim Schwoebel's Voicebook](https://github.com/jim-schwoebel/voicebook)
- [Stephen Grider's course on Docker](https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/)

## Demo
![](gif/age-app-demo.gif)

## Further directions
If you are interested in getting involved with machine learning for audio analysis,
I recommend you check out [NeuroLex Labs](https://www.neurolex.ai/), which provides
voice computing services to clients, including machine learning. A special thanks to
Jim Schwoebel, the CEO of NeuroLex, for giving me direction and help with this project!

[Behavioral Signals](https://behavioralsignals.com/) is another interesting company
that detects emotion in voice with AI. The Director of ML at the company,
(Theodoros Giannakopoulos) developed pyAudioAnalysis, which is the library I used
to featurize the audio data.
