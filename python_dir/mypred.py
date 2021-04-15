import re
import numpy as np
from sklearn import datasets
from joblib import load
import numpy as np
import json
import os
from flask import jsonify, render_template, request, redirect, url_for
from flask import send_file


my_model = load('./python_dir/heart_model.pkl')
UPLOAD_FOLDER='./python_dir/'

def fileread(fn):
  my_array = np.zeros(11)
  path = os.path.join(UPLOAD_FOLDER, fn)
  file = open(path, 'r')
  file2 = file.readlines()
  i = 0
  deci = '\d+' 
  for line in file2:
    line = re.findall(deci, line)   #finds ints in each string of file, then stores in into x[i]
    my_array[i:] = line
    i = i + 1
  
  file.close()
  return heartpred(my_array)


def heartpred(id):

  dummy = np.array(id)
  dummyT = dummy.reshape(1,-1)
  prediction = my_model.predict(dummyT)
  i = int(prediction[0])
  if( i == 0):
      i = 'Thou shalt not die'
  else:
      i = 'Death, thou shalt die'
  str =  [i]
  return str

