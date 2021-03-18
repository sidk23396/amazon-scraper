import json

import requests
from bs4 import BeautifulSoup


def get_exchange_rate():
    """
    Method to get exchange rate for gbp to eur
    :return: exchange rate of gbp to eur
    """
    try:
        curr_conv_url = 'https://api.exchangeratesapi.io/latest?symbols=GBP'
        conv_rate = requests.get(url=curr_conv_url)
        curr_data = json.loads(conv_rate.text)
        eur_to_gbp = float(curr_data['rates']['GBP'])
        gbp_to_eur = float(1 / eur_to_gbp)
        return gbp_to_eur

    except Exception as e:
        print('Unexpected error when getting exchange rate: ' + str(e))


def update_exchange_rate():
    """
    Method to update exchange rate in file once a day
    :return:
    """


def get_price_from_amazon_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

    page = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()

    try:
        price = soup.find(id='priceblock_ourprice').get_text()
    except AttributeError as e:
        price = soup.find(id='price_inside_buybox').get_text()

    if '£' in price:
        gbp_to_eur = get_exchange_rate()
        # price_in_gbp = price.replace(',','')
        price_in_gbp = float(price.replace(',', '').strip()[1:])
        price_in_eur = price_in_gbp * gbp_to_eur
        return title.strip(), f"{price_in_eur:.2f}"


def send_email():
    pass
