from tkinter import *
from tkinter.ttk import Progressbar
import sys
from turtle import width
from threading import Thread
from PIL import ImageTk ,Image
import Connexion  
i=0
def main():
    fenetre =Tk()
    fenetre.resizable(0,0)
    height = 470
    width = 660
    x=(fenetre.winfo_screenwidth()//2)-(width//2)
    y=(fenetre.winfo_screenheight()//2)-(height//2)
    fenetre.geometry('{}x{}+{}+{}'.format(width,height,x,y))
    fenetre.wm_attributes('-topmost',True)
    fenetre.overrideredirect(1)
    fenetre.config(background='#1247B0')
    exit_btn=Button(fenetre,text='X',command=lambda:exit_window(),font=("yu gothic ui",13,'bold'),fg='white',bg='#1247B0',bd=0,activebackground='grey',width=2,height=1)
    exit_btn.place(x=626,y=5)
   #  img=PhotoImage(file='.//logo.png')
    btn_flechem=Image.open('.\\AS.png')
    resize_btn_flechem = btn_flechem.resize((200,200))
    photo_flechem=ImageTk.PhotoImage(resize_btn_flechem)
    TITRE=Label(fenetre,text='ccs-1-2022' ,bg='#FFFFFF',fg="black",width=22,height=1,font=("yu gothic ui",11,'bold'))
    TITRE.place(x=0,y=0)

    bg_label=Label(fenetre,image=photo_flechem,bg='#FFFFFF',width=200,height=500)
    bg_label.place(x=0,y=20)
    progress_label=Label(fenetre,text='Chargement en cours . . .   ',font=("yu gothic ui",14,'bold'),fg='white',bg='#1247B0')
    progress_label.place(x=300,y=220)
    progress=Progressbar(fenetre,orient=HORIZONTAL,length=400 ,mode='determinate')
    progress.place(x=231,y=260)

    def exit_window():
       sys.exit(fenetre.destroy())
    
    def passage_window():
       fenetre.destroy()
       Connexion.connexion()
    
    def load():
       global i
       if i <= 10:
        txt='Chargement en cours . . .   '+(str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(1000,load)
        progress['value']=10*i
        i=i+1
    fenetre.after(10000,passage_window)
       
    load()
    fenetre.mainloop()
    

main()
              
