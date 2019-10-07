# in this script, we will do the necessary
# work to get the labels ready to plug right into
# a CNN in keras

# import necessary modules
import numpy as np
import pickle
import pandas as pd
from keras.utils import to_categorical

df_train = pd.read_csv('audio_training_data_cleaned.csv')
df_train = df_train[['filename','age']]

df_test = pd.read_csv('audio_testing_data_cleaned.csv')
df_test = df_test[['filename','age']]

with open('training_labels.pickle','rb') as ftrain:
	labels_train = pickle.load(ftrain) # note that these labels refer to the name
	# of the file

# this is our list of y_train labels
y_train = []
for label in labels_train:
	y_train.append(df_train[df_train['filename']==label]['age'].values[0])

with open('testing_labels.pickle','rb') as ftest:
	labels_test = pickle.load(ftest)

# this is our list of y_test labels
y_test = []
for label in labels_test:
	y_test.append(df_test[df_test['filename']==label]['age'].values[0])

# now we want to one hot encode the labels
# write a function to one-hot-encode

def one_hot_encode(labels,possible_labels): 
	""" One hot encode a list of labels
	@param labels: this is the list of labels to be one hot encoded
	@param possible_labels: this is the list of possible labels, 
	which is needed to properly one-hot-encode (must be numpy array)
	@return ohe_labels: numpy array of labels one hot encoded
	"""

	num_categories = len(possible_labels)
	ohe_labels = np.zeros((len(labels),num_categories))

	for i in range(len(labels)):
		j = np.where(possible_labels == labels[i])
		ohe_labels[i,j] = 1

	return ohe_labels

possible_labels = np.array(['teens','twenties','thirties','fourties',
	'fifties','sixties','seventies','eighties'])

y_train_ohe = one_hot_encode(y_train,possible_labels)
y_test_ohe = one_hot_encode(y_test,possible_labels)

# dump to a pickle file
with open('y_train_ohe.pickle','wb') as f_write:
	pickle.dump(y_train_ohe,f_write)
with open('y_test_ohe.pickle','wb') as f_write:
	pickle.dump(y_test_ohe,f_write)









