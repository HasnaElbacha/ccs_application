from time import time
from tkinter import*
from turtle import home
from PIL import ImageTk ,Image
from tkinter.ttk import Progressbar
import random
import subprocess 
from tkinter import messagebox as ms
import home
import parametre
import PAGE1
import Connexion
import time
def ping(results):
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
  def pass_para():
     root.destroy()
     parametre.parametre(results)
  def pass_compte():
     root.destroy()
     PAGE1.compte(results)
  ACC=Button(root,text="                     Acceuil                     ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18),command=pass_home).place(x=0,y=120)
  pin=Button(root,text="                         Ping                        ",bg="#318CE7",fg="#ffffff",bd=0,font=("times new roman",18)).place(x=342,y=120)
  par=Button(root,text="                Parametre des adresses                    ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18),command=pass_para).place(x=695,y=120)
  sta=Button(root,text="                   Mon compte               ",bg="#002FA7",fg="#ffffff",bd=0,font=("times new roman",18),command=pass_compte).place(x=1060,y=120)

  frame_login=Frame(root,bg="#EDEDED")
  frame_login.place(x=150,y=260,height=400,width=800)

  frame_login=Frame(root,bg="#000000")
  frame_login.place(x=200,y=510,height=60,width=700)

  tit=Label(text="Testez-vous votre connexion réseau",font=("Impact",25,"bold"),fg="#22780F",bg="white").place(x=465,y=180)
  Des=Label(text="Choissez-vous le périphérique que vous voulez tester",font=("Goudy old style",20,"bold"),fg="#000000",bg="#EDEDED").place(x=260,y=270)

  btn_f=Image.open('.\\13.png')
  resize_btn_f = btn_f.resize((400,400))
  photo_f=ImageTk.PhotoImage(resize_btn_f)
  bg_image=Label(root,image=photo_f,bd=0 ).place(x=1006,y=345)

  CARTE=Label(text="   Carte ethernet   ",font=("italic",15,"bold"),fg="#000000",bg="#9EFD38").place(x=240,y=370)
  ROUTER=Label(text="          Router        ",font=("italic",15,"bold"),fg="#000000",bg="#9EFD38").place(x=240,y=450)
  SERVER=Label(text="     Local server    ",font=("italic",15,"bold"),fg="#000000",bg="#9EFD38").place(x=680,y=370)
  HOTE=Label(text="           Hote          ",font=("italic",15,"bold"),fg="#000000",bg="#9EFD38").place(x=680,y=450)
  i = IntVar() #Basically Links Any Radiobutton With The Variable=i.
  r1 = Radiobutton(root, text="", value=1,
  width=5, variable=i)
  r1.place(x=420,y=373)
  r2 = Radiobutton(root, text="", value=2,width=5, variable=i)
  r2.place(x=420,y=453)
  r3 = Radiobutton(root, text="", value=3, width=5,variable=i)
  r3.place(x=615,y=373)
  r4 = Radiobutton(root, text="", value=4,width=5, variable=i)
  r4.place(x=615,y=453)
  r5 = Radiobutton(root, text="", value=5,width=5, variable=i)
  r5.place(x=-10,y=1080)

  r=""

  def test_ping():
   global r
   global CARTE_result
   flag = 0
   index = 0
   with open('info_ping.txt') as f:
    lines = f.readlines()
    list_ping=[]
    list_ping=lines
    print(lines)
    print(list_ping)

   if (i.get() ==1):
     ms.showinfo('Réussi', 'Veuillez patienter quelque secondes')
     file_ = open("test.txt", "w+") 
     x=subprocess.Popen("ping "+list_ping[0][:-1], stdout=file_) 
     print("ping "+list_ping[0][:-1])
     print ("code retour:",x.wait())
     print ("sortie standard")
     print("you picked option1")
     file_.close()
   elif (i.get() ==2):
     ms.showinfo('Réussi', 'Veuillez patienter quelque secondes')
     file_ = open("test.txt", "w+") 
     x=subprocess.Popen("ping "+list_ping[1][:-1], stdout=file_) 
     print ("code retour:",x.wait())
     print ("sortie standard")
     print("you picked option2") 
     file_.close()
   elif (i.get() ==3):   
     ms.showinfo('Réussi', 'Veuillez patienter quelque secondes')
     file_ = open("test.txt", "w+") 
     x=subprocess.Popen("ping "+list_ping[2][:-1], stdout=file_) 
     print ("code retour:",x.wait())
     print ("sortie standard")
     print("you picked option3")
     file_.close() 
   elif (i.get() ==4):   
     ms.showinfo('Réussi', 'Veuillez patienter quelque secondes')
     file_ = open("test.txt", "w+") 
     x=subprocess.Popen("ping "+list_ping[3][:-1], stdout=file_) 
     print ("code retour:",x.wait())
     print ("sortie standard")
     print("you picked option4") 
     file_.close()
   else:
    ms.showerror('Erreur', 'Aucun champs selectioner')
   flag = 2
   file1 = open("test.txt", "r")
   with open('test.txt') as f:
    liness = f.readlines()
    list_pings=[]
    list_pings=liness
    print(liness)
    print(list_pings[8])
    print(list_pings[8][30:49])
    print('us = 4, perdus = 0 ')
    print(list_pings[8][30:49] == 'us = 4, perdus = 0 ')
   if list_pings[8][30:49] == 'us = 4, perdus = 0 ':
    print("gyy con")
    flag = 1
   else:
    print("hhhh des")
    flag=0
   if flag == 1  : 
      r="Connected" 
      print("con")
      rad =r         
      CARTE_result=Label(text=rad,font=("italic",15,"bold"),fg="#000000",bg="#9EFD38",width=50).place(x=247,y=525)

   elif flag == 0:  
      r="desconnected"
      print("descon")        
      rad =r         
      CARTE_result=Label(text=rad,font=("italic",15,"bold"),fg="#000000",bg="#9EFD38",width=50)
      CARTE_result.place(x=247,y=520) 
   else:
    print("aucun")
# ROUTER_result=Label(text=rad,font=("italic",15,"bold"),fg="#000000",bg="#ffffff").place(x=600,y=460)
# SERVER_result=Label(text=rad,font=("italic",15,"bold"),fg="#000000",bg="#ffffff").place(x=600,y=520)
# HOTE_result=Label(text=rad,font=("italic",15,"bold"),fg="#000000",bg="#ffffff").place(x=600,y=580)
  button=Button(root,text="Test" ,bg='#040405',fg='#9EFD38', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=test_ping).place(x=325,y=600)
  def reset():
    global CARTE_result
    r1.select()
    r2.select()
    r3.select()
    r4.select()
    r5.select()
    CARTE_result.destroy()

  button2=Button(root,text="Reset" ,bg='#040405',fg='#9EFD38', border=1,width=15,height=1,font=('yu gothic ui',15,'bold'),command=reset).place(x=600,y=600)
  root.mainloop()
#ping()