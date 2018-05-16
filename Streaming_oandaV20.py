import json
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


api = API(access_token=config['account']['token'], environment="practice")

instruments = "XAU_USD"
s = PricingStream(accountID=config['account']['accountID'], params={"instruments":instruments})
try:
    n = 0
    for R in api.request(s):
        print(json.dumps(R, indent=2))
        # n += 1
        # if n > 10:
        #     s.terminate("maxrecs received: {}".format(n))

except V20Error as e:
    print("Error: {}".format(e))
