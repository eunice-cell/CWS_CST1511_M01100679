import sqlite3
conn = sqlite3.connect('cyber_incident.db')
cursor = conn.cursor()

insertScript="""CREATE TABLE IF NOT EXISTS cyber_incident (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    i_date TEXT ,
    i_type TEXT ,
    status TEXT ,
    description TEXT,
    reported_by TEXT
    );
  """

cursor.execute(insertScript)
conn.commit()