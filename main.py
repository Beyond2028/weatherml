from flask import Flask
from flask import render_template, make_response, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name=None)

@app.route('/process',methods=['POST'])
def process_form():
    precipitation = float(request.form.get('precipitation'))
    temp_max = float(request.form.get('temp_max'))
    temp_min = float(request.form.get('temp_min'))
    wind = float(request.form.get('wind'))
    import pickle
    with open('weather_prediction_model.pkl', 'rb') as f:
        model = pickle.load(f)
    X_new = np.array([precipitation, temp_max,temp_min,wind]).reshape(1, -1)
    weather_predict = model.predict(X_new)
    print(weather_predict)
    return render_template('result.html', prediction=str(weather_predict[0]))

@app.route('/returnToHome',methods=['POST'])
def returnToHomePage():
    return index()