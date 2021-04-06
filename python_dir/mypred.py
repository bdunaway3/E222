from sklearn import datasets
from joblib import load
import numpy as np
import json

my_model = load('heart_model.pkl')

def heartpred(id):
    dummy = np.array(id)
    dummyT = dummy.reshape(1,-1)
    r = dummy.shape
    t = dummyT.shape
    r_str = json.dumps(r)
    t_str = json.dumps(t)
    prediction = my_model.predict(dummyT)
    str = [t_str, r_str]
    return str
