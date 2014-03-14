# -*- coding: cp1252 -*-
from Tkinter import *


def maFonction (event):
    print"event up"
    event.widget["activeforeground"] = "red"

fenetre = Tk();
fenetre.title("Camera Controls")

champs_label = Label(fenetre,text="Entrer")
f1 = Frame(fenetre, borderwidth=1)
f1.pack(fill=X,side=TOP)
f2 = Frame(fenetre,  borderwidth=1)
f2.pack()
f3 = Frame(fenetre,height=200,borderwidth=1)
f3.pack(side=BOTTOM)
gauche=PhotoImage(file="gauche.gif")
lblGauche=Label(f2,image=gauche)
lblGauche.pack(side=LEFT,padx=5,pady=5)

bas=PhotoImage(file="bas.gif")
lblBas=Label(f3,image=bas)
lblBas.pack(side=BOTTOM,pady=5,padx=5)

droite=PhotoImage(file="droite.gif")
lblDroite=Label(f2,image=droite)
lblDroite.pack(side=RIGHT,padx=5,pady=5)

haut=PhotoImage(file="haut.gif")
lblHaut=Label(f1,image=haut)
lblHaut.pack(fill=X,side=TOP,pady=5,padx=5)

fenetre.bind("<Up>", maFonction) # Flèche haut

fenetre.mainloop()
