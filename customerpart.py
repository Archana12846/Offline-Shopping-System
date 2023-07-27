#-----MODULES-----#
##import mysql.connector
from tkinter import *
from tkinter import messagebox as box
from PIL import ImageTk, Image
import os
from tkinter import tix
import mysql.connector

global root
root=Tk()
frame=Frame(root)
root.title('ASK SHOPPERS  |  2019-2020')
root.configure(background='Black')
##########################

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw - 490)/2
y = (sh - 550)/2            
root.geometry("%dx%d+%d+%d" %(600,500,x,y))
###############################
mydb=mysql.connector.connect(host="localhost",user="root",password="ooehs",charset="utf8")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists customer")
mycursor.execute("use customer")

mycursor.execute("CREATE TABLE IF NOT EXISTS admin (username varchar(20), password varchar(20))")
mycursor.execute("SELECT * FROM admin WHERE username = 'customer' AND password = 'customer'")
if mycursor.fetchone() is None:
    mycursor.execute("INSERT INTO admin (username, password) VALUES('customer', 'customer')")
mydb.commit()

def quit():
        root.destroy()

def getuserpass():
        username=entry_user.get().lower()
        password=entry_pass.get()
        
###############################
##############################
def login():
        global frame
        
        usernames=p=[]
        username=entry_user.get().lower()
        password=entry_pass.get()
        if entry_user.get == "" or entry_pass.get() == "":
            messagebox.showinfo("msg","Please complete the required field!")
        mycursor.execute("SELECT * FROM admin")
        b=mycursor.fetchall()
        for x in b:
            for j in x:
                p.append(j)
        if entry_user.get!="customer" or entry_pass.get!="customer":
            print(p[0] ,p[1])

        if password=='':
            box.showerror('ERROR','Please enter a password before trying to login')
##################################################        
        if "customer" in usernames:
            if password=="customer":
                frame.destroy()
                root.configure(bg="darkblue")
                import searchfunction
                s=searchfunction.searchbar(root,"customer")
            else:
                box.showerror('ERROR','Incorrect username/password entered.\nPlease enter valid details')
                entry_pass.delete(0,'end')


##########################
frame.configure(height=600,width=600,bg='Black')
frame.pack()

login_label=Label(frame, text='LOGIN SCREEN', font=('Avantagesmall',50), fg='white', background='black')
login_label.place(x=90,y=100)
user_label=Label(frame, text="Enter/Choose your username: ",  font=('Avantagesmall', 13), fg='white', background='black', width=30)
user_label.place(x=0,y=190)
pass_label=Label(frame, text="Enter/Choose your password: ",  font=('Avantagesmall', 13), fg='white', background='black', width=30)
pass_label.place(x=0,y=270)

entry_user = Entry(frame, width = 25, font=("Avantagesmall", 13),background='white',fg='black')
entry_user.place(x=300, y=190)
        
entry_pass = Entry(frame, width = 25, font=("Avantagesmall", 13),background='white',fg='black')
entry_pass.place(x=300, y=270)

login = Button(frame, text="Log In", font=('Avantagesmall', 12),command=login, background='white', fg='black', height=1, width=10)
login.place(x= 270, y = 339)

quit_button = Button(frame, text="Quit", font=('Avantagesmall', 18), command=quit, background='white', fg='black', height=1, width=5)
quit_button.place(x= 480, y = 425)

root.mainloop()

#-----MAIN_SECTION-----#
