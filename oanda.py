import oandapy
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

class Price(object):
	def __init__(self):
		self.oanda = oandapy.API(environment="practice", access_token=config['account']['token'])

	def get_prices(self, instruments):	
		response = self.oanda.get_prices(instruments=instruments)
		self.prices = response.get("prices")
		self.asking_price = self.prices[0].get("ask")

	def __str__(self):
		return str(self.asking_price)

class MyStreamer(oandapy.Streamer):
    def __init__(self, count=10, *args, **kwargs):
        super(MyStreamer, self).__init__(*args, **kwargs)
        self.count = count
        self.reccnt = 0

    def on_success(self, data):
        print(data, "\n")
        self.reccnt += 1
        if self.reccnt == self.count:
            self.disconnect()

    def on_error(self, data):
        self.disconnect()

if __name__ == '__main__':
	account = 'wzhang018'
	stream = MyStreamer(environment="practice", access_token=config['account']['token'])
	stream.rates(account, instruments="EUR_USD,EUR_JPY,US30_USD,DE30_EUR")
