from bs4 import BeautifulSoup
import requests
import time

html_text = requests.get(
    'https://en.digimoncard.com/cardlist/?search=true&category=508004').text


# Takes in a html request from requests.get(website_url) and returns an array with all the cards in the set
def get_card_list(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    card_list = soup.find('ul', class_="image_lists")  # Returns all the cards
    return card_list


# Takes in an array of card lists and prints only the names of the cards
def get_names(card_list):
    card_name = card_list.find_all('div', class_="card_name")
    for cards in card_name:
        print(cards.text)


# Takes in name of series (booster, SD etc) and card_List which is retrieved from get_card_list method
def write_to_file(series_name, card_list):
    card_name = card_list.find_all('div', class_="card_name")
    text_file = open(f'{series_name}.txt', 'w')
    for cards in card_name:
        text_file.write(cards.text + "\n")
    text_file.close()
    return None


# Main method to run continuously
# if __name__ == "__main__":
#     while True:
#         card_list = get_card_list(html_text)
#         # get_names(card_list)
#         write_to_file("BT_04", card_list)
#         # time_in_minutes = 10
#         # print(f'Waiting {time_in_minutes} minutes...')
#         # time.sleep(60*time_in_minutes)

card_list = get_card_list(html_text)
# get_names(card_list)
write_to_file("BT_04", card_list)
