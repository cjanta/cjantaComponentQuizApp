from components.db.db_sqlite3_component import DB_Component_SQLite as db_component

db = db_component()

db_component() \
.create_table(db.table_name_userine) \
    .insert(db.table_name_userine,"Helga Bunterlich", 42) \
    .insert(db.table_name_userine,"Rudi Resterampe", 77) \
    .insert(db.table_name_userine,"Susi Zenzationalz", 24) \
    .insert(db.table_name_userine,"Mercedes da silvio zanahoria el torro", 47) \
    .read_table(db.table_name_userine) \
.create_table(db.table_name_questions_answers) \
    .insert(db.table_name_questions_answers,"Was wolle DQL ?", "Data Query Language") \
    .insert(db.table_name_questions_answers,"Was wolle DML ?", "Data Manipulation Language") \
    .insert(db.table_name_questions_answers,"Was wolle TCL ?", "Transaction Control Language") \
    .insert(db.table_name_questions_answers,"Was wolle DDL ?", "Data Definition Language") \
    .insert(db.table_name_questions_answers,"Was wolle DCL ?", "Data Control Language (nicht in SQLite)") \
    .insert(db.table_name_questions_answers,"Was wolle SQL ?", "Structured Query Language") \
    .read_table(db.table_name_questions_answers)
