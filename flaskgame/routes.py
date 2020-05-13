from flask import render_template, url_for
from flaskgame import app
from game import Game

g = Game()


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    question = g.rounds
    return render_template('home.html', question=question)

@app.route('/question')
def question():
    q = None
    if g.class_type is None:
        q, v = g.generate_random_class_type_question()

    return render_template('question.html', question=q)