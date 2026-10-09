import socket
# Création du socket
client_socket = socket . socket ( socket.AF_INET , socket.SOCK_STREAM )
# Connexion au serveur
client_socket . connect (('localhost', 5003) )
# Envoi d’un message
client_socket . sendall (b" Bonjour , serveur !")
# Réception de la réponse
reponse = client_socket . recv (1024) . decode ()
print (f"Réponse du serveur : { reponse }")
# Fermer la connexion
client_socket . close ()