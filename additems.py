#This will be the modify items page for the seller
#----------Modules------------
import mysql.connector
from tkinter import *
from tkinter import tix
import os
from tkinter import messagebox as box
from PIL import ImageTk, Image
from sellerspart import execute1
name=""
#############################
def close():
      mastercopy.withdraw()
      sys.exit()
      
def additems():
      global name
      mydb=mysql.connector.connect(host="localhost",user="root",password="ooehs",charset="utf8")
      mycursor=mydb.cursor()
      mycursor.execute("create database if not exists seller")
      mycursor.execute("use seller")
      mycursor.execute("create table if not exists additems(nameofitem varchar(10),price integer,quantity integer)")
      
      nameofvar1=name.get()
      hello1,hello2=1,1
      imgadd1=image.get()
      checkvariable=0
      try:
            pri=price.get()
      except ValueError:
            box.showerror("ERROR 101","Invalid integer for price")
            deletefunc()
            hello1=0
      try:
            img=ImageTk.PhotoImage(Image.open(imgadd1))
      except IOError:
            box.showerror("Error 404","Enter Valid /image Location")
            checkvariable=1
      try:
            quantv1=quante.get()
      except ValueError:
            box.showerror("ERROR 101","Invalid integer for quantity")
            deletefunc()
            hello2=0
      print(nameofvar1,pri,quantv1)
      print(str(nameofvar1))
            
      if hello1!=0 and hello2!=0 and checkvariable!=1:
            print(nameofvar1,pri,quantv1)

            mycursor.execute("insert into additems values('{}',{},{})".format(nameofvar1,pri,quantv1))
            mydb.commit()
            mycursor.execute("select * from additems")
            x=mycursor.fetchall()
            for i in x:
                print(i)
                
            print("customer contents")
            mycursor.execute("create database if not exists customer")
            mycursor.execute("use customer")
            mycursor.execute("create table if not exists additems(nameofitem varchar(10),price integer,quantity integer)")
            mycursor.execute("insert into additems values('{}',{},{})".format(nameofvar1,pri,quantv1))
            mycursor.execute("select * from additems")
            for x in mycursor:
                       print(x)
            mydb.commit()
                          
            deletefunc()
            
def deletefunc():
      #Function to reset all values to the original ones
      name.delete(0,END)
      price.delete(0,END)
      quante.delete(0,END)
      image.delete(0,END)
      
def backbutton():
      execute1(mastercopy,"seller")
##############################
def nameofitem(mainmaster,master,v):
      global c1
      global frame
      global mastercopy
      global name
      global price
      global quante
      global image
      
      mastercopy=master
      master.bind('<Escape>',close)
      nameofseller="seller"
      frame=master
      frame.configure(height=750,width=700,background="black")
      frame.pack()
      #############################

      namel=Label(master,font='Avantagesmall',text="NAME OF ITEM",background=c1[0]).place(x=100,y=100)
      naitem=StringVar()
      name=Entry(master,fg="black",background="white",text="name of item",textvariable=naitem)
      name.place(x=350,y=100)

      pricef=IntVar()
      price1=Label(master,font='Avantagesmall',text="PRICE OF THE ITEM",background=c1[0]).place(x=100,y=150)
      price=Entry(master,background="white",textvariable=pricef)
      price.place(x=350,y=150)

      quantity1=IntVar()
      quant=Label(master,font='Avantagesmall',text="QUANTITY",background=c1[0]).place(x=100,y=200)
      quante=Entry(master,background="white",textvariable=quantity1)
      quante.place(x=350,y=200)

      img=Label(master,font='Avantagesmall',text="Image of the item",background=c1[0]).place(x=100,y=250)
      imgadd=StringVar()
      image=Entry(master,text="Image location",background="white",font='Avantagesmall',textvariable=imgadd)
      image.place(x=350,y=250)

      add=Button(master,background=c1[0],text="ADD ITEM",font='Avantagesmall',command=additems).place(x=200,y=350)
      

      back=Button(master,background=c1[0],text="Back",font='Avantagesmall',command=backbutton).place(x=350,y=350)

c1=['#44B3C2','#C92D22','#16776A','#1EBBA6']
