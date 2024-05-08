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
        "image": "https://lovethenightsky.com/wp-content/uploads/2020/11/Ursa-Major-as-a-Great-Bear-scaled.jpg",
        "facts": [
            "The Big Dipper is an asterism of the constellation Ursa Major, the Greater Bear.",
            "The stars of the Big Dipper outline the Bear’s tail and hindquarters.",
            "As Earth spins, the Big Dipper and its sky neighbor, the Little Dipper, rotate around the North Star, also known as Polaris."
        ],
        "myth": "In Greek mythology, the constellations Ursa Major and Ursa Minor are associated with the myth of Arcas and his mother Callisto. Callisto was a nymph who had a son by Zeus and was transformed into a bear by the jealous Hera. Callisto’s son, Arcas, grew up to be a hunter and became king of Arcadia. During one of his hunts, he came across the bear and, not knowing that it was his mother, he aimed an arrow at it. Zeus prevented this by placing the mother and son into the sky as the constellations Ursa Major and Ursa Minor. Callisto is associated with Ursa Major.",
        "finding_tips": "The Big Dipper is one of the easiest star patterns to locate. It’s visible just about every clear night in the Northern Hemisphere. It has two parts, a bowl and a handle. So, look for a pattern that mimics a big dot-to-dot of a kitchen ladle!",
        "prev_id": 2,
        "next_id": 4
    },
    {
        "id": 4,
        "name": "Little Dipper",
        "image": "https://eblanchardblog.files.wordpress.com/2018/06/shutterstock_569889802.jpg",
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
        "type": "regular",
        "image_url": "https://theplanets.org/123/2021/05/Orions-Belt-Asterism.jpg",
        "image_alt": "Picture of Orion's Belt",
        "choices": ["Constellation", "Asterism"],
        "answer_id": "1", 
        "answer_image_url": "",
        "next_id": "1",
    },
    {
        "id": 1,
        "question": "Ursa Minor is more commonly known as...",
        "type": "regular",
        "image_url": "https://star-name-registry.com/modules/starconstpg/views/img/new/ursaminor-cons-m.jpg",
        "image_alt": "Picture of Ursa Minor",
        "choices": ["Little Orion", "Little Bear", "Greater Bear", "Little Leo"],
        "answer_id": "1", 
        "answer_image_url": "",
        "next_id": "2",
    },
    {
        "id": 2,
        "question": "What is this constellation called?", 
        "type": "regular",
        "image_url": "https://npr.brightspotcdn.com/dims4/default/30babd1/2147483647/strip/true/crop/4608x3456+0+0/resize/1760x1320!/format/webp/quality/90/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2Fec%2F26%2F27dd74af4285a6bee25f1bd2325f%2Fadobestock-188157504.jpeg",
        "image_alt": "Picture of constellation for quiz",
        "choices": ["Leo", "Ursa Minor", "Ursa Major", "Orion"],
        "answer_id": "0", 
        "answer_image_url": "",
        "next_id": "3",
    },
    {
        "id": 3,
        "question": "Which asterism or constellation is present in the picture above?", 
        "type": "identification",
        "image_url": "https://i.ibb.co/mhpLvps/Screenshot-2024-04-30-at-1-10-19-PM.png",
        "image_alt": "Picture of asterism for quiz",
        "choices": ["Little Dipper", "Big Dipper", "Orion's Belt", "Leo"],
        "answer_id": "2", 
        "answer_img_url": "https://i.ibb.co/cYPLxxp/Screenshot-2024-04-30-at-1-10-34-PM.png",
        "next_id": "4",
    },
    {
        "id": 4,
        "question": "The Greeks associated _____ with the Nemean lion, the beast defeated by Zeus' son Heracles (Hercules) during the first of his twelve labors toward repenting for murdering his family.", 
        "type": "regular",
        "image_url": "",
        "image_alt": "",
        "choices": ["Orion", "Leo"],
        "answer_id": "1", 
        "answer_image_url": "",
        "next_id": "5",
    },
    {
        "id": 5,
        "question": "Which asterism is present in the picture above?", 
        "type": "identification",
        "image_url": "https://i.ibb.co/PQcDMKj/Screenshot-2024-04-30-at-1-20-34-PM.png",
        "image_alt": "Picture of asterism for quiz",
        "choices": ["Little Dipper only", "Big Dipper only", "Both", "Neither"],
        "answer_id": "2", 
        "answer_img_url": "https://i.ibb.co/pZ1sbxr/Screenshot-2024-04-30-at-1-20-43-PM.png",
        "next_id": "6",
    },
    {
        "id": 6,
        "question": "In Greek mythology, the constellations _________ and _________ are associated with the myth of Arcas and his mother Callisto. Callisto was a nymph who had a son by Zeus and was transformed into a bear by the jealous Hera.", 
        "type": "regular",
        "image_url": "",
        "image_alt": "",
        "choices": ["Ursa Major & Ursa Minor", "Orion and Leo"],
        "answer_id": "0", 
        "answer_image_url": "",
        "next_id": "7",
    },
    {
        "id": 7,
        "question": "Which constellation is present in the picture above?", 
        "type": "identification",
        "image_url": "https://i.ibb.co/s5HchMc/Screenshot-2024-04-29-at-10-29-01-PM.png",
        "image_alt": "Picture of constellation for quiz",
        "choices": ["Little Dipper", "Orion", "Big Dipper", "Leo"],
        "answer_id": "3", 
        "answer_img_url": "https://i.ibb.co/LDywjHS/Screenshot-2024-04-29-at-10-38-09-PM.png",
        "next_id": "end",
    },
]
userActivity = []
current_question = 0
quiz_responses = []
score = 0

def log_activity(page_name):
    entry = f"{datetime.now()}: Page accessed - {page_name}"
    print(entry)
    userActivity.append(entry)

#routes
@app.route('/', methods=['GET'])
def hello_world():
    return render_template('homepage.html')

@app.route('/learning/<int:id>', methods=['GET', 'POST'])
def render_page(id):
    entry = next((item for item in dataLearning if item["id"] == id), None)
    if entry:
        log_activity(entry['name'])
        return render_template('constellationTemplate.html', data=entry)
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

# AJAX FUNCTIONS

@app.route('/add', methods=['POST'])
def save_shop():
    global current_id 
    global data

@app.route('/quiz/results')
def results_quiz():
    global quiz_responses, incorrect, score
    print("responses:", quiz_responses)
    return render_template('quizResults.html', responses=quiz_responses, score = score ) 


@app.route('/quiz/<id>')
def display_quiz(id):
    global current_question
    id = int(id)
    if id < 0 or id >= len(questions):
        abort(403)

    current_question = id     
    return render_template('quizQuestion.html', question=questions[id], num_questions=len(questions))

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
