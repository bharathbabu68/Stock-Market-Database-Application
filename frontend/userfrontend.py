from tkinter import *
import userbackend
from tkinter import font

def userreturn():
	return username_text.get()

	
def check():
	for row in userbackend.search(username_text.get()):
		if row[0]==password_text.get():
			window.destroy()
			import frontend
		
def create():
	window.destroy()
	import newaccount

	
window = Tk()
window.configure(bg='#f0f0f0')


window.geometry("225x225")
window.wm_title("Stock Exchange Database")

#labels
rf= font.Font(family='Times New Roman BOLD', size=20)
l7=Label(window,text="--Stock Exchange--",font=rf)
l7.place(x=0,y=0)
rf1= font.Font(family='Times New Roman BOLD', size=15)
l8=Label(window,text="Login",font=rf1)
l8.place(x=0,y=40)
l1=Label(window,text="Username")
l1.place(x=0,y=80)
l2=Label(window,text="Password")
l2.place(x=0,y=110)


#entry boxes
username_text=StringVar()
e1=Entry(window,textvariable=username_text)
e1.place(x=70,y=80)
password_text=StringVar()
e2=Entry(window,textvariable=password_text)
e2.place(x=70,y=110)

#photo buttons

b1=Button(window,text="login", width=20,command=check)
b1.place(x=15,y=150)
b2=Button(window,text="create account", width=20,command=create)
b2.place(x=15,y=180)



window.mainloop()

