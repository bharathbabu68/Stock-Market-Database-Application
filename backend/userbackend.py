import sqlite3

def connect():
    conn=sqlite3.connect("logininfo.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS USER2 (id INTEGER , name text, age INTEGER,password text)")
    conn.commit()
    conn.close()


def search(name=""):
    conn=sqlite3.connect("logininfo.db")
    cur=conn.cursor()
    cur.execute("SELECT password FROM USER2 WHERE name=?", (name,))
    rows=cur.fetchall()
   
    conn.close()
    return rows


def insert(id,name,age,password):
    conn=sqlite3.connect("logininfo.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO USER2 VALUES (?,?,?,?)",(id,name,age,password))
  
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("logininfo.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM USER2")
    rows=cur.fetchall()
    conn.close()
   


connect()
