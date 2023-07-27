#------Modules-------
from tkinter import *
from PIL import ImageTk, Image
from tkinter import tix
from tkinter import messagebox as box
import string
import Payment
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="ooehs",charset="utf8")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists customer")
mycursor.execute("use customer")
def returnname():
      return name

def priceandquantity(master,price,quantity):                                                                              #Displaying the price and quantity
      frame=master
      frame.configure(bg="black")
      global c1,quant,qu
      price=price
      quantity=quantity
      frame.configure(height=100,width=100,padx=10,pady=10,bg='black')
      pricelabel=Label(frame,text='PRICE:',font="AvantageSmall",bg="black",fg="white",width=20).grid(row=0,column=0)
      qu=quantlabel=Label(frame,text='QUANTITY:',font="AvantageSmall",bg="black",fg="white",width=20).grid(row=1,column=0)
      price=Label(frame,text=price,bg="black",font="AvantageSmall",fg="white").grid(row=0,column=1)
      quant=Scale(frame,from_=0,to=int(quantity),bg="white")
      quant.grid(row=1,column=1)

####################################################
def back(root,v):
      
      import searchfunction
      parent = root
      d.destroy()
      parent.configure(background='black')
      s=searchfunction.searchbar(root,v)
      
def additems(l):
      mycursor.execute("create table if not exists cart(nameofitem varchar(10),price integer,quant integer)")
      print("the quanty=",quant.get())
      quantity=c
      mycursor.execute("insert into cart values('{}',{},{})".format(l[0],l[1],quant.get()))
      print("the quanti still is",quant.get())
      mycursor.execute("select * from cart")
      for i in mycursor:
                       print(i[0],"\t",i[1],"\t",c)
      print("yes,added")
      mydb.commit()
      box.showinfo("Cart","Added Item to cart")
def cart1():
      d.destroy()

      p=Payment.payment(tk,nameofcustomer)      
def cart(mainmaster,tkwindow,master,v,n,pri,quant):
      global b,c,d
      global tk ,nameofcustomer
##      a=img
      b=pri
      c=quant
      d=mainmaster
      cartt=Button(master,text="VIEW CART",command=cart1,width=20,height=2,font="AvantageSmall",bg="white")
      cartt.grid(row=20,column=0)
      priceandquantity(master,pri,quant)
      mainmaster.configure(bg="black")
      tk=tkwindow
      master=master
      nameofcustomer=v
      m=[n,pri]
      cartbutton=Button(master,text='ADD TO CART',bg="white",width=20,height=2,font="AvantageSmall",command=lambda: additems(m))
      cartbutton.grid(row=14,column=0)

      backbutton=Button(master,text='BACK TO SHOPPING',bg="white",width=20,height=2,font="AvantageSmall",command=lambda: back(tk,v))
      backbutton.grid(row=26,column=0)
      
def pulldownmenu(master,v):
      menubar=Menu(master)

      #Creating a display of the sellers name
      display=Menu(menubar,tearoff=0)
      display.add_command(label="Go to cart")
      name="Hello"+" "+v
      menubar.add_cascade(label=name,menu=display)
      master.config(menu=menubar)

#---------------Mainsection----------------------
c1=['white','#C92D22','#16776A','#1EBBA6']
