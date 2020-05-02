import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

res = requests.get(url)

dom = res.content

soup = BeautifulSoup(dom, 'html.parser')

title_l = soup.find_all('td', {'class': 'titleColumn'})
rating_l = soup.find_all('td', {'class': 'ratingColumn imdbRating'})

with open('imdb.txt', 'w') as file:
    for title, rating in zip(title_l, rating_l):
        title = title.text
        rating = rating.text

        title = title.lstrip()
        # rating = rating.rstrip()

        title = title.replace('\n', '')
        rating = rating.replace('\n', '\t')

        con = title + rating + '\n \n'

        file.write(con)



