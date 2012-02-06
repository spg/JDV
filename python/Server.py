# -*- coding: utf-8 -*
import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(1)
print "Le serveur ecoute a présent sur le port", port

connexion_avec_client, infos_connexion = connexion_principale.accept()

msg_recu = b""
while msg_recu != b"fin":
    msg_recu = connexion_avec_client.recv(1024)

    print msg_recu.decode()
    connexion_avec_client.send(b"5 / 5")

print "Fermetures de connexions"
connexion_avec_client.close()
connexion_principale.close()
