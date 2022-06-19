from time import time
from tkinter import*
from PIL import ImageTk ,Image
from tkinter import messagebox as ms
import random
import time
import Connexion
import home
import ping1
import PAGE1
def parametre(results):
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
  def pass_home():
    root.destroy()
    home.acc(results)
  def pass_ping():
    root.destroy()
    ping1.ping(results)
  def pass_compte():
    root.destroy()
    PAGE1.compte(results)
  ACC=Button(root,text="                     Acceuil                     ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18),command=pass_home).place(x=0,y=120)
  pin=Button(root,text="                         Ping                        ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18),command=pass_ping).place(x=342,y=120)
  par=Button(root,text="            Parametre des adresses                     ",bg="#318CE7",fg="#ffffff",bd=0,font=("times new roman",18)).place(x=695,y=120)
  sta=Button(root,text="                 Mon compte               ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18),command=pass_compte).place(x=1060,y=120)



  tit=Label(text=" Modification des adresses ",font=("Impact",25,"bold"),fg="#22780F",bg="white").place(x=1,y=195)
  t=Label(text=" Les adresses acualles  ",font=("Impact",25,"bold"),fg="#22780F",bg="white").place(x=570,y=195)

  btn_f=Image.open('.\\14.png')
  resize_btn_f = btn_f.resize((300,500))
  photo_f=ImageTk.PhotoImage(resize_btn_f)
  bg_image=Label(root,image=photo_f,bd=0 ).place(x=1080,y=220)
  def dec():
    root.destroy()
    Connexion.connexion()
  ping = Image.open('.\\68.png')
  resize_ping = ping.resize((100,100))
  ping=ImageTk.PhotoImage(resize_ping)
  button=Button(image=ping,bg='white',activebackground='white',cursor='hand2',command=dec)
  button.place(x=1260,y=10,height=100,width=100)

  frame_login=Frame(root,bg="#3AF24B")
  frame_login.place(x=0,y=270,height=300,width=400)
  
  frame_login=Frame(root,bg="#3AF24B")
  frame_login.place(x=540,y=270,height=300,width=410)
  CART=Label(root,text="carte ethernet",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=0,y=300)
  txt_CART1=Entry(root,font=("times new roman",12),bg="lightgray")
  txt_CART1.place(x=120,y=300,width=50,height=30)
  CARTA=Label(root,text=".",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=170,y=300)
  txt_CART2=Entry(root,font=("times new roman",12),bg="lightgray")
  txt_CART2.place(x=183,y=300,width=50,height=30)
  CARTB=Label(root,text=".",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=233,y=300)
  txt_CART3=Entry(root,font=("times new roman",12),bg="lightgray")
  txt_CART3.place(x=246,y=370,width=50,height=30)
  CARTC=Label(root,text=".",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=296,y=370)
  txt_CART4=Entry(root,font=("times new roman",12),bg="lightgray")
  txt_CART4.place(x=310,y=370,width=50,height=30)


  ROU=Label(root,text="routeur",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=0,y=370)
  txt_ROU1=Entry(root,font=("times new roman",12),bg="lightgray")
  txt_ROU1.place(x=120,y=370,width=50,height=30)
  ROUA=Label(root,text=".",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=170,y=370)
  txt_ROU2=Entry(root,font=("times new roman",12),bg="lightgray")
  txt_ROU2.place(x=183,y=370,width=50,height=30)
  ROUB=Label(root,text=".",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=233,y=370)
  txt_ROU3=Entry(root,font=("times new roman",12),bg="lightgray")
  txt_ROU3.place(x=246,y=300,width=50,height=30)
  ROUC=Label(root,text=".",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=296,y=300)
  txt_ROU4=Entry(root,font=("times new roman",12),bg="lightgray")
  txt_ROU4.place(x=310,y=300,width=50,height=30)


  SER=Label(root,text="serveur local",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=0,y=440)
  txt_SER1=Entry(root,font=("times new roman",12),bg="lightgray")
  txt_SER1.place(x=120,y=440,width=50,height=30)
  SERA=Label(root,text=".",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=170,y=440)
  txt_SER2=Entry(root,font=("times new roman",12),bg="lightgray")
  txt_SER2.place(x=183,y=440,width=50,height=30)
  SERB=Label(root,text=".",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=233,y=440)
  txt_SER3=Entry(root,font=("times new roman",12),bg="lightgray")
  txt_SER3.place(x=246,y=440,width=50,height=30)
  SERC=Label(root,text=".",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=296,y=440)
  txt_SER4=Entry(root,font=("times new roman",12),bg="lightgray")
  txt_SER4.place(x=310,y=440,width=50,height=30)


  HOT=Label(root,text="hote",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=0,y=510)
  txt_HOT1=Entry(root,font=("times new roman",12),bg="lightgray")
  txt_HOT1.place(x=120,y=510,width=50,height=30)
  HOTA=Label(root,text=".",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=170,y=510)
  txt_HOT2=Entry(root,font=("times new roman",12),bg="lightgray")
  txt_HOT2.place(x=183,y=510,width=50,height=30)
  HOTB=Label(root,text=".",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=233,y=510)
  txt_HOT3=Entry(root,font=("times new roman",12),bg="lightgray")
  txt_HOT3.place(x=246,y=510,width=50,height=30)
  HOTC=Label(root,text=".",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=296,y=510)
  txt_HOT4=Entry(root,font=("times new roman",12),bg="lightgray")
  txt_HOT4.place(x=310,y=510,width=50,height=30)
  def info_ping():
    if (str(txt_CART1.get()) == "" or str(txt_CART4.get()) == "" or str(txt_CART2.get()) == "" or str(txt_CART3.get()) == "" or str(txt_ROU4.get())=="" or str(txt_ROU2.get())=="" or str(txt_ROU3.get())=="" or str(txt_ROU4.get())=="" or str(txt_SER1.get())=="" or str(txt_SER2.get())=="" or str(txt_SER3.get())=="" or str(txt_SER4.get())=="" or str(txt_HOT1.get())=="" or str(txt_HOT2.get())=="" or  str(txt_HOT3.get())=="" or str(txt_HOT4.get())==""):
      ms.showerror('Erreir', 'Veuillez compléter tous les champs !!')
      lines = [str(txt_CART1.get())+'.'+str(txt_CART2.get())+'.'+str(txt_ROU3.get())+'.'+str(txt_ROU4.get()),
      str(txt_ROU1.get())+'.'+str(txt_ROU2.get())+'.'+str(txt_CART3.get())+'.'+str(txt_CART3.get()),
      str(txt_SER1.get())+'.'+str(txt_SER2.get())+'.'+str(txt_SER3.get())+'.'+str(txt_SER4.get()),
      str(txt_HOT1.get())+'.'+str(txt_HOT2.get())+'.'+str(txt_HOT3.get())+'.'+str(txt_HOT4.get())]
    else:
     with open('info_ping.txt', 'w+') as f:
      for line in lines:
        f.write(line)
        f.write('\n')
     ms.showinfo('Réussi', 'Les mofication ont effectuées')
  with open('info_ping.txt') as f:
    lin = f.readlines()
    listping=[]
    listping=lin
    print(lin)
    print(listping) 
  c=Label(root,text="Carte ethernet ",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=555,y=300)
  c1=Label(root,text=listping[0],font=("Goudy old style",13,"bold"),fg="black",bg="lightgray",width=20).place(x=700,y=300)

  r=Label(root,text="Routeur",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=555,y=360)
  r1=Label(root,text=listping[1],font=("Goudy old style",13,"bold"),fg="black",bg="lightgray",width=20).place(x=700,y=360)

  s=Label(root,text="Serveur local ",font=("Goudy old style",15,"bold"),fg="BLACK",bg="#3AF24B").place(x=555,y=430)
  s1=Label(root,text=listping[2],font=("Goudy old style",13,"bold"),fg="black",bg="lightgray",width=20).place(x=700,y=430)

  s=Label(root,text="hote ",font=("Goudy old style",15,"bold"),fg="black",bg="#3AF24B").place(x=555,y=500)
  s1=Label(root,text=listping[3],font=("Goudy old style",13,"bold"),fg="black",bg="lightgray",width=20).place(x=700,y=500)
  Validé=Button(root,text="     Validé     ",bg="#22780F",fg="#FFFFFF",font=("times new roman",16),command=info_ping ).place(x=330,y=600)
  def actualise():
    root.destroy()
    parametre()
  Actualisé=Button(root,text="     Actualisé     ",bg="#22780F",fg="#FFFFFF",font=("times new roman",16),command=actualise ).place(x=480,y=600)
  root.mainloop()

# parametre()