from bs4 import BeautifulSoup
from selenium import webdriver
import time

coins = ['ethereum','bitcoin', 'litecoin', 'ripple', 'tenx', 'stratis', 'golem-network-tokens', 'bitquence']
def getDetails():
    #Logic to scrape the site and get the prices.
    base_url = "https://coinmarketcap.com/currencies/"
    browser = webdriver.Chrome('/Users/rgeorgewinsathia/PycharmProjects/priceScrapper/ChromeDriverFolder/chromedriver')

    for coin in coins:
        url = base_url + coin
        browser.get(url)
        time.sleep(5)

        soup = BeautifulSoup(browser.page_source)

        #print soup.prettify()

        usd_price = soup.find('span', id='quote_price')
        #print usd_price
        usd_change = usd_price.find_next_sibling('span')
        btc_price = usd_change.find_next_sibling('small')
        btc_change = btc_price.find_next_sibling('small')

        print coin
        print usd_price.text + "\t" + usd_change.text + "\n"
        print btc_price.text + "\t" + btc_change.text + "\n"

getDetails()

