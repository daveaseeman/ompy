from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.amazon.com/s/field-keywords=emoji+mask"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
# print (response.text)
soup = BeautifulSoup(response.text, "html.parser")

items = soup.find_all('li', 's-result-item')
for item in items:
    print(item.find('h2').text).encode('utf-8')
    whole_price = item.find('span', 'sx-price-whole').text
    fractional_price = item.find('sup', 'sx-price-fractional').text
    print('This item is ${}.{}'.format(whole_price, fractional_price))
    # print(item.get('href'))

csvfile = open('scraper_data.csv', 'a')
writer = csv.writer(csvfile)

for item in items:
    name = item.find('h2').text
    price = item.find('span', 's-price').text
    writer.writerow([name, price])
