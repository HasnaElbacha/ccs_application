from pickle import GLOBAL
from time import time
from tkinter import*
from PIL import ImageTk ,Image
import threading
import time
i=1
j=3
def acceuil():
  
  root=Tk()
  root.title("C.C.S")
  root.state("zoomed")
  root.geometry("800x550")
  root.config(background="#357ab7")
  root.config(background="#ffffff")

  btn_flechem=Image.open('.\\30.png')
  resize_btn_flechem = btn_flechem.resize((1367,120))
  photo_flechem=ImageTk.PhotoImage(resize_btn_flechem)
  bg_image=Label(root,image=photo_flechem,bd=0 ).place(x=0,y=1)

  ACC=Button(root,text="                     Acceuil                     ",bg="#318CE7",fg="#ffffff",bd=0,font=("times new roman",18)).place(x=0,y=120)
  pin=Button(root,text="                         Ping                        ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18)).place(x=342,y=120)
  par=Button(root,text="                      Parametre des adresses                     ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18)).place(x=695,y=120)
  sta=Button(root,text="                   Mon compte               ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18)).place(x=1060,y=120)

  photo='.\\2.png'
  btn_flechem1=Image.open(photo)
  resize_btn_flechem1 = btn_flechem1.resize((700,600))
  photo_flechem1=ImageTk.PhotoImage(resize_btn_flechem1)
  background1=Label(root,bd=0,image=photo_flechem1,width=700,height=600)
  background1.place(x=0,y=163)
  photo2='.\\4.png'
  btn_flechem2=Image.open(photo2)
  resize_btn_flechem2 = btn_flechem2.resize((700,600))
  photo_flechem2=ImageTk.PhotoImage(resize_btn_flechem2)
  background2=Label(root,bd=0,image=photo_flechem2,width=700,height=600)
  background2.place(x=700,y=163)
  def function1():
   global i
   global j
   threading.Timer(2.0, function1).start()
  
   if i==1:
    i=2
    j=3
    photo='.\\2.png'
    btn_flechem1=Image.open(photo)
    resize_btn_flechem1 = btn_flechem1.resize((700,600))
    photo_flechem1=ImageTk.PhotoImage(resize_btn_flechem1)
    background1=Label(root,bd=0,image=photo_flechem1,width=700,height=600)
    background1.place(x=0,y=163)
    photo2='.\\3.png'
    btn_flechem2=Image.open(photo2)
    resize_btn_flechem2 = btn_flechem2.resize((700,600))
    photo_flechem2=ImageTk.PhotoImage(resize_btn_flechem2)
    background2=Label(root,bd=0,image=photo_flechem2,width=700,height=600)
    background2.place(x=700,y=163)
    time.sleep(3)
    
   else :
    i=1
    j=4
    photo='.\\1.png'
    btn_flechem1=Image.open(photo)
    resize_btn_flechem1 = btn_flechem1.resize((700,600))
    photo_flechem1=ImageTk.PhotoImage(resize_btn_flechem1)
    background1=Label(root,bd=0,image=photo_flechem1,width=700,height=600)
    background1.place(x=0,y=163)
    photo2='.\\4.png'
    btn_flechem2=Image.open(photo2)
    resize_btn_flechem2 = btn_flechem2.resize((700,600))
    photo_flechem2=ImageTk.PhotoImage(resize_btn_flechem2)
    background2=Label(root,bd=0,image=photo_flechem2,width=700,height=600)
    background2.place(x=700,y=163)
    time.sleep(3)
  function1() 
#   photo2='.\\3.png'
#   btn_flechem2=Image.open(photo2)
#   resize_btn_flechem2 = btn_flechem2.resize((700,600))
#   photo_flechem2=ImageTk.PhotoImage(resize_btn_flechem2)
#   background2=Label(root,bd=0,image=photo_flechem2,width=700,height=600)
#   background2.place(x=700,y=163)
#   def function2():
#    global i
#    threading.Timer(3.0, function2).start()
#    print ("Hello, World!")
#    if i==3:
#     i=4
#     photo='.\\4.png'
#     btn_flechem2=Image.open(photo)
#     resize_btn_flechem2 = btn_flechem2.resize((700,600))
#     photo_flechem2=ImageTk.PhotoImage(resize_btn_flechem2)
#     background2=Label(root,bd=0,image=photo_flechem2,width=700,height=600)
#     background2.place(x=700,y=163)
#     time.sleep(3)
    
#    else :
#     i=3
#     photo2='.\\3.png'
#     btn_flechem2=Image.open(photo2)
#     resize_btn_flechem2 = btn_flechem2.resize((700,600))
#     photo_flechem2=ImageTk.PhotoImage(resize_btn_flechem2)
#     background2=Label(root,bd=0,image=photo_flechem2,width=700,height=600)
#     background2.place(x=700,y=163)
#     time.sleep(3)
#   function2() 
  
  root.mainloop()
# acceuil()