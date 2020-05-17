from flask import render_template, url_for, redirect
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


@app.route('/answer/<b>')
def answer(b):
    a = None
    b = g.handle_answer(answer)
    if b == 'True':
        a = g.viable_questions()
    else:
        return redirect(url_for('question'))
    return render_template('answer.html', answer=a)
