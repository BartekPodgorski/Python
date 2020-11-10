import json
import sqlite3
conn = sqlite3.connect('Script.db')
c = conn.cursor()
c.execute("CREATE TABLE persons (id varchar(3), data json)")
for person in persons:
    c.execute("insert into persons values (?, ?)",
              [person['results'], json.dumps(person)])
c.execute("SELECT * FROM users")
print(c.fetchmany(2))
conn.commit()
conn.close()
