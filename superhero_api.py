import json
import requests
import pprint
import os

from pars_id import get_data

pp = pprint.PrettyPrinter(indent=4)

API_KEY = '10218686935504422'

directory_list = os.listdir()

if 'heroes_data.json' not in directory_list:
    get_data()

with open('heroes_data.json','r+') as f:
    heroes_data = json.loads(f.read())


class NotFoundError(Exception):
    pass






class SuperheroAPI:                                                                                                    
    def __init__(self, API = API_KEY, data = heroes_data):
        self._token = API
        self._data = data
        self._url = f'https://www.superheroapi.com/api/{self._token}'
        self._proxy = {'http': 'http://proxy.server:3128'}
    
    
    def get_hero(self, name):
        name = self._parse_name(name)
        hero_id = self._get_id(name)
        return self._parse_api(self._url + f'/{hero_id}')    
    
    def get_hero_stats(self,name):
        name = self._parse_name(name)
        hero_id = self._get_id(name)

        return self._parse_api(self._url + f'/{hero_id}/powerstats')


    def _parse_name(self, name):
        return  name.lower().title()

    def _get_id(self, name):
        data = self._data.get(name,False)
        if data:
            return data
        else:
            raise NotFoundError('Name not found')
    
    def _parse_api(self,url):
        response = requests.get(url, timeout=15, proxies=self._proxy)
        response.close()
        return response.json()
    

    def download_image(self,name):
        image_url = self.get_hero_image_url(name)

        with open(f'{name}.jpg','wb') as file:
           image = requests.get(image_url).content
           file.write(image)
    
    def get_hero_image_url(self, name):
        name = self._parse_name(name)
        id = self._get_id(name)
        return self._parse_api(self._url + f'/{id}/image')['url']

    of = 1

if __name__ == '__main__':
    hero = SuperheroAPI()

    result = hero.get_hero('yoda')
    hero.download_image('Luke Skywalker')

