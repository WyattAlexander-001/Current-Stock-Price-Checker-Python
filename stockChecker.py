from bs4 import BeautifulSoup
import requests

stockMarket = {
    "stockname" : "Yahoo Finance Link",
    "apple":"https://finance.yahoo.com/quote/AAPL/",
    "aapl": "https://finance.yahoo.com/quote/AAPL/",

    "microsoft":"https://finance.yahoo.com/quote/MSFT/",
    "msft":"https://finance.yahoo.com/quote/MSFT/",

    "amazon":"https://finance.yahoo.com/quote/AMZN/",
    "amzn":"https://finance.yahoo.com/quote/AMZN/",

    "starbucks":"https://finance.yahoo.com/quote/SBUX/",
    "sbux":"https://finance.yahoo.com/quote/SBUX/",

    "algonquin":"https://finance.yahoo.com/quote/AQN/",
    "aqn":"https://finance.yahoo.com/quote/AQN/",




}

url = stockMarket[input("Enter a Stock Name or Ticker:\n").lower()]

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

def currentPrice():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find('span', class_= 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
    return price
while True:
    print("Stock Price Right Now Is: $" + str(currentPrice()))
