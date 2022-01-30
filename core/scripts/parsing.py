import requests
from bs4 import BeautifulSoup
link = 'https://www.hltv.org/ranking/teams/'


def get_all_names():
    soup = BeautifulSoup(requests.get(link).text, 'lxml')
    name = soup.find('div', class_='ranking').find_all('span', class_='name')
    names = []
    for i in name:
        names.append(i.string)
    return names
