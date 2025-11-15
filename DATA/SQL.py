import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
CreateTableScript="""create table IF NOT EXISTS users(
id integer primary key autoincrement,
username text not null,
password_hash text not null,
role text default 'user')"""
#db creation
cursor.execute (CreateTableScript)
conn.commit()