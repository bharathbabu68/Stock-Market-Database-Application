from tkinter import *
from tkinter import font
import userbackend
from simplecrypt import encrypt, decrypt

def add_command():
	ciphertext = encrypt('password',password_text.get())
	userbackend.insert(id_text.get(),name_text.get(),name_text.get(),password_text.get())	
	window.destroy()
	import userfrontend
def add_command():
	userbackend.insert(id_text.get(),name_text.get(),name_text.get(),password_text.get())
	
	window.destroy()
	import userfrontend
	print("done")
    
    
window = Tk()
window.configure(bg='#f0f0f0')

window.geometry("300x400")
window.wm_title("Create new account")

#labels
rf= font.Font(family='Times New Roman BOLD', size=20)
l1=Label(window,text="Create New Account",font=rf)
l1.place(x=0,y=0)
l2=Label(window,text="ID")
l2.place(x=0,y=50)
l3=Label(window,text="NAME")
l3.place(x=0,y=100)
l4=Label(window,text="AGE")
l4.place(x=0,y=150)
l5=Label(window,text="EMAIL ID")
l5.place(x=0,y=200)
l6=Label(window,text="PASSWORD")
l6.place(x=0,y=250)
l6=Label(window,text="CONFIRM PASSWORD")
l6.place(x=0,y=300)

id_text=StringVar()
e1=Entry(window,textvariable=id_text)
e1.place(x=150,y=50)

name_text=StringVar()
e2=Entry(window,textvariable=name_text)
e2.place(x=150,y=100)

age_text=StringVar()
e3=Entry(window,textvariable=age_text)
e3.place(x=150,y=150)

emailid_text=StringVar()
e4=Entry(window,textvariable=emailid_text)
e4.place(x=150,y=200)

password_text=StringVar()
e5=Entry(window,textvariable=password_text)
e5.place(x=150,y=250)

cpassword_text=StringVar()
e6=Entry(window,textvariable=cpassword_text)
e6.place(x=150,y=300)


b1=Button(window,text="Create your account", width=37,command=add_command)
b1.place(x=0,y=350)


window.mainloop()

