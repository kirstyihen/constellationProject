from flask import Flask, abort, redirect, url_for
from flask import render_template
from flask import Response, request,redirect, jsonify, session
from datetime import datetime
app = Flask(__name__)


dataLearning = [
    {
        "id": 1,
        "name": "Orion's Belt",
        "image": "https://cdn.mos.cms.futurecdn.net/jBaW3ZCr6XK4zM5wRaCUxc-1200-80.jpg.webp",
        "facts": [
            "Orion’s belt is an asterism of three stars within the constellation Orion, the Hunter.",
            "On the left side of the belt is the star Alnitak, which is roughly 800 light-years away. At the middle of the belt is Alnilam, which is approximately 1,300 light-years away. On the right side, about 900 light-years away, is Mintaka.",
            "All three stars are several times larger and brighter than our sun!"
        ],
        "myth": "Greek mythology says that Orion the Hunter was chasing the Pleiades (seven sisters) on Earth, and Zeus put them in the sky for safety. Orion is still chasing them there.",
        "finding_tips": "To find Orion's Belt, look for the hourglass shape of Orion and the three stars that create the narrow part of the hourglass form Orion's Belt. In late November, Orion appears to be lying on his side, with the three stars of the belt pointing upward, in the Northern Hemisphere.",
        "prev_id": 4,
        "next_id": 2
    },
    {
    "id": 2,
    "name": "Leo",
    "image": "https://arabiannightsrum.com/wp-content/uploads/2021/02/Leo-star-constellation-810x500.png",
    "facts": [
        "Leo is the 12th largest constellation in size",
        "Leo belongs to the popular Zodiac family of constellations (Aries, Gemini, etc)",
        "In English, the constellation is known as the Lion."
    ],
    "myth": "The Greeks associated Leo with the Nemean lion, the beast defeated by Zeus’ son, Heracles (Hercules), during the first of his twelve labors toward repenting for murdering his family. Ancient pioneers of science and literature wrote that the lion was placed among the constellations because it was the king of beasts.",
    "finding_tips": "First locate the Big Dipper, then follow the curve of its handle away from the dipper's bowl until you reach a bright star. This star is part of Leo's backward question mark shape, which outlines the lion's mane.",
    "prev_id": 1,
    "next_id": 3
    },

    {
        "id": 3,
        "name": "Big Dipper",
        "image": "https://blog.nameastarlive.com/wp-content/uploads/uma_pinterest_560.jpg",
        "facts": [
            "The Big Dipper is an asterism of the constellation Ursa Major, the Greater Bear.",
            "The stars of the Big Dipper outline the Bear’s tail and hindquarters.",
            "As Earth spins, the Big Dipper and its sky neighbor, the Little Dipper, rotate around the North Star, also known as Polaris."
        ],
        "myth": "In Greek mythology, the constellations Ursa Major and Ursa Minor are associated with the myth of Arcas and his mother Callisto. Callisto was a nymph who had a son by Zeus and was transformed into a bear by the jealous Hera. Callisto’s son, Arcas, grew up to be a hunter and became king of Arcadia. During one of his hunts, he came across the bear and, not knowing that it was his mother, he aimed an arrow at it. Zeus prevented this by placing the mother and son into the sky as theconstellations Ursa Major and Ursa Minor. Castillo is associated with Ursa Major.",
        "finding_tips": "The Big Dipper is one of the easiest star patterns to locate. It’s visible just about every clear night in the Northern Hemisphere. It has two parts, a bowl and a handle. So, look for a pattern that mimics a big dot-to-dot of a kitchen ladle!",
        "prev_id": 2,
        "next_id": 4
    },
    {
        "id": 4,
        "name": "Little Dipper",
        "image": "https://cdn.mos.cms.futurecdn.net/8dAkqvtHb3Y7Vcjx2N8q3g-1200-80.jpg",
        "facts": [
            "The Little Dipper is an asterism whose stars belong to the constellation Ursa Minor, “the Little Bear.”",
            "It is smaller and fainter than the Big Dipper."
        ],
        "myth": "In Greek mythology, the constellations Ursa Major and Ursa Minor are associated with the myth of Arcas and his mother Callisto. Callisto was a nymph who had a son by Zeus and was transformed into a bear by the jealous Hera. Callisto’s son, Arcas, grew up to be a hunter and became king of Arcadia. During one of his hunts, he came across the bear and, not knowing that it was his mother, he aimed an arrow at it. Zeus prevented this by placing the mother and son into the sky as the constellations Ursa Major and Ursa Minor. Arcas is associated with Ursa Minor.",
        "finding_tips": "Look for the two outer stars in the bowl of the Big Dipper. They are called Dubhe and Merak, and they’re known as The Pointers. An imaginary line drawn between them points to Polaris, the North Star. And, once you have Polaris, you can find the Little Dipper, because Polaris is at the end of the Little Dipper’s handle.",
        "prev_id": 3,
        "next_id": 1
    }
]

questions = [
    {
        "id": 0,
        "question": "Orion's Belt is a(n)...",
        "image_url": "https://theplanets.org/123/2021/05/Orions-Belt-Asterism.jpg",
        "image_alt": "Picture of Orion's Belt",
        "choices": ["Constellation", "Asterism"],
        "answer_id": "1", 
        "next_id": "1",
    },
    {
        "id": 1,
        "question": "Ursa Minor is more commonly known as...",
        "image_url": "https://star-name-registry.com/modules/starconstpg/views/img/new/ursaminor-cons-m.jpg",
        "image_alt": "Picture of Ursa Minor",
        "choices": ["Little Dipper", "Big Dipper"],
        "answer_id": "0", 
        "next_id": "2",
    },
    {
        "id": 2,
        "question": "The Greeks associated _____ with the Nemean lion, the beast defeated by Zeus' son Heracles (Hercules) during the first of his twelve labors toward repenting for murdering his family.", 
        "image_url": "",
        "image_alt": "",
        "choices": ["Orion", "Leo"],
        "answer_id": "1", 
        "next_id": "3",
    }
    # {
    #     "id": 3,
    #     "question": "What is this constellation called?", 
    #     "image_url": "https://npr.brightspotcdn.com/dims4/default/30babd1/2147483647/strip/true/crop/4608x3456+0+0/resize/1760x1320!/format/webp/quality/90/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2Fec%2F26%2F27dd74af4285a6bee25f1bd2325f%2Fadobestock-188157504.jpeg",
    #     "image_alt": "Picture of constellation for quiz",
    #     "choices": ["Leo", "Ursa Minor"],
    #     "answer_id": "0", 
    #     "next_id": "4",
    # },
    # {
    #     "id": 4,
    #     "question": "What are the names of these asterisms?", 
    #     "image_url": "https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/msnbc/Components/Photos/071012/071012_dippers_vmed_10a.jpg",
    #     "image_alt": "Picture of asterisms for quiz",
    #     "choices": ["Leo & Little Dipper", "Big Dipper & Little Dipper"],
    #     "answer_id": "1", 
    #     "next_id": "5",
    # },
    # {
    #     "id": 5,
    #     "question": "What is this asterism called?", 
    #     "image_url": "https://itsreleased.com/wp-content/uploads/2023/08/Orions-Belt-Asterism.jpg",
    #     "image_alt": "Picture of asterism for quiz",
    #     "choices": ["Orion's Belt", "Little Dipper"],
    #     "answer_id": "1", 
    #     "next_id": "6",
    # },
    # {
    #     "id": 6,
    #     "question": "In Greek mythology, the constellations _________ and _________ are associated with the myth of Arcas and his mother Callisto. Callisto was a nymph who had a son by Zeus and was transformed into a bear by the jealous Hera.", 
    #     "image_url": "",
    #     "image_alt": "",
    #     "choices": ["Ursa Major & Ursa Minor", "Big Dipper & Little Dipper"],
    #     "answer_id": "0", 
    #     "next_id": "7",
    # },
    # {
    #     "id": 7,
    #     "question": "What is the name of this constellation?", 
    #     "image_url": "https://theplanets.org/123/2021/05/Orions-Belt-Asterism.jpg",
    #     "image_alt": "Picture of constellation for quiz",
    #     "choices": ["Orion", "Ursa Major"],
    #     "answer_id": "0", 
    #     "next_id": "8",
    # },
    # {
    #     "id": 8,
    #     "question": "What is the is one of the easiest star patterns to locate?", 
    #     "image_url": "",
    #     "image_alt": "",
    #     "choices": ["Orion's Belt", "Big Dipper"],
    #     "answer_id": "1", 
    #     "next_id": "end",
    # }
]

current_question = 0
quiz_responses = []
score = 0

def log_activity(page_name):
    entry = f"{datetime.now()}: Page accessed - {page_name}"
    dataLearning.append(entry)

#routes
@app.route('/', methods=['GET'])
def hello_world():
    return render_template('homepage.html')

@app.route('/learning/<int:id>', methods=['GET', 'POST'])
def render_page(id):
    entry = next((item for item in dataLearning if item["id"] == id), None)
    if entry:
        log_activity(entry['name'])
        return render_template('orionBelt.html', data=entry)
    else:
        return "Page not found", 404


@app.route('/starGallery')
def star_gallery():
    return render_template('starGallery.html')

@app.route('/quiz')
def start_quiz():
    global quiz_responses, score
    quiz_responses.clear()
    score = 0
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
    global quiz_responses, incorrect, score
    print("responses:", quiz_responses)
    return render_template('quizResults.html', responses=quiz_responses, score = score) 


@app.route('/quiz/<id>')
def display_quiz(id):
    global current_question
    id = int(id)
    if id < 0 or id >= len(questions):
        abort(403)

    current_question = id     
    return render_template('quizQuestion.html', question=questions[id])

@app.route('/quiz/log_response/<response_id>')
def add_response(response_id):
    global current_question, score
    # print("abt to log:", response_id)
    if response_id == questions[current_question]["answer_id"]:
        quiz_responses.append((response_id, True))
        score += 1
    else:
        quiz_responses.append((response_id, False))

    if current_question != len(questions) - 1:
        return redirect(url_for('display_quiz', id=current_question+1))
    else:
        return redirect(url_for('results_quiz'))
 

if __name__ == '__main__':
   app.run(debug = True, port=8001)
