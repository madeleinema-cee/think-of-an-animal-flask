from random import randint
from uuid import uuid4
from flask import render_template, url_for, redirect, flash, session
from flaskgame import app, db
from flaskgame.forms import AnimalForm
from flaskgame.models import AnimalName
from flaskgame.user_answers import user_answers
from flaskgame.game_dict import game_dict
from game import Game

g = Game()

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/instantiate_game')
def instantiate_game():
    session.clear()
    game_id = randint(1, 100)
    session[game_id] = str(uuid4())
    id = session[game_id]
    session.modified = True
    return redirect(url_for('question', id=id, r=g.rounds-1))


@app.route('/question/<string:id>/<int:r>', methods=['GET'])
def question(id, r):
    q = g.generate_question()
    if g.viable_questions:
        r = r+1
        return render_template('question.html', question=q, data=g.animal_data,
                               r=r, query=g.query, viable_q=g.viable_questions, id=id)
    else:
        return redirect(url_for('guess', id=id, r=g.rounds))


@app.route('/answer/<string:id>/<int:r>/<user_input>', methods=['GET'])
def answer(user_input, id, r):
    if r < 10:
        if g.viable_questions:
            g.handle_answer(user_input)
            return redirect(url_for('question', id=id, r=r))
        else:
            if g.animal_data:
                return redirect(url_for('guess', id=id, r=r))
            else:
                return redirect(url_for('input'))
    else:
        return redirect(url_for('guess', id=id, r=r))


@app.route('/guess/<string:id>/<int:r>', methods=['GET', 'POST'])
def guess(id, r):
    question = g.guess_animal()
    return render_template('guess.html', question=question, r=r, id=id)


@app.route('/result/<string:id>/<user_input>')
def result(user_input, id):
    if g.rounds < 10:
        if user_input == 'True':
            return render_template('result.html', id=id, content='I won!')
        else:
            g.rounds += 1
            if len(g.animal_data) > 1:
                g.animal_data.remove(g.animal)
                return redirect(url_for('guess', id=id))
            else:
                return redirect(url_for('input'))
    else:
        if user_input == 'True':
            return render_template('result.html', id=id, content='I guessed the animal, but I ran out of rounds!')
        return redirect(url_for('input'))


@app.route('/input')
def input():
    return render_template('input.html', content='I lost!')


@app.route('/input/feature', methods=['GET', 'POST'])
def input_feature():
    form = AnimalForm()
    if form.validate_on_submit():
        animal = AnimalName(animal_name=form.animal_name.data, hair=form.hair.data,
                            feathers=form.feathers.data, eggs=form.eggs.data,
                            milk=form.milk.data, airborne=form.airborne.data,
                            aquatic=form.aquatic.data, predator=form.predator.data,
                            toothed=form.toothed.data, backbone=form.backbone.data,
                            breathes=form.breathes.data, venomous=form.venomous.data,
                            fins=form.fins.data, legs=form.legs.data,
                            tail=form.tail.data, domestic=form.domestic.data,
                            catsize=form.catsize.data, class_type=form.class_type.data,
                            )
        db.session.add(animal)
        db.session.commit()
        flash('Thank you! Your animal has been accepted!')
        return redirect(url_for('home'))
    for k in user_answers:
        if k == 'hair':
            form.hair.default = user_answers[k]
        if k == 'feather':
            form.feathers.default = user_answers[k]
        if k == 'eggs':
            form.eggs.default = user_answers[k]
        if k == 'milk':
            form.milk.default = user_answers[k]
        if k == 'airborne':
            form.airborne.default = user_answers[k]
        if k == 'aquatic':
            form.aquatic.default = user_answers[k]
        if k == 'predator':
            form.predator.default = user_answers[k]
        if k == 'toothed':
            form.toothed.default = user_answers[k]
        if k == 'backbone':
            form.backbone.default = user_answers[k]
        if k == 'breathes':
            form.breathes.default = user_answers[k]
        if k == 'venomous':
            form.venomous.default = user_answers[k]
        if k == 'fins':
            form.fins.default = user_answers[k]
        if k == 'legs':
            form.legs.default = user_answers[k]
        if k == 'tail':
            form.tail.default = user_answers[k]
        if k == 'domestic':
            form.domestic.default = user_answers[k]
        if k == 'catsize':
            form.catsize.default = user_answers[k]
        if k == 'class_type':
            form.class_type.default = user_answers[k]
        form.process()
    return render_template('input_feature.html', form=form)



