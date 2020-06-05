from flask import render_template, url_for, redirect, flash
from flaskgame import app, db
from flaskgame.forms import AnimalForm
from flaskgame.models import AnimalName
from game import Game


g = Game()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/question')
def question():
    q = g.generate_question()
    if g.viable_questions:
        return render_template('question.html', question=q, data=g.animal_data,
                           r=g.rounds, query=g.query, viable_q=g.viable_questions)
    else:
        return redirect(url_for('guess'))


@app.route('/answer/<user_input>')
def answer(user_input):
    if g.rounds < 10:
        if g.viable_questions:
            g.handle_answer(user_input)
            return redirect(url_for('question'))
        else:
            return redirect(url_for('guess'))
    else:
        return redirect(url_for('guess'))


@app.route('/guess')
def guess():
    question = g.guess_animal()
    return render_template('guess.html', question=question, r=g.rounds)


@app.route('/result/<user_input>')
def result(user_input):
    if g.rounds < 10:
        if user_input == 'True':
            return render_template('result.html', content='I won!')
        else:
            g.rounds += 1
            if len(g.animal_data) > 1:
                g.animal_data.remove(g.animal)
                return redirect(url_for('guess'))
            else:
                return redirect(url_for('input'))
    else:
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
        flash('Your animal has been accepted!', 'success')
        return redirect(url_for('home'))
    return render_template('input_feature.html', form=form)




