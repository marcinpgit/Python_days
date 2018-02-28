from ogloszenie import Ogloszenie
from bs4 import BeautifulSoup
import requests

adres = "https://www.otodom.pl/wynajem/mieszkanie/gdansk/?search%5Bdescription%5D=" \
        "1&search%5Bdist%5D=0&search%5Bdistrict_id%5D=16&search%5Bsubregion_id%" \
        "5D=439&search%5Bcity_id%5D=40#form"

response = requests.get(adres)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

# print(response.text)

ads = soup.select(".offer-item-header a")
for ad in ads:
    # print(ad)

    # print(ad.getText())
    # print(ad.get('href'))
    # print("--------------------\n")

    o = Ogloszenie(ad.getText(), ad.get('href'))
#     print(o.opis)
# print(len(ads))

Ogloszenie.zapisz_ogloszenie("ogloszenia.dat")