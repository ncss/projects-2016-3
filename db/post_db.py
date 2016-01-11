import sqlite3

def select(fields, table):
    connect = sqlite3.connect('database.db')
    cur = connect.cursor()
    cur.execute('''select %s from %s''' % (",".join(fields), table))
    results = cur.fetchall()
    cur.close()
    connect.close()
    return results

def insert(table, columnvaluedict):
    connect = sqlite3.connect('database.db')
    cur = connect.cursor()
    keys = list(columnvaluedict.keys())
    columns = ', '.join(keys)
    value = []
    qmarks = []
    for key in keys:
        value.append(columnvaluedict[key])
        qmarks.append('?')
    qmarks = ', '.join(qmarks)
    query = ''' insert into %s (%s) values (%s);''' % (table, columns, qmarks)
    cur.execute(query, value)
    connect.commit()
    cur.close()
    connect.close()

insert('post', {
	'message': 'hello world! 12',
	'author_id': 76,
	'status': 2,
	'timestamp': '35/1/10/2016'
})

#def where, insert
#check location, dob

#query(('message','author_id'), 'post')

def get_all_posts():
    results = select(('*',), 'post')
    return results



def get_all_user_posts(user_id):
    connect = sqlite3.connect('database.db')
    cur = connect.cursor()
    keys = list(columnvaluedict.keys())
    columns = ', '.join(keys)
    value = []
    qmarks = []
    for key in keys:
        value.append(columnvaluedict[key])
        qmarks.append('?')
    qmarks = ', '.join(qmarks)
    query = ''' insert into %s (%s) values (%s);''' % (table, columns, qmarks)
    cur.execute(query, value)
    connect.commit()
    cur.close()
    connect.close()

#def where, insert
#check location, dob

#query(('message','author_id'), 'post')

def get_all_posts():
    results = select(('*',), 'post')
    return results



def get_all_user_posts(user_id):
    select(posts, user_id)

def create_post(columnvaluedict):
    insert('post', columnvaluedict)

create_post({
        'message': 'hello world! 12',
        'author_id': 76,
        'status': 2,
        'timestamp': '35/1/10/2016'
    })

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
