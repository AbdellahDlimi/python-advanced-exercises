import socket
# Création du socket
serveur_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM )
# Lier le socket à l’adresse IP locale et au port 5000
serveur_socket.bind (('localhost',5000) )
# Écouter les connexions entrantes
serveur_socket.listen (1)
print ("Serveur en attente de connexion ... ")
# Accepter une connexion
connexion , adresse = serveur_socket . accept ()
print (f" Connecté par { adresse }")
# Recevoir un message (1024 octets maximum )
message_recu = connexion . recv (1024) . decode ()
print (f" Message reçu : { message_recu }")
# Envoyer une réponse
connexion.sendall ( b"Bonjour , client !")
connexion.close ()
serveur_socket.close ()