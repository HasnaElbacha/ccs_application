from pickle import GLOBAL
from time import time
from tkinter import*
from PIL import ImageTk ,Image
import threading
import time
import ping1
import parametre
import Connexion
import PAGE1
i=1
j=3
x=1
def acc(results):
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
  def dec():
    root.destroy()
    Connexion.connexion()
  ping = Image.open('.\\68.png')
  resize_ping = ping.resize((100,100))
  ping=ImageTk.PhotoImage(resize_ping)
  button=Button(image=ping,bg='white',activebackground='white',cursor='hand2',command=dec)
  button.place(x=1260,y=10,height=100,width=100)

  def pass_ping():
    root.destroy()
    ping1.ping(results)
  def pass_parametre():
    root.destroy()
    parametre.parametre(results)
  def pass_compte():
    root.destroy()
    PAGE1.compte(results)
  ACC=Button(root,text="                     Acceuil                     ",bg="#318CE7",fg="#ffffff",bd=0,font=("times new roman",18)).place(x=0,y=120)
  pin=Button(root,text="                         Ping                        ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18),command=pass_ping).place(x=342,y=120)
  par=Button(root,text="             Parametre des adresses                    ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18),command=pass_parametre).place(x=695,y=120)
  sta=Button(root,text="                   Mon compte               ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18),command=pass_compte).place(x=1060,y=120)

  background1=Label(root,bd=0,width=700,height=600)
  background1.place(x=0,y=163)
  background2=Label(root,bd=0,width=700,height=600)
  background2.place(x=700,y=163)

  im1=Image.open("1.png")
  resize_1 = im1.resize((700,600))
  img1=ImageTk.PhotoImage(resize_1)
  im2=Image.open("2.png")
  resize_2 = im2.resize((700,600))
  img2=ImageTk.PhotoImage(resize_2)
  im3=Image.open("3.png")
  resize_3 = im3.resize((700,600))
  img3=ImageTk.PhotoImage(resize_3)
  im4=Image.open("4.png")
  resize_4 = im4.resize((700,600))
  img4=ImageTk.PhotoImage(resize_4)  
  def move1():
    global x
    if x==1:
        background1.config(image=img1)
        background2.config(image=img4)
        x=2
    elif x==2:
        background1.config(image=img2)
        background2.config(image=img3)
        x=1
    root.after(2000,move1)

  move1()
  root.mainloop()
 #acc()