from flask import Flask,render_template, make_response, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process',methods=['POST'])
def process_form():
    precipitation = request.form.get('precipitation')
    temp_max = request.form.get('temp_max')
    temp_min = request.form.get('temp_min')
    wind = request.form.get('wind')
    index()
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html',error = error)

@app.errorhandler()
def error_handler(error):
    return render_template('error.html', error=error)