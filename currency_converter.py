#!/usr/bin/env python

import json
import sys
import urllib.request

###
# The user inputs a price, a currency, and the desired currency
# The program then outputs a statement telling the price in the
# desired currency

if len(sys.argv) !=4:
    print("Incorrect NO. Arguments. Please enter the following:\n \\         ./currency_rates.py lookup_price lookup_currency base_currency")
    sys.exit()

lookup_price = sys.argv[1]
base_currency = sys.argv[2]
lookup_currency = sys.argv[3]

currencyurl = "http://freecurrencyrates.com/api/action.php?do=cvals&iso=" + lookup_currency + "&f=" + base_currency + "&v=1&s=cbr"

try:
    f=urllib.request.urlopen(currencyurl)
except urllib.error.URLError:
    print("URL not found, check currency codes, or else idk m8.")


obj = json.loads(f.read()) # Deserialise the json data
conversion_rate = obj[lookup_currency.upper()] # Gives conversion rate from one unit to another
converted_price = round(int(lookup_price) * conversion_rate, 2)

print(f"{round(float(lookup_price), 2)} {base_currency.upper()} is {converted_price} {lookup_currency}")
