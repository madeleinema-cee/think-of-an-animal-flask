"""Think of An Animal
This game allows the user to think of an animal and let the game guess the animal by answering alternative questions
regarding the animal's features such as class type, size, and hair from a database. If the answer is correct, the game
wins; if the answer is incorrect, the user wins, and his/her answer will be stored.
"""
import random

from db import Db
from questions import questions


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
        self.db = Db('animals.db')
        self.animal_data = None
        self.viable_questions = None
        self.query = 'select * from animals'
        self.rounds = 0
        self.question = None

    def main_question(self):
        if self.rounds < 10:
            self.retrieve_animal_data()
            viable_questions = self.find_viable_questions()
            if viable_questions:
                return viable_questions

    def main(self):
        """platform to sequentially call class methods."""

        while self.rounds < 10:
            print(self.query)
            viable_questions = self.main_question()
            print(viable_questions)
            if viable_questions:
                self.ask_question()
                if len(self.animal_data) == 1:
                    break
            else:
                break
            self.rounds += 1
            # print(self.animal_data)
            # print(self.query)
            # print(self.rounds)
        self.guess_animal()

    def retrieve_animal_data(self):
        """retrieve the animal data in a array from the result of the query generated from identify_class_type
        Attribute
        ---------
        animal_data: list
            a list of dictionaries of animals
        """

        data = self.db.fetchall(self.query)
        self.animal_data = data

    def answer_question(self, question_key):
        if question_key:
            question = questions[question_key]['question']
            answer = self.validate_answer(question, input(self.format_question(question)))
            answer = self.convert_answer(answer)
            # print('answer--------')
            # print(question)
            self.modify_query(question_key, answer)

    def ask_question(self):
        """use the viable_questions returned from find_viable_question
        to run a query regarding the viable question in the database.
        """

        viable_questions = self.find_viable_questions()
        question_key = random.choice(viable_questions)
        if question_key == 'class_type':
            self.identify_class_type()
        elif question_key == 'legs':
            self.identify_legs()
        else:
            print(question_key)
            self.answer_question(question_key)
            return question_key

    def find_viable_questions(self):
        """find viable questions based on the animal feature keys of the array such as ‘hair’.
        If all animal have the same feature, the question about that feature is not viable.
        Returns
        ------
        viable_questions: list
            a list of dictionaries' keys where at lease one animal has a distinct value
        """
        viable_questions = []
        keys = list(self.animal_data[0].keys())
        keys.remove('id')
        keys.remove('animal_name')

        for key in keys:
            for animal in self.animal_data:
                if animal[key] != self.animal_data[0][key]:
                    viable_questions.append(key)
        viable_questions = list(set(viable_questions))

        return viable_questions

    def find_viable_class_values(self):
        class_values = []
        for animal in self.animal_data:
            class_values.append(animal['class_type'])
        class_values = list(set(class_values))
        # print(class_values)
        return class_values

    def find_viable_leg_values(self):
        leg_values = []
        for animal in self.animal_data:
            leg_values.append(animal['legs'])
        leg_values = list(set(leg_values))
        return leg_values

    def identify_class_type(self):
        """identify the class type of the animal by asking question and validate the answer,
        run the query in the database using the value based on answer returned from validate_answer.
        Attribute
        ---------
        class_type: int
            the number of the animal's class type (mammal is 1, fish is 2)
        """

        question, value = self.generate_random_class_type_question()
        answer = input(self.format_question(question))
        answer = self.validate_answer(question, answer)

        if answer == 'yes':
            questions['class_type']['viable'] = False
            self.modify_query('class_type', value)
        else:
            self.modify_query('class_type', value, conditional=False)

    def generate_random_class_type_question(self):
        """generate random question about animal class by using the value in questions.py
        return value and question"""

        viable_questions = self.identify_viable_class_type_questions()
        class_type_key = random.choice(viable_questions)
        class_type = questions['class_type']['class_type_questions'][class_type_key]
        class_type['viable'] = False

        return class_type['question'], class_type['value']

    def identify_viable_class_type_questions(self):
        viable_questions = []
        class_values = self.find_viable_class_values()
        class_types = questions['class_type']['class_type_questions']
        for key, value in class_types.items():
            for v in class_values:
                if value['viable'] and v == value['value']:
                    viable_questions.append(key)
        return viable_questions

    def identify_legs(self):
        question, value = self.generate_random_legs_question()
        answer = input(self.format_question(question))
        answer = self.validate_answer(question, answer)

        if answer == 'yes':
            questions['legs']['viable'] = False
            self.modify_query('legs', value)
        else:
            self.modify_query('legs', value, conditional=False)

    def generate_random_legs_question(self):
        viable_questions = self.identify_viable_legs_questions()
        leg_key = random.choice(viable_questions)
        legs = questions['legs']['leg_questions'][leg_key]
        legs['viable'] = False

        return legs['question'], legs['value']

    def identify_viable_legs_questions(self):
        viable_questions = []
        leg_values = self.find_viable_leg_values()
        legs = questions['legs']['leg_questions']
        for key, value in legs.items():
            for v in leg_values:
                if value['viable'] and v == value['value']:
                    viable_questions.append(key)
        return viable_questions

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
        """guess the animal and analyze the answer"""

        # print(self.animal_data)
        animal = random.choice(self.animal_data)
        name = animal['animal_name']
        question = f'is {name} your animal?'
        animal_answer = input(self.format_question(question))
        animal_answer = self.validate_answer(question, animal_answer)
        self.rounds += 1
        if animal_answer == 'yes':
            print("I won!")
        else:
            if self.rounds < 10 and len(self.animal_data) > 1:
                self.animal_data.remove(animal)
                self.guess_animal()
            else:
                print("I lost!")

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
        return 1 if answer == 'yes' else 0

    def modify_query(self, key, value, conditional=True):
        if self.rounds == 0:
            self.query = f'{self.query} where {key} {"=" if conditional else "!="} {value}'
        else:
            self.query = f'{self.query} and {key} {"=" if conditional else "!="} {value}'

if __name__ == '__main__':
    g = Game()
    g.main()