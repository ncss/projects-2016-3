import sqlite3

def select(table, where, *arg):
    connect = sqlite3.connect('db/database.db')
    cur = connect.cursor()
    if where:
        cur.execute('''select %s from %s where %s''' % (",".join(arg), table, where))
    else:
        cur.execute('''select %s from %s''' % (",".join(arg), table))
    results = cur.fetchall()
    cur.close()
    connect.close()
    return results

def insert(table, columnvaluedict):
    connect = sqlite3.connect('db/database.db')
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
    inserted_id = cur.lastrowid
    cur.close()
    connect.close()
    return inserted_id

def update(table, feild, value):
    connect = sqlite3.connect('db/database.db')
    cur = connect.cursor()
    cur.execute('''update %s set %s = %s''' % (table, field, value))
    results = cur.fetchall()
    cur.close()
    connect.close()
    return results