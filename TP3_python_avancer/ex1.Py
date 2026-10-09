import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("house_prices.csv")

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12, 6)

# 1. Histogramme des surfaces habitables (sqft_living)
plt.figure()
plt.hist(data['sqft_living'], bins=100, color='steelblue', edgecolor='white')
plt.title('Distribution de la surface habitable des maisons')
plt.xlabel('Surface habitable (pieds carrés)')
plt.ylabel('Nombre de maisons')
plt.grid(True, alpha=0.3)
# 2. Histogramme de la taille des lots (sqft_lot)
plt.figure()
plt.hist(data['sqft_lot'], bins=100, color='forestgreen', edgecolor='white', range=(0, 50000))
plt.title('Distribution de la taille des terrains')
plt.xlabel('Taille du terrain (pieds carrés)')
plt.ylabel('Fréquence')
plt.grid(True, alpha=0.3)
plt.show()

# 3. Histogramme du nombre de salles de bain
plt.figure()
plt.hist(data['bathrooms'], bins=30, color='darkorange', edgecolor='white')
plt.title('Distribution du nombre de salles de bain')
plt.xlabel('Nombre de salles de bain')
plt.ylabel('Nombre de maisons')
plt.xticks(np.arange(0, 8, 0.5))
plt.grid(True, alpha=0.3)
plt.show()

# 4. Boxplot du prix selon le nombre d’étages (floors)
plt.figure()
data.boxplot(column='price', by='floors', grid=True, patch_artist=True,
            boxprops=dict(facecolor='lightblue'),
            medianprops=dict(color='red'))
plt.title('Distribution des prix par nombre d\'étages')
plt.suptitle('')  
plt.xlabel('Nombre d\'étages')
plt.ylabel('Prix ($)')
plt.show()

# 5. Boxplot du prix selon la presence de waterfront
plt.figure()
data.boxplot(column='price', by='waterfront', grid=True, patch_artist=True,
            boxprops=dict(facecolor='lightgreen'),
            medianprops=dict(color='red'))
plt.title('Distribution des prix selon la présence de waterfront')
plt.suptitle('')
plt.xticks([1, 2], ['Sans waterfront', 'Avec waterfront'])
plt.ylabel('Prix ($)')
plt.yscale('log')
plt.show()

# 6. Diagramme de dispersion surface habitable vs prix
plt.figure()
plt.scatter(data['sqft_living'], data['price'], alpha=0.4, color='royalblue')
plt.title('Relation entre surface habitable et prix')
plt.xlabel('Surface habitable (sqft)')
plt.ylabel('Prix ($)')
plt.grid(True, alpha=0.3)
plt.show()


# 7. Diagramme de dispersion nombre de chambres vs prix
plt.figure()
plt.scatter(data['bedrooms'], data['price'], alpha=0.5, color='mediumpurple')
plt.title('Relation entre nombre de chambres et prix')
plt.xlabel('Nombre de chambres')
plt.ylabel('Prix ($)')
plt.grid(True, alpha=0.3)
plt.show()

# 8. Évolution du prix moyen par année de rénovation
renovated = data[data['yr_renovated'] > 0].groupby('yr_renovated')['price'].mean()
plt.figure()
plt.plot(renovated.index, renovated.values, marker='o', color='crimson')
plt.title('Prix moyen des maisons par année de rénovation')
plt.xlabel('Année de rénovation')
plt.ylabel('Prix moyen ($)')
plt.grid(True)
plt.show()




# 9. Prix moyen par code postal (top 10)
zip_price = data.groupby('zipcode')['price'].mean().sort_values(ascending=False).head(10)
plt.figure()
zip_price.plot(kind='bar', color='teal')
plt.title('Top 10 des codes postaux avec le prix moyen le plus élevé')
plt.xlabel('Code postal')
plt.ylabel('Prix moyen ($)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.show()

# 10. Évolution du nombre de constructions par année
constructions = data['yr_built'].value_counts().sort_index()
plt.figure()
plt.plot(constructions.index, constructions.values, color='darkblue')
plt.title('Nombre de constructions par année')
plt.xlabel('Année de construction')
plt.ylabel('Nombre de maisons construites')
plt.grid(True)
plt.show()

# 11. Matrice de corrélation (nécessite numpy pour la création du masque)
corr = data.select_dtypes(include=[np.number]).corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
plt.figure()
plt.imshow(corr, cmap='coolwarm')
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title('Matrice de corrélation entre variables numériques')
plt.show()

# 12. Nuage de points géographique coloré par prix
plt.figure()
sc = plt.scatter(data['long'], data['lat'], c=data['price'], 
                cmap='viridis', alpha=0.5, s=10)
plt.colorbar(sc, label='Prix ($)')
plt.title('Localisation des maisons colorée par prix')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# 13. Relation entre surface du sous-sol et prix
has_basement = data[data['sqft_basement'] > 0]
plt.figure()
plt.scatter(has_basement['sqft_basement'], has_basement['price'], alpha=0.5, color='darkcyan')
plt.title('Relation entre surface du sous-sol et prix')
plt.xlabel('Surface du sous-sol (sqft)')
plt.ylabel('Prix ($)')
plt.grid(True, alpha=0.3)
plt.show()

# 14. Comparaison prix moyen avec/sans sous-sol
basement_comparison = data.groupby(data['sqft_basement'] > 0)['price'].mean()
plt.figure()
basement_comparison.plot(kind='bar', color=['lightgray', 'gold'])
plt.title('Prix moyen selon la présence de sous-sol')
plt.xticks([0, 1], ['Sans sous-sol', 'Avec sous-sol'], rotation=0)
plt.ylabel('Prix moyen ($)')
plt.grid(True, alpha=0.3)
plt.show()


# 15. Boxplot des prix par grade
plt.figure()
data.boxplot(column='price', by='grade', grid=True, patch_artist=True,
            boxprops=dict(facecolor='lightpink'),
            medianprops=dict(color='darkred'))
plt.title('Distribution des prix par grade de qualité')
plt.suptitle('')
plt.xlabel('Grade de qualité')
plt.ylabel('Prix ($)')
plt.yscale('log')
plt.show()

# 16. Tendance prix moyen vs surface habitable des voisins
living15_price = data.groupby('sqft_living15')['price'].mean().sort_index()
plt.figure()
plt.scatter(living15_price.index, living15_price.values, alpha=0.7, color='indigo')
plt.title('Prix moyen en fonction de la surface habitable des voisins')
plt.xlabel('Surface habitable moyenne des 15 maisons voisines')
plt.ylabel('Prix moyen ($)')
plt.grid(True)
plt.show()

# 17. Distribution de la surface au-dessus du sol
plt.figure()
plt.hist(data['sqft_above'], bins=50, color='salmon', edgecolor='white')
plt.title('Distribution de la surface au-dessus du sol')
plt.xlabel('Surface au-dessus du sol (sqft)')
plt.ylabel('Nombre de maisons')
plt.grid(True, alpha=0.3)
plt.show()

# 18. Prix moyen par qualité de vue
view_price = data.groupby('view')['price'].mean()
plt.figure()
view_price.plot(kind='bar', color='mediumseagreen')
plt.title('Prix moyen selon la qualité de la vue')
plt.xlabel('Qualité de la vue (0-4)')
plt.ylabel('Prix moyen ($)')
plt.xticks(rotation=0)
plt.grid(True, alpha=0.3)
plt.show()

# 19. Surface habitable moyenne par année de construction
living_by_year = data.groupby('yr_built')['sqft_living'].mean()
plt.figure()
plt.plot(living_by_year.index, living_by_year.values, color='darkred')
plt.title('Évolution de la surface habitable moyenne par année de construction')
plt.xlabel('Année de construction')
plt.ylabel('Surface habitable moyenne (sqft)')
plt.grid(True)
plt.show()

# 20. Histogramme cumulatif des prix
plt.figure()
plt.hist(data['price'], bins=100, color='darkorchid', edgecolor='white', 
         cumulative=True, density=True)
plt.title('Distribution cumulative des prix des maisons')
plt.xlabel('Prix ($)')
plt.ylabel('Proportion cumulative')
plt.grid(True, alpha=0.3)
plt.show()






