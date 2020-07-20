import random
from db import Db
from questions import questions
from flaskgame.user_answers import user_answers

class Game:
    def __init__(self):
        self.animal_data = None
        self.db = Db('animals.db')
        self.query = 'select * from animals'
        self.rounds = 1
        self.question_key = None
        self.value = None
        self.viable_questions = None
        self.animal = None
        self.questions = questions
    
    
    def generate_question(self):
        self.viable_questions = self.find_viable_question()
        if self.viable_questions:
            self.question_key = random.choice(self.viable_questions)
            if self.question_key == 'class_type':
                question = self.identify_viable_class_types()
                return question
            elif self.question_key == 'legs':
                question = self.identify_viable_legs()
                return question
            else:
                return self.questions[self.question_key]['question']
        else:
            self.guess_animal()

    def guess_animal(self):
        if len(self.animal_data) == 1:
            self.animal = random.choice(self.animal_data)
            name = self.animal['animal_name']
            question = f'is {name} your animal?'
            return question
        else:
            self.animal = random.choice(self.animal_data)
            name = self.animal['animal_name']
            question = f'is {name} your animal?'
            return question

    def find_viable_question(self):
        data = self.db.fetchall(query=self.query)
        self.animal_data = data
        self.viable_questions = []
        keys = list(self.animal_data[0].keys())
        keys.remove('id')
        keys.remove('animal_name')

        for key in keys:
            for animal in self.animal_data:
                if animal[key] != self.animal_data[0][key]:
                    self.viable_questions.append(key)

        viable_questions = list(set(self.viable_questions))

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
        viable_class_types = []
        class_values, leg_values = self.find_viable_class_or_leg_values()
        class_types = self.questions['class_type']['class_type_questions']

        for key, value in class_types.items():
            for v in class_values:
                if value['viable'] and v == value['value']:
                    viable_class_types.append(key)

        class_type_key = random.choice(viable_class_types)
        class_type = self.questions['class_type']['class_type_questions'][class_type_key]
        if class_type['viable']:
            class_question = class_type['question']
            class_type['viable'] = False
            self.value = class_type['value']
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
        leg_type = self.questions['legs']['leg_questions'][leg_key]
        if leg_type['viable']:
            leg_question = leg_type['question']
            leg_type['viable'] = False
            self.value = leg_type['value']

            return leg_question

    def handle_answer(self, user_input):
        if user_input == 'True':
            if self.question_key == 'class_type':
                self.modify_query('class_type', self.value)
                user_answers['class_type'] = self.value
            elif self.question_key == 'legs':
                self.modify_query('legs', self.value)
                user_answers['legs'] = self.value
            else:
                self.modify_query(self.question_key, 1)
                user_answers[self.question_key] = 1
        if user_input == 'False':
            if self.question_key == 'class_type':
                self.modify_query('class_type', self.value, conditional=False)
            elif self.question_key == 'legs':
                self.modify_query('legs', self.value, conditional=False)
            else:
                self.modify_query(self.question_key, 0)
                user_answers[self.question_key] = 0
        self.rounds += 1

    def modify_query(self, key, value, conditional=True):
        if self.rounds == 1:
            self.query = f'{self.query} where {self.question_key} {"=" if conditional else "!="} {value}'
        else:
            self.query = f'{self.query} and {key} {"=" if conditional else "!="} {value}'


# if __name__ == '__main__':
#     g = Game()
#     g.generate_question()

