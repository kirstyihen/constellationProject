from flask import Flask
from flask import render_template
from flask import Response, request,redirect, jsonify
app = Flask(__name__)


current_id = 10
data = [
   {
    }
]

#routes
@app.route('/', methods=['GET'])
def hello_world():
    return render_template('homepage.html')

@app.route('/learning/<int:id>', methods=['GET', 'POST'])
def render_page(id):
    if id == 1:
        return render_template('leo.html')
    if id == 2:
        return render_template('orionBelt.html')
    if id == 3:
        return render_template('littleDipper.html')
    if id == 4:
        return render_template('bigDipper.html')


@app.route('/starGallery')
def star_gallery():
    return render_template('starGallery.html')

@app.route('/test')
def start_test():
    return render_template('test.html')

# AJAX FUNCTIONS

@app.route('/add', methods=['POST'])
def save_shop():
    global current_id 
    global data


 

if __name__ == '__main__':
   app.run(debug = True)
