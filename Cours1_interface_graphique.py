from tkinter import *

fenetre=Tk()
fenetre.title("Interface")
fenetre.iconbitmap("logo.ico")
fenetre.minsize(200,400)
fenetre.maxsize(400,500)

titre=Label(fenetre, text="Mon interface")
titre.pack()


champ=Entry(fenetre)
champ.pack()

check=Checkbutton(text="checker")
check.pack()

bouton=Button(text="checker")
bouton.pack()

mainloop()