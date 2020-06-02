from flask import render_template, url_for, redirect
from flaskgame import app
from game import Game
import random

g = Game()

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/question')
def question():
    q = g.generate_question()
    if g.viable_questions:
        return render_template('question.html', question=q, data=g.animal_data,
                           r=g.rounds, query=g.query, viable_q=g.viable_questions)
    else:
        return redirect(url_for('guess', user_input=True or False))


@app.route('/answer/<user_input>')
def answer(user_input):
    if g.rounds < 10:
        if g.viable_questions:
            g.handle_answer(user_input)
            return redirect(url_for('question'))
        else:
            return redirect(url_for('guess', user_input=True or False))
    else:
        return redirect(url_for('guess', user_input=True or False))


@app.route('/guess/<user_input>')
def guess(user_input):
    question = g.guess_animal()
    if user_input == 'True':
        print('I won')

    if user_input == 'False':
        g.rounds += 1
        g.animal_data.remove(g.animal)
        question = g.guess_animal()
    return render_template('guess.html', question=question, r=g.rounds)


