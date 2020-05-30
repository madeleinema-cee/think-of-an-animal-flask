from flask import render_template, url_for, redirect
from flaskgame import app
from game import Game

g = Game()


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/question')
def question():
    g.generate_question()
    return render_template('question.html', question=g.question)


@app.route('/answer/<b>')
def answer(b):
    # b = g.handle_answer(b)
    # if b == 'True':
    #     return 'True', redirect(url_for('question'))
    # else:
    #     return redirect(url_for('question'))
    return render_template('answer.html')

