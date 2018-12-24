# compress numpy array using so we can
# import into Google colab
import bz2
import numpy as np
train_feature_arr = bz2.BZ2File('training_feature_arr_reshaped.npy.bz2','w')
np.save(train_feature_arr,np.load('training_feature_arr_reshaped.npy', mmap_mode='r'))
train_feature_arr.close()