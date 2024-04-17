from flask import Flask
from flask import render_template
from flask import Response, request,redirect, jsonify
from datetime import datetime
app = Flask(__name__)


dataLearning = []

def log_activity(page_name):
    entry = f"{datetime.now()}: Page accessed - {page_name}"
    dataLearning.append(entry)

#routes
@app.route('/', methods=['GET'])
def hello_world():
    return render_template('homepage.html')

@app.route('/learning/<int:id>', methods=['GET', 'POST'])
def render_page(id):
    if id == 1:
        log_activity("Orion's Belt")
        return render_template('orionBelt.html')
    if id == 2:
        log_activity("Leo")
        return render_template('leo.html')
    if id == 3:
        log_activity("Big Dipper")
        return render_template('bigDipper.html')
    if id == 4:
        log_activity("Little Dipper")
        return render_template('littleDipper.html')


@app.route('/starGallery')
def star_gallery():
    return render_template('starGallery.html')

@app.route('/test')
def start_test():
    return render_template('test.html')

@app.route('/leo')
def render_leo():
    return render_template('leo.html')

@app.route('/orionBelt')
def render_orion():
    return render_template('orionBelt.html')

@app.route('/littleDipper')
def render_ld():
    return render_template('littleDipper.html')

@app.route('/bigDipper')
def render_bd():
    return render_template('bigDipper.html')

# AJAX FUNCTIONS

@app.route('/add', methods=['POST'])
def save_shop():
    global current_id 
    global data


 

if __name__ == '__main__':
   app.run(debug = True)
