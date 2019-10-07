# Analyzing Voice Samples to Predict Age

## The Problem

[NeuroLex Labs](https://www.neurolex.ai/) is a company that applies machine learning modeling to voice samples. They provide clients a variety of services, including dataset curation, featurization, ML modeling, and server deployment. Companies can use these services to create models for speech recognition, schizophrenia diagnosis, depression detection, and more.

Because the age of the speaker can bias voice datasets, it can often be useful to create models that automatically label voice samples with age ranges (we may not know the age of the speaker when the sample was recorded). In other words, the difference in spectral features between ages can reduce the signal of interest.

Here, in order to help solve this problem, we create a model that can predict the age range of the speaker.

## Data
We're going to use the Common Voice Dataset that was curated by Mozilla. It has a total of 200,000 samples, but only about 74,000 are labeled with age.



## Important note (as of October 2019):
This repo is being modified, and integrated into a new application, and so
it is in development at the moment. Stay tuned.
