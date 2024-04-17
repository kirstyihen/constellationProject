from flask import Flask, abort, redirect, url_for
from flask import render_template
from flask import Response, request,redirect, jsonify
from datetime import datetime
app = Flask(__name__)


dataLearning = []

questions = [
    {
        "id": 0,
        "question": "Orion's Belt is a(n)...",
        "image_url": "https://theplanets.org/123/2021/05/Orions-Belt-Asterism.jpg",
        "image_alt": "Picture of Orion's Belt",
        "choices": ["Constellation", "Asterism"],
        "answer_id": 1, 
    },
    {
        "id": 0,
        "question": "Ursa Minor is more commonly known as...",
        "image_url": "https://star-name-registry.com/modules/starconstpg/views/img/new/ursaminor-cons-m.jpg",
        "image_alt": "Picture of Ursa Minor",
        "choices": ["Little Dipper", "Big Dipper"],
        "answer_id": 0, 
    },
    {
        "id": 0,
        "question": "The Greeks associated _____ with the Nemean lion, the beast defeated by Zeus' son Heracles (Hercules) during the first of his twelve labors toward repenting for murdering his family.", 
        "image_url": "",
        "image_alt": "",
        "choices": ["Orion", "Leo"],
        "answer_id": 1, 
    }
]

current_question = 0
quiz_responses = []
correct_answers = ['1','0','1']
incorrect = 0
score = 3 - incorrect

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

@app.route('/quiz')
def start_quiz():
    quiz_responses.clear()
    return render_template('quizMain.html')

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

@app.route('/quiz/results')
def results_quiz():
    global quiz_responses, correct_answers, incorrect, score
    return render_template('quizResults.html', responses=quiz_responses, correct=correct_answers, incorrect=incorrect, score = score) 


@app.route('/quiz/<id>')
def display_quiz(id):
    global current_question
    id = int(id)
    if id < 0 or id >= len(questions):
        abort(403)

    current_question = id     
    return render_template('quizQuestion.html', question=questions[id])

@app.route('/quiz/add_response/<response_id>')
def add_response(response_id):
    global current_question, incorrect
    quiz_responses.append(response_id)
    if response_id != correct_answers[current_question]:
        incorrect += 1

    if current_question != len(questions) - 1:
        return redirect(url_for('display_quiz', id=current_question+1))
    else:
        return redirect(url_for('results_quiz'))
 

if __name__ == '__main__':
   app.run(debug = True, port=8001)
