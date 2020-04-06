import sqlite3
conn = sqlite3.connect('adaptive_test.db')
c = conn.cursor()

c.execute('''CREATE TABLE users
             (username VARCHAR(50), password VARCHAR(50),firstname VARCHAR(50),lastname VARCHAR(50),email varchar(50))''')

c.execute('''CREATE TABLE test
             (testid INTEGER PRIMARY KEY AUTOINCREMENT,username VARCHAR(50), marks INTEGER(3),difficulty INTEGER(2))''')

conn.commit()
conn.close()