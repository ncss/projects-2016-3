import sqlite3
#***************************************
#Setup
connect = sqlite.connect('database.db')
cur = connect.cursor()
#***************************************



cur.execute('<SQL CODE>')
for row in cur:
	cur.fetchone()




#***************************************
#Cleanup
connect.close() 
#***************************************
