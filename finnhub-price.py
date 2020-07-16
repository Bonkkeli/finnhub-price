
import requests
import json
from datetime import datetime
import os

# write to JSON file


def write_to_JSON(path, filename, data):
    filepath_name_wext = "./" + path + "/" + filename + ".json"
    with open(filepath_name_wext, "w") as fp:
        json.dump(data, fp)
    return None

# gets current stock price


def get_price(symbol):
    url = "https://finnhub.io/api/v1/quote?symbol="

    # add your API key here as string
    api_key = ""

    api = url+symbol+"&token="+api_key
    response = requests.get(api)
    return response.json()

# saves JSON file


def save_price():

    # comma separated symbols
    symbols = input("Symbols (comma separated,no spaces):")
    symbols = symbols.split(",")
    data = []
    for symbol in symbols:
        price = get_price(symbol)
        price["symbol"] = symbol

        # converts unix timestamp to datetime string with format %d/%m/%Y %H:%M
        dt_object = datetime.fromtimestamp(price["t"])
        date_time = dt_object.strftime("%d/%m/%Y %H:%M")
        price["t"] = date_time

        data.append(price)
    write_to_JSON("./", "Stock-prices", data)
    print("File saved.")
    return None


# asks user for symbol(s)
# saves file to folder
# JSON file will say "error": "Symbol not supported." if symbol not valid
# Only US stock symbols are supported
# save JSON file to same folder as .py

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    save_price()
