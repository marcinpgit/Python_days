import requests
from bs4 import BeautifulSoup

response = requests.get("http://trojmiasto.pl")
print(response.status_code)

response.raise_for_status()
if response.status_code == 200:
    with open("trojmiasto.txt", "w", encoding="utf-8") as plik:
        plik.write(response.text)

trojmiasto_soup = BeautifulSoup(response.text, "html.parser")

linki = trojmiasto_soup.select(".news-list li a")
# print(linki)

for link in linki:
    print(link.getText())
    print(str(link))
    # print(link.attrs)
    print(link.get('id'))
    print(link.get('title'), link.get('href'))
