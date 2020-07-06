import sqlite3
def findestvalue(shareid,noshares):
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("SELECT lastprice*? from STOCKS where id=?",(noshares,shareid,))
    rows=cur.fetchall()
    return rows
    conn.close()


def connect():
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS userstocks ( usrname text, shareid int, noshares int, estvalue int)")
    conn.commit()
    conn.close()


def search(usrname=""):
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("SELECT estvalue FROM userstocks WHERE shareid=?", (shareid,))
    rows=cur.fetchall()
    conn.close()
    return rows



def insert(usrname,shareid,noshares):
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO userstocks VALUES (?,?,?,?)",(usrname,shareid,noshares,findans(shareid,noshares)))
    conn.commit()
    conn.close()
    
def view(usrname=""):
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("SELECT usrname,cmpname,noshares,estvalue from userstocks,STOCKS where stocks.id=userstocks.shareid and usrname=?",(usrname,))
    rows=cur.fetchall()
    conn.close()
    return rows
    
def viewall(estvalue=""):
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("SELECT usrname from userstocks where estvalue<?",(estvalue,))
    rows=cur.fetchall()
    conn.close()
    print(rows)    
    
def all():
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("select * FROM userstocks")
    conn.commit()
    rows=cur.fetchall()
    conn.close()    
    print(rows)
   
def findans(shareid,noshares):
    a=findestvalue(shareid,noshares)
    b=int(a[0][0])
    return b

connect()

# insert("hari",1,15)
all()
viewall(4)
