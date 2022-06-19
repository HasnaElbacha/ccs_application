from tkinter import*
from PIL import ImageTk ,Image
def connexion():
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

  title=Label(frame_login,text="Connectez-vous ici",font=("Impact",25,"bold"),fg="#22780F",bg="white").place(x=80,y=10)
  Desc=Label(frame_login,text="Zone de connexion des utilisateurs",font=("Goudy old style",15,"bold"),fg="#22780F",bg="white").place(x=77,y=60)

  usr=Label(frame_login,text="Nom utilisateur",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=40,y=140)
  txt_user=Entry(frame_login,font=("times new roman",12),bg="lightgray")
  txt_user.place(x=46,y=170,width=350,height=35)
        
  passT=Label(frame_login,text="Mot de passe",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=40,y=205)
  txt_passT=Entry(frame_login,font=("times new roman",12),bg="lightgray",show='*')
  txt_passT.place(x=46,y=235,width=350,height=35)
        
  forget=Button(frame_login,text="Mot de passe oublié ? ",bg="white",fg="#22780F",bd=0,font=("times new roman",12)).place(x=165,y=280)
  login=Button(root,text=" Connexion ",bg="#22780F",fg="#FFFFFF",font=("times new roman",16)).place(x=150,y=398)
  ISC=Button(root,text="    Inscrire    ",bg="#22780F",fg="#FFFFFF",font=("times new roman",16)).place(x=280,y=398)
        
  def show():
            hide_button = Button(frame_login,image=photo ,bg='gray',activebackground='gray',cursor='hand2',bd=0,command=hide)
            hide_button.image=photo
            hide_button.place(x=400,y=240)
            txt_passT.config(show='')
  def hide ():
            show_button = Button(frame_login,image=photo1 ,bg='white',activebackground='white',cursor='hand2',bd=0,command=show)
            show_button.image=photo1 
            show_button.place(x=400,y=240)
            txt_passT.config(show='*')

  show_image = Image.open('.\\y1.png')
  resize_show_image = show_image.resize((25,25))
  photo1 = ImageTk.PhotoImage(resize_show_image)
  show_image=ImageTk.PhotoImage(resize_show_image)
  show_button=Button(frame_login,image=photo1,bg='white',activebackground='white',cursor='hand2',bd=0,command=show)
  show_button.image=photo1
  show_button.place(x=400,y=240,height=25,width=25)
        
  hide_image = Image.open('.\\y2.png')
  resize_hide_image = hide_image.resize((25,25))
  photo = ImageTk.PhotoImage(resize_hide_image)



  
  root.mainloop() 
            
connexion()
      