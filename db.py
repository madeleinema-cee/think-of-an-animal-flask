import sqlite3


class Db:
    """
    A class used to represent database(Db)
    """

    def __init__(self, database):
        self.conn = sqlite3.connect(database, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def fetchall(self, query):
        self.cursor = self.conn.cursor()
        self.execute(query)
        result = [dict(row) for row in self.cursor.fetchall()]
        return result

    def close(self):
        self.conn.close()

    def setup(self, data):
        self.create_classes_table()
        self.create_animals_table()
        for d in data:
            self.insert_data_from_csv(d[0], d[1])

    def create_animals_table(self):
        query = '''
        create table animals
        (id integer not null, animal_name text, hair integer, feathers integer, eggs integer, milk integer, airborne integer, 
        aquatic integer, predator integer, toothed integer, backbone integer, breathes integer, venomous integer, 
        fins integer, legs integer, tail integer, domestic integer, catsize integer, class_type integer,
        primary key (id), foreign key (class_type) references classes(id))'''
        self.execute(query)

    def create_classes_table(self):
        query = '''
        create table classes
        (id integer not null, number_of_animal_species_in_class integer, class_type text,
        primary key (id))
        '''
        self.execute(query)

    def insert_data_from_csv(self, csv_path, table):
        with open(csv_path, 'r') as file:
            next(file)
            for line in file:
                line = line.strip().split(',')
                line[0] = f"'{line[0]}'" if not line[0].isdigit() else line[0]
                line[1] = f"'{line[1]}'" if not line[1].isdigit() else line[1]
                query = f'insert into {table} values (null, {", ".join(line)})'
                self.execute(query)

    # def add_foreign_key(self, table, foreign_key, ref_table, ref_column):
    #     query = f'''
    #     alter table {table}
    #     add foreign key ({foreign_key}) references {ref_table}({ref_column})'''
    #     print(query)
    #     self.execute(query)







