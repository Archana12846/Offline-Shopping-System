from tkinter import *
from tkinter import tix
import os
global master
global mastercopy
#####################
def centerWindow(mastercopy):

      sw =1300
      sh = 1000

      x = (sw - 490)/2
      y = (sh - 550)/2
            
####################
def setvariable():
      import additems
      frame1.destroy()
      mastercopy.configure(background=c1[0])
      mastercopy.update()
      frame=Frame(mastercopy,background=c1[0])
      frame.pack()
      global hello
      hello="seller"
      p=additems.nameofitem(mastercopy,frame,hello)
######################
def setmodify():
      import modifyitems
      frame1.destroy()
      mastercopy.configure(background=c1[0])
      mastercopy.update()
      frame=Frame(mastercopy,background=c1[0])
      frame.pack()
      nameofseller="seller"
      p=modifyitems.nameofitem(mastercopy,frame,"seller")
######################
def setdelete():
      import deleteitem
      frame1.destroy()
      mastercopy.configure(background=c1[0])
      mastercopy.update()
      frame=Frame(mastercopy,background=c1[0])
      frame.pack()
      nameofseller="seller"
      p=deleteitem.nameofitem(mastercopy,frame,nameofseller)

def execute1(master,name):
      global c1
      global mastercopy
      global frame1
      
      mastercopy=master
      centerWindow(mastercopy)
      frame1=Frame(mastercopy)
      frame1.configure(height=500,width=500)
      frame1.pack()
      nameofseller="seller"
      display=Label(frame1,text="What do you want to do today?",font=("AvantageSmall",18),background="#44B3C2")
      display.place(x=40,y=60)
      add=Button(frame1,text="ADD ITEMS",command=setvariable,borderwidth=0,background="white",font=("Avante",15))
      modify=Button(frame1,text="MODIFY ITEMS",command=setmodify,borderwidth=0,background="white",font=("Avante",15))
      delete=Button(frame1,text="DELETE ITEMS",command=setdelete,borderwidth=0,background="white",font=("Avante",15))
      add.place(x=93,y=120)
      add.configure(height=1,width=27)
      modify.place(x=93,y=170)
      modify.configure(height=1,width=27)
      delete.place(x=93,y=220)
      delete.configure(width=27)

c1=['white','#C92D22','#16776A','#1EBBA6']

