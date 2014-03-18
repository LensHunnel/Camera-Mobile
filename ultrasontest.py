# -*- coding: cp1252 -*-

#!/usr/bin/python

#+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|N|e|c|r|o|m|a|n|c|i|e|n|-+
#+-+-+-+-+-+-+-+-+-+-+-+-+-+
## ultrasonic_1.py
# Measure distance using an ultrasonic sensor
#
# Auteur : Lens Hunnel
# Date   : 11/03/2014
# Importation des librairies Python requises
import random
import time

# definition des GPIO que nous allons utiliser
# Utilise les references GPIO BCM 
# au lieu des numeros de pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24
  

class Ultrason(object):
        def __init__(self):
           self.valeur = list()
           self.distance=-1;
  
        
        def calculMoy(self,tab):
                somme=0
                moy = 0
                for i in tab:
                        somme = somme + i
                moy = somme/len(tab)
                return moy
                
        def supValmin(self,tab):
                valeurMin=tab[0]
                for i in tab:
                        if i<valeurMin:
                                valeurMin=i
                tab.remove(valeurMin)
        def supValmax(self,tab):
                valeurMax=tab[0]
                for i in tab:
                        if i>valeurMax:
                                valeurMax=i
                tab.remove(valeurMax)
        def getdistance(self):
                print "Ultrasonic Measurement"

                print" Definition des entrees/sorties"
                print "mise a zero de trigger"


                print "Temps d'initialisation du module"
                time.sleep(0.5)
                n = 0 
                while n < 10 :
                        #print "Envoie d'une impulsion de 10uS a  la broche Trigger"
                        start = time.time()
                        time.sleep(random.uniform(1,10)/1000)
                        stop = time.time()

                        #print "Calcul de la longueur de l'impulsion de la broche Echo"
                        elapsed = stop-start

                        #print"""Distance pulse travelled in that time is time
                        #multipliÃ© par la vitesse du son (cm/s)"""
                        self.distance = elapsed * 34000

                        #print "That was the distance there and back so halve the value"
                        self.distance = self.distance / 2

                        self.valeur.append(self.distance)
                        n=n+1
                self.supValmin(self.valeur)
                self.supValmax(self.valeur)
                self.distance = self.calculMoy(self.valeur)

                print "Distance : %.3f" % self.distance
                return self.distance
if __name__  == "__main__":
        print Ultrason().getdistance()
