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
import time
import RPi.GPIO as GPIO

# Utilise les references GPIO BCM 
# au lieu des numeros de pins
GPIO.setmode(GPIO.BCM)

# definition des GPIO que nous allons utiliser 
GPIO_TRIGGER = 23
GPIO_ECHO = 24

print "Ultrasonic Measurement"

print" Definition des entrées/sorties"
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

print" mise à zero de trigger"
GPIO.output(GPIO_TRIGGER, False)

print "Temps d'initialisation du module"
time.sleep(0.5)

print "Envoie d'une impulsion de 10uS à la broche Trigger"
GPIO.output(GPIO_TRIGGER, True)
time.sleep(0.00001)
GPIO.output(GPIO_TRIGGER, False)
start = time.time()
while GPIO.input(GPIO_ECHO)==0:
	start = time.time()

while GPIO.input(GPIO_ECHO)==1:
	stop = time.time()

print "Calcul de la longueur de l'impulsion de la broche Echo"
elapsed = stop-start

print"""Distance pulse travelled in that time is time
multiplié par la vitesse du son (cm/s)"""
distance = elapsed * 34000

print "That was the distance there and back so halve the value"
distance = distance / 2

print "Distance : %.1f" % distance

# Reset GPIO settings
GPIO.cleanup()
