# note that this is to reshape the arrays for
# the convolutional neural network
# we add the delta feature
# so there are two channels
import numpy as np
import pickle
import librosa

training_features_not_reshaped = np.load('training_feature_arr.npy',mmap_mode='r')
testing_features_not_reshaped = np.load('testing_feature_arr.npy',mmap_mode='r')

# reshape training
training_features_reshaped = np.asarray(np.array(training_features_not_reshaped)).reshape(len(training_features_not_reshaped)
                                                                           ,60,41,1)
training_features_reshaped = np.array(training_features_reshaped)
training_features_reshaped = np.concatenate((training_features_reshaped,
                          np.zeros(np.shape(training_features_reshaped))), axis = 3)
# add delta for training
for i in range(len(training_features_reshaped)):
	training_features_reshaped[i,:,:,1] = librosa.feature.delta(training_features_reshaped[i,:,:,0])

# reshape testing
testing_features_reshaped = np.asarray(np.array(testing_features_not_reshaped)).reshape(len(testing_features_not_reshaped)
                                                                           ,60,41,1)
testing_features_reshaped = np.array(testing_features_reshaped)
testing_features_reshaped = np.concatenate((testing_features_reshaped,
                          np.zeros(np.shape(testing_features_reshaped))), axis = 3)
# add delta for testing
for i in range(len(testing_features_reshaped)):
	testing_features_reshaped[i,:,:,1] = librosa.feature.delta(testing_features_reshaped[i,:,:,0])

np.save('training_feature_arr_reshaped.npy',training_features_reshaped)
np.save('testing_feature_arr_reshaped.npy',testing_features_reshaped)