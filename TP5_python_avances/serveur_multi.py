import socket
import threading
def gerer_client ( connexion , adresse ) :
    print (f" Connecté par { adresse }")
    try:
        message_recu = connexion . recv (1024) . decode ()
        print (f" Message reçu de { adresse } : { message_recu }")
        connexion . sendall ( b" Bonjour , client depuis le serveur multi-clients !")
    finally :
        connexion . close ()
# Création du socket
serveur_socket = socket . socket ( socket.AF_INET , socket.SOCK_STREAM )
serveur_socket.bind (('localhost',5002) )
serveur_socket.listen ()
print (" Serveur prêt à accepter plusieurs clients ... ")
# Boucle principale
while True :
    connexion , adresse = serveur_socket . accept ()
    print ( f" Nouvelle connexion de { adresse }")
    # Démarrer un thread pour gérer ce client
    thread = threading . Thread ( target = gerer_client , args =( connexion ,
    adresse ) )
    thread . start ()
