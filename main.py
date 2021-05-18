from flask import Flask, render_template
from pycoingecko import CoinGeckoAPI
import requests


cg = CoinGeckoAPI()
app = Flask('app')


# def fetch_data(id, vs_currencies):
#   res = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies={vs_currencies}").json()
#   return res



@app.route('/')
def main():
	prices = cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd')
	# data = fetch_data(id='bitcoin', vs_currencies='usd')
	# print(data['bitcoin'])
	print(prices)
	return render_template("index.html", price = prices)

app.run(host='0.0.0.0', port = 8080, debug=True)
