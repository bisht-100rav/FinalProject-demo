# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 23:42:32 2022

@author: Saurav
"""
# -*- coding: utf-8 -*-

import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template
import pandas as pd

app=Flask(__name__)


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = classifier.predict(final_features)
    # kama, rosa, canadian
    if prediction == 0:
        prediction = 'Kama'
    elif prediction == 1:
        prediction = 'Rosa'
    else:
        prediction = 'Canadian'
    return render_template('index.html', prediction_text='The wheat belongs to category {}'.format(prediction))
    
if __name__=='__main__':
    app.run()