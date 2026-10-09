import socket
import os

# Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Lier le socket à l’adresse IP locale et au port 5000
socket.bind(('localhost', 5000))
# Écouter les connexions entrantes
socket.listen()
print(f"Serveur en attente sur le port {5000}...")

while True:
    #accepter la connexion
    conn, addresse = socket.accept()
    print(f"Connecté à {addresse}")
    
    try:
        while True:
            # Recevoir le nom du fichier
            nom_fichier = conn.recv(1024).decode()
            
            if  nom_fichier == 'exit':
                print("Déconnexion du client.")
                break
            
            print(f"Fichier reçu : {nom_fichier}")
            
            # Vérifier si le fichier existe
            if os.path.exists(nom_fichier):
                reponse = "Oui, le fichier existe."
            else:
                reponse = "Non, le fichier n'existe pas."
            
            # Envoyer la réponse
            conn.sendall(reponse.encode())
    finally:
        conn.close()