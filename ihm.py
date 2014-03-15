# -*- coding: cp1252 -*-
from Tkinter import *


def AppuiBtnHaut (event):
    print"event up"
    lblHaut["relief"] = "sunken"
    lblHaut["relief"] = "raised"
def AppuiBtnBas (event):
    print"event down"
    lblHaut["relief"] = "sunken"
    lblHaut["relief"] = "raised"
def AppuiBtnGauche (event):
    print"event Left"
    lblHaut["relief"] = "sunken"
    lblHaut["relief"] = "raised"
def AppuiBtnDroite (event):
    print"event Right"
    lblHaut["relief"] = "sunken"
    lblHaut["relief"] = "raised"

fenetre = Tk();
fenetre.title("Camera Controls")
frame = Frame(fenetre,  borderwidth=1)
frame.pack(side = LEFT)
frame2 = Frame(fenetre,  borderwidth=1)
frame2.pack(side = LEFT)
champs_label = Label(frame2,text="Distance Capteur Ultrason")
champs_label.pack(side=TOP, pady=5)
f1 = Frame(frame, borderwidth=1)
f1.pack(fill=X,side=TOP)
f2 = Frame(frame,  borderwidth=1)
f2.pack()
f3 = Frame(frame,height=200,borderwidth=1)
f3.pack(side=BOTTOM)
gauche=PhotoImage(file="gauche.gif")
lblGauche=Button(f2,image=gauche)
lblGauche.pack(side=LEFT,padx=5,pady=5)

bas=PhotoImage(file="bas.gif")
lblBas=Button(f3,image=bas)
lblBas.pack(side=BOTTOM,pady=5,padx=5)

droite=PhotoImage(file="droite.gif")
lblDroite=Button(f2,image=droite)
lblDroite.pack(side=RIGHT,padx=5,pady=5)

haut=PhotoImage(file="haut.gif")
lblHaut=Button(f1,image=haut)
lblHaut.pack(side=TOP,pady=5,padx=5)



quitter=Button(frame2,text="Quitter",command=fenetre.quit)
quitter.pack(side=BOTTOM, pady=20)
fenetre.bind("<Up>", AppuiBtnHaut) # Flèche haut
fenetre.bind("<Down>", AppuiBtnBas) # Flèche bas
fenetre.bind("<Left>", AppuiBtnGauche) # Flèche gauche
fenetre.bind("<Right>", AppuiBtnDroite) # Flèche droite
fenetre.mainloop()
