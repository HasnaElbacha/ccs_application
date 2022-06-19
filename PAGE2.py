from time import time
from tkinter import*
from PIL import ImageTk ,Image
import sqlite3
from tkinter import messagebox as ms
from tkinter import messagebox
import random
import Connexion
import PAGE1
import time
import home
import ping1
import parametre
def modifier(results):
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
   def pass_para():
      root.destroy()
      parametre.parametre(results)
   def pass_compte():
       root.destroy()
       PAGE1.compte(results)
   ACC=Button(root,text="                     Acceuil                     ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18),command=pass_home).place(x=0,y=120)
   pin=Button(root,text="                         Ping                        ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18),command=pass_ping).place(x=342,y=120)
   par=Button(root,text="            Parametre des adresses                     ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18),command=pass_para).place(x=695,y=120)
   sta=Button(root,text="                 Mon compte               ",bg="#318CE7",fg="#ffffff",bd=0,font=("times new roman",18),command=pass_compte).place(x=1060,y=120)

# frame_login=Frame(root,bg="#318CE7")
# frame_login.place(x=60,y=210,height=450,width=1250)

   tit=Label(text=" Mon compte ",font=("Impact",25,"bold"),fg="#22780F",bg="white").place(x=599,y=195)


   btn_f=Image.open('.\\65.png')
   resize_btn_f = btn_f.resize((100,100))
   photo_f=ImageTk.PhotoImage(resize_btn_f)
   bg_image=Label(root,image=photo_f,bd=0 ).place(x=500,y=190)

   r=Label(root,text="Email : ",font=("Goudy old style",12,"bold"),fg="white",bg="black").place(x=610,y=250)
   r1=Label(root,text=results[0][2],font=("Goudy old style",13,"bold"),fg="WHITE",bg="BLACK",width=20).place(x=659,y=250)

   NOM=Label(root,text=" Nom complet : ",font=("Goudy old style",18,"bold"),fg="black",bg="white").place(x=170,y=420)
   txt_NOM=Entry(root,font=("times new roman",14),bg="black",fg="white")
   txt_NOM.place(x=330,y=420,width=250,height=35)


   mot=Label(root,text=" Mot de passe : ",font=("Goudy old style",18,"bold"),fg="black",bg="white").place(x=795,y=420)
   txt_mot=Entry(root,font=("times new roman",13),bg="black",fg="white")
   txt_mot.place(x=945,y=420,width=250,height=35)

   def change_info():
    email=results[0][2]
    print(email)
    nom=txt_NOM.get()
    password = txt_mot.get()
    password_conf = txt_mot.get()
    conn = sqlite3.connect('.\\db.db')
    cursor = conn.cursor()
    try:
       cursor.execute('Update  db set username = "'+nom+'",password="'+password+'",password_conf="'+password_conf+'"where email="'+email+'"')
       conn.commit()
       messagebox.showinfo("information", "Mot de passe ou nom est mis à jour avec succés ...")
       txt_NOM.delete(0, END)
       txt_mot.delete(0, END)
       txt_NOM.focus_set()
    except Exception as e:  
       print(e)
       conn.rollback()
       conn.close()
   def pass_page1():
      root.destroy()
      PAGE1.compte()
   modf=Button(root,text="     Vadidé     ",bg="#22780F",fg="#FFFFFF",font=("times new roman",16),command=change_info).place(x=630,y=550)
   r=Button(root,text="     Retour     ",bg="#22780F",fg="#FFFFFF",font=("times new roman",16),command=pass_page1).place(x=630,y=600)
   root.mainloop()
# modifier()