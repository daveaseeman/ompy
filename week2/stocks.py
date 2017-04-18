from googlefinance import getQuotes
import json

stocks = ["AAPL", "GOOG", "TSLA"]

# print(json.dumps(getQuotes(stocks), indent = 2))

def print_prices(stocks):
    stock_data = getQuotes(stocks)
    for stock in stock_data:
        print("The price of {} is: ${}".format(stock['StockSymbol'], stock['LastTradePrice']))

print_prices(stocks)
