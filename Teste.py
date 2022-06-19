from tkinter import*
from PIL import ImageTk ,Image
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
  resize_btn_flechem = btn_flechem.resize((400,400))
  photo_flechem=ImageTk.PhotoImage(resize_btn_flechem)
  bg_image=Label(root,image=photo_flechem ).place(x=490,y=0)
         
         #======login frame
  frame_login=Frame(bg="white")
  frame_login.place(x=0,y=0,height=700,width=600)

  title=Label(frame_login,text="inscrivez-vous ici",font=("Impact",25,"bold"),fg="#22780F",bg="white").place(x=150,y=15)
  Desc=Label(frame_login,text="Zone d'inscription des utilisateurs",font=("Goudy old style",15,"bold"),fg="#22780F",bg="white").place(x=135,y=60)

  usr=Label(frame_login,text="Nom Complet",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=40,y=180)
  txt_user=Entry(frame_login,font=("times new roman",12),bg="lightgray")
  txt_user.place(x=46,y=210,width=350,height=35)
        
  passT=Label(frame_login,text="Email",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=40,y=250)
  txt_email=Entry(frame_login,font=("times new roman",12),bg="lightgray")
  txt_email.place(x=46,y=280,width=350,height=35)

  COF=Label(frame_login,text="Mot de passe",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=40,y=320)
  txt_password=Entry(frame_login,font=("times new roman",12),bg="lightgray",show='*')
  txt_password.place(x=46,y=350,width=350,height=35)    

  ind=Label(frame_login,text="Confirmation de mot de passe",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=40,y=390)
  txt_confirmaion=Entry(frame_login,font=("times new roman",12),bg="lightgray",show='*')
  txt_confirmaion.place(x=46,y=420,width=350,height=35) 
  
  ISC=Button(root,text="    Inscrire    ",bg="#22780F",fg="#FFFFFF",font=("times new roman",16)).place(x=150,y=480)
        
  def show():
            hide_button = Button(frame_login,image=photo ,bg='gray',activebackground='gray',cursor='hand2',bd=0,command=hide)
            hide_button.image=photo
            hide_button.place(x=400,y=350)
            txt_password.config(show='')
  def hide ():
            show_button = Button(frame_login,image=photo1 ,bg='white',activebackground='white',cursor='hand2',bd=0,command=show)
            show_button.image=photo1 
            show_button.place(x=400,y=350)
            txt_password.config(show='*')

  show_image1 = Image.open('.\\y1.png')
  resize_show_image = show_image1.resize((25,25))
  photo1 = ImageTk.PhotoImage(resize_show_image)
  show_image=ImageTk.PhotoImage(resize_show_image)
  show_button=Button(frame_login,image=photo1,bg='white',activebackground='white',cursor='hand2',bd=0,command=show)
  show_button.image=photo1
  show_button.place(x=400,y=350,height=25,width=25)
        
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
            hide_buttonc.place(x=400,y=425)
            txt_confirmaion.config(show='')
  def hidec ():
            show_buttonc = Button(frame_login,image=photo1c ,bg='white',activebackground='white',cursor='hand2',bd=0,command=showc)
            show_buttonc.image=photo1c 
            show_buttonc.place(x=400,y=425)
            txt_confirmaion.config(show='*')

  show_image1c = Image.open('.\\y1.png')
  resize_show_imagec = show_image1c.resize((25,25))
  photo1c = ImageTk.PhotoImage(resize_show_imagec)
  show_image=ImageTk.PhotoImage(resize_show_imagec)
  show_buttonc=Button(frame_login,image=photo1c,bg='white',activebackground='white',cursor='hand2',bd=0,command=showc)
  show_buttonc.image=photo1c
  show_buttonc.place(x=400,y=425,height=25,width=25)
        
  hide_imagec = Image.open('.\\y2.png')
  resize_hide_imagec = hide_imagec.resize((25,25))
  photoc = ImageTk.PhotoImage(resize_hide_imagec)
  
  root.mainloop() 
            
inscription()
      