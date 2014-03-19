#!/usr/bin/python
# -*- coding: cp1252 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|N|e|c|r|o|m|a|n|c|i|e|n|-+
#+-+-+-+-+-+-+-+-+-+-+-+-+-+
## ultrason.py
# Mesure deistance utilisant un capteur a ultrason
# Auteur : Lens Hunnel
# Date   : 11/03/2014
# Importation des librairies Python requises
import time
import RPi.GPIO as GPIO

# Utilise les references GPIO BCM 
# au lieu des numeros de pins
GPIO.setmode(GPIO.BCM)

# definition des GPIO que nous allons utiliser 
GPIO_TRIGGER = 23
GPIO_ECHO = 24


class Ultrason(object):
        def __init__(self):
                self.valeur = list()
                self.distance=-1;
                GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
                GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo  
                print" mise à zero de trigger"
                GPIO.output(GPIO_TRIGGER, False)
                time.sleep(0.5)
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
                n = 0 
                while n < 10 :
                        #print "Envoie d'une impulsion de 10uS a� la broche Trigger"
                        GPIO.output(GPIO_TRIGGER, True)
                        time.sleep(0.00001)
                        GPIO.output(GPIO_TRIGGER, False)
                        start = time.time()
                        while GPIO.input(GPIO_ECHO)==0:
                                start = time.time()

                        while GPIO.input(GPIO_ECHO)==1:
                                stop = time.time()

                        #print "Calcul de la longueur de l'impulsion de la broche Echo"
                        elapsed = stop-start

                        #print"""Distance pulse travelled in that time is time
                        #multiplié par la vitesse du son (cm/s)"""
                        self.distance = elapsed * 34000

                        #print "That was the distance there and back so halve the value"
                        self.distance = self.distance / 2

                        self.valeur.append(self.distance)
                        n=n+1
                self.supValmin(self.valeur)
                self.supValmax(self.valeur)
                self.distance = self.calculMoy(self.valeur)

                print "Distance : %.3f" % self.distance
                # Reset GPIO settings
                GPIO.cleanup()
                return self.distance
if __name__  == "__main__":
        print Ultrason().getdistance()
