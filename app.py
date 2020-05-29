import requests
from bs4 import BeautifulSoup
response = requests.get(
    "https://leagueoflegends.fandom.com/wiki/Free_champion_rotation")
soup = BeautifulSoup(response.text, "html.parser")
rotation_date = soup.select_one("#rotationweek").text
list_of_champs = soup.select_one(".free_champion_rotation")
champions = [champ.get("data-champion")
             for champ in list_of_champs.select(".champion-icon")]

print(f"{rotation_date} free champions : {champions}")
