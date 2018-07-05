import csv

import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
allLinks = soup.find_all("a")

dataList = soup.find("tbody", {"class": "lister-list"})
rows = dataList.find_all("tr")
movie = []
for item in rows:
    movieName = item.contents[3].find("a").text
    year = item.contents[3].find("span", {"class": "secondaryInfo"}).text.replace("(", " ").replace(")", " ")
    rating = item.contents[5].find("strong").text
    movie.append([movieName, year, rating])

with open("imdb250.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["movieName", "year", "rating"])
    for movieName, year, rating in movie:
        writer.writerow([movieName, year, rating])
