
#-----MODULES-----#
from tkinter import *
from tkinter import messagebox as box
from tkinter import font as tkfont
import os
import random
from tkinter import tix
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mysql.connector

global tagline2
def payment(master,name):
    parent= master
    parent1 = master
    parent.geometry("{0}x{1}+0+0".format(parent.winfo_screenwidth(), parent.winfo_screenheight()))
    parent.configure(background='black')

    parent2=Frame(parent,height=2000,width=2000)
    parent2.configure(background="black")
    parent2.pack()

    parent3=Frame(parent)
    parent4=Frame(parent)
    parent5=Frame(parent)
    parent6=Frame(parent)
    
    cart=Label(parent2, text='CART', font=('AvantageSmall',48), fg='white' , bg='black')
    cart.place(x=50,y=30)

    custom(parent2)

    f = tkfont.Font(tagline2, tagline2.cget("font"))        
    f.configure(underline = True)

    
    itemname=Label(parent2, text="Item Name",  font=("AvantageSmall", 20),fg='white',bg='black')
    itemname.place(x=55,y=150)
    itemname.configure(font=f)

    quantity=Label(parent2, text="Quantity",  font=("AvantageSmall", 20),fg='white',bg='black')
    quantity.place(x=470,y=150)
    quantity.configure(font=f)

    price=Label(parent2, text="Price",  font=("AvantageSmall", 20),fg='white',bg='black')
    price.place(x=855,y=150)
    price.configure(font=f)

    list2 = []
    list1=[]
    y=200
    mydb=mysql.connector.connect(host="localhost",user="root",password="ooehs",charset="utf8")
    mycursor=mydb.cursor()
    mycursor.execute("create database if not exists customer")
    mycursor.execute("use customer")
    mycursor.execute("select nameofitem from cart")
    for i in mycursor:
        for j in i:
            list1.append(j)
    
    mycursor.execute("select * from cart")
    for i in mycursor:
            list2.append(i)
    print ( "List2 contents",list2)
    
    mycursor.execute("create database if not exists userdb")
    mycursor.execute("use userdb")
    mycursor.execute("create table if not exists cartitems(S_no integer,Item_name varchar(20),quantity integer,price integer)")
    nameofitems=list2
    i=len(list1)
    total=0
    n=0
    while n<i:
     
        mycursor.execute("insert into cartitems values({},'{}','{}','{}')".format(n,nameofitems[n][0],nameofitems[n][2],nameofitems[n][1]))
        global nameofcust
        nameofcust = name

        item=Label(parent2, text=nameofitems[n][0],  font=("Avantagesmall", 15),fg='white',bg='black')
        item.place(x=55,y=y)

        quantity=Label(parent2, text=nameofitems[n][2],  font=("Avantagesmall", 15),fg='white',bg='black')
        quantity.place(x=470,y=y)
        price=Label(parent2, text=nameofitems[n][1],  font=("Avantagesmall", 15),fg='white',bg='black')
        price.place(x=855,y=y)

        
        total+=int(nameofitems[n][1])*int(nameofitems[n][2])
        y=y+50
        f2 = tkfont.Font(item, item.cget("font"))
        f2.configure(underline=True)

        n=n+1

    blankline=Label(parent2, text="                        ",  font=("AvantageSmall", 15),fg='white',bg='black')
    blankline.place(x=780,y=575)
    blankline.configure(font=f2)

    blankline2=Label(parent2, text="                        ",  font=("AvantageSmall", 15),fg='white',bg='black')
    blankline2.place(x=780,y=625)
    blankline2.configure(font=f2)
    
    tprice=Label(parent2, text=total,  font=("AvantageSmall", 15),fg='white',bg='black')
    tprice.place(x=855,y=610)

    tprice=Label(parent2, text="TOTAL",  font=("AvantageSmall", 15),fg='white',bg='black')
    tprice.place(x=785,y=610)

    colon=Label(parent2, text=": ", font=("Century Gothic",15),fg='white',bg='black')
    colon.place(x=840,y=607)

def custom(parent):
    #Custom#
    global tagline2
    hello=parent
    
    canvas=Canvas(hello,height=900,width=500,background='white')
    canvas.place(x=1010,y=0)

    tm=Label(hello,text='TM',font=('AvantageSmall',10),bg='white')
    tm.place(x=1290,y=28)
    
    ask=Label(hello,text='A S K',font=('AvantageSmall',60),bg='white')
    ask.place(x=1090,y=15)
    
    shoppers=Label(hello,text='S     H     O     P     P     E     R     S ', font=('AvantageSmall',8),bg='white')
    shoppers.place(x=1088,y=110)

    tagline=Label(hello,text="Shop", font=('AvantageSmall',30),bg='white')
    tagline.place(x=1088,y=240)

    tagline2=Label(hello,text="the",font=('AvantageSmall',20),bg='white')
    tagline2.place(x=1088,y=290)

    tagline3=Label(hello,text="Desire", font=('AvantageSmall',60),bg='white')
    tagline3.place(x=1088,y=318)

    
 

