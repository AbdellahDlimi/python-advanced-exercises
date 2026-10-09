# serveur_multi_lock .py
import socket
import threading
# Variables globales
nb_clients = 0
lock = threading . Lock ()
def gerer_client ( connexion , adresse ) :
    global nb_clients
    with lock :
        nb_clients += 1
        print ( f"[+] Nouveau client connecté : {adresse} | Clients actifs : { nb_clients }")
    try :
        message_recu = connexion.recv (1024) . decode ()
        print ( f" Message reçu de { adresse } : { message_recu }")
        connexion . sendall ( b" Bonjour , client depuis le serveur multi -clients avec compteur !")
    finally :
        connexion . close ()
    with lock :
        nb_clients -= 1
        print ( f"[ -] Client déconnecté : { adresse } | Clients actifs : { nb_clients }")       
# Création du socket
serveur_socket = socket . socket ( socket . AF_INET , socket . SOCK_STREAM )
serveur_socket . bind (('localhost', 5003) )
serveur_socket . listen ()
print (" Serveur prêt à accepter plusieurs clients ( avec compteur )... ")
# Boucle principale
while True :
    connexion , adresse = serveur_socket . accept ()
    thread = threading . Thread ( target = gerer_client , args =( connexion,adresse ) )
    thread.start()