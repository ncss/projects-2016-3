import sqlite3

def select(fields, table):
    connect = sqlite3.connect('database.db')
    cur = connect.cursor()
    cur.execute('''select %s from %s''' % (",".join(fields), table))   
    results = cur.fetchall()
    cur.close()
    connect.close()
    return results

#def where, insert
#check location, dob

#query(('message','author_id'), 'post')

def get_all_posts():
    select(('*',), 'post')
    return 

get_all_posts()


def get_all_user_posts(user_id):
    connect = sqlite3.connect('database.db')
    cur = connect.cursor()
    cur.execute (''' select * from post where author_id = %d''' % user_id)
    #print(cur.fetchall())

    cur.close()
    connect.close()


#get_all_user_posts(0)




def create_post(message, status, user_id):
    connect = sqlite3.connect('database.db')
    cur = connect.cursor()
    cur.execute (''' insert into post (message, author_id, status, timestamp) values ('%s', %d, %d, '%s');''' % (message, user_id, status, ""))
    connect.commit()
    #print(cur.fetchall())

    cur.close()
    connect.close()


create_post('The world is ending! Help me and my family pleazzzzzz!!111!!!', 2, 1)

## user test


##insert into user values ('14kdi@mail.com', 'BeN', 'Dog14', '98-12-2', '-40.7127, -74.0059', 'M', null, '5lo4', '04 123 567', 'S: 78');
##
##insert into user values ('88@mail.com', 'S1', '123', 5 ,12 , 1998, '0.7127, 0.0059', 'Other', null, '56_oP%', '+61 4123 567', 'Skype: timeisahealer');
##
##
#### post test
##
##
##insert into post values ('hello world! 12', 76, '2', '16/35/1/10/2016')
##
##insert into post values ('The world is ending! Help me and my family pleazzzzzz!!111!!!', 103, '2', '16/35/1/10/2016')
##
##insert into post values (1, 'hello world! 12', 1, 2, '16-35-1-10-2016')
##
