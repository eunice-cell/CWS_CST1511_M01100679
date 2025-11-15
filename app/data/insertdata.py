import csv
import sqlite3
databaseLoc='DATA/test.db'

conn = sqlite3.connect(databaseLoc)
cursor = conn.cursor()

insertScript= """insert into users (username,password_hash)
values('abc','12345')"""

cursor.execute(insertScript)
all_users=cursor.fetchall()
for user in all_users:
    print(user,type(user))
conn.commit()