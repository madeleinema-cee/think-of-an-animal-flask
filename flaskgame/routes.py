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
    question_key = g.main()
    return render_template('question.html', question=question_key)


@app.route('/answer/<b>')
def answer(b):
#     a = None
#     b = g.handle_answer(answer)
#     if b == 'True':
#         a = g.viable_questions()
#     else:
#         return redirect(url_for('question'))
    return render_template('answer.html')
