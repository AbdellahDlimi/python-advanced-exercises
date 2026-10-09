import requests as r
from bs4 import BeautifulSoup
import csv

date = input("Enter a date (dd/mm/yyyy): ")
url = f"https://www.yallakora.com/match-center/مركز-المباريات?date={date}#matchesclipPrev"
page = r.get(url)

def main(page):
    src = page.content
    soup = BeautifulSoup(src, 'lxml')

    champio_leagues = soup.find_all("div", {'class': 'matchCard'})
    liste = []

    for champ in champio_leagues:
        try:
            league_title = champ.find("h2").text.strip()
            all_matches = champ.find_all("li", {'class': 'matchItem'})
            
            for match in all_matches:
                try:
                    team1 = match.find("div", {'class': 'teamA'}).find("p").text.strip()
                    team2 = match.find("div", {'class': 'teamB'}).find("p").text.strip()

                    result_spans = match.find("div", {'class': 'MResult'}).find_all("span", {'class': 'score'})
                    if len(result_spans) == 2:
                        score = f"{result_spans[0].text.strip()} - {result_spans[1].text.strip()}"
                    else:
                        score = "N/A"

                    time = match.find("div", {'class': 'MResult'}).find("span", {'class': 'time'}).text.strip()

                    liste.append({
                        'Competition': league_title,
                        'Team 1': team1,
                        'Team 2': team2,
                        'Score': score,
                        'Time': time
                    })
                except:
                    continue
        except:
            continue

    if liste:
        with open('matches.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['Competition', 'Team 1', 'Team 2', 'Score', 'Time'])
            writer.writeheader()
            writer.writerows(liste)
        print("✅ Les matchs ont été enregistrés dans 'matches.csv'")
    else:
        print("❌ Aucun match trouvé pour cette date.")

main(page)
