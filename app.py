from flask import Flask, render_template
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
app = Flask('app')

@app.route('/')
def main():
	prices = cg.get_price(ids='Bitcoin, litecoin, dogecoin, ethereum, binance coin, tether, cardano, Polkadot, iXRP, USD-Coin', vs_currencies='usd',  include_market_cap=True, include_24hr_vol=True, include_24hr_change=True)
	return render_template("index.html", prices = prices)

app.run(host='0.0.0.0', port = 8080, debug=True)
