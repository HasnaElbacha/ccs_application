from tkinter import*
from PIL import ImageTk ,Image
import home
from tkinter import messagebox as ms
import sqlite3
import Connexion
# import loading_page
def inscription():
  root=Tk()
  root.title("Inscription")
  height = 550
  width = 800
  x=(root.winfo_screenwidth()//2)-(width//2)
  y=(root.winfo_screenheight()//2)-(height//2)
  root.geometry('{}x{}+{}+{}'.format(width,height,x,y))
  root.resizable(False,False)
        
        
        
  btn_flechem=Image.open('.\\gryyy.png')
  resize_btn_flechem = btn_flechem.resize((300,600))
  photo_flechem=ImageTk.PhotoImage(resize_btn_flechem)
  bg_image=Label(root,image=photo_flechem ).place(x=600,y=0)
         
         #======login frame
  frame_login=Frame(bg="white")
  frame_login.place(x=0,y=0,height=700,width=600)

  title=Label(frame_login,text="inscrivez-vous ici",font=("Impact",25,"bold"),fg="#22780F",bg="white").place(x=150,y=15)
  Desc=Label(frame_login,text="Zone d'inscription des utilisateurs",font=("Goudy old style",15,"bold"),fg="#22780F",bg="white").place(x=135,y=60)

  usr=Label(frame_login,text="Nom Complet",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=40,y=160)
  txt_user=Entry(frame_login,font=("times new roman",12),bg="lightgray")
  txt_user.place(x=46,y=190,width=350,height=35)
        
  passT=Label(frame_login,text="Email",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=40,y=230)
  txt_email=Entry(frame_login,font=("times new roman",12),bg="lightgray")
  txt_email.place(x=46,y=260,width=350,height=35)

  COF=Label(frame_login,text="Mot de passe",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=40,y=300)
  txt_password=Entry(frame_login,font=("times new roman",12),bg="lightgray",show='*')
  txt_password.place(x=46,y=330,width=350,height=35)    

  ind=Label(frame_login,text="Confirmation de mot de passe",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=40,y=370)
  txt_confirmaion=Entry(frame_login,font=("times new roman",12),bg="lightgray",show='*')
  txt_confirmaion.place(x=46,y=400,width=350,height=35) 
  def passconnexion():
    root.destroy()
    Connexion.connexion()
  def database():
      
        # Getting entries
        username = txt_user.get()
        email = txt_email.get()
        password=txt_password.get()
        password_conf=txt_confirmaion.get()
        # Validating Entries
        validation = []

        # Adding information to the list
        validation.append(username)
        validation.append(email)
        validation.append(username)
        validation.append(password)
        validation.append(password_conf)

        # Boolean for condition
        condition = True
        
        # Looping and checking conditions
        for ele in validation:
            if ele == '':
                condition = False
                break

        if condition:
            # Checking for password match
            if password != password_conf:
                ms.showerror('Erreur', 'Mots de passe de sont pas identiques!!!')    
            else:
                # Making connection
                conn = sqlite3.connect('.\\db.db')
                #Creating cursor
                with conn:
                    cursor = conn.cursor()
                cursor.execute('select * from db where username= "'+username+'"and email="'+email+'" and password="'+password_conf+'"')
                result=cursor.fetchall()
                if(result):
                    ms.showerror('Erreir', 'Compte existe déjà')
                else:
                    cursor.execute('INSERT INTO db (username,email,password,password_conf) VALUES ("'+username+'","'+email+'","'+password+'","'+password_conf+'")')
                    conn.commit()
                    # Showing success message
                    ms.showinfo('Réussi', 'Compte créé avec succès !! Vous pouvez maintenant vous connecter au système !!')
                    # Closing the window
                    root.destroy()
                    Connexion.connexion()
    
            
        else:
            ms.showerror('Erreur', 'Veuillez remplir tous les champs de saisie')
  ISC=Button(root,text="    Inscrire    ",bg="#22780F",fg="#FFFFFF",font=("times new roman",16),command=database).place(x=250,y=480)
  rev=Button(root,text="    Retour    ",bg="#22780F",fg="#FFFFFF",font=("times new roman",16),command=passconnexion ).place(x=80,y=480)      
  def show():
            hide_button = Button(frame_login,image=photo ,bg='gray',activebackground='gray',cursor='hand2',bd=0,command=hide)
            hide_button.image=photo
            hide_button.place(x=400,y=335)
            txt_password.config(show='')
  def hide ():
            show_button = Button(frame_login,image=photo1 ,bg='white',activebackground='white',cursor='hand2',bd=0,command=show)
            show_button.image=photo1 
            show_button.place(x=400,y=335)
            txt_password.config(show='*')

  show_image1 = Image.open('.\\y1.png')
  resize_show_image = show_image1.resize((25,25))
  photo1 = ImageTk.PhotoImage(resize_show_image)
  show_image=ImageTk.PhotoImage(resize_show_image)
  show_button=Button(frame_login,image=photo1,bg='white',activebackground='white',cursor='hand2',bd=0,command=show)
  show_button.image=photo1
  show_button.place(x=400,y=335,height=25,width=25)
        
  hide_image = Image.open('.\\y2.png')
  resize_hide_image = hide_image.resize((25,25))
  photo = ImageTk.PhotoImage(resize_hide_image)
  
  ping = Image.open('.\\pho5.png')
  resize_ping = ping.resize((250,350))
  ping=ImageTk.PhotoImage(resize_ping)
  button=Button(root,image=ping,bg='white',activebackground='white',cursor='hand2',bd=0)
  button.place(x=500,y=100,height=350,width=250)

  def showc():
            hide_buttonc = Button(frame_login,image=photoc ,bg='gray',activebackground='gray',cursor='hand2',bd=0,command=hidec)
            hide_buttonc.image=photoc
            hide_buttonc.place(x=400,y=405)
            txt_confirmaion.config(show='')
  def hidec ():
            show_buttonc = Button(frame_login,image=photo1c ,bg='white',activebackground='white',cursor='hand2',bd=0,command=showc)
            show_buttonc.image=photo1c 
            show_buttonc.place(x=400,y=405)
            txt_confirmaion.config(show='*')

  show_image1c = Image.open('.\\y1.png')
  resize_show_imagec = show_image1c.resize((25,25))
  photo1c = ImageTk.PhotoImage(resize_show_imagec)
  show_image=ImageTk.PhotoImage(resize_show_imagec)
  show_buttonc=Button(frame_login,image=photo1c,bg='white',activebackground='white',cursor='hand2',bd=0,command=showc)
  show_buttonc.image=photo1c
  show_buttonc.place(x=400,y=405,height=25,width=25)
        
  hide_imagec = Image.open('.\\y2.png')
  resize_hide_imagec = hide_imagec.resize((25,25))
  photoc = ImageTk.PhotoImage(resize_hide_imagec)
  
  root.mainloop() 
            
# inscription()
          
