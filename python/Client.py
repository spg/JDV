# -*- coding: utf-8 -*
import socket

hote = "10.240.230.197" #adresse ip du mac mini
port = 8080

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print "Connexion établie avec le serveur sur le port", port

msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    msg_a_envoyer = raw_input("> ")
    # Peut planter si vous entrez des caractères spéciaux
    msg_a_envoyer = msg_a_envoyer.encode()
    # On envoie le message
    connexion_avec_serveur.send(msg_a_envoyer)
    msg_recu = connexion_avec_serveur.recv(1024)
    print msg_recu.decode() # là encore, peut planter si y'a des accents

print "Fermeture de la connexion"
connexion_avec_serveur.close()
