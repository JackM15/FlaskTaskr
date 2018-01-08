# Create the database for the app

import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    cursor = connection.cursor()

    #create table 
    cursor.execute("""CREATE TABLE tasks(
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        due_date TEXT NOT NULL,
        priority INTEGER NOT NULL,
        status INTEGER NOT NULL)""")
    
    #dummy data for table (no task_id as its auto incremented)
    cursor.execute('INSERT INTO tasks (name, due_date, priority, status)' 
                'VALUES("Finnish this app", "03/02/2018", 10, 1)')
    
    cursor.execute('INSERT INTO tasks (name, due_date, priority, status)' 
                'VALUES("Complete this whole book", "01/06/2018", 10, 1)')