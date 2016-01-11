import sqlite3
import os

def get_db_path():
    return os.path.join(os.path.dirname(__file__), '../db/database.db')

def select(table, where, *arg):
    connect = sqlite3.connect(get_db_path())
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
    connect = sqlite3.connect(get_db_path())
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


def update(table, field, value, whereClause):
    connect = sqlite3.connect('db/database.db')
    cur = connect.cursor()
    cur.execute('''update %s set %s = '%s' where %s;''' % (table, field, value, whereClause))
    results = cur.fetchall()
    connect.commit()
    cur.close()
    connect.close()
    return results
