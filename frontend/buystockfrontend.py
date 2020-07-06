from tkinter import *
from tkinter import font
import backend
import buystockbackend

window=Tk()


def cartview_command():
    window.geometry("575x455")
    l3label_text.set("Welcome " + user_text.get() +" Here's Your Portfolio")
    list1.delete(0,END)
    # list1.insert(END,("Username","Company_Name","No_of_shares","Estimated_Value"))
    for row in buystockbackend.view(user_text.get()):
        list1.insert(END, ('{}      {}     {}    {}').format(*row)) 



def sizer_command():
    window.geometry("575x700")
def buy_command():
    buystockbackend.insert(user_text.get(),retrieveid_text.get(),noofshares_text.get())
    list1.delete(0,END)
    list1.insert(END,("***Transaction_Complete***",))
    window.geometry("575x500")


def view_command():
    l3label_text.set("Available Shares")
    window.geometry("575x455")
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)


def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e2.delete(0,END)
    e2.insert(END,selected_tuple[1])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e5.delete(0,END)
    e5.insert(END,selected_tuple[0])
     
window.configure(bg='#f0f0f0')
window.geometry("575x455")
window.wm_title("Buy Stocks")


sf= font.Font(family='Helvetica', size=15)
list1=Listbox(window, height=10,width=50,font=sf)
list1.place(x=10,y=150)
list1.bind('<<ListboxSelect>>',get_selected_row)

#labels
rf= font.Font(family='Times New Roman BOLD', size=20)
l1=Label(window,text="------Buy Stocks------  ",font=rf)
l1.place(x=145,y=0)
l2=Label(window,text="User: ")
l2.place(x=0,y=50)
rf1= font.Font(family='Times New Roman BOLD', size=14)
l3label_text=StringVar()
l3=Label(window,textvariable=l3label_text,font=rf1)
l3.place(x=0,y=115)

l3label_text.set("Available Shares")
rf2= font.Font(family='Times New Roman BOLD', size=10)
l4=Label(window,text="You have chosen to buy the following",font=rf2)
l4.place(x=25,y=470)
l5=Label(window,text="Company ")
l5.place(x=25,y=500)
l6=Label(window,text="Share Price ")
l6.place(x=225,y=500)
l7=Label(window,text="Enter no of shares : ")
l7.place(x=25,y=550)






#buttons
b1=Button(window,text="View All",command=view_command)
b1.place(x=125,y=420)
b2=Button(window,text="Buy Now",command=sizer_command)
b2.place(x=225,y=420)
b4=Button(window,text="View Cart",command=cartview_command)
b4.place(x=325,y=420)
b3=Button(window,text="Confirm Purchase",command=buy_command)
b3.place(x=25,y=600)



#entry
user_text=StringVar()
e1=Entry(window,textvariable=user_text)
e1.place(x=35,y=50)
cmp_text=StringVar()
e2=Entry(window,textvariable=cmp_text)
e2.place(x=85,y=500)
share_text=StringVar()
e3=Entry(window,textvariable=share_text)
e3.place(x=290,y=500)
noofshares_text=StringVar()
e4=Entry(window,textvariable=noofshares_text)
e4.place(x=125,y=550)
retrieveid_text=StringVar()
e5=Entry(window,textvariable=retrieveid_text)
e5.place(x=1000,y=1000)




window.mainloop()
