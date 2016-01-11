import sqlite3
import datetime, time
print('blah')
#***************************************
#Setup
connect = sqlite3.connect('db/database.db')
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

cur.execute("""

    create table skills (
        skill_id integer not null,
        category text not null,
        specialisation text not null,
        rank integer not null,

        primary key (skill_id)
    );

""")

cur.execute("""

    create table user_skills (
        user_id integer not null,
        skill_id integer not null,

        foreign key (user_id) references user (user_id),
        foreign key (skill_id) references skills (skill_id)
    );

""")

cur.execute("""

    create table user (
        user_id integer not null,
        email text not null,
        fname text not null,
        lname text not null,
        DOB text not null,
        gender text not null,
        photo blob null,
        password text not null,
        phone text null,
        other text null,
        location text null,
        primary key(user_id)
    );


""")

cur.execute("""

    create table post (
        post_id integer not null ,
        message text not null,
        author_id integer not null,
        status integer not null,
        timestamp text not null,

        primary key (post_id) ,
        foreign key (author_id) references user (user_id)
    );

""")

cur.execute("""insert into  skills (category, specialisation, rank) values ( 'medical', 'Acupuncturist', 1); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'medical', 'Nurse', 7); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'medical', 'GP', 10); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'medical', 'Dentist', 2); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'medical', 'Vet', 5); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'medical', 'Nutritionist', 4); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'social', 'Physiotherapist', 4); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'social', 'Social Worker', 6); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'social', 'Chef', 3); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'social', 'Funeral Worker', 2); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'social', 'Policeman', 7); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'social', 'Criminal', 7); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'food related', 'Farmer', 7); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'food related', 'Botanist', 7); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'food related', 'Baker', 4); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'professional', 'Lawyer', 1); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'professional', 'Scientist', 5); """)
cur.execute("""insert into  skills (category, specialisation, rank) values ( 'professional', 'Engineer', 5); """)
connect.commit()

#insert into user values ('sofia123@mail.com', 'Sofia', 'HeLlo', '20/12/98', '40.7127, -74.0059', 'F', null, '56_ol%'


# for row in cur:
#     cur.fetchone()

#***************************************
#Cleanup
connect.close()
#***************************************
