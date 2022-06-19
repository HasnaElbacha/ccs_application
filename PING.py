from time import time
from tkinter import*
from PIL import ImageTk ,Image
import random
import time
def ping():
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

  ACC=Button(root,text="                     Acceuil                     ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18)).place(x=0,y=120)
  pin=Button(root,text="                         Ping                        ",bg="#318CE7",fg="#ffffff",bd=0,font=("times new roman",18)).place(x=342,y=120)
  par=Button(root,text="                      Parametre                     ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18)).place(x=695,y=120)
  sta=Button(root,text="                   Statistique               ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18)).place(x=1060,y=120)

# frame_login=Frame(root,bg="#318CE7")
# frame_login.place(x=5,y=210,height=450,width=1250)

  tit=Label(text="Testez-vous votre connexion réseau",font=("Impact",25,"bold"),fg="#22780F",bg="white").place(x=475,y=180)
  Des=Label(text="Choissez-vous le périphérique que vous voulez tester",font=("Goudy old style",20,"bold"),fg="#22780F",bg="white").place(x=450,y=230)

  btn_f=Image.open('.\\13.png')
  resize_btn_f = btn_f.resize((400,400))
  photo_f=ImageTk.PhotoImage(resize_btn_f)
  bg_image=Label(root,image=photo_f,bd=0 ).place(x=1000,y=345)

  CARTE=Label(text=" Carte ethernet ",font=("italic",15,"bold"),fg="#000000",bg="#FFFFFF").place(x=100,y=400)
  ROUTER=Label(text="        Router      ",font=("italic",15,"bold"),fg="#000000",bg="#FFFFFF").place(x=100,y=460)
  SERVER=Label(text="   Local server  ",font=("italic",15,"bold"),fg="#000000",bg="#FFFFFF").place(x=100,y=520)
  HOTE=Label(text="         Hote        ",font=("italic",15,"bold"),fg="#000000",bg="#FFFFFF").place(x=100,y=580)


  root.mainloop()
# ping()