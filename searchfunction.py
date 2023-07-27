#Search Function
#---------------Modules------------------
from tkinter import *
from tkinter import tix
import string
import objectdisplay
from tkinter import font as font
from tkinter import messagebox as box
import random
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="ooehs",charset="utf8")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists customer")
mycursor.execute("use customer")

#--------------Class-----------------------


def searchbar(master,v):
      global c1
      global entry
      global root
      global nameofcustomer
      global st
      st=''
      
      nameofcustomer="customer"
      root=master
      root.configure(bg='black')

      global frame
      frame=Frame(master,height=1000,width=1000,bg='black')
      frame.pack()

      today=Frame(master,height=600,width=600,bg='black')
      today.pack(side=TOP)

      todaydeal(today,v)

      search=StringVar()
      entry=Entry(frame,textvariable=search,bg="white",width=71,font=('AvantageSmall','10'))
      entry.place(x=700,y=700)
      entry.pack()
      search.set("What are you looking for?")

      global frame1
      frame1=Frame(frame)                                     #Sample Frame on top of which another frame is made so that the products are displayed under the search bar
      frame1.pack(side=TOP)
      global frame2
      frame2=Frame(frame1)                              #Frame where the name of the products are displayed
      frame2.pack(side=TOP)
      
      entry.bind("<Button-1>",clear)
      entry.bind("<Key>",hello1)


def change(variable):                                                                                                    #Function to convert the variables to a lower case and no space string
      t=variable.split(' ')
      changevariable=''
      for k in t:
            changevariable+=k
      changevariable=changevariable.lower()
      return changevariable.strip()

def clear(event):
      entry.delete(0,END)

def hello1(event):
      global frame3
      i2=0
      
      searchitem=entry.get()
      global frame2
      frame2.destroy()
      
      frame2=Frame(frame1)                                #Each time the person enters a letter this function is called the frame where the names are displayed is deleted so that the new names can be displayed
      frame2.pack(side=TOP)

      list2 = []

      mycursor.execute("select nameofitem from additems")
      for i in mycursor:
            for j in i:
                  list2.append(j)

      print (list2)

      variable=1
      a=0
      print("The entered value=",searchitem)
      if searchitem!='':
            for i in list2:
                  i1=change(i)                                                #Function to convert the variable into a lower case variable with no spaces so that all the variables have the familiar type
                  searchitem=change(searchitem)
                  if len(i1)>=len(searchitem):                         #Checking first if the length of the entered variable is less than the name of the existing variable
                        mnum=len(searchitem)
                        if i1[0:mnum]==searchitem:
                              st=i
                              display1=Button(frame2,width=70,height=2,bg='white',text=i,command=lambda m=i :open1(m),borderwidth=0,relief="sunken",textvariable=i1).pack(side=BOTTOM)
                              variable=0
                              a+=1

                        elif variable==1:                                             #If the variable doesnot entirely match with the entered variable then we check if the first letter matches with the variable
                              if i[0]==searchitem[0]:
                                    display2=Button(frame2,width=70,height=2,bg='white',text=i,relief="sunken",borderwidth=0,command=lambda m=i :open1(m)).pack(side=BOTTOM)
                                    a+=1    

      else:
            if a==0:
                  display3=Button(frame2,width=70,height=2,bg='white',text="Product Not Found",relief=SUNKEN,borderwidth=0).pack(side=BOTTOM)
                  

def open1(st):
      frame.destroy()#Deleting all the searchbar frames
      frame1.destroy()
      frame2.destroy()
      global c1
      str=st
      print (str)
      productdetails=[]
      mycursor.execute("select * from additems where nameofitem='{}'".format(str))
      for i in mycursor:
            for j in i:
                  productdetails.append(j)                  
            
      framet.destroy()
      root.configure(bg='black')
      mainframe=Frame(root,bg='black')     #A frame where the objects name price image is being displayed
      mainframe.pack()
      print (productdetails)
      frame4=Frame(mainframe)
      frame4.pack(side=LEFT)

##      o=objectdisplay.objectheader(frame4,str)
####      image=productdetails[-1]
##      image=str+".jpg"
##      print("image=",image)
##      o2=objectdisplay.objectimage(frame4,image)

      frame5=Frame(mainframe)
      frame5.pack(side=RIGHT)
      price=productdetails[1]
      quantity=productdetails[2]
      c=objectdisplay.cart(mainframe,root,frame5,nameofcustomer,str,price,quantity)
##      
##
      p2=objectdisplay.pulldownmenu(root,nameofcustomer)
      
def todaydeal(master,v):

      global framet
      framet=master
      deal=Label(framet,text="Today's Deal",font=('AvantageSmall','18'),bg='black',fg='white')
      deal.place(x=200,y=200)
      deal.pack(side=TOP)

#-------------MainSection---------------
c1=['white','#C92D22','#16776A','#1EBBA6']
