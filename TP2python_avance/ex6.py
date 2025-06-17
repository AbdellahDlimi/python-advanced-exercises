import tkinter as tk
from tkinter.ttk import Combobox

# Création de la fenêtre principale
root = tk.Tk()
root.title("Choisir un fruit")
root.geometry("700x300")

# Fonction appelée quand on clique sur le bouton
def afficher_fruit():
    fruit_choisi = combo.get()
    label_resultat.config(text=f"Tu as choisi : {fruit_choisi}")

def ajouter_fruit():
    nouveau_fruit = entry.get()
    if nouveau_fruit not in fruits :
        combo['values'] = fruits + [nouveau_fruit]
        entry.delete(0, tk.END)

entry = tk.Entry(root,width=30)
entry.pack(pady=10)

# Liste de fruits
fruits = ["Pomme", "Banane", "Orange", "Mangue", "Fraise"]

# Combobox
combo = Combobox(root, values=fruits)
combo.current(0)  # Par défaut : premier élément
combo.pack(pady=10)

# Bouton pour afficher le fruit choisi
btn_afficher = tk.Button(root, text="Afficher le fruit", command=afficher_fruit)
btn_afficher.pack(pady=10)

btn_afficher = tk.Button(root, text="Ajouter le fruit", command=ajouter_fruit)
btn_afficher.pack(pady=10)
# Label pour afficher le résultat
label_resultat = tk.Label(root, text="Fais ton choix")
label_resultat.pack(pady=10)

# Lancement de l'appli
root.mainloop()
