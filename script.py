import sqlite3
connection = sqlite3.connect('movies-database.db')

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS 
movies(mov_id INTEGER PRIMARY KEY, mov_title TEXT, actor_name TEXT,
 year INTEGER, dir_name TEXT)"""

cursor.execute(command1)
cursor.execute("INSERT INTO movies VALUES(1,'ARYA','Allu Arjun',2009,'Bunny')")
cursor.execute("INSERT INTO movies VALUES(2,'RRR','Ram Charan',2022,'Raj Mouli')")
cursor.execute("INSERT INTO movies VALUES(3,'Googly','Yash',2015,'Prashanth Neel')")

cursor.execute("SELECT * FROM movies")
results = cursor.fetchall()

print(results)
print('Details of the movie in which  Yash was the lead actor')
cursor.execute("SELECT * FROM movies WHERE actor_name='Yash'")
res = cursor.fetchall()
print(res)