import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

BASE_URL = "http://books.toscrape.com/catalogue/"
books = []

if not os.path.exists('images'):
    os.makedirs('images')

for page in range(1, 51):
    print(f"Scraping page {page}...")
    url = f"{BASE_URL}page-{page}.html"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erreur sur la page {page}: {e}")
        continue
    
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article', class_='product_pod')
    
    for article in articles:
        title = article.h3.a['title']
        price = article.find('p', class_='price_color').text.strip().replace('£', '')
        
        # Ici on prend directement la note sous forme de texte ("One", "Two", etc.)
        rating = article.p['class'][1]
        
        stock = article.find('p', class_='instock availability').text.strip()
        image_rel_url = article.find('img')['src'].replace('../../', '')
        image_url = f"http://books.toscrape.com/{image_rel_url}"
        
        try:
            img_data = requests.get(image_url).content
            img_name = title.replace('/', '_')[:50] + '.jpg'  # Eviter les noms trop longs
            with open(os.path.join('images', img_name), 'wb') as handler:
                handler.write(img_data)
        except:
            print(f"Impossible de télécharger l'image de {title}")
        
        books.append({'Title': title,'Price': price,'Rating': rating,  
            'Stock': stock,
            'Image_URL': image_url
        })

df = pd.DataFrame(books)
df.to_csv('books.csv', index=False)

print("Scraping terminé ! Données sauvegardées dans books.csv")
