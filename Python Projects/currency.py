import json
from urllib.request import urlopen
response = urlopen("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd.json")
response1 = urlopen("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.min.json")
source = response.read()
source1 = response1.read()
data = json.loads(source)
data1 = json.loads(source1)
currencies = data["usd"]
currencyName = data1
isTrue = True
exchange_rate = 0
while isTrue == True:
    currency = input("Enter a country currency to convert to: ")
    currency = currency.lower()
    isValid = False
    if currencies.get(currency, None):
        if currencyName.get(currency, None):
            name = currencyName.get(currency) 
        exchangeRate = currencies.get(currency)
        amount = float(input("Enter an amount to convert: $"))
        total = amount * exchangeRate
        print(f"A ${amount} US dollars is worth ${total} in {name}")    
    else:
        print(f"Country code of {currency} not found")
    remain = input("Another? Y or N: ")
    remain = remain.upper()
    if remain != "Y":
        isTrue = False
