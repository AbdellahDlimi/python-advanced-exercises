import requests
from bs4 import BeautifulSoup
import csv

base_url = "http://books.toscrape.com/"

books = []

def convert_rating(rating_class):
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings.get(rating_class, 0)

# Boucle sur toutes les pages
url = base_url + "catalogue/page-1.html"
while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Trouver tous les livres sur la page
    articles = soup.find_all("article", class_="product_pod")
    
    for article in articles:
        title = article.h3.a["title"]
        price = article.find("p", class_="price_color").text.strip()
        rating_class = article.find("p", class_="star-rating")["class"][1]
        rating = convert_rating(rating_class)
        stock = article.find("p", class_="instock availability").text.strip()
        image_url = base_url + article.find("img")["src"].replace("../", "")
        
        books.append([title, price, rating, stock, image_url])

    # Vérifier s'il y a une page suivante
    next_button = soup.find("li", class_="next")
    if next_button:
        next_page = next_button.a["href"]
        url = base_url + "catalogue/" + next_page
    else:
        break

# Enregistrer les données dans un fichier CSV
with open("books.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Rating", "Stock", "Image_URL"])
    writer.writerows(books)

print("Scraping terminé et fichier books.csv créé avec succès !")
