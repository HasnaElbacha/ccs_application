from time import time
from tkinter import*
from PIL import ImageTk ,Image
import random
import time
import home
import ping1
import parametre
import PAGE2
import sqlite3
import Connexion
from tkinter import messagebox as ms
from tkinter import messagebox
import Connexion
def compte(results):
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
  def pass_home():
    root.destroy()
    home.acc(results)
  def pass_ping():
    root.destroy()
    ping1.ping(results)
  def pass_parametre():
    root.destroy()
    parametre.parametre(results)
  ACC=Button(root,text="                     Acceuil                     ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18),command=pass_home).place(x=0,y=120)
  pin=Button(root,text="                         Ping                        ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18),command=pass_ping).place(x=342,y=120)
  par=Button(root,text="            Parametre des adresses                     ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18),command=pass_parametre).place(x=695,y=120)
  sta=Button(root,text="                 Mon compte               ",bg="#318CE7",fg="#ffffff",bd=0,font=("times new roman",18)).place(x=1060,y=120)

# frame_login=Frame(root,bg="#318CE7")
# frame_login.place(x=60,y=210,height=450,width=1250)

  tit=Label(text=" Mon compte ",font=("Impact",25,"bold"),fg="#22780F",bg="white").place(x=665,y=195)


  btn_f=Image.open('.\\65.png')
  resize_btn_f = btn_f.resize((100,100))
  photo_f=ImageTk.PhotoImage(resize_btn_f)
  bg_image=Label(root,image=photo_f,bd=0 ).place(x=565,y=180)

  print(results)
  NOM=Label(root,text="    Nom complet :  ",font=("Goudy old style",15,"bold"),fg="WHITE",bg="black").place(x=480,y=370)
  NOM1=Label(root,text=results[0][1],font=("Goudy old style",15,"bold"),fg="WHITE",bg="BLACK",width=30).place(x=630,y=370)

  email=Label(root,text="       Email :     ",font=("Goudy old style",15,"bold"),fg="WHITE",bg="black").place(x=480,y=450)
  NOM1=Label(root,text=results[0][2],font=("Goudy old style",15,"bold"),fg="WHITE",bg="BLACK",width=30).place(x=630,y=450)

  mot=Label(root,text="     Mot de passe :  ",font=("Goudy old style",15,"bold"),fg="WHITE",bg="black").place(x=480,y=530)
  NOM1=Label(root,text=results[0][3],font=("Goudy old style",15,"bold"),fg="WHITE",bg="BLACK",width=30).place(x=630,y=530)


  def pass_modifier():
    root.destroy()
    PAGE2.modifier(results)
  def suprission():
    email=results[0][2]
    print(email)
    conn = sqlite3.connect('.\\db.db')
    cursor = conn.cursor()
    try:
       cursor.execute('Delete  from db where email="'+email+'"')
       conn.commit()
       messagebox.showinfo("information", "Compte est bien supprimer")
       root.destroy()
       Connexion.connexion()
    except Exception as e:  
       print(e)
       conn.rollback()
       conn.close()

  modf=Button(root,text="     Modifie     ",bg="#22780F",fg="#FFFFFF",font=("times new roman",16),command=pass_modifier ).place(x=550,y=610)
  ssup=Button(root,text="     supprimer     ",bg="#22780F",fg="#FFFFFF",font=("times new roman",16),command=suprission ).place(x=740,y=610)
  root.mainloop()
# compte()