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


def analys_match(link_on_match):
    soup = BeautifulSoup(requests.get(link_on_match).text, 'lxml')
    main_block = soup.find('div', class_="standard-box pick-a-winner")
    first_team_block = main_block.find(
        'div', class_="pick-a-winner-team team1 canvote")
    first_team_name = first_team_block.find(
        'div', class_="pick-a-winner-team-name text-ellipsis").text
    first_team_percents = first_team_block.find(
        'div', class_="percentage").text
    first_team_logo = first_team_block.find('img', class_="logo").attrs['src']
    second_team_block = main_block.find(
        'div', class_="pick-a-winner-team team2 canvote")
    second_team_name = second_team_block.find(
        'div', class_="pick-a-winner-team-name text-ellipsis").text
    second_team_percents = second_team_block.find(
        'div', class_="percentage").text
    second_team_logo = second_team_block.find(
        'img', class_="logo").attrs['src']
    return first_team_name, first_team_percents, first_team_logo, second_team_name, second_team_percents, second_team_logo
