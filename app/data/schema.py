import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT DEFAULT 'user'
        );
""")

conn.commit()



#cyber table
conn = sqlite3.connect('cyber_incidents.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cyber_incidents (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    i_date TEXT ,
    i_type TEXT ,
    status TEXT ,
    description TEXT,
    reported_by TEXT
    );
  """)
conn.commit()



#dataset table
conn = sqlite3.connect('datasets.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS datasets (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT ,
    rows INTEGER,
    columns INTEGER ,
    uploaded_by TEXT,
    date TEXT
    );
  """)
conn.commit()


# tickets table
conn = sqlite3.connect('tickets.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tickets (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    priority TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'open',
   created_at TEXT,
    created_date TEXT
    );
  """
               )
conn.commit()