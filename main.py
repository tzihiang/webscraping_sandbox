from bs4 import BeautifulSoup
import requests


def find_bt04:
html_text = requests.get(
    'https://en.digimoncard.com/cardlist/?search=true&category=508004').text
soup = BeautifulSoup(html_text, 'lxml')
card = soup.find('ul', class_="image_lists")  # Returns all the cards

# Scrape name only
card_name = card.find_all('div', class_="card_name")
for cards in card_name:
    print(cards.text)

