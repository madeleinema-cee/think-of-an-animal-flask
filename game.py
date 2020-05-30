import random
from db import Db
from questions import questions


class Game:

    def __init__(self):
        self.animal_data = None
        self.db = Db('animals.db')
        self.query = 'select * from animals'
        self.question = None

    def generate_question(self):
        viable_questions = self.find_viable_question()
        question_key = random.choice(viable_questions)
        if question_key == 'class_type':
            self.question = self.identify_viable_class_types()
        elif question_key == 'legs':
            self.question = self.identify_viable_legs()
        else:
            self.question = questions[question_key]['question']

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

    def identify_viable_class_types(self):
        viable_class_types= []
        class_values, leg_values = self.find_viable_class_or_leg_values()
        class_types = questions['class_type']['class_type_questions']

        for key, value in class_types.items():
            for v in class_values:
                if value['viable'] and v == value['value']:
                    viable_class_types.append(key)

        class_type_key = random.choice(viable_class_types)
        class_type = questions['class_type']['class_type_questions'][class_type_key]
        if class_type['value']:
            class_question = class_type['question']
            class_type['value'] = False

            return class_question

    def identify_viable_legs(self):
        viable_legs = []
        class_values, leg_values = self.find_viable_class_or_leg_values()
        legs = questions['legs']['leg_questions']

        for key, value in legs.items():
            for v in leg_values:
                if value['viable'] and v == value['value']:
                    viable_legs.append(key)

        leg_key = random.choice(viable_legs)
        leg_type = questions['legs']['leg_questions'][leg_key]
        if leg_type['value']:
            leg_question = leg_type['question']
            leg_type['value'] = False

            return leg_question


# if __name__ == '__main__':
#     g = Game()
#     g.question()


