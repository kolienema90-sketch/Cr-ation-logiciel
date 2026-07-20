from tkinter import *

fenetre=Tk()
fenetre.title("Mon Premier Projet")
fenetre.minsize(400,300)
fenetre.maxsize(700,600)
fenetre.config(bg="#191923")

titre=Label(fenetre,text="Prénom et Nom")
titre.pack()

champ=Entry(fenetre)
champ.pack()

check=Checkbutton(fenetre,text="Marié")
check.pack()

bouton=Button(fenetre,text="Ok")
bouton.pack()

mainloop()
