import sqlite3

def connect():
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS STOCKS (id INTEGER PRIMARY KEY, cmpname text, industry text, lastprice integer, change integer,marketcap integer)")
    conn.commit()
    conn.close()

def insert(cmpname,industry,lastprice,change,marketcap):
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO STOCKS VALUES (NULL,?,?,?,?,?)",(cmpname,industry,lastprice,change,marketcap))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM STOCKS")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(cmpname="",industry="",lastprice="",change="",marketcap=""):
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM STOCKS WHERE cmpname=? OR industry=? OR lastprice=? OR change=? OR marketcap=?", (cmpname,industry,lastprice,change,marketcap))
    rows=cur.fetchall()
    conn.close()
    return rows

def getcompanies(industry=""):
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM STOCKS WHERE lastprice>(select lastprice from stocks where industry=?) and industry!=?", (industry,industry))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM STOCKS WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,cmpname,industry,lastprice,change,marketcap):
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("UPDATE STOCKS SET cmpname=?, industry=?, lastprice=?, change=?, marketcap=? WHERE id=?",(cmpname,industry,lastprice,change,marketcap,id))
    conn.commit()
    conn.close()

def get_marketcap():
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("SELECT marketcap FROM STOCKS")
    rows=cur.fetchall()
    conn.close()
    return rows

def get_lastprice():
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("SELECT lastprice FROM STOCKS")
    rows=cur.fetchall()
    conn.close()
    return rows

def get_sharenames():
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("SELECT cmpname FROM STOCKS")
    rows=cur.fetchall()
    conn.close()
    return rows

def get_percentchange():
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("SELECT change FROM STOCKS")
    rows=cur.fetchall()
    conn.close()
    return rows

def getbyindustry(industry):
    conn=sqlite3.connect("stocks.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM STOCKS where industry=?",(industry,))
    rows=cur.fetchall()
    conn.close()
    return rows

def trigger():
	conn=sqlite3.connect("stocks.db")
	cur=conn.cursor()
	cur.execute("create or replace trigger as is check before insert on STOCKS  for each row begin if (:new.lastprice<0) then raise_application_error(-2000,?)end if;end;/")
	conn.close()
    	
   	
    		
connect()