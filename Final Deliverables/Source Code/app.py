import numpy as np
import pickle
import sklearn
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
model = pickle.load(open('heart.pkl', 'rb')) 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/back')
def back():
    return render_template('index.html')
@app.route('/predict', methods =['GET', 'POST'])
def predict():
  if request.method == 'POST':
    features = [float(i) for i in request.form.values()]
    array_features = [np.array(features)]
    prediction = model.predict(array_features)
    output = prediction
    print(output)
    result=""
    tip1=""
    tip2=''
    tip3=""
    if output == 1:
        result = "You are not likely to have heart disease!"
        tip1=" Have a great day!"
        tip2=" "
        tip3=" "
        final=tip1+tip2+tip3
    else:
        
        result="Hey there! You are likely to have heart disease "
        tip1="Eat a heart-healthy diet, "
        tip2="Maintain a healthy weight and "
        tip3="Get good quality sleep"
        final=tip1+tip2+tip3
    return render_template("result.html",result=result,tip=final)
if __name__ == '__main__':
   app.run(debug=True)

   