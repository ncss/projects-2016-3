import sqlite3
#***************************************
#Setup
connect = sqlite3.connect('database.db')
cur = connect.cursor()
#***************************************


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#DELETE THIS BEFORE TESTING AND PRODUCTION

cur.execute('drop table if exists skills;')
cur.execute('drop table if exists user_skills;')
cur.execute('drop table if exists user;')
cur.execute('drop table if exists post;')

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

cur.execute('''

	create table skills (
		skill_id integer not null,
		category text not null,
		specialisation text not null,
		rank integer not null,

		primary key (skill_id)
	);

''')

cur.execute('''

	create table user_skills (
		user_id integer not null,
		skill_id integer not null,

		foreign key (user_id) references user (user_id),
		foreign key (skill_id) references skills (skill_id)
	);

''')

cur.execute('''

	create table user (
		user_id integer not null,
	    email text not null,
	    fname text not null,
	    lname text not null,
	    DOB text not null,
	    location text not null,
	    gender text not null,
	    photo blob null,
	    password text not null,
	    phone text null,
	    other text null,
	    primary key(user_id)
	);


''')

cur.execute('''

	create table post (
	    post_id integer not null ,
	    message text not null,
	    author_id integer not null,
	    status integer not null,
	    timestamp text not null,

	    primary key (post_id) ,
	    foreign key (author_id) references user (user_id)
	);

''')


#insert into user values ('sofia123@mail.com', 'Sofia', 'HeLlo', '20/12/98', '40.7127, -74.0059', 'F', null, '56_ol%' 


# for row in cur:
# 	cur.fetchone()

#***************************************
#Cleanup
connect.close() 
#***************************************
