import sqlite3


class DB_Component_SQLite:

    table_name_userine = "userine"
    table_name_questions_answers = "qanda"

    __tableshemes = {
        f"{table_name_userine}" : "(id INTEGER PRIMARY KEY, name text, age int)",
        f"{table_name_questions_answers}" : "(id INTEGER PRIMARY KEY, question text, answer text)"
    }
    __col_descriptions = {
        f"{table_name_userine}" : "(name, age)",
        f"{table_name_questions_answers}" : "(question, answer)"
    }

    def __init__(self):
        self.db = None
        self.__check_db()

    def __check_db(self):
        if not self.db:
            self.db = sqlite3.connect("quizapp.db")

    def name_to_sheme(self,table_name :str):
        return self.__tableshemes.get(table_name)
    
    def name_to_col_description(self,table_name :str):
        return self.__col_descriptions.get(table_name)

    def create_table(self, table_name :str) :
        self.__check_db()
        c = self.db.cursor()
        c.execute(f"DROP TABLE IF EXISTS {table_name}")
        c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} {self.name_to_sheme(table_name)}")
        return self

    def insert(self, table_name :str, value_0 :str, value_1 :str):
        self.__check_db()
        self.db.cursor().execute(f"INSERT INTO {table_name} {self.name_to_col_description(table_name)} VALUES ('{value_0}', '{value_1}')")
        self.db.commit()
        return self

    def read_table(self, table_name :str):
        self.__check_db()
        c = self.db.cursor()
        c.execute(f"SELECT * FROM {table_name}")   
        datasets = c.fetchall()
        for data in datasets:
            print(data) 
        return self
    
    def force_db_close(self):
        if self.db:
            self.db.close()
            self.db = None
            print("Conncetion to db closed by force.")
    
    def __del__(self):
        if self.db:
            self.db.close()
            print("Conncetion to db closed.")
        