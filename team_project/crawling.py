import requests
from bs4 import BeautifulSoup
from requests import get
def ranking():
    response = requests.get('https://www.premierleague.com/')
    status_code = response.status_code

    if status_code == 200:
        soup = BeautifulSoup(response.text)
        text = soup.select_one('.standingEntriesContainer')
        text_a = text.select('a')

        ranking_list = []
        for i in range(len(text_a)):
            ranking_list.append(text_a[i].text.replace('\n', '').replace("  ", ""))

        return ranking_list