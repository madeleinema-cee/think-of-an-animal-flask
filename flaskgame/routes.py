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
    q = g.generate_question()
    return render_template('question.html', question=q, data=g.animal_data, r=g.rounds, query=g.query)


@app.route('/answer/<user_input>')
def answer(user_input):
    g.handle_answer(user_input)
    return redirect(url_for('question'))

