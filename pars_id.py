import json
import requests
from bs4 import BeautifulSoup

URL = 'https://www.superheroapi.com/ids.html'
def get_data():
    proxy = {'http': 'http://proxy.server:3128'}

    heroes_page = requests.get(URL, proxies=proxy).text
    heroes_parser = BeautifulSoup(heroes_page,'html.parser')
    heroes_data = {}
    for row in heroes_parser.find_all('tr'):
        
        id = row.find_all('td')[0].text
        name = row.find_all('td')[1].text
        heroes_data[name] = id

    with open('heroes_data.json', 'w+') as f:
        json_data = json.dumps(heroes_data)
        f.write(json_data)
    





