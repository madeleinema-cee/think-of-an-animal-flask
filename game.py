import random
from db import Db
from questions import questions


class Game:

    def __init__(self):
        self.animal_data = None
        self.db = Db('animals.db')
        self.query = 'select * from animals'

    def question(self):
        viable_questions = self.find_viable_question()
        question_key = random.choice(viable_questions)
        if question_key == 'class_type':
            class_question, leg_question = self.identify_viable_class_types_or_legs()
            print(class_question)
            return class_question
        if question_key == 'legs':
            class_question, leg_question = self.identify_viable_class_types_or_legs()
            print(leg_question)
            return leg_question
        else:
            question = questions[question_key]['question']
            print(question)
            return question

    def find_viable_question(self):
        data = self.db.fetchall(query=self.query)
        self.animal_data = data
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

    def find_viable_class_or_leg_values(self):
        class_values = []
        leg_values = []
        for animal in self.animal_data:
            class_values.append(animal['class_type'])
            leg_values.append(animal['legs'])
        class_values = list(set(class_values))
        leg_values = list(set(leg_values))
        return class_values, leg_values

    def identify_viable_class_types_or_legs(self):
        viable_class_types= []
        viable_legs= []
        class_values, leg_values = self.find_viable_class_or_leg_values()
        class_types = questions['class_type']['class_type_questions']
        legs = questions['legs']['leg_questions']
        for key, value in class_types.items():
            for v in class_values:
                if value['viable'] and v == value['value']:
                    viable_class_types.append(key)
        for key, value in legs.items():
            for v in leg_values:
                if value['viable'] and v == value['value']:
                    viable_legs.append(key)
        class_type = random.choice(viable_class_types)
        class_question = questions['class_type']['class_type_questions'][class_type]['question']

        leg = random.choice(viable_legs)
        leg_question = questions['legs']['leg_questions'][leg]['question']

        return class_question, leg_question

# if __name__ == '__main__':
#     g = Game()
#     g.question()


