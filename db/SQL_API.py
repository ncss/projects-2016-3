import sqlite3
#***************************************
#Setup
connect = sqlite3.connect('database.db')
cur = connect.cursor()
#***************************************



cur.execute('''

	create table skills (
		skill_id integer not null,
		category text not null,
		specialisation text not null,
		rank integer not null,

		primary key (skill_id),
		foreign key (skill_id) references user_skills (skill_id)
	);

''')


# for row in cur:
# 	cur.fetchone()




#***************************************
#Cleanup
connect.close() 
#***************************************
