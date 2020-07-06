from tkinter import *
from tkinter import font
import ltbackend

window=Tk()
def backto_command():
    view_command()
    
def view_command():
    list1.delete(0,END)
    for row in ltbackend.view():
        # list1.insert(END,row)
        list1.insert(END, ('{}      {}     {}   ').format(*row)) 
     
window.configure(bg='#f0f0f0')
window.geometry("575x350")
window.wm_title("Log Table")
sf= font.Font(family='Helvetica', size=15)
list1=Listbox(window, height=10,width=50,font=sf)
list1.place(x=0,y=0)
view_command()
b9=Button(window,text="Refresh",command=backto_command)
b9.place(x=215,y=275)
window.mainloop()