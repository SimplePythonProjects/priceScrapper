from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import telebot

bot = telebot.TeleBot("410814681:AAEAsNsqywiZ4C8iFrwZbl-DdyEHUPmlcww")

coins = ['ethereum','bitcoin', 'litecoin', 'ripple', 'tenx', 'stratis', 'golem-network-tokens', 'bitquence']
def getDetails():
    #Logic to scrape the site and get the prices.
    display = Display(visible=0, size=(800, 600))
    display.start()
    base_url = "https://coinmarketcap.com/currencies/"
    browser = webdriver.Chrome()
    result = ""

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

        result += coin + "\n"
        result += usd_price.text + "\t" + usd_change.text + "\n"
        result += btc_price.text + "\t" + btc_change.text + "\n \n"
    return result

def sendMessage(data):
    #Write code to send the message
    id = -1001123624076
    bot.send_message(id, data)

result = getDetails()
#print result
sendMessage(result)
