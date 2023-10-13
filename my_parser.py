from bs4 import BeautifulSoup
import requests

def get_anime_data(URL):
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, "html.parser")
    return soup.find_all("div", class_="col-12")

def get_anime_rating(anime_info):
    anime_rating = anime_info.find("div", class_="p-rate-flag__text")
    return anime_rating.get_text(strip=True) if anime_rating else ""

def get_anime_name(anime_info):
    anime_name = anime_info.find("div", class_="mb-1")
    return anime_name.get_text(strip=True) if anime_name else ""

def print_anime_info(anime_info):
    anime_rating = get_anime_rating(anime_info)
    anime_name = get_anime_name(anime_info)
    if anime_rating:
        print("Rating:", anime_rating)
    if anime_name:
        print("Name:", anime_name)
    print("--------------------")

def parse_anime_data(URL):
    anime_data = get_anime_data(URL)
    for anime_info in anime_data:
        print_anime_info(anime_info)

if __name__ == "main":
    URL = "https://animego.org/anime?sort=r.rating&direction=desc"
    parse_anime_data(URL)