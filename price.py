from oandapyV20.contrib.factories import InstrumentsCandlesFactory
from oandapyV20 import API
import oandapyV20.endpoints.accounts as accounts
import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')



class Instruments(object):

	def __init__(self):
		client = API(access_token=config['account']['token'])
		r = accounts.AccountInstruments(accountID=config['account']['accountID'])
		self.rv = client.request(r)

	def get_instruments(self):
		'''return a dict. key: instruments, value: a list of instruments'''
		return self.rv

	def  __str__(self):
		return json.dumps(self.rv, indent=2)


class Candle(object):

	def __init__(self, _from, _to, gran, instr):
		'''2017-01-01T00:00:00Z 2017-06-30T00:00:00Z H4 EUR_USD'''
		client = API(access_token=config['account']['token'])
		instrument = instr
		params = {
			    "granularity": gran,
			    "from": _from,
			    "to": _to
				}
		for res in InstrumentsCandlesFactory(instrument=instr, params=params):
			self.rv = client.request(res)


	def get_candle(self):
		return self.rv


	def __str__(self):
		return json.dumps(self.rv, indent=2)

def main():
	print(Candle('2018-04-01T00:00:00Z', '2018-05-17T00:00:00Z', 'H4', 'EUR_USD'))
	

if __name__ == '__main__':
	main()