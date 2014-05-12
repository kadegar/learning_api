import json
import requests
import sqlite3

API_KEY="xxx"
url=requests.get("http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=%s" % (API_KEY,))

binary=url.content
output=json.loads(binary)

movies=output["movies"]

with sqlite3.connect("movies.db") as connection:
	c=connection.cursor()
	for movie in movies:
		insert_value=["x","x","x","x","x","x","x"]
		insert_value[0]=movie["title"]
		insert_value[1]=movie["year"]
		insert_value[2]=movie["mpaa_rating"]
		insert_value[3]=movie["release_dates"]["theater"]
		insert_value[4]=movie["runtime"]
		insert_value[5]=movie["ratings"]["critics_score"]
		insert_value[6]=movie["ratings"]["audience_score"]
		c.execute("""INSERT INTO new_movies VALUES(?,?,?,?,?,?,?)""",insert_value)
	c.execute("""SELECT * FROM new_movies ORDER BY title ASC""")
	rows=c.fetchall()
	for r in rows:
		print r[0],r[1],r[2],r[3],r[4],r[5],r[6]
