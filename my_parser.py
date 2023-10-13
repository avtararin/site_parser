'''This module contains functions for parsing an anime site'''
import bs4
from bs4 import BeautifulSoup
import requests
from requests import Timeout


def get_anime_data(url: str):
    '''This function gets data from the site'''
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print('Ошибка:')
            print(response.status_code)
            return response.status_code
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.find_all("div", class_="col-12")
    except Timeout:
        print('Ошибка таймаута')
        return 504
    except  ConnectionError:
        print('Ошибка соединения')
        return 503
    except:
        print('Не опознанная ошибка')
        return 404


def get_anime_rating(anime_info: bs4.element.Tag):
    '''This function gets anime rating'''
    anime_rating = anime_info.find("div", class_="p-rate-flag__text")
    return anime_rating.get_text(strip=True) if anime_rating else ""

def get_anime_name(anime_info: bs4.element.Tag):
    '''This function gets anime name'''
    anime_name = anime_info.find("div", class_="mb-1")
    return anime_name.get_text(strip=True) if anime_name else ""

def print_anime_info(anime_info: bs4.element.Tag):
    '''Anime information output function(rating and title)'''
    anime_rating = get_anime_rating(anime_info)
    anime_name = get_anime_name(anime_info)
    if anime_rating:
        print("Rating:", anime_rating)
    if anime_name:
        print("Name:", anime_name)
    print("--------------------")

def parse_anime_data(url: str):
    '''The function performs parsing of the site, displaying information about anime'''
    anime_data = get_anime_data(url)
    for anime_info in anime_data:
        print_anime_info(anime_info)
if __name__ == "__main__":
    URL = "https://animego.org/anime?sort=r.rating&direction=desc"
    parse_anime_data(URL)
