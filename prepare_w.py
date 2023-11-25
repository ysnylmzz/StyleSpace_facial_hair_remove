import pickle

import os
path = "./npy/beard/metadata"
dirs = os.listdir(path)
import numpy as np
listt  =[]
for file in dirs:

    with open(os.path.join(path,file), 'rb') as handle:
        metadata = pickle.load(handle)
    
    print(metadata.keys())

    listt.append(metadata["z"])

np.save("npy/beard/W.npy",np.asarray(listt))

    