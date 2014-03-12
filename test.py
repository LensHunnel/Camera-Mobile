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
import socket

hote = ''
port = 12801

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print ("le serveur ecoute a present sur le port{}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

msg_recu = b""
while msg_recu != b"fin":
    msg_recu = connexion_avec_client.recv(1024)
    # L'instruction ci-dessous peut lever une exception si le message
    #Receptionne comporte des accents
    print(msg_recu.decode())
    connexion_avec_client.send(b"5 / 5")

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()
