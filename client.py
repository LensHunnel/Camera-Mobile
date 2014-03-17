import socket
from ihm import ControlsIHM
hote = "localhost"
port = 12800
try:
    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect((hote, port))
    print("connexion etablie avec le port {}".format(port))
    print 'debut mainloop'
    ControlsIHM().mainloop()
    print "fin mainloop"
    msg_a_envoyer = b""
    msg = b""
    while msg != b"fin":
        msg_a_envoyer = input("> ")
        while msg_a_envoyer != "":       
            str(msg_a_envoyer)
            # Peut planter si vous tapez des caracteres speciaux
            msg_a_envoyer = msg_a_envoyer.encode()
            # On envoie le message
            connexion_avec_serveur.send(msg_a_envoyer)
            msg_recu = connexion_avec_serveur.recv(1024)
            print(msg_recu.decode()) # La encore, peut planter s'il y a des accents

    print("Fermeture de la connexion")
    connexion_avec_serveur.close()
except socket.error:
    print "connexion closed"
