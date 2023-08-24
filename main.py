import requests
from bs4 import BeautifulSoup

url = "https://www.premierleague.com/tables"
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml") 

standings = soup.find("div", attrs={"data-ui-tab": "First Team"}).find_all(
"tr")[1::2]  

with open("files.txt", "w") as f:
    
    for standing in standings:
        position = standing.find("span", attrs={"class": "league-table__value value"}).text.strip()
        club_name = standing.find("span",{"class": "long"}).text
        points = standing.find("td", {"class": "points"}).text
        f.write (f'{position} {club_name}, {points}\n')
        
        