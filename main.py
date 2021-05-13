from bs4 import BeautifulSoup
import requests
from selenium import webdriver
#pokemon web scrapping

def get_page_html(url):
    result = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }).text
    page_soup = BeautifulSoup(result, 'html.parser')
    return page_soup
def underscore():
    under = '_'
    return under*8
if __name__ == '__main__':
    rand_or_choose = input('Do you want a random pokemon or do you want to choose a pokemon??')
    if rand_or_choose.lower() == 'random':
        pass
    elif rand_or_choose.lower() == 'choose':
        choice = input('Pick a pokemon!')
        url = 'https://www.pokemon.com/us/pokedex/'
        url += choice
        page_soup = get_page_html(url)
        basic_info = page_soup.find(class_='version-x')
        stats_a = page_soup.find('div', class_='column-7').find_all('li')
        stats_b = page_soup.find('div', class_='column-7').find_all('li')
        stats_c = page_soup.find('div', class_='column-7 push-7').find_all('li')
        power_move_info = page_soup.find('div', class_='pokemon-ability-info-detail match').find('p')
        print(underscore())
        print(stats_a[0].text.strip())
        print(underscore())
        print(stats_b[1].text.strip())
        print(underscore())
        print(stats_c[0].text.strip())
        print(underscore())
        print(stats_c[1].text.strip())
        print(power_move_info.text.strip())
        print(underscore())







