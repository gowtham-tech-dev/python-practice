#clear button for Radio needed

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox

w=Tk()
w.title("Form")
w.geometry('600x700')

def submit():
    if gender.get()==1:
        a=ch1.cget("text")
    if gender.get()==2:
        a=ch2.cget("text")
    b=[]
    if c1==1:
        b.append(cb1.cget("text"))
    if c2==1:
        b.append(cb2.cget("text"))
    if c3==1:
        b.append(cb3.cget("text"))
    data = f"Name:{ent_a.get()}\nRoll_no:{ent_b.get()}\nDept:{cmb_c.get()}\nLanguage:{b}\nGender:{a}\nYear_of_Birth:{spn_f.get()}"
    messagebox.showinfo("data", data)



def clear():
    ent_a.delete(0,END)
    ent_b.delete(0,END)
    cmb_c.delete(0,END)
    cb1.deselect()
    cb2.deselect()
    cb3.deselect()
    #clear response for Radiobox Needed
    spn_f.delete(0,END)
lab_a=Label(w,text="Name:",font=("Times",15))
lab_a.place(x=50,y=100)
lab_b=Label(w,text="Roll no:",font=("Times",15))
lab_b.place(x=50,y=150)
lab_c=Label(w,text="Dept:",font=("Times",15))
lab_c.place(x=50,y=200)
lab_d=Label(w,text="Language:",font=("Times",15))
lab_d.place(x=50,y=250)
lab_e=Label(w,text="Gender:",font=("Times",15))
lab_e.place(x=50,y=300)
lab_f=Label(w,text="YOB:",font=("Times",15))
lab_f.place(x=50,y=350)
ent_a=Entry(w,font=("Times",15),width=15)
ent_a.place(x=150,y=100)
ent_b=Entry(w,font=("Times",15),width=15)
ent_b.place(x=150,y=150)
cmb_c=Combobox(w,width=15)#combo box
cmb_c.place(x=150,y=200)
cmb_c["values"]=("Mechanical","Civil","EEE","ECE","CSE")
c1=IntVar #Checkbox
c2=IntVar
c3=IntVar
cb1=Checkbutton(w,text="Tamil",font=("Times",15),onvalue=1,offvalue=0,variable=c1)
cb1.place(x=150,y=250)
cb2=Checkbutton(w,text="English",font=("Times",15),onvalue=1,offvalue=0,variable=c2)
cb2.place(x=250,y=250)
cb3=Checkbutton(w,text="Hindi",font=("Times",15),onvalue=1,offvalue=0,variable=c3)
cb3.place(x=350,y=250)
gender=IntVar()#Radio box
ch1=Radiobutton(w,text="Male",font=("Times",15),value=1,variable=gender)
ch1.place(x=150,y=300)
ch2=Radiobutton(w,text="Female",font=("Times",15),value=2,variable=gender)
ch2.place(x=250,y=300)
spn_f=Spinbox(w,width=20,from_=1990,to=2025)#spin box
spn_f.place(x=150,y=350)
but_a=Button(w,text="Submit",font=("Times",15),bg="blue",fg="white",command=submit)
but_a.place(x=50,y=400)
but_b=Button(w,text="Cancel",font=("Times",15),bg="red",fg="white",command=clear)
but_b.place(x=150,y=400)
w.mainloop()