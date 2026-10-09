# 🐍 Travaux Pratiques — Python Avancé

Bienvenue dans le dépôt dédié aux travaux pratiques de **Python Avancé**. Ce projet regroupe l'ensemble des exercices, codes sources et supports de cours organisés par modules thématiques.

---

## 📁 Structure du Projet

```text
TP_python_avanceé/
├── TP2python_avance/       # TP 2 : Interfaces Graphiques (GUI) avec Tkinter
│   ├── TP.pdf              # Énoncé du TP 2
│   ├── ex1.py ... ex6.py   # Exercices d'application Tkinter
│   └── try.py              # Tests & expérimentations
│
├── TP3_python_avancer/     # TP 3 : Analyse & Visualisation de Données
│   ├── TP3.pdf             # Énoncé du TP 3
│   ├── ex1.Py, ex2.py      # Exercices pratiques
│   ├── exircice.py         # Visualisation avec Matplotlib
│   └── house_prices.csv    # Jeu de données d'exemple
│
├── TP4_puthon_Avancer/     # TP 4 : Web Scraping & Extraction de Données
│   ├── TP4.pdf             # Énoncé du TP 4
│   ├── web_Scraping.py     # Scraping de données web (BeautifulSoup / Requests)
│   ├── books.csv           # Données extraites de livres
│   ├── matches.csv         # Données extraites de matchs
│   └── devoir.py           # Exercices / devoirs associés
│
├── TP5_python_avances/     # TP 5 : Programmation Réseau & Sockets
│   ├── client*.py          # Implémentations clients TCP
│   ├── serveur*.py         # Implémentations serveurs TCP
│   └── serveur_multi.py    # Serveur multi-clients
│
└── README.md               # Documentation du dépôt
```

---

## 📚 Détail des Modules

### 🖥️ TP 2 — Interfaces Graphiques (Tkinter)
- **Objectif :** Conception d'applications de bureau interactives en Python.
- **Notions abordées :** Fenêtres principales, labels, boutons, champs de saisie (`Entry`), mise en page (`pack`), gestion des événements et liaisons de callbacks.
- **Technologies :** `tkinter`

### 📊 TP 3 — Analyse & Visualisation de Données
- **Objectif :** Exploration, manipulation et représentation graphique de jeux de données.
- **Notions abordées :** Tableaux multidimensionnels, sous-graphiques (`subplots`), personnalisation de courbes, graphiques de comparaison, chargement et traitement de fichiers CSV (`house_prices.csv`).
- **Technologies :** `numpy`, `matplotlib`, `pandas`

### 🌐 TP 4 — Web Scraping
- **Objectif :** Récupération automatisée et structuration de données à partir de sites web.
- **Notions abordées :** Requêtes HTTP, parsing HTML avec arbres DOM, sélection d'éléments via classes/balises CSS, gestion des erreurs d'extraction et persistance au format CSV.
- **Technologies :** `requests`, `beautifulsoup4`, `lxml`, `csv`

### 🔌 TP 5 — Programmation Réseau & Sockets
- **Objectif :** Communication réseau point-à-point et en étoile via sockets TCP.
- **Notions abordées :** Création de sockets, liaison d'adresses/ports (`bind`), écoute (`listen`), acceptation de connexions (`accept`), échanges bidirectionnels de messages (`recv`/`sendall`) et gestion de serveurs multi-clients.
- **Technologies :** `socket`, `threading`

---

## ⚙️ Prérequis & Installation

### 1. Prérequis
- **Python 3.8+** installé sur votre machine.

### 2. Cloner le dépôt
```bash
git clone https://github.com/AbdellahDlimi/TP_python_avance-.git
cd TP_python_avance-
```

### 3. Installer les dépendances
```bash
pip install numpy matplotlib pandas requests beautifulsoup4 lxml
```
*(Le module `tkinter` et le module `socket` sont intégrés par défaut avec l'installation standard de Python).*

---

## 🚀 Exécution des Exercices

Chaque script peut être exécuté individuellement depuis son dossier respectif ou depuis la racine :

```bash
# Exemple : Lancer un exercice Tkinter (TP 2)
python TP2python_avance/ex1.py

# Exemple : Lancer le script de visualisation (TP 3)
python TP3_python_avancer/exircice.py

# Exemple : Lancer un script de scraping (TP 4)
python TP4_puthon_Avancer/web_Scraping.py

# Exemple : Lancer le serveur de socket puis un client (TP 5)
python TP5_python_avances/serveur.py
python TP5_python_avances/client.py
```

---

## 👤 Auteur
- **Abdellah Dlimi** — [GitHub](https://github.com/AbdellahDlimi)
