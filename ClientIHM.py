# -*- coding: cp1252 -*-
from Tkinter import *
import socket
hote = "localhost"
port = 12800
class ControlsIHM(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Controls  Moteurs")
        self.pack()
        
        frame = Frame(self,  borderwidth=1)
        frame.pack(side = LEFT)
        frame2 = Frame(self,  borderwidth=1)
        frame2.pack(side = LEFT)
        frame3 = Frame(frame2,  borderwidth=1)
        frame3.pack(side=TOP)
        self.champs_label = Label(frame3,text=" cm")
        self.champs_label.pack(side=RIGHT,pady=5)
        self.BtnUltrason=Button(frame3,text = "Distance Obstacle",command=self.ClicBtnUltrason)
        self.BtnUltrason.pack(side=RIGHT,pady=25,padx=5)

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

        self.pause=PhotoImage(file="pause.gif")
        self.lblPause=Button(self.f2,image=self.pause, command=self.ClicBtnPause)
        self.lblPause.pack(side=LEFT,padx=5,pady=5)

        self.droite=PhotoImage(file="droite.gif")
        self.lblDroite=Button(self.f2,image=self.droite, command=self.ClicBtnDroite)
        self.lblDroite.pack(side=RIGHT,padx=5,pady=5)

        self.haut=PhotoImage(file="haut.gif")
        self.lblHaut=Button(self.f1,image=self.haut,command=self.ClicBtnHaut)
        self.lblHaut.pack(side=TOP,pady=5,padx=5)

        self.quitter=Button(frame2,text="Quitter",command=self.quit)
        self.quitter.pack(side=BOTTOM, pady=25)

        self.stop=PhotoImage(file="stop.gif")
        self.lblStop=Button(frame2,image=self.stop,command=self.ClicBtnStop)
        self.lblStop.pack(side=BOTTOM,pady=5,padx=5)
        
        self.master.bind("<Up>", self.AppuiBtnHaut) # Flèche haut
        self.master.bind("<Down>", self.AppuiBtnBas) # Flèche bas
        self.master.bind("<Left>", self.AppuiBtnGauche) # Flèche gauche
        self.master.bind("<Right>", self.AppuiBtnDroite) # Flèche droite
        self.master.bind("<space>", self.AppuiBtnPause) # Flèche espace
        self.master.bind("<Key-s>", self.AppuiBtnStop) # Flèche droite
        self.master.bind("<Key-u>", self.AppuiBtnUltrason) # Flèche droite
        try:
            self.connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connexion_avec_serveur.connect((hote, port))
            print("connexion etablie avec le port {}".format(port))
        except socket.error:
            self.connexion_avec_serveur.close()
            print("Fermeture de la connexion")
            
    def ClicBtnHaut (self):
        print"event up"
        self.envoiMsg('u')
        self.messageRecu()
        

    def ClicBtnBas (self):
        print"event down"
        self.envoiMsg('d')
        self.messageRecu()
    def ClicBtnGauche (self):
        print"event Left"
        self.envoiMsg('l')
        self.messageRecu()
    def ClicBtnDroite (self):
        print"event Right"
        self.envoiMsg('r')
        self.messageRecu()
    def ClicBtnPause (self):
        print"event Pause"
        self.envoiMsg('p')
        self.messageRecu()
    def ClicBtnStop (self):
        print"event Stop"
        self.envoiMsg('s')
        self.messageRecu()
    def ClicBtnUltrason (self):
        print"event Ultrason"
        self.envoiMsg('ultrason')
        dis=self.messageRecu()
        dis=float(self.messageRecu())
        self.champs_label["text"]="%.1f"%dis+" cm"
    def AppuiBtnHaut (self,event):
        self.ClicBtnHaut()
    def AppuiBtnBas (self,event):
        self.ClicBtnBas()

    def AppuiBtnGauche (self,event):
        self.ClicBtnGauche()
    def AppuiBtnDroite (self,event):
        self.ClicBtnDroite()
    def AppuiBtnPause (self,event):
        self.ClicBtnPause()
    def AppuiBtnStop (self,event):
        self.ClicBtnStop()
    def AppuiBtnUltrason (self,event):
        self.ClicBtnUltrason()
    def messageRecu (self):
        try:
            msg_recu = self.connexion_avec_serveur.recv(1024)
            if msg_recu == "fin":
                self.connexion_avec_serveur.close()
                print("Fermeture de la connexion")
            print(msg_recu.decode())
        except socket.error:
            print("Fermeture de la connexion")
        return msg_recu
    def envoiMsg(self,commande):
         commande.encode()
         self.connexion_avec_serveur.send(commande)
         print"message "+commande+" envoye"

if __name__ == '__main__':                                                 #33
    ControlsIHM().mainloop()
