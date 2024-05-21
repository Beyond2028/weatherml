from flask import Flask
from flask import render_template, make_response, request

from keras.models import load_model, Sequential
import numpy as np


app = Flask(__name)

@app.route('/')
def index():
    return render_template('hello.html', name=None)

@app.route('/process',methods=['POST'])
def process_form():
    precipitation = float(request.form.get('precipitation'))
    temp_max = float(request.form.get('temp_max'))
    temp_min = float(request.form.get('temp_min'))
    wind = float(request.form.get('wind'))
    model = load_model('weather_prediction_model.h5')
    X_new = np.array([precipitation, temp_max,temp_min,wind]).reshape(1, -1)
    weather_predict = model.predict(X_new)
    return 'Weather forcast: '+str(weather_predict[0])