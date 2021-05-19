from flask import Flask, render_template
from pycoingecko import CoinGeckoAPI
import requests
# https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc


cg = CoinGeckoAPI()
app = Flask('app')


def fetch_data(id, vs_currencies):
	res = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies={vs_currencies}").json()
	return res

fetch_data('litecoin', 'usd')

@app.route('/')
def main():
	prices = cg.get_price(ids='bitcoin, litecoin, dogecoin', vs_currencies='usd')
	# data = fetch_data(id='bitcoin', vs_currencies='usd')
	# print(data['bitcoin'])
	#print(prices)
	return render_template("index.html", price = prices)

app.run(host='0.0.0.0', port = 8080, debug=True)
