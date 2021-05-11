import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('Eyantra.pickle', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def homeform():
    if request.method == 'POST':
      fname = request.form['fname']
      cough = request.form['cough']
      fever = request.form['fever']
      sore_throat = request.form['sore_throat']
      shortness_of_breath = request.form['shortness_of_breath']
      head_ache = request.form['headache']
      test_indication = request.form['test_indication']
      print(fname,cough,fever,sore_throat,shortness_of_breath,headache,test_indication)
      prediction = model.predict([[cough,fever,sore_throat,shortness_of_breath,head_ache,test_indication]])
      result=""
      if prediction.all() == 0:
        result="Negative"
      elif prediction.all() == 1:
        result="Positive"

      return render_template('index.html',result=result,name=fname)
    
if __name__ == '__main__':
    app.run(debug = True)
