import sqlite3

def connect():
    conn=sqlite3.connect("dblog.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS LOG (id INTEGER PRIMARY KEY,actiondate text, actiontime text, action text)")
    conn.commit()
    conn.close()

def insert(actiondate,actiontime,action):
    conn=sqlite3.connect("dblog.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO LOG VALUES (NULL,?,?,?)",(actiondate,actiontime,action))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("dblog.db")
    cur=conn.cursor()
    cur.execute("SELECT actiondate,actiontime,action FROM LOG")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(actiondate="",actiontime="",action=""):
    conn=sqlite3.connect("dblog.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM LOG WHERE actiondate=? or actiontime=? OR action=? ", (actiondate,actiontime,action))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("dblog.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM LOG WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,actiontime,action):
    conn=sqlite3.connect("dblog.db")
    cur=conn.cursor()
    cur.execute("UPDATE LOG SET actiondate=?,actiontime=?, action=? WHERE id=?",(actiondate,actiontime,action,id))
    conn.commit()
    conn.close()

connect()