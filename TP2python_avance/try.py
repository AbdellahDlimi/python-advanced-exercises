import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import filedialog, messagebox

from PIL import Image, ImageTk  # 📸 Import de Pillow

# Liste des livres
livres = []
selected_image_path = None

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()
    
    if not title or not author or not year:
        messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
        return
    
    # Ajouter le livre à la liste
    book = {
        "title": title,
        "author": author,
        "year": year,
        "image": selected_image_path
    }
    livres.append(book)
    
    # Mettre à jour la Combobox
    book_combobox["values"] = [book["title"] for book in livres]
    messagebox.showinfo("Succès", "Le livre a été ajouté avec succès.")
    
    # Réinitialiser les champs
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)

def delete_book():
    selected_book_title = book_combobox.get()
    
    if not selected_book_title:
        messagebox.showerror("Erreur", "Veuillez sélectionner un livre à supprimer.")
        return
    
    global livres
    livres = [book for book in livres if book["title"] != selected_book_title]
    
    # Mettre à jour la Combobox
    book_combobox["values"] = [book["title"] for book in livres]
    image_label.config(image="")
    image_label.image = None  # Supprimer l'image affichée

    messagebox.showinfo("Succès", "Le livre a été supprimé avec succès.")

def show_book_details(event):
    selected_book_title = book_combobox.get()
    if selected_book_title:
        book = next((b for b in livres if b["title"] == selected_book_title), None)
        if book:
            title_entry.delete(0, tk.END)
            title_entry.insert(0, book["title"])
            author_entry.delete(0, tk.END)
            author_entry.insert(0, book["author"])
            year_entry.delete(0, tk.END)
            year_entry.insert(0, book["year"])
            
            if book["image"]:
                try:
                    img = Image.open(book["image"])
                    img = img.resize((200, 300))  # Redimensionner pour l'affichage
                    photo = ImageTk.PhotoImage(img)
                    image_label.config(image=photo)
                    image_label.image = photo  # 🔥 Garde une référence
                except Exception as e:
                    messagebox.showerror("Erreur", f"Impossible d'afficher l'image : {e}")

def browse_image():
    global selected_image_path
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")]
    )
    if file_path:
        selected_image_path = file_path

# 🪟 Fenêtre principale
root = tk.Tk()
root.title("Gestion de Bibliothèque")
root.geometry("600x600")

# Champs texte
title_label = tk.Label(root, text="Titre:")
title_label.grid(row=0, column=0, padx=10, pady=10)

title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1, padx=10, pady=10)

author_label = tk.Label(root, text="Auteur:")
author_label.grid(row=1, column=0, padx=10, pady=10)

author_entry = tk.Entry(root)
author_entry.grid(row=1, column=1, padx=10, pady=10)

year_label = tk.Label(root, text="Année:")
year_label.grid(row=2, column=0, padx=10, pady=10)

year_entry = tk.Entry(root)
year_entry.grid(row=2, column=1, padx=10, pady=10)

# Combobox
book_label = tk.Label(root, text="Sélectionner un livre:")
book_label.grid(row=3, column=0, padx=10, pady=10)

book_combobox = Combobox(root, state="readonly")
book_combobox.grid(row=3, column=1, padx=10, pady=10)
book_combobox.bind("<<ComboboxSelected>>", show_book_details)

# Affichage de l'image
image_label = tk.Label(root)
image_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Boutons
browse_button = tk.Button(root, text="Parcourir une image", command=browse_image)
browse_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

add_button = tk.Button(root, text="Ajouter", command=add_book)
add_button.grid(row=6, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Supprimer", command=delete_book)
delete_button.grid(row=6, column=1, padx=10, pady=10)

# Lancer l'app
root.mainloop()
