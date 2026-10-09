import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

livres = []
def ajouter_book():
    title = titre_entry.get()
    author = auteur_entry.get()
    annee = annee_entry.get()
    
    if not title or not author or not annee or not image_path.get():
        text.delete(1.0, tk.END)
        text.insert(tk.END, "Tous les champs doivent être remplis, y compris l'image.")
        return

    book = {     "title": title, "author": author,"year": annee,"image": image_path.get()    }
    livres.append(book)
    
    Combo["values"] = [book["title"] for book in livres]
    
    text.delete(1.0, tk.END)
    text.insert(tk.END, "Le livre a été ajouté avec succès.")

    titre_entry.delete(0, tk.END)
    auteur_entry.delete(0, tk.END)
    annee_entry.delete(0, tk.END)
    image_path.set("")
    image_label.config(image="")  # Réinitialise l'image affichée

def suprimer_box():
    titre_selectionner = Combo.get()
    if not titre_selectionner:
        text.insert(tk.END, "Veuillez sélectionner un livre à supprimer.")
        return
    else:
        global livres
        livres = [book for book in livres if book["title"] != titre_selectionner]
        Combo["values"] = [book["title"] for book in livres]
        text.delete(1.0, tk.END)
        text.insert(tk.END, "Le livre a été supprimé avec succès.")
        image_label.config(image="")

def afficher_details():
    titre_selectionner = Combo.get()
    if titre_selectionner:
        # book = next((book for book in livres if book["title"] == titre_selectionner), None)
        book = None
        for b in livres:
            if b["title"] == titre_selectionner:
                book = b
                break
            
        if book:
            titre_entry.delete(0, tk.END)
            auteur_entry.delete(0, tk.END)
            annee_entry.delete(0, tk.END)
            titre_entry.insert(0, book["title"])
            auteur_entry.insert(0, book["author"])
            annee_entry.insert(0, book["year"])
            image_path.set(book["image"])
            afficher_image(book["image"])

def browse_image():
    chemin = filedialog.askopenfilename(
        title="Choisir une image",
        filetypes=[("Fichiers image", "*.jpg *.jpeg *.png *.gif *.bmp")]
    )
    if chemin:
        image_path.set(chemin)
        afficher_image(chemin)

def afficher_image(chemin):
    try:
        img = Image.open(chemin)
        img = img.resize((150, 200))  # Redimensionner pour affichage
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo  # Garder une référence
    except:
        image_label.config(image="")
        text.insert(tk.END, "Impossible de charger l'image.")

root = tk.Tk()
root.title("Gestion de Bibliothèque")
root.geometry("600x650")

image_path = tk.StringVar()  # Variable pour stocker le chemin de l'image

label = tk.Label(root, text="Gestion de Bibliothèque",
                 fg="#750404", bg="#F0F0F0",
                 font="Helvatica 20 bold", pady=30)
label.grid(row=0, column=1, padx=10, pady=2)

Elements = [("Titre", 1), ("Auteur", 2), ("Année", 3)]
for (elm, row) in Elements:
    label = tk.Label(root, text=elm + "   :")
    label.grid(row=row, column=0, padx=10, pady=10)
    entry = tk.Entry(root)
    if elm == "Titre":
        titre_entry = entry
    elif elm == "Auteur":
        auteur_entry = entry
    elif elm == "Année":
        annee_entry = entry
    entry.grid(row=row, column=1, padx=10, pady=10)

combo_label = tk.Label(root, text="Sélectionner un livre:")
combo_label.grid(row=5, column=0, padx=10, pady=10)
Combo = Combobox(root, state="normal", width=30)
Combo.grid(row=5, column=1, padx=10, pady=10)

browse_button = tk.Button(root, text="Parcourir une image", pady=3,
                          fg="#fcfbfa", bg="#f0823e", font="Helvatica 10 bold",
                          command=browse_image)
browse_button.grid(row=6, column=1, padx=10, pady=10)

button_ajouter = tk.Button(root, text="ajouter", pady=3, fg="#fcfbfa",
                           bg="#f0823e", font="Helvatica 10 bold", command=ajouter_book)
button_ajouter.grid(row=7, column=0, padx=10, pady=10)

button_suprimer = tk.Button(root, text="supprimer", pady=3, fg="#fcfbfa",
                            bg="#f0823e", font="Helvatica 10 bold", command=suprimer_box)
button_suprimer.grid(row=7, column=2, padx=10, pady=10)

affiche_button = tk.Button(root, text="Afficher les details", fg="#fcfbfa",
                           bg="#f0823e", font="Helvatica 10 bold", command=afficher_details)
affiche_button.grid(row=9, column=1, padx=10, pady=10)

text = tk.Text(root, height=5, width=50)
text.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

image_label = tk.Label(root)
image_label.grid(row=10, column=1, pady=10)
root.mainloop()
