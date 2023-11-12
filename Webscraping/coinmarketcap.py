from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/all/views/all/"
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')

tbody = doc.tbody
trs = tbody.contents

prices = {}

for tr in trs[:10]:
    name = tr.contents[1]
    price = tr.contents[4]
    fixed_name = name.a.string
    fixed_price = price.span.string
    prices[fixed_name] = fixed_price

#print(prices)
while True:
    user_input = input("Enter the cryptocurrency name (or 'exit' to quit): ").strip().upper()

    if user_input == 'EXIT':
        break

    if user_input in prices:
        print(f"The price of {user_input} is {prices[user_input]}")
    else:
        print("Invalid cryptocurrency name. Try again.")






