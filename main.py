from flask import Flask,render_template, make_response, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html', name=None)

@app.route('/process',methods=['POST'])
def process_form():
    precipitation = request.form.get('precipitation')
    temp_max = request.form.get('temp_max')
    temp_min = request.form.get('temp_min')
    wind = request.form.get('wind')
    return 'Form processed'+precipitation