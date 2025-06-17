import matplotlib.pyplot as plt
import numpy as np

mois = ['Jan', 'Fev', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Aout', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [0, 7, 10, 14, 18, 22, 25, 24, 20, 15, 9, 6]
temperature2 = [0, 12, 15, 18, 20, 24, 27, 26, 22, 17, 11, 8]

font1 = {'family': 'fantasy', 'color': 'r', 'size': 8}
font2 = {'family': 'fantasy', 'color': 'r', 'size': 10}

plt.suptitle('Evolution de la temperature', fontdict={'family': 'fantasy', 'color': 'b', 'fontsize': 80})

# Premier graphique
plt.subplot(1, 2, 1)
plt.plot(mois, temperature, c='r', marker='o', lw=2, ls='-.')
plt.grid(True, alpha=0.5, ls=':', lw=1, color='darkred')
plt.xlabel('Mois', fontdict=font1)
plt.ylabel('Temperature', fontdict=font1)
plt.title('Evolution de la temperature dans Casablanca',familly='fantasy', color='b', size=10 , loc='center')

# Deuxieme graphique
plt.subplot(1, 2, 2)
plt.plot(mois, temperature2, c='g', marker='o', lw=2, ls='-.')
plt.grid(True, alpha=0.5, ls=':', lw=1, color='darkred')
plt.xlabel('Mois', fontdict=font1)
plt.ylabel('Temperature', fontdict=font1)
plt.title('Evolution de la temperature dans Agadir', fontdict=font2, loc='center')

plt.tight_layout(rect=[0, 0, 1, 0.95])  

plt.show()


x = np.random.rand(10)
y = np.random.rand(10)

# Couleurs aléatoires
colors = np.random.rand(10)
sizes=np.random.rand(10)*100
plt.subplot(2, 1, 1)  
plt.scatter(x, y, c=colors, cmap='viridis',s=sizes)  
plt.colorbar()
plt.title('Scatter avec couleur par valeur')

plt.show()


categories = ['A', 'B', 'C', 'D', 'E']
valeurs = np.random.rand(5)*100
color= ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
plt.bar(categories, valeurs,color =color,ls='--',lw=2)
plt.title("Graphique à Barres")
plt.xlabel("Catégories")
plt.ylabel("Valeurs")
plt.grid(True, alpha=0.3)
plt.show()


data = np.random.rand(10)


plt.hist(data, bins=5, color='steelblue', edgecolor='white', ls='--',lw=2)
plt.title('Distribution de la surface habitable des maisons')
plt.xlabel('Surface habitable (pieds carrés)')
plt.ylabel('Nombre de maisons')
plt.grid(True, alpha=0.3)
plt.show()



porcetage = np.array([30,20,40,10])

label=['France', 'Espagne', 'Italie', 'Allemagne']
color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
explode = [0.1, 0.3, 0, 0] # explode 1er element
plt.pie(porcetage, labels=label, colors=color,autopct='%1.1f%%',explode=explode)
plt.title('Distribution de la surface habitable des maisons')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

