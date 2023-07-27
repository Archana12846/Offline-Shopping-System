#This will be the add items page for the seller
#----------Modules------------
import mysql.connector
from tkinter import *
from tkinter import tix
from tkinter import messagebox as box
from PIL import ImageTk, Image
import os
from sellerspart import execute1

def changefunc():
      st=st.strip()
      st=st.lower()
      str=st.split(" ")
      st=''
      for i in str:
            st=st+i
      return st

def deletefunc():                              #Function to reset all values to the original ones
      name.delete(0,END)
      pricee.delete(0,END)
      quantity.delete(0,END)
      image.delete(0,END)
            
def backbutton():
      execute1(mastercopy,"seller")

def modify():

      mydb=mysql.connector.connect(host="localhost",user="root",password="ooehs",charset="utf8",database="seller")
      mycursor=mydb.cursor()
      
      flag=0
      nameofvar1=name.get()
      hello1,hello2=1,1
      checkvariable=0
      imgadd1=image.get()
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
            
      if hello1!=0 and hello2!=0 and checkvariable!=1:

            mycursor.execute("update additems set price={} , quantity={} where nameofitem='{}'".format(pri,quantv1,nameofvar1))
            mycursor.execute("select * from additems")
            for i in mycursor:
                  print(i)
            mydb.commit()
                
            print("customer contents")
            mycursor.execute("use customer")
            mycursor.execute("create table if not exists additems(nameofitem varchar(10),price integer,quantity integer)")
            mycursor.execute("update additems set price={}, quantity={} where nameofitem= '{}' ".format(pri,quantv1,nameofvar1))
            mycursor.execute("select * from additems")
            for i in mycursor:
                       print(i)
            mydb.commit()
            

############################
def nameofitem(mainmaster,master,v):
            global c1
            global frame
            global name
            global price
            global quante
            global image
            global mastercopy

            mastercopy=master
            nameofseller="seller"
            frame=master
            frame.configure(height=800,width=800,background="black")
            frame.pack()

            namel=Label(frame,text="NAME OF ITEM",background=c1[0]).place(x=100,y=100)
            nameofvar1=StringVar()
            name=Entry(frame,fg="black",background="white",text="name of item",textvariable=nameofvar1)
            name.place(x=350,y=100)

            pricee=IntVar()
            price1=Label(frame,text="PRICE OF THE ITEM",background=c1[0]).place(x=100,y=150)
            price=Entry(frame,background="white",textvariable=pricee)
            price.place(x=350,y=150)
            pricee.set("0")

            quantity=IntVar()
            quant=Label(frame,text="QUANTITY",background=c1[0]).place(x=100,y=200)
            quante=Entry(frame,background="white",textvariable=quantity)
            quante.place(x=350,y=200)
            quantity.set("0")

            img=Label(frame,text="Image of the item",background=c1[0]).place(x=100,y=250)
            imgadd=StringVar()
            image=Entry(frame,text="Image location",background="white",textvariable=imgadd)
            image.place(x=350,y=250)

            add=Button(frame,background=c1[0],text="MODIFY ITEM",command=modify).place(x=200,y=350)#Button to add items to the text file

            back=Button(frame,background=c1[0],text="Back",command=backbutton)
            back.place(x=350,y=350)
            

#--------------Mainsection---------
c1=['white','#C92D22','#16776A','#1EBBA6']

