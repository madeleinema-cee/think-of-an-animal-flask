"""Think of An Animal
This game allows the user to think of an animal and let the game guess the animal by answering alternative questions
regarding the animal's features such as class type, size, and hair from a database. If the answer is correct, the game
wins; if the answer is incorrect, the user wins, and his/her answer will be stored.
"""
import sys
import random

from db import Db
from questions import questions
from flask import app
from flask import render_template

class Game:
    """
    A class used to represent the Game. This class shows you how the game works.
    ...
    Attributes
    ----------
    class_type: int
        the number of the animal's class type (mammal is 1, fish is 2)
    db: database
        db is animals.db
    animal_data: list
        a list of dictionaries of animals
    viable_questions: list
        a list of dictionaries' keys where at lease one animal has a distinct value
    query:str
        Sql query to check the database for animal data
    rounds: int
        the number of the round of the game (default is 0)
    """
    def __init__(self):
        self.sys = sys
        self.class_type = None
        self.db = Db('animals.db')
        self.animal_data = None
        self.viable_questions = None
        self.query = None
        self.rounds = 0
        self.question = None

    def main(self):
        """platform to sequentially call class methods."""
        self.identify_class_type()
        while self.rounds < 10:
            self.retrieve_animal_data()
            if len(self.animal_data) == 1:
                break
            # print(len(self.animal_data))
            # print(f'round {self.rounds}')
            self.ask_question()
            self.rounds += 1
        self.guess_animal()

    @staticmethod
    def format_question(question):
        """append (yes/no) to a string

        Argument
        --------
        question: str
            question in questions.py
        """
        return f'{question} (yes/no): '

    def guess_animal(self):
        """guess the animal and analyze the answer
        """
        question = ''
        animal = random.choice(self.animal_data)
        name = animal['animal_name']
        question = f'is {name} your animal?'
        animal_answer = input(self.format_question(question))
        animal_answer = self.validate_answer(question, animal_answer)
        self.rounds += 1
        if animal_answer == 'yes':
            print("I won!")
            self.sys.exit()
        else:
            if self.rounds < 10 and len(self.animal_data) > 1:
                self.animal_data.remove(animal)
                self.guess_animal()
            else:
                print("I lost!")
        return question

    def generate_random_class_type_question(self):
        """ generate random question about animal class by using the value in questions.py
        return value and question"""
        values = []
        for q in questions['class_type']:
            if not q['asked']:
                values.append(q['value'])
        if values:
            random_num = random.choice(values)
            for q in questions['class_type']:
                if random_num == q['value']:
                    q['asked'] = True
                    # print(q['question'])
                    return q['question'], q['value']
        else:
            print('No class type')

    def identify_class_type(self):
        """identify the class type of the animal by asking question and validate the answer,
        run the query in the database using the value based on answer returned from validate_answer.

        Attribute
        ---------
        class_type: int
            the number of the animal's class type (mammal is 1, fish is 2)
        """
        while self.class_type is None:
            question, value = self.generate_random_class_type_question()
            answer = input(self.format_question(question))
            answer = self.validate_answer(question, answer)
            self.rounds += 1
            if answer == 'yes':
                self.class_type = value
                self.query = f'select * from animals where class_type = {self.class_type}'


    def validate_answer(self, question, answer):
        """Validate the answer input by the user. So only ‘yes’ or ‘no’ can be answered.
        Return the answer to its function.

        Returns
        -------
        answer: str
            answer input by the user. ('yes' or 'no')
        """
        if answer == 'yes':
            return answer
        if answer == 'no':
            return answer
        else:
            print('Invalid Answer! Please type "yes" or "no"')
            answer = input(self.format_question(question))
            self.validate_answer(question, answer)
            return answer

    def retrieve_animal_data(self):
        """retrieve the animal data in a array from the result of the query generated from identify_class_type

        Attribute
        ---------

        animal_data: list
            a list of dictionaries of animals
        """
        data = self.db.fetchall(self.query)
        self.animal_data = data

    def find_viable_questions(self):
        """find viable questions based on the animal feature keys of the array such as ‘hair’.
        If all animal have the same feature, the question about that feature is not viable.

        Returns
        ------
        viable_questions: list
            a list of dictionaries' keys where at lease one animal has a distinct value

        # TODO: legs question.
        """
        viable_questions = []
        keys = list(self.animal_data[0].keys())
        keys.remove('id')
        keys.remove('animal_name')
        keys.remove('legs')

        for key in keys:
            for animal in self.animal_data:
                if animal[key] != self.animal_data[0][key]:
                    viable_questions.append(key)
        viable_questions = list(set(viable_questions))
        print(viable_questions)

        return viable_questions


    def ask_question(self):
        """use the viable_questions returned from find_viable_question
        to run a query regarding the viable question in the database.
        """
        viable_questions = self.find_viable_questions()
        if viable_questions:
            question_key = random.choice(viable_questions)
            question = questions[question_key][0]['question']
            answer = self.validate_answer(question, input(self.format_question(question)))
            answer = self.convert_answer(answer)
            questions[question_key][0]['asked'] = True
            questions[question_key][0]['answer'] = answer

            self.query = self.query + f' and {question_key} = {answer}'
        else:
            self.guess_animal()

    def convert_answer(self, answer):
        """convert the answer from ask_question into values

        Argument
        --------
        answer: str
            'yes' or 'no
        Returns
        ------
        int
            int 1 or 0
        """
        if answer == 'yes':
            return 1
        else:
            return 0






