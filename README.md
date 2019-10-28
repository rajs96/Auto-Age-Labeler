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
    ├── server                       # Backend code                #
├── .gitignore                       # Only push necessary files
├── .travis.yml                      # For eventual testing, not used yet
├── Dockerrun.aws.json               # For eventual deployment, not used yet
├── README.md                        # Readme that details the repo
├── docker-compose.yml               # Necessary to run the app on user machine
```
