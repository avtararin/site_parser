from bs4 import BeautifulSoup
import requests

url = "https://animego.org/anime?sort=r.rating&direction=desc"
request = requests.get(url)

soup = BeautifulSoup(request.text, "html.parser")

teme = soup.find_all("div", class_="col-12")

for temes in teme:
    anime_rating = temes.find("div", class_="p-rate-flag__text")
    anime_name = temes.find("div", class_="mb-1")
    print("Rating:", anime_rating)
    print("Name:", anime_name)
    print("--------------------")