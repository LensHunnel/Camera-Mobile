# -*- coding: cp1252 -*-
from Tkinter import *
class ControlsIHM(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Controls  Moteurs")
        self.pack()
        
        frame = Frame(self,  borderwidth=1)
        frame.pack(side = LEFT)
        frame2 = Frame(self,  borderwidth=1)
        frame2.pack(side = LEFT)
        self.champs_label = Label(frame2,text="Distance Capteur Ultrason: 4.3 cm")
        self.champs_label.pack(side=TOP, pady=5)
        self.f1 = Frame(frame, borderwidth=1)
        self.f1.pack(fill=X,side=TOP)
        self.f2 = Frame(frame,  borderwidth=1)
        self.f2.pack()
        self.f3 = Frame(frame,height=200,borderwidth=1)
        self.f3.pack(side=BOTTOM)
        self.gauche=PhotoImage(file="gauche.gif")
        self.lblGauche=Button(self.f2,image=self.gauche, command=self.ClicBtnGauche)
        self.lblGauche.pack(side=LEFT,padx=5,pady=5)

        self.bas=PhotoImage(file="bas.gif")
        self.lblBas=Button(self.f3,image=self.bas, command=self.ClicBtnBas)
        self.lblBas.pack(side=BOTTOM,pady=5,padx=5)

        self.droite=PhotoImage(file="droite.gif")
        self.lblDroite=Button(self.f2,image=self.droite, command=self.ClicBtnDroite)
        self.lblDroite.pack(side=RIGHT,padx=5,pady=5)

        self.haut=PhotoImage(file="haut.gif")
        self.lblHaut=Button(self.f1,image=self.haut,command=self.ClicBtnHaut)
        self.lblHaut.pack(side=TOP,pady=5,padx=5)



        self.quitter=Button(frame2,text="Quitter",command=self.quit)
        self.quitter.pack(side=BOTTOM, pady=20)
        self.master.bind("<Up>", self.AppuiBtnHaut) # Flèche haut
        self.master.bind("<Down>", self.AppuiBtnBas) # Flèche bas
        self.master.bind("<Left>", self.AppuiBtnGauche) # Flèche gauche
        self.master.bind("<Right>", self.AppuiBtnDroite) # Flèche droite
    def ClicBtnHaut (self):
        print"event up"
    def ClicBtnBas (self):
        print"event down"
    def ClicBtnGauche (self):
        print"event Left"
    def ClicBtnDroite (self):
        print"event Right"
    def AppuiBtnHaut (self,event):
        self.ClicBtnHaut()
    def AppuiBtnBas (self,event):
        self.ClicBtnBas()
    def AppuiBtnGauche (self,event):
        self.ClicBtnGauche()
    def AppuiBtnDroite (self,event):
        self.ClicBtnDroite()
if __name__ == '__main__':                                                 #33
    ControlsIHM().mainloop()
