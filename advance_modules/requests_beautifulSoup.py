import requests
from bs4 import BeautifulSoup


url = 'https://www.sahibinden.com/motosiklet-yamaha-royal-star-xvz-1300'
# url = 'https://yellowpages.com.tr/ara?q=istanbul'
# headers = { "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36" }

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}

response = requests.get(url, headers=headers)
dom = response.content

soup = BeautifulSoup(dom, 'html.parser')

# print(soup.find_all('class="searchResultsItem"'))
for i in soup.findAll("a", {"class": "classifiedTitle"}):
    print(i.text)
# print(soup.prettify())

