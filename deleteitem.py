#This will be the add items page for the seller
#----------Modules------------
import mysql.connector
from tkinter import *
from tkinter import tix
from tkinter import messagebox as box
from PIL import ImageTk, Image
import os
from sellerspart import execute1

#################################
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
      
def backbutton():
      execute1(mastercopy,"seller")

def delete():

      mydb=mysql.connector.connect(host="localhost",user="root",password="ooehs",charset="utf8",database="seller")
      mycursor=mydb.cursor()
      
      flag=0
      nameofvar1=name.get()

      mycursor.execute("delete from additems where nameofitem='{}'".format(nameofvar1))
      mycursor.execute("select * from additems")
      for i in mycursor:
            print(i)
      mydb.commit()
      
      print("customer contents")
      mycursor.execute("use customer")
      mycursor.execute("delete from additems where nameofitem='{}'".format(nameofvar1))
      mycursor.execute("select * from additems")
      for i in mycursor:
            print(i)
      mydb.commit()

############################################

def nameofitem(mainmaster,master,v):
      global c1
      global mastercopy
      global name
      global frame
      
      mastercopy=master
      nameofseller="seller"
      frame=master
      frame.configure(height=250,width=350,background="black")
      frame.pack()
      namel=Label(frame,text="NAME OF ITEM",background=c1[0]).place(x=50,y=50)
      nameofvar1=StringVar()
      name=Entry(frame,fg="black",background="white",text="name of item",textvariable=nameofvar1)
      name.place(x=150,y=50)

      add=Button(frame,background=c1[0],text="DELETE ITEM",command=delete).place(x=100,y=100)#Button to add items to the text file

      back=Button(frame,background=c1[0],text="Back",command=backbutton).place(x=200,y=100)

c1=['white','#C92D22','#16776A','#1EBBA6']                

