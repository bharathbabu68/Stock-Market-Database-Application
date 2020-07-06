import sys
if sys.version_info[0] < 3:
    from Tkinter import *     ## Python 2.x
else:
    from tkinter import *
import backend
import ltbackend
from tkinter import font
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime
# from usernamefront import userreturn

#all the functions that deal witth backend
def buystock_command():
    import buystockfrontend
def viewlogs_command():
    logtable("view logs")
    import ltfrontend

def logtable(operation):
    currentDT = datetime.datetime.now()
    ltbackend.insert(currentDT.strftime("%d/%m/%Y") , currentDT.strftime("%H:%M:%S") , operation )


def marketcap_command():
    b=[]
    a=backend.get_marketcap()
    for row in a:
        b.append(row[0])
    return b

def lastprice_command():
    b=[]
    a=backend.get_lastprice()
    for row in a:
        b.append(row[0])
    return b

def sharename_command():
    b=[]
    a=backend.get_sharenames()
    for row in a:
        b.append(row[0])
    return b

def percentchange_command():
    b=[]
    a=backend.get_percentchange()
    for row in a:
        b.append(row[0])
    return b

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    e5.delete(0,END)
    e5.insert(END,selected_tuple[5])
    
def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
    logtable("view")
     

def search_command():
    list1.delete(0,END)
    for row in backend.search(cmpname_text.get(),industry_text.get(),lastprice_text.get(),change_text.get(),marketcap_text.get()):
        list1.insert(END,row)
    logtable("search")

def add_command():
	print(type(lastprice_text.get()))
	if float(lastprice_text.get())<0.0:
		a=("INTEGRITY CONSTRAINT:SHARE PRICE SHOULD NOT BE NEGATIVE",)
		list1.delete(0,END)
		list1.insert(END,a)
	else:	
		backend.insert(cmpname_text.get(),industry_text.get(),lastprice_text.get(),change_text.get(),marketcap_text.get())
		list1.delete(0,END)
		view_command()
		whichgraph_command()
		logtable("insert")



def whichcomapny_command():
	a=tkvar2.get()
	list1.delete(0,END)
	for row in backend.getcompanies(a):
		list1.insert(END,row)
	

    
def delete_command():
    backend.delete(selected_tuple[0])
    view_command()
    whichgraph_command()
    logtable("delete")

def update_command():
    backend.update(selected_tuple[0],cmpname_text.get(),industry_text.get(),lastprice_text.get(),change_text.get(),marketcap_text.get())
    view_command()
    whichgraph_command()
    logtable("update")

def clearall():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    list1.delete(0,END)
    logtable("clear all")

window = Tk(className='Python Examples - window Size')
window.configure(bg='#f0f0f0')

def graph1():
    data1 = {'Company': sharename_command(),
         'Share Price': lastprice_command()
        }
    df1 = DataFrame(data1,columns=['Company','Share Price'])
    figure1 = plt.Figure(figsize=(10,6), dpi=55)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, window)
    # bar1.get_tk_widget().place(x=50,y=100)
    bar1.get_tk_widget().place(x=650,y=375)
    df1 = df1[['Company','Share Price']].groupby('Company').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Company Vs. Share Price')
    logtable("graph plotted (bar)")

def graph2():
    data2 = {'Share Price': lastprice_command(),
         'MarketCap': marketcap_command()
        }
    df2 = DataFrame(data2,columns=['Share Price','MarketCap'])
    figure2 = plt.Figure(figsize=(10,6), dpi=55)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, window)
    line2.get_tk_widget().place(x=650,y=375)
    df2 = df2[['Share Price','MarketCap']].groupby('Share Price').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
    ax2.set_title('Market Cap Vs. Share Price')
    logtable("graph plotted (line)")
    # graph1()
# graph2()

def graph3():
    data3 = {'Percent Change': percentchange_command(),
         'Stock_Index_Price': lastprice_command()
        }
    df3 = DataFrame(data3,columns=['Percent Change','Stock_Index_Price'])
    figure3 = plt.Figure(figsize=(10,6), dpi=60)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(df3['Percent Change'],df3['Stock_Index_Price'], color = 'g')
    scatter3 = FigureCanvasTkAgg(figure3, window) 
    scatter3.get_tk_widget().place(x=650,y=375)
    ax3.legend(['Stock_Index_Price']) 
    ax3.set_xlabel('Percent Change')
    ax3.set_title('Percent Change Vs Stock Index Price')
    logtable("graph plotted (scatter)")

def whichgraph_command():
    if tkvar.get()=="Share Price vs Market Cap":
        graph2()
    elif tkvar.get()=="Company vs Share Price":
        graph1()
    else:
        graph3()
        

        
  
        

window.geometry("1200x700")
window.wm_title("Stock Exchange Database")

#labels
l1=Label(window,text="Company Name")
l1.place(x=0,y=200)
l2=Label(window,text="   Industry     ")
l2.place(x=0,y=250)
l3=Label(window,text=" Share Price  ")
l3.place(x=300,y=250)
l4=Label(window,text="  % Change")
l4.place(x=0,y=300)
l5=Label(window,text="   Market Cap  ")
l5.place(x=300,y=200)
sf= font.Font(family='Times New Roman', size=15)
l6=Label(window,text="   NIFTY-50 Top Performing Shares  ",font=sf)
l6.place(x=150,y=410)
rf= font.Font(family='Times New Roman BOLD', size=20)
l7=Label(window,text="-----Stock Exchange Database-----",font=rf)
l7.place(x=450,y=10)
l8=Label(window,text="  Graphs to analyze data ",font=sf)
l8.place(x=800,y=200)

#entry boxes
cmpname_text=StringVar()
e1=Entry(window,textvariable=cmpname_text)
e1.place(x=100,y=200)
industry_text=StringVar()
e2=Entry(window,textvariable=industry_text)
e2.place(x=100,y=250)
lastprice_text=StringVar()
e3=Entry(window,textvariable=lastprice_text)
e3.place(x=390,y=250)
change_text=StringVar()
e4=Entry(window,textvariable=change_text)
e4.place(x=100,y=300)
marketcap_text=StringVar()
e5=Entry(window,textvariable=marketcap_text)
e5.place(x=390,y=200)

#font for listbox
sf= font.Font(family='Helvetica', size=15)
list1=Listbox(window, height=10,width=50,font=sf)
list1.place(x=20,y=450)
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
list1.config(yscrollcommand=sb1.set)
sb1.config(command=list1.yview())
list1.bind('<<ListboxSelect>>',get_selected_row)


#photo buttons
photo1 = PhotoImage(file = r"view.png") 
b1=Button(window,text="", width=200,command=view_command,image=photo1,compound=RIGHT)
b1.place(x=0,y=50)
photo2 = PhotoImage(file = r"sarch.png") 
b2=Button(window,text="", width=200,command=search_command,image=photo2,compound=RIGHT)
b2.place(x=200,y=50)
photo3 = PhotoImage(file = r"insert.png") 
b3=Button(window,text="", width=200,command=add_command,image=photo3,compound=RIGHT)
b3.place(x=400,y=50)
photo4 = PhotoImage(file = r"update.png") 
b4=Button(window,text="", width=200,command=update_command,image=photo4,compound=RIGHT)
b4.place(x=600,y=50)
photo5 = PhotoImage(file = r"delete.png") 
b5=Button(window,text="", width=200,command=delete_command,image=photo5,compound=RIGHT)
b5.place(x=800,y=50)
photo6 = PhotoImage(file = r"close.png") 
b6=Button(window,text="", width=200,command=window.destroy,image=photo6,compound=RIGHT)
b6.place(x=1000,y=50)
b7=Button(window,text="Generate Graph",command=whichgraph_command)
b7.place(x=1050,y=250)
b8=Button(window,text="Clear All",command=clearall)
b8.place(x=200,y=350)
b9=Button(window,text="View Logs",command=viewlogs_command)
b9.place(x=270,y=350)
b11=Button(window,text="Buy Stocks",command=buystock_command)
b11.place(x=340,y=350)
b10=Button(window,text="View greater cost companies",command=whichcomapny_command)
b10.place(x=1000,y=300)



tkvar = StringVar(window)
choices = { "Share Price vs Market Cap","Company vs Share Price","Percent Change vs Stock Index Price"}
tkvar.set("Share Price vs Market Cap") # set the default option
popupMenu = OptionMenu(window, tkvar, *choices)
popupMenu.place(x=800,y=250)



tkvar2 = StringVar(window)
choices2 = { "Finance","Textiles","Banks","Computers","Telecommunications","Oil","Refineries"}
tkvar2.set("Computers") # set the default option
popupMenu2 = OptionMenu(window, tkvar2, *choices2)
popupMenu2.place(x=800,y=300)



graph2()
window.mainloop()

