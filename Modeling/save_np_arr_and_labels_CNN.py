# this is a script to save the npy array
# as a smaller file so we can import into
# Google colab
import numpy as np
import bz2
import pickle

f_read = bz2.BZ2File('training_data_not_reshaped_small.bz2')

data_label_not_reshaped = pickle.load(f_read)

np.save('training_feature_arr.npy',data_label_not_reshaped[0])

labels = data_label_not_reshaped[1]

del data_label_not_reshaped

with open('training_labels.pickle','wb') as label_write:
	pickle.dump(labels,label_write)

