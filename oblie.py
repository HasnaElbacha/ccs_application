from tkinter import*
from PIL import ImageTk ,Image
import Inscription
from tkinter import messagebox as ms
from tkinter import messagebox
import smtplib,ssl
import sqlite3
import Connexion
import home
def oblie():
  root=Tk()
  root.title("connexion")
  height = 550
  width = 800
  x=(root.winfo_screenwidth()//2)-(width//2)
  y=(root.winfo_screenheight()//2)-(height//2)
  root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
  root.resizable(False,False)
        
        
        
  btn_flechem=Image.open('.\\w.png')
  resize_btn_flechem = btn_flechem.resize((796,546))
  photo_flechem=ImageTk.PhotoImage(resize_btn_flechem)
  bg_image=Label(root,image=photo_flechem,bd=0 ).place(x=3,y=1)
         
         #======login frame
  frame_login=Frame(root,bg="white")
  frame_login.place(x=40,y=80,height=340,width=450)

  title=Label(frame_login,text="Récupérez-vous votre mot de passe",font=("Impact",19,"bold"),fg="#22780F",bg="white").place(x=28,y=10)
  Desc=Label(frame_login,text="Zone de récupération de mot de passe ",font=("Goudy old style",15,"bold"),fg="#22780F",bg="white").place(x=77,y=60)

  usr=Label(frame_login,text="Email",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=40,y=150)
  txt_user=Entry(frame_login,font=("times new roman",12),bg="lightgray")
  txt_user.place(x=46,y=180,width=350,height=35)
  def send():
        global email
        conn = sqlite3.connect('.\\db.db')
        email = txt_user.get()
        with conn:
                cursor = conn.cursor()
        cursor.execute('select * from db where email= "'+email+'"')
        result=cursor.fetchall()
        print(result)
        
        if (email==''):
            messagebox.showinfo("Erreur",'Remplit le champ')
        else:
            if(result):
                user=email
                print(user)
                with conn:
                    cursor = conn.cursor()
                cursor.execute('select password from db where email= "'+email+'"')
                result1=cursor.fetchall()
                for results in result1:
                    print(results)
                    txte=results
            
                try:
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.login("elbachahasna2@gmail.com", "lokckvgnfxwhiwpg")
                    server.sendmail("expediteur@address.com",user,  "subject: test \nBonjour ,"+str(user)+"\nVotre mot de passe de CCS est : "+str(txte))
                    server.quit()
                    ms.showinfo('Réussi', 'Email envoyer')
                    root.destroy()
                    Connexion.connexion()
                    # wcghjigielgdmutxadmin_expl.mainadminempl()kzdurpjwxxkjenimserver.login("elbacha.asma@gmail.com", "tpfzozdfwmhfevhx")
                except:
                    ms.showerror('Erreur', 'Email non envoyer!!!')
                    
                
            else:
               ms.showerror('Erreur', 'Cette adresse n\'existe pas!!!')
  def ROTEUR():
    root.destroy()
    Connexion.connexion()
  ISC=Button(root,text="    envoyer    ",bg="#22780F",fg="#FFFFFF",font=("times new roman",16),command=send).place(x=80,y=360)
  routeur=Button(root,text="    Roteur    ",bg="#22780F",fg="#FFFFFF",font=("times new roman",16),command=ROTEUR).place(x=330,y=360)
  root.mainloop() 
#oblie()