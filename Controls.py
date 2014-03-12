import socket
import select
import RPi.GPIO as GPIO
import wiringpi2 as wiringpi  
from time import sleep
GPIO.setmode(GPIO.BCM)

wiringpi.wiringPiSetupGpio()    
wiringpi.pinMode(18,2)      # hardware pwm only works on GPIO port 18    
wiringpi.pwmWrite(18,0)     # duty cycle between 0 and 1024  
left_in1_pin = 4
left_in2_pin = 17
right_in1_pin = 27
right_in2_pin = 22
hote = ''
port = 12800
pause_time = 0.001          # you can change this to slow down/speed up  
class Motor(object):
	def __init__(self, in1_pin, in2_pin):
		self.in1_pin = in1_pin
		self.in2_pin = in2_pin

		GPIO.setup(self.in1_pin, GPIO.OUT)
		GPIO.setup(self.in2_pin, GPIO.OUT)
       
	def clockwise(self):
		GPIO.output(self.in1_pin, True)    
		GPIO.output(self.in2_pin, False)
	def counter_clockwise(self):
		GPIO.output(self.in1_pin, False)
		GPIO.output(self.in2_pin, True)
	       
	def stop(self):
		GPIO.output(self.in1_pin, False)    
		GPIO.output(self.in2_pin, False)
               
"""
#############################    Program principal    ########################################
"""
try:
	connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connexion_principale.bind((hote, port))
	connexion_principale.listen(5)
	print("Le serveur ecoute a present sur le port {}".format(port))
	serveur_lance = True
	clients_connectes = []
	set("delayed", "0")
	set("frequency", "500")
	set("active", "1")
	left_motor = Motor(left_in1_pin, left_in2_pin)
	right_motor = Motor(right_in1_pin, right_in2_pin)

	direction = None
	while serveur_lance:
	    # On va verifier que de nouveaux clients ne demandent pas a se connecter
	    # Pour cela, on ecoute la connexion_principale en lecture
	    # On attend maximum 50ms
		connexions_demandees, wlist, xlist = select.select([connexion_principale],
	        [], [], 0.05)
	    
		for connexion in connexions_demandees:
			connexion_avec_client, infos_connexion = connexion.accept()
	        # On ajoute le socket connecte a la liste des clients
			clients_connectes.append(connexion_avec_client)
	    
	    # Maintenant, on ecoute la liste des clients connectes
	    # Les clients renvoyes par select sont ceux devant etre lus (recv)
	    # On attend la encore 50ms maximum
	    # On enferme l'appel a select.select dans un bloc try
	    # En effet, si la liste de clients connectes est vide, une exception
	    # Peut etre levee
		clients_a_lire = []
		try:
			clients_a_lire, wlist, xlist = select.select(clients_connectes,[], [], 0.05)
		except select.error:
			pass

		else:
	        # On parcourt la liste des clients a lire
			for client in clients_a_lire:
				client.send(b"Command, f/r/o/p/s 0..9, E.g. f5 :")
				# Client est de type socket
				msg_recu = client.recv(1024)
				# Peut planter si le message contient des caracteres speciaux
				msg_recu = msg_recu.decode()
				print("Recu {}".format(msg_recu))
				client.send(b"5 / 5")
				if len(msg_recu)>0:
					direction = cmd[0]
				if len(cmd) > 1:
					speed = cmd[1]
					if speed == "1":
						speed = 615
					elif speed ==  "2":
						speed = 820
					elif speed == "3":
						speed = 1025
					else:
						speed = 820
					for i in range(0,speed):         # 1025 because it stops at 1024  
						wiringpi.pwmWrite(18,i)  
						sleep(pause_time) 
				if direction == "f":
					left_motor.clockwise()
					right_motor.clockwise()
				elif direction == "r":
					left_motor.counter_clockwise()
					right_motor.counter_clockwise()
				elif direction == "o": # opposite1
					left_motor.counter_clockwise()
					right_motor.clockwise()
				elif direction == "p":
					left_motor.clockwise()
					right_motor.counter_clockwise()
				elif msg_recu == "s":
					serveur_lance = False 
					left_motor.stop()
					right_motor.stop()       
				else:
					left_motor.stop()
					right_motor.stop()
	print("Fermeture des connexions")
	for client in clients_connectes:
		client.close()
	connexion_principale.close()
except KeyboardInterrupt:
	left_motor.stop()
	right_motor.stop()
	print "\nstopped"