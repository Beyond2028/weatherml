from flask import Flask,render_template, make_response, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/process',methods=['POST'])
def process_form():
    precipitation = request.form.get('precipitation')
    temp_max = request.form.get('temp_max')
    temp_min = request.form.get('temp_min')
    wind = request.form.get('wind')
    index()
    return render_template('hello.html')

@app.errorhandler(404)
def something_went_wrong(error):
    return render_template()