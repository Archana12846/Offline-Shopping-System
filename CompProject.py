import mysql.connector
from tkinter import messagebox as box
import os
from tkinter import tix
from tkinter import *

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

########################################
mydb=mysql.connector.connect(host="localhost",port="3307",user="root",password="ooehs",charset="utf8")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists seller")
mycursor.execute("use seller")

mycursor.execute("CREATE TABLE IF NOT EXISTS admin (username varchar(20) primary key, password varchar(20))")
mycursor.execute("SELECT * FROM admin WHERE username = 'seller' AND password = 'seller'")
if mycursor.fetchone() is None:
    mycursor.execute("INSERT INTO admin (username, password) VALUES('seller', 'seller')")
    mydb.commit()
    

def quit():
        root.destroy()

def getuserpass():
        username=entry_user.get().lower()
        password=entry_pass.get()
        
def login():
            global frame
            username=entry_user.get().lower()
            password=entry_pass.get()
            if entry_user.get == "" or entry_pass.get() == "":
                messagebox.showinfo("msg","Please complete the required field!")
            else:
                mycursor.execute("SELECT * FROM admin")
                b=mycursor.fetchall()
                usernames=pl=[]
                for x in b:
                    for j in x:
                        pl.append(j)
                if entry_user.get!="seller" or entry_pass.get!="seller":
                    print(pl[0] ,pl[1])

            if password=='':
                box.showerror('ERROR','Please enter a password before trying to login')
            else:
                if username.strip() not in pl:
                    box.showerror('ERROR',"That username wasn't found in our directory.\nPlease sign up first")
            if username.strip() in usernames:
                if password=="seller":
                    frame.destroy()
                    root.configure(bg="darkblue")

                    timeframe=Frame(root,bg='white',height=1500,width=1500)
                    timeframe.pack()
                    canvas=Canvas(timeframe,height=900,width=500,background='white')
                    canvas.place(x=110,y=0)

                    tm=Label(timeframe,text='TM',font=('Avantagesmall',10),bg='white')
                    tm.place(x=290,y=28)
                    
                    ask=Label(timeframe,text='A S K',font=('Avantagesmall',60),bg='white')
                    ask.place(x=190,y=15)
                    
                    shoppers=Label(timeframe,text='S     H     O     P     P     E     R     S ', font=('Avantagesmall',8),bg='white')
                    shoppers.place(x=188,y=110)

                    tagline=Label(timeframe,text="Shop", font=('Avantagesmall',30),bg='white')
                    tagline.place(x=188,y=240)

                    tagline2=Label(timeframe,text="the",font=('Avantagesmall',20),bg='white')
                    tagline2.place(x=188,y=290)

                    tagline3=Label(timeframe,text="Desire", font=('Avantagesmall',60),bg='white')
                    tagline3.place(x=188,y=318)

                    tagline4=Label(timeframe,text="Loading...",font=('Avantagesmall',20),bg='white')
                    tagline4.place(x=220,y=410)

                    timeframe.after(3000,lambda:timeframe.destroy())
                    frame=Frame(root)
                    frame.destroy()
                    import sellerspart
                    e=sellerspart.execute1(root,username.strip())
                else:
                    box.showerror('ERROR','Incorrect username/password entered.\nPlease enter valid details')
                    entry_pass.delete(0,'end')
        

##########################
c=0
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

login = Button(frame, text="Log In", font=('Avantagesmall', 15),command=login, background='white', fg='black', height=2, width=10)
login.place(x= 270, y = 339)

quit_button = Button(frame, text="Quit", font=('Avantagesmall', 18), command=quit, background='white', fg='black', height=1, width=5)
quit_button.place(x= 480, y = 425)

root.mainloop()
