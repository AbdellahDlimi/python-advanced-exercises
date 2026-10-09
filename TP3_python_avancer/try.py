import matplotlib.pyplot as plt

# mois = ['Jan', 'Fev', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Aout', 'Sep', 'Oct', 'Nov', 'Dec']
# temperature = [0, 7, 10, 14, 18, 22, 25, 24, 20, 15, 9, 6]

# x = mois
# y = temperature

# plt.plot(x, y,c='g',ls='--',marker='x',lw=2,label='Temperature')
# plt.grid(True, alpha=0.3, ls=':', lw=1, color='darkred')
# plt.xlabel('X-axis',fontdict={'family': 'fantasy', 'color': 'r', 'size': 8})
# plt.ylabel('Y-axis')
# plt.title('Line Graph')
# plt.show()
# import numpy as np

# # Génération de données aléatoires
# np.random.seed(42)
# x = np.random.rand(50)
# y = np.random.rand(50)
# tailles = np.random.randint(10, 200, size=50)
# couleurs = np.random.rand(50)
# valeurs = np.random.rand(50)  # Pour la colormap

# plt.figure(figsize=(10, 6))

# # Nuage de points avec paramètres avancés
# scatter = plt.scatter(
#     x, y,
#     c=valeurs,          # Couleurs basées sur 'valeurs' (utilise cmap)
#     s=tailles,          # Tailles variables
#     alpha=0.7,          # Transparence (0=transparent, 1=opaque)
#     cmap='viridis',     # Palette de couleurs
#     edgecolor='black',  # Couleur des contours
#     linewidths=0.5      # Épaisseur des contours
# )

# # Ajout de la barre de couleur
# plt.colorbar(scatter, label='Valeurs')

# # Titres et légendes
# plt.title('Nuage de points avancé', fontsize=14)
# plt.xlabel('Axe X', fontsize=12)
# plt.ylabel('Axe Y', fontsize=12)

# # Grille et affichage
# plt.grid(True, alpha=0.3)
# plt.show()

# import matplotlib.pyplot as plt

# # Données simples
# notes = [12, 15, 13, 17, 14, 12, 15, 19, 17, 13, 16, 18, 11, 14, 15]

# # Création de l'histogramme
# plt.hist(notes, bins=5, range=(10, 20), density=False, color='skyblue', edgecolor='black')

# # Ajouter un titre et des labels
# plt.title("Distribution des notes")
# plt.xlabel("Notes")
# plt.ylabel("Fréquence")

# # Afficher le graphique
# plt.show()

# import matplotlib.pyplot as plt

# # Données
# parts = [40, 25, 20, 15]
# labels = ['Python', 'Java', 'C++', 'PHP']
# colors = ['gold', 'lightgreen', 'skyblue', 'lightcoral']
# explode = [0.1, 0, 0, 0]  # Mettre en avant la 1ère part (Python)

# # Diagramme circulaire
# plt.pie(
#     parts,
#     labels=labels,
#     explode=explode,
#     startangle=90,
#     shadow=True,
#     colors=colors,
#     autopct='%1.1f%%'
# )

# # Légende (facultative si labels sont dans le graphique)
# plt.legend(title="Langages")

# plt.title("Répartition des langages")
# plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
print(df.head())

# sns.histplot(data=df, x='total_bill', kde=False, color='skyblue')
# plt.title("Distribution des factures (total_bill)")
# plt.show()

# sns.kdeplot(data=df, x='total_bill', fill=True, color='green')
# plt.title("Courbe de densité (total_bill)")
# plt.show()

# sns.jointplot(data=df, x='total_bill', y='tip')
# plt.show()

# sns.pairplot(data=df, hue='sex')
# plt.show()

# sns.boxplot(data=df, x='day', y='total_bill')
# plt.title("Boxplot : Total des factures par jour")
# plt.show()
# sns.barplot(data=df, x='day', y='tip', ci='sd')
# plt.title("Pourboire moyen par jour")
# plt.show()

# sns.violinplot(data=df, x='day', y='total_bill')
# plt.title("Violinplot : Total des factures par jour")
# plt.show()

sns.pointplot(data=df, x='day', y='tip', hue='sex')
plt.title("Tendance des pourboires selon le sexe")
plt.show()









