import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("house_prices.csv")
# Configuration globale
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# 1. Histogramme des surfaces habitables
plt.figure()
sns.histplot(data=data, x='sqft_living', bins=50, kde=True, color='steelblue')
plt.title('Distribution des surfaces habitables')
plt.xlabel('Surface habitable (sqft)')
plt.ylabel('Fréquence')
plt.show()

# 2. Histogramme de la taille des lots
plt.figure()
sns.histplot(data=data, x='sqft_lot', bins=100, color='forestgreen', kde=True)
plt.title('Distribution de la taille des terrains')
plt.xlabel('Taille du terrain (sqft)')
plt.ylabel('Fréquence')
plt.xlim(0, 50000)
plt.show()

# 3. Boxplot du prix par nombre d'étages
plt.figure()
sns.boxplot(data=data, x='floors', y='price', palette='viridis')
plt.title('Distribution des prix par nombre d\'étages')
plt.xlabel('Nombre d\'étages')
plt.ylabel('Prix ($)')
plt.yscale('log')
plt.show()

# 4. Diagramme de dispersion surface habitable vs prix
plt.figure()
sns.scatterplot(data=data, x='sqft_living', y='price', alpha=0.5, color='royalblue')
plt.title('Relation entre surface habitable et prix')
plt.xlabel('Surface habitable (sqft)')
plt.ylabel('Prix ($)')
plt.show()

# 5. Carte thermique des corrélations
plt.figure()
corr = data.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', center=0)
plt.title('Matrice de corrélation entre variables numériques')
plt.show()

# 6. Pairplot des variables sélectionnées
sns.pairplot(data=data[['price', 'sqft_living', 'bedrooms', 'bathrooms']])
plt.suptitle('Relations entre variables clés', y=1.02)
plt.show()

# 7. Diagramme de dispersion chambres vs prix coloré par waterfront
plt.figure()
sns.scatterplot(data=data, x='bedrooms', y='price', hue='waterfront', 
               palette=['red', 'blue'], alpha=0.6)
plt.title('Relation chambres/prix selon waterfront')
plt.xlabel('Nombre de chambres')
plt.ylabel('Prix ($)')
plt.legend(title='Waterfront', labels=['Non', 'Oui'])
plt.show()

# 8. Évolution du prix moyen par année de construction
plt.figure()
sns.lineplot(data=data, x='yr_built', y='price', estimator='mean', color='crimson')
plt.title('Prix moyen selon l\'année de construction')
plt.xlabel('Année de construction')
plt.ylabel('Prix moyen ($)')
plt.show()

# 9. Prix moyen par code postal (top 10)
top_zips = data.groupby('zipcode')['price'].mean().sort_values(ascending=False).head(10).index
plt.figure()
sns.barplot(data=data[data['zipcode'].isin(top_zips)], x='zipcode', y='price', 
           estimator='mean', palette='magma')
plt.title('Top 10 des codes postaux par prix moyen')
plt.xlabel('Code postal')
plt.ylabel('Prix moyen ($)')
plt.xticks(rotation=45)
plt.show()

# 10. Boxplot prix selon présence de sous-sol
data['has_basement'] = data['sqft_basement'] > 0
plt.figure()
sns.boxplot(data=data, x='has_basement', y='price', palette='Set2')
plt.title('Distribution des prix selon présence de sous-sol')
plt.xlabel('A un sous-sol')
plt.ylabel('Prix ($)')
plt.xticks([0, 1], ['Non', 'Oui'])
plt.yscale('log')
plt.show()

# 11. Violinplot des prix par catégorie de vue
plt.figure()
sns.violinplot(data=data, x='view', y='price', palette='rocket')
plt.title('Distribution des prix selon la qualité de la vue')
plt.xlabel('Qualité de la vue (0-4)')
plt.ylabel('Prix ($)')
plt.show()

# 12. Relation linéaire chambres vs prix
sns.lmplot(data=data, x='bedrooms', y='price', height=6, aspect=1.5)
plt.title('Relation linéaire entre nombre de chambres et prix')
plt.xlabel('Nombre de chambres')
plt.ylabel('Prix ($)')
plt.show()

# 13. Catplot comparant prix par chambres et waterfront
sns.catplot(data=data, x='bedrooms', y='price', hue='waterfront', 
           kind='box', height=6, aspect=1.5, palette='Set3')
plt.title('Distribution des prix par chambres et waterfront')
plt.xlabel('Nombre de chambres')
plt.ylabel('Prix ($)')
plt.show()

# 14. Scatterplot surface habitable vs lot avec style par étages
plt.figure()
sns.scatterplot(data=data, x='sqft_living', y='sqft_lot', hue='floors', 
               palette='viridis', alpha=0.6)
plt.title('Relation surface habitable vs terrain selon étages')
plt.xlabel('Surface habitable (sqft)')
plt.ylabel('Taille du terrain (sqft)')
plt.show()

# 15. Stripplot des prix par année de rénovation
renovated = data[data['yr_renovated'] > 0]
plt.figure()
sns.stripplot(data=renovated, x='yr_renovated', y='price', jitter=True, alpha=0.5)
plt.title('Distribution des prix par année de rénovation')
plt.xlabel('Année de rénovation')
plt.ylabel('Prix ($)')
plt.xticks(rotation=45)
plt.show()

# 16. Boxplot des prix par année de rénovation
plt.figure()
sns.boxplot(data=renovated, x='yr_renovated', y='price')
plt.title('Distribution des prix par année de rénovation')
plt.xlabel('Année de rénovation')
plt.ylabel('Prix ($)')
plt.xticks(rotation=45)
plt.show()

# 17. Regplot surface habitable vs prix avec régression
plt.figure()
sns.regplot(data=data, x='sqft_living', y='price', scatter_kws={'alpha':0.3})
plt.title('Relation surface habitable vs prix avec régression linéaire')
plt.xlabel('Surface habitable (sqft)')
plt.ylabel('Prix ($)')
plt.show()

# 18. Lineplot prix moyen par année de rénovation
plt.figure()
sns.lineplot(data=renovated, x='yr_renovated', y='price', estimator='mean')
plt.title('Évolution du prix moyen par année de rénovation')
plt.xlabel('Année de rénovation')
plt.ylabel('Prix moyen ($)')
plt.show()

# 19. Jointplot latitude vs longitude avec régression
sns.jointplot(data=data, x='long', y='lat', kind='reg', height=8)
plt.suptitle('Relation latitude/longitude avec régression', y=1.02)
plt.show()

# 20. KDEplot des prix selon la vue
plt.figure()
sns.kdeplot(data=data, x='price', hue='view', palette='crest', fill=True)
plt.title('Distribution des prix selon la qualité de la vue')
plt.xlabel('Prix ($)')
plt.ylabel('Densité')
plt.xlim(0, 3e6)
plt.show()

# 21. Barplot prix moyen par grade
plt.figure()
sns.barplot(data=data, x='grade', y='price', estimator='mean', palette='viridis')
plt.title('Prix moyen selon le grade de qualité')
plt.xlabel('Grade de qualité')
plt.ylabel('Prix moyen ($)')
plt.show()

# 22. Histplot de sqft_above
plt.figure()
sns.histplot(data=data, x='sqft_above', bins=50, kde=True, color='salmon')
plt.title('Distribution de la surface au-dessus du sol')
plt.xlabel('Surface au-dessus du sol (sqft)')
plt.ylabel('Fréquence')
plt.show()

# 23. Scatterplot géographique coloré par prix
plt.figure()
sns.scatterplot(data=data, x='long', y='lat', hue='price', 
               palette='viridis', alpha=0.6)
plt.title('Localisation des maisons colorée par prix')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# 24. Carte thermique des corrélations (version améliorée)
plt.figure()
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap='vlag', center=0)
plt.title('Matrice de corrélation (triangulaire)')
plt.show()

# 25. Boxplot des prix par grade
plt.figure()
sns.boxplot(data=data, x='grade', y='price', palette='rocket')
plt.title('Distribution des prix selon le grade de qualité')
plt.xlabel('Grade de qualité')
plt.ylabel('Prix ($)')
plt.yscale('log')
plt.show()