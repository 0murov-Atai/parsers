from bs4 import BeautifulSoup as bs
import requests
# import psycopg2 


HOST = 'https://globus-online.kg/'


globus_page = requests.get(url = 'https://globus-online.kg/').text

data = bs(globus_page, 'html.parser')
print(globus_page)
view_showcase = data.find('div', attrs={"id":"view-showcase"})

all_cards = view_showcase.find_all('div', class_="list-showcase__part-main")

for card in all_cards:

    print(card.find('div', class_="list-showcase__picture").a.img.get('src'))
    print(card.find('div', class_="list-showcase__name").a.text)
    print(card.find('div', class_="list-showcase__prices").find('span', class_="c-prices__price   js-prices__price js-prices__price-code_ГЛОБУС Розничная"))