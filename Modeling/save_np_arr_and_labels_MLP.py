import numpy as np
import pandas as pd

# define function to one hot encode labels
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

# read in the csv file and put it in the dataframe
df_train = pd.read_csv('audio_training_data_cleaned.csv')

# drop any null values we may have forgotten
df_train = df_train.dropna(how='any',axis=0)

# split into X_train and y_train
X_train = df_train.drop(columns=['filename','age','Unnamed: 0']).values
y_train = list(df_train['age'])

y_train_ohe = one_hot_encode(y_train,possible_labels)

# now we need to test data against the testing set
# import testing set
df_test = pd.read_csv('audio_testing_data_cleaned.csv')
# drop any null values we may have forgotten
df_test = df_test.dropna(how='any',axis=0)

X_test = df_test.drop(columns=['filename','age','Unnamed: 0']).values
y_test = list(df_test['age'])

y_test_ohe = one_hot_encode(y_test,possible_labels)

# now save the numpy arrays to disk
np.save('training_feature_arr_MLP.npy',X_train)
np.save('testing_feature_arr_MLP.npy',X_test)
np.save('training_labels_MLP.npy',y_train_ohe)
np.save('testing_labels_MLP.npy',y_test_ohe)


