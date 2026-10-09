import socket

# Connexion au serveur
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('localhost', 5000))
print("Connecté au serveur. Tapez 'exit' pour quitter.")

while True:
    nom_fichier = input("Entrez le nom du fichier à rechercher : ")
    
    if nom_fichier== 'exit':
        socket.sendall(nom_fichier.encode()) #le server doit afiicher la deconnexion du client
        break
    
    # Envoyer la requête
    socket.sendall(nom_fichier.encode())
    
    # Recevoir la réponse
    reponse = socket.recv(1024).decode()
    print(f"Réponse du serveur : {reponse}")

# Fermer la connexion
socket.close()