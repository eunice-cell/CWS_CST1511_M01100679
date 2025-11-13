import sqlite3
databaseLoc='Data/cyber_incident.db'
conn = sqlite3.connect(databaseLoc)
cursor = conn.cursor()

conn = sqlite3.connect(databaseLoc)
cursor = conn.cursor()

with open('Data\cyber_incidents.csv', 'r') as cyber:
       i = 0
       for line in cyber.readlines():
           if i == 0:
               i += 1
               continue
           line = line.strip()
           vals = line.split(',')
           insertScript = """INSERT INTO cyber_incident(
                 id,i_date,i_type,status,description,reported_by)
            values(?,?,?,?,?,?)"""
           cursor.execute(insertScript,(vals[0], vals[1], vals[2], vals[3], vals[4], vals[5]))
           conn.commit()



