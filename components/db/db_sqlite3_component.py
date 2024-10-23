import sqlite3


class DB_Component_SQLite:

    def __init__(self) -> None:
        self.db = sqlite3.connect("quizapp.db")
        self.cursor = self.db.cursor()
        self.__create_tables()
        self.insert_userine_values("Frida", "42")
        self.__print_userine_table()
        self.__close_connection()
    
    def __create_tables(self) -> None:
        self.cursor.execute("DROP TABLE IF EXISTS userine")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS userine (id INTEGER PRIMARY KEY, name text, age int)")

    def insert_userine_values(self, name, age):
        self.cursor.execute(f"INSERT INTO userine (name, age) VALUES ('{name}', '{age}')")
        self.db.commit()

    def __print_userine_table(self):
        self.cursor.execute("SELECT * FROM userine")   
        datasets = self.cursor.fetchall()
        for data in datasets:
            print(data) 

    def __close_connection(self):
        self.db.close()
        self.db = None
        self.cursor = None
        print("Conncetion to db closed.")


# DQL > Data Query Language
# DML > Data Manipulation Language
# TCL > Transaction Control Language
# DDL > Data Definition Language
# DCL > Data Control Language (nicht in SQLite)
# SQL > Structured Query Language