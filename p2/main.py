from tkinter import *
from tkinter import messagebox
import os

f = open("datafile","a+")
ui = Tk()
ui.title("pharmacy")
ui.configure(width=1500, height=600, bg = "black")

var = 1
def additem():
    global var
    num_line = 0
    with open("database_proj", "r") as f10:
        for i in f:
            num_line += 1
            
    var = num_line - 1
    e1= entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    f.write('{0} {1} {2} {3} {4}\n'.format(str(e1),e2,e3,str(e4),e5))
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)


def deleteitem():
    e1=entry1.get()
    with open(r"database_proj") as f, open(r"database_proj1", "w") as working:
        for line in f:
            if str(e1) not in line:
                working.write(line)
    os.remove(r"database_proj")
    os.rename(r"database_proj1", r"database_proj")
    f.close()
    working.close()
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

def firstitem():
    global var
    var=0
    f.seek(var)
    c=f.readline()
    v=list(c.split(" "))
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry1.insert(0,str(v[0]))
    entry2.insert(0,str(v[1]))
    entry3.insert(0,str(v[2]))
    entry4.insert(0,str(v[3]))
    entry5.insert(0,str(v[4]))

def nextitem():
    global var
    var = var + 1
    f.seek(var)
    try:
        c=f.readlines()
        xyz = c[var]
        v = list(xyz.split(" "))
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry1.insert(0, str(v[0]))
        entry2.insert(0, str(v[1]))
        entry3.insert(0, str(v[2]))
        entry4.insert(0, str(v[3]))
        entry5.insert(0, str(v[4]))
    except:
        messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")
def previousitem():
        global var
        var=var-1
        f.seek(var)
        try:
            z = f.readlines()
            xyz=z[var]
            v = list(xyz.split(" "))
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)

            entry1.insert(0, str(v[0]))
            entry2.insert(0, str(v[1]))
            entry3.insert(0, str(v[2]))
            entry4.insert(0, str(v[3]))
            entry5.insert(0, str(v[4]))
        except:
            messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")


def lastitem():
    global var
    f4=open("database_proj",'r')
    x=f4.read().splitlines()
    last_line= x[-1]
    num_lines = 0
    with open("database_proj", 'r') as f8:
        for line in f8:
            num_lines += 1
    var=num_lines-1
    print(last_line)
    try:
        v = list(last_line.split(" "))
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)

        entry1.insert(0, str(v[0]))
        entry2.insert(0, str(v[1]))
        entry3.insert(0, str(v[2]))
        entry4.insert(0, str(v[3]))
        entry5.insert(0, str(v[4]))
    except:
        messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")


def updateitem():

    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    e5 = entry5.get()
    with open(r"database_proj") as f1, open(r"database_proj1", "w") as working:
        for line in f1:
            if str(e1) not in line:
                working.write(line)
            else:
                working.write('{0} {1} {2} {3} {4}'.format(str(e1), e2, e3, str(e4), e5))
    os.remove(r"database_proj")
    #brought to you by code-projects.org
    os.rename(r"database_proj1", r"database_proj")


def searchitem():
    i=0
    e11 = entry1.get()
    with open(r"database_proj") as working:
        for line in working:
            i=i+1
            if str(e11) in line:
                break
        try:
            v = list(line.split(" "))
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry1.insert(0, str(v[0]))
            entry2.insert(0, str(v[1]))
            entry3.insert(0, str(v[2]))
            entry4.insert(0, str(v[3]))
            entry5.insert(0, str(v[4]))
        except:
            messagebox.showinfo("Title", "error end of file")
    working.close()


def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)    








Label0 = Label(ui, text="Make your List:", bg='black', fg = 'white', font = ('Times', 30))
Label1 = Label(ui, text="Enter Item Name ->", bg='black', fg = 'white', font = ('Times', 12))
entry1 = Entry(ui, font=("Times", 12))
Label2 = Label(ui, text="Enter Item Price ->", bg='black', fg = 'white', font = ('Times', 12))
entry2 = Entry(ui, font=("Times", 12))
Label3 = Label(ui, text="Enter Item Quantity ->", bg='black', fg = 'white', font = ('Times', 12))
entry3 = Entry(ui, font=("Times", 12))
Label4 = Label(ui, text="Enter Item Category ->", bg='black', fg = 'white', font = ('Times', 12))
entry4 = Entry(ui, font=("Times", 12))
Label5 = Label(ui, text="Enter Item Discount ->", bg='black', fg = 'white', font = ('Times', 12))
entry5 = Entry(ui, font=("Times", 12))
button1 = Button(ui,text="delete item", bg='white',fg='black', width=20,command=deleteitem)
button2 = Button(ui,text="view next item", bg='white',fg='black', width=20, command=nextitem)
button3 = Button(ui,text="view last item", bg='white',fg='black', width=20,command=lastitem)
button4 = Button(ui,text="search item", bg='white',fg='black', width=20,command=searchitem)
button5 = Button(ui,text="clear screen", bg='white',fg='black', width=20,command=clearitem)
button6 = Button(ui,text="add item", bg='white',fg='black', width=20,command=additem)
button7 = Button(ui,text="view first item", bg='white',fg='black', width=20,command=firstitem)
button8 = Button(ui,text="view privious item", bg='white',fg='black', width=20,command=previousitem)
button9 = Button(ui,text="update item", bg='white',fg='black', width=20,command=updateitem)
Label0.grid(columnspan= 6, padx=10, pady=10)
Label1.grid(row=1,column=0, padx=40, pady=10)
entry1.grid(row=1,column=2, padx=40, pady=10)
Label2.grid(row=2,column=0, padx=40, pady=10)
entry2.grid(row=2,column=2, padx=40, pady=10)
Label3.grid(row=3,column=0, padx=40, pady=10)
entry3.grid(row=3,column=2, padx=40, pady=10)
Label4.grid(row=4,column=0, padx=40, pady=10)
entry4.grid(row=4,column=2, padx=40, pady=10)
Label5.grid(row=5,column=0, padx=40, pady=10)
entry5.grid(row=5,column=2, padx=40, pady=10)
button1.grid(row=1,column=4, padx=40, pady=10)
button2.grid(row=2,column=4, padx=40, pady=10)
button3.grid(row=3,column=4, padx=40, pady=10)
button4.grid(row=4,column=4, padx=40, pady=10)
button5.grid(row=5,column=4, padx=40, pady=10)
button6.grid(row=1,column=3, padx=40, pady=10)
button7.grid(row=2,column=3, padx=40, pady=10)
button8.grid(row=3,column=3, padx=40, pady=10)
button9.grid(row=4,column=3, padx=40, pady=10)

ui.mainloop()