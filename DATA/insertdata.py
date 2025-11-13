import csv
import sqlite3
databaseLoc='Data/test.db'

conn = sqlite3.connect(databaseLoc)
cursor = conn.cursor()

insertScript= """insert into users (username,password_hash)
values('abc','12345')"""

with open('Data/cyber_incidents.csv', 'r') as cyber:
    i = 0
    for line in cyber.readlines():
        if i == 0:
            i += 1
            continue
        line = line.strip()
        vals = line.split(',')
        insertScript = """insert into cyber_incidents (
              id,i_date,severity,i_type,status,description,reported_by)
         values(?,?,?,?,?,?)"""
        cursor.execute(insertScript, (vals[0], vals[1], vals[2], vals[3], vals[4], vals[5],))


cursor.execute(insertScript)
all_users=cursor.fetchall()
for user in all_users:
    print(user,type(user))
conn.commit()