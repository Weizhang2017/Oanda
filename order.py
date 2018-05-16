import json

from oandapyV20.contrib.requests import MarketOrderRequest
from oandapyV20.contrib.requests import TakeProfitDetails, StopLossDetails

import oandapyV20.endpoints.orders as orders
from oandapyV20 import API

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

class MarketOrder(object):
	def __init__(self, instr, units, take_profit, stop_loss):
		access_token = config['account']['token']
		accountID = config['account']['accountID']
		api = API(access_token=access_token)

		mktOrder = MarketOrderRequest(
		    instrument=instr,
		    units=units,
		    takeProfitOnFill=TakeProfitDetails(price=take_profit).data,
		    stopLossOnFill=StopLossDetails(price=stop_loss).data)

		r = orders.OrderCreate(accountID, data=mktOrder.data)
		try:
		    rv = api.request(r)
		except oandapyV20.exceptions.V20Error as err:
		    print(r.status_code, err)
		else:
		    print(json.dumps(rv, indent=2))

def main():
	EUR_USD_STOP_LOSS = 1.17
	EUR_USD_TAKE_PROFIT = 1.19
	instr = 'EUR_USD'
	units = 1000
	MarketOrder(instr, units, EUR_USD_TAKE_PROFIT, EUR_USD_STOP_LOSS)

if __name__ == '__main__':
	main()