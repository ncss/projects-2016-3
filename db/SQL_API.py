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

cur.execute('''

	create table user_skills (
		user_id integer not null,
		skill_id integer not null,

		foreign key (user_id) references user (user_id)
		foreign key (skill_id) references skills (skill_id)
	);

''')

cur.execute('''

	create table user (
	    email text not null,
	    fname text not null,
	    lname text not null,
	    DOB text,
	    location text,
	    gender text,
	    photo blob,
	    password text not null,
	    phone text,
	    other text,
	    primary key(user_id) not null
);


''')

cur.execute('''

	create table user_skills (
		user_id integer not null,
		skill_id integer not null,

		foreign key (user_id) references user (user_id)
		foreign key (skill_id) references skills (skill_id)
	);

''')


# for row in cur:
# 	cur.fetchone()




#***************************************
#Cleanup
connect.close() 
#***************************************
