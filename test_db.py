import sqlite3
conn = sqlite3.connect('adaptive_test.db')
c = conn.cursor()

# query = "INSERT INTO users(username,password,firstname,lastname,email) VALUES ('username','password','firstname','lastname','email');"
# query = "select * from users"
# query = "INSERT INTO test(username,marks,difficulty) VALUES ('nihal',100,9);"
query = "SELECT * FROM test"
c.execute(query)
rows = c.fetchall()
print(rows)
conn.commit()
conn.close()